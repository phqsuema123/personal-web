from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import HomepageContent,Activity,AcademicProject

class HomepageContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'body', 'image1', 'image2', 'image3')

admin.site.register(HomepageContent)
admin.site.register(Activity)
admin.site.register(AcademicProject)