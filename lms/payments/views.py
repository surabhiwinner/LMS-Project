from django.shortcuts import render,redirect

from django.views import View

from courses.models import Courses

from .models import Payments

from students.models import Students
from decouple import config

import razorpay

import datetime

from .models import Transactions

# Create your views here.
class EnrollConfirmationView(View):


    def get(self, request, *args, **kwargs):

        uuid = kwargs.get('uuid')

        course = Courses.objects.get(uuid=uuid)

        payment, created = Payments.objects.get_or_create(student= Students.objects.get(profile=request.user),
                                       course = course,
                                         amount= course.offer_fee if course.offer_fee else course.fees)

        data ={
            'payment'    : payment
        }

        return render(request,'payments/enroll-confirmation.html', context=data)

class RazorpayView(View):


    def get(self, request, *args, **kwargs):

        uuid = kwargs.get('uuid')

        course = Courses.objects.get(uuid=uuid)

        payment = Payments.objects.get(student__profile = request.user, course=course)

        client = razorpay.Client(auth=(config('RZP_CLIENT_ID'), config('RZP_CLIENT_SECRET')))

        data = { "amount": payment.amount*100, "currency": "INR", "receipt": "order_rcptid_11" }




        transaction = Transactions.objects.create(payment=payment)


        
        order  = client.order.create(data=data) 
        # Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise

        print(order)

        rzp_order_id = order.get('id')
        transaction.rzp_order_id = rzp_order_id
        transaction.save()

        data = {
            'client_id' : config('RZP_CLIENT_ID'),
            'amount'    : payment.amount*100 ,
            'rzp_order_id': rzp_order_id
        }
        return render(request,'payments/payment-page.html',context=data)


class PaymentVerifyView(View):

    def post(self,request,*args,**kwargs):

        print(request.POST)

        rzp_order_id =request.POST.get('razorpay_order_id')
        rzp_payment_id = request.POST.get('razorpay_payment_id')

        rzp_payment_signature = request.POST.get('razorpay_signature')

        client = razorpay.Client(auth=(config('RZP_CLIENT_ID'),  config('RZP_CLIENT_SECRET')))

        transaction = Transactions.objects.get(rzp_order_id=rzp_order_id)

        time_now =  datetime.datetime.now()

        transaction.transaction_at = time_now

        transaction.rzp_paymenyt_id = rzp_payment_id

        transaction.rzp_payment_signature = rzp_payment_signature

        try:

            client.utility.verify_payment_signature({
                                        'razorpay_order_id': rzp_order_id,
                                        'razorpay_payment_id': rzp_payment_id,
                                        'razorpay_signature': rzp_payment_signature
                                    }) # checks the transaction is successfull or not , if not redirect to except
            
            
            transaction.status = 'Success'
           

            transaction.save()

            transaction.payment.status = 'Success'

            transaction.payment.paid_at = time_now
            transaction.payment.save()

            return redirect('home')

        except:

            transaction.status = 'Failed'
           
            transaction.save()

            
            transaction.payment.status = 'Failed'

            transaction.payment.save()

            return redirect('razorpay-view',uuid=transaction.payment.course.uuid)
            

       