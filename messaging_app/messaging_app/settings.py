# messaging_app/settings.py

# Add 'rest_framework' to INSTALLED_APPS if not already
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'chats',  # your messaging app
]

# Django REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',  # ← لازم
    'PAGE_SIZE': 20,  # ← لازم
}
