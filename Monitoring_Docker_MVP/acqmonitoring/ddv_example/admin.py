from django.contrib import admin

from .models import AgregateData
from .models import DetailData

admin.site.register(AgregateData)
admin.site.register(DetailData)
