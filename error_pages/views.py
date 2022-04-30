from django.shortcuts import render

# Create your views here.


def error_404(request, exception):
    '''
    view rendering the 404 error page
    '''
    return render(request, 'templates/404.html')


def error_414(request, exception):
    '''
    view rendering the 404 error page
    '''
    return render(request, 'templates/414.html')


def error_500(request, exception):
    '''
    view rendering the 404 error page
    '''
    return render(request, 'templates/500.html')