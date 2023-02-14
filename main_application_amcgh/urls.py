from django.conf.urls.static import static
from django.conf import settings
from main_application_amcgh.views import *
from django.urls import path

app_name = 'main_application'
urlpatterns = [
                  path('', home_view, name='Home'),
                  path('contact/', contact_view, name='contact-us'),
                  path('news/', news_list_view, name='News-List'),
                  path('news_details/<int:id>', news_details_view, name='News-Details'),
                  path('about/', about_us_view, name='about'),
                  path('gallery/', gallery_view, name='gallery'),
                  path('service_details/<int:id>', service_details_view, name='service_detail'),
                  path('service-list/', service_list_view, name='service-list'),
                  path('doctor-list/', doctor_list_view, name='doctor-list'),
                  path('<slug:department_slug>', doctor_list_view, name='doc_by_department'),
                  path('department_details/<int:id>/', department_details, name='department_details'),
                  path('department-list/', department_list, name='department-list'),
                  path('doctor_details/<int:id>', doctor_details, name="doctor_details"),
                  path('gb_list/', gb_list_view, name="governing-body"),
                  path('mt_list/', management_team_view, name="management-team"),
                  path('career/', career, name="career"),
                  path('mission&vission/', missionvission, name="mission&vission"),
                  path('whoWeAre/', whoweare, name="whoWeAre"),
                  path('backgroundHistory/', backgroundhistory, name="backgroundHistory"),
                  path('message_from_president/', message_from_president, name="messageFromPresident"),
                  path('goverment_donation/', goverment_donation_view , name="Goverment-Donation"),
                  path('corporate_donation/', corporate_donation_view , name="Corporate-Donation"),
                  path('corporate_donation_others/', corporate_donation_others_view , name="Corporate-Donation(Others)"),
                  path('donation_overseas/', donation_overseas_view , name="Donation-Overseas"),
                  path('donation_over_10L/', donation_over_10Lac_view , name="Donation-Over-10Lac"),
                  path('donation_over_5L/', donation_over_5Lac_view , name="Donation-Over-5Lac"),
                  path('donation_over_1L/', donation_over_1Lac_view , name="Donation-Over-1Lac"),
                  path('donation_over_10K/', donation_over_10k_view , name="Donation-Over-10k"),
                  path('doctors_schedule/', doctors_schedule, name="Doctors-Schedule"),




              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
