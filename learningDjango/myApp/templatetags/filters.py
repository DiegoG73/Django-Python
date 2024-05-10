from django import template

register = template.Library()

@register.filter(name='greetings')
def greetings(value):
    large = ""
    if len(value) >= 8:
        large = "<p>Your name is to long</p>"
    return f"<h1 style='background:green; color:white'>Welcome, {value}</h1> " + large