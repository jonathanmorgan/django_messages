from django.apps import AppConfig

class DjangoMessagesConfig(AppConfig):

    name = 'django_messages'

    default_auto_field = 'django.db.models.AutoField'
    # if you have lots of rows:
    # default_auto_field = 'django.db.models.BigAutoField'

#-- END AppConfig class DjangoMessagesConfig --#
