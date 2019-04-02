from django.contrib import admin
from firstapp.models import Webpage,AccessRecord,Topic
# Register your models here.


admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(Topic)