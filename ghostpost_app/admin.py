from django.contrib import admin
from ghostpost_app.models import BoastsRoastsModel


# Register your models here.
class BoastsRoastsAdmin(admin.ModelAdmin):
    display = ('id', 'post_content')


admin.site.register(BoastsRoastsModel, BoastsRoastsAdmin)
