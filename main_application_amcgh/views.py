from django.shortcuts import render, get_object_or_404
from main_application_amcgh.models import *

from django.db.models import Q
import time


def home_view(request):
    department_1 = Department.objects.filter(department_name__icontains='Oncology')
    department_2 = Department.objects.all()[0:10]
    department_3 = Department.objects.all()[11:20]
    department_4 = Department.objects.all()[21:30]
    department_home_list_1 = Department.objects.all().reverse()[:2]
    department_home_list_2 = Department.objects.all()[:3]
    service_home_view = Service.objects.all()[:8]
    doc_list = Doctor.objects.all()
    news_list = New.objects.all()
    donor_list= Donor.objects.all()
    context = {
        'service_list': service_home_view,
        'doc_list': doc_list,
        'department_home_list_1': department_home_list_1,
        'department_home_list_2': department_home_list_2,
        'department_1': department_1,
        'department_2': department_2,
        'department_3': department_3,
        'department_4': department_4,
        'news_list': news_list,
        'donor_list': donor_list
    }
    return render(request, 'homepage/index.html', context)


def news_list_view(request):
    department_menu = Department.objects.all()
    news_list = New.objects.all()
    context = {
        'department_menu': department_menu,
        'news_list': news_list

    }
    return render(request, 'News&events/blog-sidebar.html', context)


def news_details_view(request, id):
    request.session['news_id'] = id
    news_obj = New.objects.get(id=id)
    news_obj.news_views=  news_obj.news_views + 1
    news_obj.save()
    news_details = New.objects.all()
    department_menu = Department.objects.all()
    news_list = New.objects.all()
    news_category= NewsCategory.objects.all()
    context = {
        'department_menu': department_menu,
        'news_obj': news_obj,
        'news_details': news_details,
        'news_category': news_category


    }
    return render(request, 'News&events/blog-single.html', context)


def about_us_view(request):
    department_menu = Department.objects.all()
    context = {
        'department_menu': department_menu
    }
    return render(request, 'about.html', context)


def doctor_details(request, id):
    request.session['doctor_id'] = id
    obj = Doctor.objects.get(id=id)
    doctor_details = Doctor.objects.all()
    department_menu = Department.objects.all()
    context = {
        'object': obj,
        'doctor_details': doctor_details,
        'department_menu': department_menu
    }
    return render(request, "Doctors/doctor_profile_new.html", context)


def department_details(request, id):
    request.session['department_id'] = id
    doctor_list = Doctor.objects.all()
    departments = request.GET.get('departments')
    if departments is None:
        pass
    else:
        doctor_list = Doctor.objects.filter(department__department_name__icontains=departments)

    department = Department.objects.get(id=id)
    department_menu = Department.objects.all()
    department_list = Department.objects.all()

    context = {
        'doctor_list': doctor_list,
        'department': department,
        'department_list': department_list,
        "id": id,
        'department_menu': department_menu
    }
    return render(request, "Department/department-single.html", context)


def is_valid_queryparam(param):
    return param != '' and param is not None


from django.db.models import Count


def doctor_list_view(request, department_slug=None):

    departments = Department.objects.all().annotate(posts_count=Count('doctor'))
    departments_slug = Department_Slug.objects.all()
    department_menu = Department.objects.all()

    if department_slug:
        department = get_object_or_404(Department_Slug, slug=department_slug)
        doctor = Doctor.objects.filter(department__department_slug=department)

    else:
        doctor = Doctor.objects.all()

    context = {
        'doctor': doctor,
        'department_list': department_list,
        'departments': departments,
        'departments_slug': departments_slug,
        'department_menu': department_menu

    }

    return render(request, "Doctors/doctor_list.html", context)


def service_list_view(request):
    department_menu = Department.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        filtered_service_list = Service.objects.filter(service_name__icontains=q)
    else:
        filtered_service_list = Service.objects.all()

    context = {
        's_list': filtered_service_list,
        'department_menu': department_menu
    }
    return render(request, "Services/service.html", context)


def department_list(request):
    department_list = Department.objects.all()
    context = {
        'dept_list': department_list
    }
    return render(request, 'Department/department.html', context)


def gb_list_view(request):
    department_menu = Department.objects.all()
    gb = GoverningBody.objects.all()

    context = {
        'gb': gb,
        'department_menu': department_menu
    }
    return render(request, "governing_body.html", context)


def management_team_view(request):
    management_team = ManagementTeam.objects.all()
    department_menu = Department.objects.all()
    context = {
        'management_team': management_team,
        'department_menu': department_menu
    }
    return render(request, "management_team.html", context)


def service_details_view(request, id):
    service = Service.objects.get(id=id)
    service_details = Service.objects.all()
    department_menu = Department.objects.all()
    context = {
        'service': service,
        'service_details': service_details,
        'department_menu': department_menu
    }
    return render(request, "Services/service-detail.html", context)


def contact_view(request):
    department_menu = Department.objects.all()
    context = {
        'department_menu': department_menu
    }
    return render(request, 'contact.html', context)


def gallery_view(request):
    department_menu = Department.objects.all()
    gallery_category = GalleryCategory.objects.all()
    gallery = Gallery.objects.all()
    filterd_gallery_category = request.GET.get('category')

    if filterd_gallery_category == 'All':
        gallery = Gallery.objects.all()
    elif is_valid_queryparam(filterd_gallery_category):
        gallery = gallery.filter(category_id__category_name=filterd_gallery_category)

    context = {
        'gallery_category': gallery_category,
        'filterd_gallery': gallery,
        'department_menu': department_menu
    }
    return render(request, 'gallary.html', context)


def career(request):
    return render(request, 'career.html')


def missionvission(request):
    return render(request, 'mission&vision.html')


def whoweare(request):
    return render(request, 'whoweare.html')


def backgroundhistory(request):
    return render(request, 'backgroundhistory.html')


def message_from_president(request):
    return render(request, 'message_from_president.html')


def goverment_donation_view(request):
    gv_donation = DonationGoverment.objects.all()

    context = {
        'gv_donation': gv_donation
    }
    return render(request, 'Donation/goverment_donation.html', context)


def corporate_donation_view(request):
    corporate_donation = DonationCorporateBank.objects.all()

    context = {
        'corporate_donation': corporate_donation
    }
    return render(request, 'Donation/corporate_donation.html', context)


def corporate_donation_others_view(request):
    corporate_donation_others = DonationCorporateOthers.objects.all()

    context = {
        'corporate_donation_others': corporate_donation_others
    }
    return render(request, 'Donation/corporate_donation_others.html', context)


def donation_overseas_view(request):
    donation_overseas = DonationOverseas.objects.all()

    context = {
        'donation_overseas': donation_overseas
    }
    return render(request, 'Donation/donation_overseas.html', context)


def donation_over_10Lac_view(request):
    donation_over_10Lac = DonationOver10Lac.objects.all()

    context = {
        'donation_over_10Lac': donation_over_10Lac
    }
    return render(request, 'Donation/donation_over_10lacs.html', context)


def donation_over_5Lac_view(request):
    donation_over_5Lac = DonationOver5LacsTo10Lac.objects.all()

    context = {
        'donation_over_5Lac': donation_over_5Lac
    }
    return render(request, 'Donation/donation_over_5Lacs.html', context)


def donation_over_1Lac_view(request):
    donation_over_1Lac = DonationOver1LacTo5Lac.objects.all()

    context = {
        'donation_over_1Lac': donation_over_1Lac
    }
    return render(request, 'Donation/donation_over_1lacs.html', context)


def donation_over_10k_view(request):
    donation_over_10k = DonationOver10kTo1Lac.objects.all()

    context = {
        'donation_over_10k': donation_over_10k
    }
    return render(request, 'Donation/donation_over_10k.html', context)
    
def doctors_schedule(request):

    return render(request, 'doctors_schedule.html')
