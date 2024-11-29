from django.urls import path
from . import views

urlpatterns = [
    path('', views.DoctorList.as_view(), name='home'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
    path('post/<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='edit_comment'),
]