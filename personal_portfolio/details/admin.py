from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(WhoAreYou)
admin.site.register(AboutMe)
admin.site.register(socialMedia)