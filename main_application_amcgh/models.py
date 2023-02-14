from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Department(models.Model):
    department_name = models.CharField(max_length=255)
    department_short_description = models.TextField(null=True, blank=True)
    department_description = RichTextField(blank=False, null=False, default='Nothing')
    department_image = models.ImageField(upload_to='Department/',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('department_name',)

    def get_absolute_url(self):
        return reverse("main_application:department_details", kwargs={"id": self.id})

    def __str__(self):
        return self.department_name


class Department_Slug(models.Model):
    name = models.ForeignKey(Department, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('main_application:doc_by_department', args=[self.slug])

    def __str__(self):
        return self.slug



class Doctor(models.Model):
    
    doctor_name = models.CharField(max_length=255)
    designation = models.TextField(null=False)
    department = models.ManyToManyField(Department)
    degree = models.CharField(max_length=255)
    profile_pic = models.FileField(upload_to='Doctor_Profile_Pic', default='User-avatar.png')
    research_publication = RichTextField(blank=True, null=True)
    appointment = models.CharField(max_length=255,null=True, blank=True)
    sorting_order= models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    

    def get_absolute_url(self):
        return reverse("main_application:doctor_details", kwargs={"id": self.id})

    def __str__(self):
        return self.doctor_name


class ManagementTeam(models.Model):
    member_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255,null=True, blank=True)
    institution = models.CharField(max_length=255)
    profile_pic = models.ImageField(default='default.png', upload_to='Management Team')

    def __str__(self):
        return self.member_name


class GoverningBody(models.Model):
    member_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255,null=True, blank=True)
    institution = models.CharField(max_length=255, default='None')
    profile_pic = models.ImageField(default='default.png', upload_to='Governing Body')

    def __str__(self):
        return self.member_name


class GalleryCategory(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class Gallery(models.Model):
    image_name = models.CharField(max_length=255)
    gallery_image = models.ImageField(upload_to='Gallery', default='default.png')
    category_id = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name


class NewsCategory(models.Model):
    news_category_name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.news_category_name


class New(models.Model):
    news_title = models.CharField(max_length=255)
    news_category = models.ManyToManyField(NewsCategory)
    excert = models.TextField(null=False, blank=False)
    news_description = RichTextField(blank=False, null=False, default='Nothing')
    news_thumbnail = models.ImageField(upload_to='News/News Thumbnail/')
    news_image = models.ImageField(upload_to='News/News Image/')
    news_views = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("main_application:News-Details", kwargs={"id": self.id})

    def __str__(self):
        return self.news_title


class Service(models.Model):
    logo = models.ImageField(default='default.png', upload_to='Service/logo')
    service_name = models.CharField(max_length=255)
    service_description = RichTextField(blank=True, null=True)
    service_image = models.FileField(upload_to='Service/Image', )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.service_name

    def get_absolute_url(self):
        return reverse("main_application:service_detail", kwargs={"id": self.id})


class DonationGoverment(models.Model):
    logo = models.ImageField(default='default.png', upload_to='Donatiom/Goverment Donation')
    name = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DonationCorporateBank(models.Model):
    company_logo = models.ImageField(upload_to='Corporate Company Logo', blank=True, null=True)
    company_name_address = models.CharField(max_length=255)
    committed_amount = models.CharField(max_length=255)
    donated_amount = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name_address


class DonationCorporateOthers(models.Model):
    company_logo = models.ImageField(upload_to='Corporate Company Logo', blank=True, null=True)
    company_name_address = models.CharField(max_length=255, blank=False)
    committed_amount = models.CharField(max_length=255, blank=True, default='0')
    donated_amount = models.CharField(max_length=255, blank=True, default='0')

    def __str__(self):
        return self.company_name_address


class DonationOverseas(models.Model):
    name_address = models.CharField(max_length=255)
    committed_amount = models.CharField(max_length=255)
    donated_amount = models.CharField(max_length=255)

    def __str__(self):
        return self.name_address


class DonationOver10Lac(models.Model):
    name_address = models.CharField(max_length=255)
    committed_amount = models.CharField(max_length=255)
    recieved_amount = models.CharField(max_length=255)

    def __str__(self):
        return self.name_address


class DonationOver5LacsTo10Lac(models.Model):
    name_address = models.CharField(max_length=255)
    committed_amount = models.CharField(max_length=255)
    recieved_amount = models.CharField(max_length=255)

    def __str__(self):
        return self.name_address


class DonationOver1LacTo5Lac(models.Model):
    name_address = models.CharField(max_length=255)
    committed_amount = models.CharField(max_length=255)
    recieved_amount = models.CharField(max_length=255)

    def __str__(self):
        return self.name_address


class DonationOver10kTo1Lac(models.Model):
    name_address = models.CharField(max_length=255)
    committed_amount = models.CharField(max_length=255)
    recieved_amount = models.CharField(max_length=255)

    def __str__(self):
        return self.name_address
        
        
class Donor(models.Model):
    donor_name = models.CharField(blank=True, default='None', max_length=255)
    donor_logo = models.ImageField(default='default.png', upload_to='Donors')

    def __str__(self):
        return self.donor_name

