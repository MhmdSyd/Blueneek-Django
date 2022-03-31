from django.http import HttpResponse


HTML_STRING = """
<h1>This is Home Page</h1>
"""

def home(request):

    return HttpResponse(HTML_STRING)