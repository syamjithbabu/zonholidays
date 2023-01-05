from django.shortcuts import render
from web.models import Testimonial, Blog, Service, Gallery, Place, Package, TourType

# Create your views here.

def index(request):
    testimonials = Testimonial.objects.filter().all()[:3]
    gallery = Gallery.objects.filter().all()[:6]
    package = Package.objects.filter().all()[:6]
    tour_type = TourType.objects.filter().all()
    place = Place.objects.filter().all()
    domestic_packages = Package.objects.filter(tour_type=1)
    international_packages = Package.objects.filter(tour_type=2)
    hajj_packages = Package.objects.filter(tour_type=3)  
    context = {
        'testimonials' : testimonials,
        'gallery' : gallery,
        'packages' : package,
        'tour_type' : tour_type,
        'place' : place,
        'domestic_packages' : domestic_packages,
        'international_packages' : international_packages,
        'hajj_packages' : hajj_packages
    }
    return render(request,'web/index.html',context)

def about(request):
    testimonials = Testimonial.objects.filter().all()[:3]
    context = {
        'testimonials' : testimonials,
    }
    return render(request,'web/about.html',context)

def services(request):
    services = Service.objects.filter().all()
    context = {
        'services' : services
    }
    return render(request,'web/services.html',context)

def packages(request):
    packages = Package.objects.filter().all()
    tour_type = TourType.objects.filter().all()
    domestic_packages = Package.objects.filter(tour_type=1)
    international_packages = Package.objects.filter(tour_type=2)
    hajj_packages = Package.objects.filter(tour_type=3)
    context = {
        'packages' : packages,
        'tour_type' : tour_type,
        'domestic_packages' : domestic_packages,
        'international_packages' : international_packages,
        'hajj_packages' : hajj_packages
    }
    return render(request,'web/packages.html',context)

def blog(request):
    blogs = Blog.objects.filter().all()
    context = {
        'blogs' : blogs
    }
    return render(request,'web/blog.html',context)

# def guide(request):
#     guides = Guide.objects.filter().all()
#     context = {
#         'guides' : guides
#     }
#     return render(request,'web/guide.html',context)

def gallery(request):
    gallery = Gallery.objects.filter().all()
    context = {
        'gallery' : gallery
    }
    return render(request,'web/gallery.html',context)

def contact(request):
    return render(request,'web/contact.html')

def service_details(request,id):
    service_details = Service.objects.get(id=id)
    context = {
        'service_details' : service_details
    }
    return render(request,'web/service-details.html',context)

def blog_details(request,id):
    blog = Blog.objects.get(id=id)
    context = {
        'blog' : blog
    }
    return render(request,'web/blog-details.html',context)

def package_details(request,id):
    package_details = Package.objects.get(id=id)
    context = {
        'package_details' : package_details
    }
    return render(request,'web/package-details.html',context)

def gallery_single(request,id):
    place = Place.objects.get(id=id)
    images = Gallery.objects.filter(place = place.id)
    print(place)
    context = {
        'images' : images,
        'place' : place
    }
    return render(request,'web/gallery-single.html',context)