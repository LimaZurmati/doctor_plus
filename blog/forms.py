from django import forms
from django.forms import ModelForm
from .models import Comment, Post
from .models import ContactRequest
from django_summernote.widgets import SummernoteWidget

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ('name', 'email', 'message', 'age', 'gender',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


      

class AddDoctorForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())    

    class Meta:
        model = Post
        fields = ['title', 'email', 'service', 'doctor_image', 'content', 'categories', 'status']
    

widgets = {
    'title': forms.TextInput(attrs={'class': 'form-control'}),
    'content': forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Write content here ...',
    }),
    'categories': forms.SelectMultiple(attrs={'class': 'form-select'}),
    'status': forms.Select(attrs={'class': 'form-control'}),
}