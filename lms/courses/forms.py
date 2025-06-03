from django import forms

from .models import Courses,CategoryChoices,LevelChoices,TypeChoices

class CourseCreateForm(forms.ModelForm):

    class Meta :

        model = Courses

        # fields = ['title', 'description', 'image', 'category' , 'level', 'fees', 'offer_fee']

        # field = '__all__'

        exclude = ['instructor', 'uuid', 'active_status' ]

        widgets = {

            'title' : forms.TextInput( attrs={
                                            'class':'form-control',
                                            'required':'required',
                                            'placeholder': 'Enter Course Name '
                                    }),
            'image' : forms.FileInput( attrs = {

                                            'class': 'form-control',
                                            
                                     }),

            'description' :forms.Textarea( attrs={
                                            'class' : 'form-control',
                                            'required' : 'required',
                                            'placeholder' : "Enter course description"

                                    }),
            'tags' : forms.TextInput( attrs={
                                            'class':'form-control',
                                            'required':'required',
                                            
                                    }),


            'fees': forms.NumberInput(attrs= {
                                        'class' : 'form-control',
                                        'required' : 'required',
                                        'placeholder' : "Enter course fees"
                                    }),

            'offer_fee' : forms.NumberInput(attrs={
                                        'class' : 'form-control',
                                    
                                        'placeholder' : "Enter offer fees"

                                    }),

        }
    
    category = forms.ChoiceField(choices= CategoryChoices.choices,widget= forms.Select( 
                                                                        attrs={

                                                                        
                                              'required' : 'required',
                                              'class' : 'form-select'                          
                                }))
    level = forms.ChoiceField(choices= LevelChoices.choices,widget= forms.Select( attrs= {

                                              'required' : 'required',
                                              'class' : 'form-select'  
                                }))
    type = forms.ChoiceField(choices= TypeChoices.choices,widget= forms.Select( attrs= {

                                              'required' : 'required',
                                              'class' : 'form-select'  
                                }))
        
    def clean(self):

        validated_data = super().clean()

        if validated_data.get('fees')  and validated_data.get('fees') < 0:

            self.add_error('fees', 'course fee must be greaterthan Zero')

        if validated_data.get('offer_fee') and validated_data.get('offer_fee') < 0:

            self.add_error('offer_fee', 'course fee must be greaterthan Zero')
        

        print(validated_data)
        return validated_data
    
    def __init__(self, *args, **kwargs):

        super(CourseCreateForm,self).__init__(*args, **kwargs)

        if not self.instance :

            self.fields.get('image').widget.attrs['required'] = 'required'