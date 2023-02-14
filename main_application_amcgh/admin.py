from django.contrib import admin
from main_application_amcgh.models import *

# Register your models here.
admin.site.register(Gallery)
admin.site.register(Doctor)
admin.site.register(Department)
admin.site.register(Department_Slug)
admin.site.register(ManagementTeam)
admin.site.register(GoverningBody)
admin.site.register(Service)
admin.site.register(GalleryCategory)
admin.site.register(New)
admin.site.register(NewsCategory)
admin.site.register(DonationGoverment)
admin.site.register(DonationCorporateBank)
admin.site.register(DonationCorporateOthers)
admin.site.register(DonationOverseas)
admin.site.register(DonationOver10Lac)
admin.site.register(DonationOver5LacsTo10Lac)
admin.site.register(DonationOver1LacTo5Lac)
admin.site.register(DonationOver10kTo1Lac)
admin.site.register(Donor)