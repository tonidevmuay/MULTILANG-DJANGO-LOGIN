from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import translation
from django.conf import settings

from web.models import UserProfile

def index(request):
    if request.user.is_authenticated:
        user_language = request.user.userprofile.language
    else:
        user_language = settings.LANGUAGE_CODE
        
    translation.activate(user_language)
    request.session['django_language'] = user_language  # Cambiado aquí
    return render(request, 'index.html')

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def contact(request):
    return render(request, 'contact.html')
  
@login_required
def change_language(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
            # Guardar preferencia de usuario
            if not hasattr(request.user, 'userprofile'):
                UserProfile.objects.create(user=request.user)
            request.user.userprofile.language = language
            request.user.userprofile.save()
            
            # Activar el idioma
            translation.activate(language)
            request.session['django_language'] = language  # Cambiado aquí
            
            response = redirect(request.META.get('HTTP_REFERER', 'index'))
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
            return response
    return redirect('index')