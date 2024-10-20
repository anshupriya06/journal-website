from django.urls import path
from . import views
from .views import index


urlpatterns = [
   path('', views.index, name='index'),  # Home page (index view)
    path('pdfs/', views.pdf_list, name='pdf_list'),  # PDF list page
    path('upload/', views.upload_jaser, name='upload_jaser'),  # Upload new PDF
    path('jasers/', views.jaser_list, name='jaser_list'),  # JASER list page
    path('jasers/edit/<int:jaser_id>/', views.edit_jaser, name='edit_jaser'),  # Edit path
    path('jasers/delete/<int:jaser_id>/', views.delete_jaser, name='delete_jaser'),  # Delete path
]


   

