from django.contrib import admin
from .models import Banda, Integrante, Album

admin.site.register(Banda, Integrante, Album)


# Register your models here.
