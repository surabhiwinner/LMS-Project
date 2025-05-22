from django import template


register = template.Library()
# createing an object named register  of class Library

@register.simple_tag
def convert_uppercase(text):

    return text.upper() # this is a sample function to convert a word into uppercase



@register.simple_tag
def user_role_checking(request,roles):


    roles = roles.split(',')

    if request.user.is_authenticated and request.user.role in roles:
        
        return True

    return False

