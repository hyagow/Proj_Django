from django.contrib import admin
from .models import Categoria  # importing Categoria model
from .models import Transacao

# Register your models here.

# Registering Categoria model to make it operational.
# Allow manage this table on frontend with all HTTP verbs.
admin.site.register(Categoria)  # Now, go to http://127.0.0.1:8000/admin/ and it's possible add new items (Categorias)
admin.site.register(Transacao)