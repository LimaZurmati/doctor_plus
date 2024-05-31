from . import views
from django.urls import path


urlpatterns = [
    path('', views.DoctorList.as_view(), name='home'),
    path('add_doctor/', views.AddNewDoctor.as_view(), name='add_doctor'),
    #path('', views.ContactForm.as_view(), name='contact'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
        views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
        views.comment_delete, name='comment_delete'),    
    
]
