from django.contrib import admin

# Register your models here.
from accounts.models import ProfileModel

class ProfileModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(ProfileModel, ProfileModelAdmin)

from accounts.models import ImageUpload

class ImageUploadAdmin(admin.ModelAdmin):
    pass
admin.site.register(ImageUpload, ImageUploadAdmin)