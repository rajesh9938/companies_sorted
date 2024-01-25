from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Users,CompaniesSorted,CandidateUsers
# Register your models here.
admin.site.register(Users)
admin.site.register(CompaniesSorted)
admin.site.register(CandidateUsers)


