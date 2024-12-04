from django.core.exceptions import ValidationError  # Import ValidationError
from django.utils.translation import gettext_lazy as _  # Import translation function
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Status choices for posts
STATUS = ((0, "Draft"), (1, "Published"))

class Category(models.Model):
    """Category model"""
    category_name = models.CharField(max_length=60)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Post(models.Model):
    """Post model"""
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)  # Allow blank for slug
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    doctor_image = CloudinaryField('image', default='placeholder', blank=False)
    nationality = models.CharField(max_length=100, null=True)
    service = models.CharField(max_length=200, null=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)  # Ensure a default ID
    email = models.EmailField(max_length=254, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def clean(self):
        # Validate title for invalid characters
        invalid_chars = ['.', ',', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
        if any(char in self.title for char in invalid_chars):
            raise ValidationError(_('Title cannot contain special characters like ".", ",", etc.'))


class ContactRequest(models.Model):
    """ContactRequest model"""
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)  # Changed to CharField for better control
    age = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"


class Comment(models.Model):
    """Comment model"""
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body[:20]}... by {self.author}"  # Show only the first 20 characters