"""
URL configuration for MIS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from MISWebSite import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.index, name = 'index'),
    path('index', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('services', views.services, name = 'services'),
    path('contact', views.contact, name = 'contact'),
    path('thank_you', views.thank_you, name = 'thank_you'),
    path('error', views.error, name = 'error'),
    path('book_online', views.book_online, name = 'book_online'),
    path('view_software_development', views.view_software_development, name = 'view_software_development'),
    path('view_web_development', views.view_web_development, name = 'view_web_development'),
    path('view_app_development', views.view_app_development, name = 'view_app_development'),
    path('view_blog_development', views.view_blog_development, name = 'view_blog_development'),
    path('view_landing_page_development', views.view_landing_page_development, name = 'view_landing_page_development'),
    path('view_digital_marketing', views.view_digital_marketing, name = 'view_digital_marketing'),
    path('view_seo', views.view_seo, name = 'view_seo'),
    path('view_facebook_ads', views.view_facebook_ads, name = 'view_facebook_ads'),
    path('view_google_ads', views.view_google_ads, name = 'view_google_ads'),
    path('view_web_hosting', views.view_web_hosting, name = 'view_web_hosting'),
    path('terms_and_conditions', views.terms_and_conditions, name = 'terms_and_conditions'),
    path('privacy_policy', views.privacy_policy, name = 'privacy_policy'),
    path('sitemap', views.sitemap, name = 'sitemap')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)