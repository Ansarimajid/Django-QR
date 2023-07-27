from django.contrib import admin
from .models import QRModel
# Register your models here.

# admin.site.register(QRModel)
@admin.register(QRModel)
class QRModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'qr_image', 'created_at']