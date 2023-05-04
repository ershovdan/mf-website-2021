from django.shortcuts import render
import logging
import random

logger = logging.getLogger(__name__)

# Create your views here.
def MainPage(request):
    greet_list = ['back', 'again']
    greet = random.choice(greet_list)
    context = {'status': request.user.is_active, 'greet': greet}
    return render(request, 'MainPage/main.html', context)

def EULA_page(request):
    return render(request, 'MainPage/EULA.html')

def handler404(request, exception):
    return render(request, 'errors_pages/404_page.html', locals())

def handler500(request):
    logger.error('User has 500 error')
    return render(request, 'errors_pages/500_page.html', locals())


