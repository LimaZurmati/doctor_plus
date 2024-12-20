from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, AddDoctorForm
from .forms import ModelForm
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required  # Import the decorator
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

"""Class add_doctor"""
@login_required  # Add the decorator here
def add_doctor(request):
    if request.method == 'POST':
        adddoctorform = AddDoctorForm(request.POST, request.FILES)
        if adddoctorform.is_valid():
            new_doctor = adddoctorform.save(commit=False)
            new_doctor.author = request.user
            new_doctor.slug = new_doctor.title.replace(" ", "-" ).lower()
            new_doctor.save()
            messages.success(request, "Doctor added successfully!")
            return redirect('home')
    else:
        adddoctorform = AddDoctorForm()

    context = {
        'adddoctorform': adddoctorform
    }

    return render(request, 'blog/add_doctor.html', context)

"""Class DoctorList"""
class DoctorList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

"""Class post_details"""
def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment posted and awaiting approval')
    else:
        comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form
        }
    )

"""Comment Edit"""
@login_required  # Add the decorator here
def comment_edit(request, slug, comment_id):
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

"""Comment Delete"""
@login_required  # Add the decorator here
def comment_delete(request, slug, comment_id):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted now!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))