from django.urls import path
from .views import Home, Internships, FindOpenings, OpeningsDetails, SmartHiring, CheckYourSkill, AboutUs, ContactUs, PrivacyPolicy, TermsOfUse


app_name = 'uitech'

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('internships/', Internships.as_view(), name = 'internships'),
    path('find_openings/', FindOpenings.as_view(), name = 'find_openings'),
    path('openings_details/', OpeningsDetails.as_view(), name = 'openings_details'),
    path('smart_hiring/', SmartHiring.as_view(), name = 'smart_hiring'),
    path('check_your_skill/', CheckYourSkill.as_view(), name = 'check_your_skill'),
    path('about_us/', AboutUs.as_view(), name = 'about_us'),
    path('contact_us/', ContactUs.as_view(), name = 'contact_us'),
    path('privacy_policy', PrivacyPolicy.as_view(), name = 'privacy_policy'),
    path('terms_of_use', TermsOfUse.as_view(), name = 'terms_of_use'),
]