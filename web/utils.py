from web.models import UserProfile

def get_user_language(request):
    # Si el usuario está autenticado y tiene un idioma seleccionado
    if request.user.is_authenticated:
        profile = getattr(request.user, 'userprofile', None)
        if profile and profile.language:
            return profile.language
    
    # Obtener idioma del navegador
    accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', '')
    for lang in accept_language.split(','):
        lang = lang.split(';')[0].strip()
        if lang[:2] in dict(UserProfile.LANGUAGE_CHOICES):
            return lang[:2]
    
    return 'en'  # fallback por defecto