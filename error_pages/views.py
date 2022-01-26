from django.shortcuts import render

# Create your views here.


def error_404(request, exception):
    '''
    view rendering the 404 error page
    '''
    return render(request, 'error_responses/404.html')
