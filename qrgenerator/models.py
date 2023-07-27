from django.db import models
from django.dispatch import receiver
import os
# Create your models here.

class QRModel(models.Model):
    text = models.TextField()
    qr_image = models.ImageField(upload_to='Qr-Images')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.text

@receiver(models.signals.post_delete, sender=QRModel)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.qr_image:
        if os.path.isfile(instance.qr_image.path):
            os.remove(instance.qr_image.path)

@receiver(models.signals.pre_save, sender=QRModel)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = QRModel.objects.get(pk=instance.pk).qr_image
    except QRModel.DoesNotExist:
        return False

    new_file = instance.qr_image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)