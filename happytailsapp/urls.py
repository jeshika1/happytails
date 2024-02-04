from django.contrib import admin
from django.urls import path
from happytailsapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path("",views.index, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_views, name='login'),
    path('page/', views.page, name='page'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),
    path('signup/', views.signup, name='signup'),
    path('addyour/', views.addyour, name='addyour'),
    path('description/', views.description, name='description'),
    path('logout/', views.logout, name='logout'),
    path('linear_search/', views.linear_search, name='linear_search'),
     path('process/<int:process_id>/', views.processStatusView, name='process_status'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)