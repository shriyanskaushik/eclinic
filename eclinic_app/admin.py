from django.contrib import admin
from eclinic_app.models import *

# Register your models here.
admin.site.register(Locality)
admin.site.register(Assistant)
admin.site.register(Patient)
admin.site.register(Hospital)
admin.site.register(Doctor)
admin.site.register(Pharmacy)
admin.site.register(DiagnosticLab)
admin.site.register(PharmacyExtended)
admin.site.register(DiagExtended)
admin.site.register(DoctorExtended)
admin.site.register(Test)
admin.site.register(PatientRecords)
admin.site.register(FAQ)
admin.site.register(DoctorFeedback)
admin.site.register(PharmacyFeedback)
admin.site.register(DiagonosticFeedback)