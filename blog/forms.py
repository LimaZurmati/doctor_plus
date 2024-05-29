from .models import Comment
from .models import ContactRequest
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ('name', 'email', 'message', 'age', 'gender',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)