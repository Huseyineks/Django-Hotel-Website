from django.contrib import admin

from .models import AppModel
class AppAdmin(admin.ModelAdmin):
    class Meta:
        model = AppModel
        fields = '__all__'




admin.site.register(AppModel,AppAdmin)
