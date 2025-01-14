from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import translation
from django.conf import settings
from web.utils import get_user_language


def index(request):
    if request.user.is_authenticated:
        user_language = request.user.userprofile.language
    else:
        user_language = settings.LANGUAGE_CODE
        
    translation.activate(user_language)
    request.session['django_language'] = user_language 
    return render(request, 'index.html')

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def contact(request):
    return render(request, 'contact.html')
  


@login_required
def change_language(request):  # Solo guardamos en el perfil si el usuario explícitamente selecciona un idioma
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
           
            request.user.userprofile.language = language
            request.user.userprofile.save()
            translation.activate(language)
    else:
        # En peticiones GET, usamos el helper
        language = get_user_language(request)
        translation.activate(language)
    
    return redirect(request.META.get('HTTP_REFERER', '/'))