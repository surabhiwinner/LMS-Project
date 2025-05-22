from django.shortcuts import redirect


# @permission_roles(roles=['Instructor'])
def permission_roles(roles):

    def decorator(func):

        def wrapper(request, *args, **kwargs):

            if request.user.is_authenticated and request.user.role in roles :

                    return func(request, *args, **kwargs)
        
            return redirect('login')
    

        return wrapper
    return decorator