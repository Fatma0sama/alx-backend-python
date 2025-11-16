# messaging_app/settings.py

# Add 'rest_framework' to INSTALLED_APPS if not already
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'chats',  # your messaging app
]

# Django REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
}
