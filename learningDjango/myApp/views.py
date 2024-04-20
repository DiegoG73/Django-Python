from django.shortcuts import render, HttpResponse, redirect

#* MVC: Model-View-Controller -> Actions (methods)
#^ MVT: Model-View-Template -> Actions (methods)

layout = """
<h1>Mi sitio web con django</h1>
<hr/>
<ul>
    <li>
        <a href="/home">Home</a>
    </li>
    <li>
        <a href="/hello-world">Hello World</a>
    </li>
    <li>
        <a href="/test-page">Test page</a>
    </li>
    <li>
        <a href="/contact">Contact</a>
    </li>
</ul>
<hr/>
"""

def index(request):
    html = """
        <h1> Inicio </h1>
        <p> Years until 2050: </p>
        <ul>
    """
    year = 2024
    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year += 1
    html += "</ul>"
    
    return render(request, 'index.html')

def hello_world(request):
    return render(request, 'hello_world.html')

def page(request, redirection = 0):
    if redirection == 1:
        #*This is how we do a redirection
        return redirect('contact', name="Diego", surname="Guzmán")
    
    return render(request, 'page.html')
    
def contact(request, name="", surname=""):
    html = ""
    if name and surname:
        html += "<p>The complete name is:</p>"
        html += f"{name} {surname}"
    
    return HttpResponse(layout+ f"<h2>Contact</h2>"+ html)