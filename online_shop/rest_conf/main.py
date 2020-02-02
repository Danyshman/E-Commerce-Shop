REST_FRAMEWORK = {
    'DEFAULT_AUTHENTIFICATION_CLASSES': (
        'rest_framework.authentification.BasicAuthentification',
        'rest_framework.authentification.SessionAuthentification',
        'rest_framework.authentification.TokenAuthentification'
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        "rest_framework.permissions.IsAuthenticated",
    ),
}