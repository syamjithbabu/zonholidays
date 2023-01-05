from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('services',views.services,name="services"),
    path('packages',views.packages,name="packages"),
    path('blog',views.blog,name="blog"),
    path('gallery',views.gallery,name="gallery"),
    path('gallery-single/<int:id>/',views.gallery_single,name="gallery_single"),
    path('contact',views.contact,name="contact"),
    path('service-details/<int:id>/',views.service_details,name="service_details"),
    path('blog-details/<int:id>/',views.blog_details,name="blog_details"),
    path('package-details/<int:id>/',views.package_details,name="package_details")
]