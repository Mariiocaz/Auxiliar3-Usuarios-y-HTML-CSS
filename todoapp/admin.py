from django.contrib import admin

# Register your models here.
from todoapp.models import Categoria

admin.site.register(Categoria)

from todoapp.models import User, Tarea
admin.site.register(User)
admin.site.register(Tarea)