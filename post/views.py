from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import CreatePostForm, CreateCommentForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):    
    if request.method == "POST":
        create_post_form = CreatePostForm(request.POST or None)
        create_comment_form = CreateCommentForm(request.POST or None)
        
        if 'create_post' in request.POST and create_post_form.is_valid():
            post_form = create_post_form.save(commit=False)
            post_form.author = request.user
            post_form.save()
            
            return redirect('post:home')
        
        elif 'create_comment' in request.POST and create_comment_form.is_valid():
            post_id = request.POST.get('post_id')
            post = get_object_or_404(Post, id=post_id)
            comment_form = create_comment_form.save(commit=False)
            comment_form.user = request.user
            comment_form.post = post
            comment_form.save()
            
            return redirect('post:home')
        
    else:
        create_post_form = CreatePostForm()
        create_comment_form = CreateCommentForm()
    
    post_list = Post.objects.order_by('-created_at')
    
    return render(request, 'home.html', {
        'post_list': post_list,
        'create_post_form': create_post_form,
        'create_comment_form': create_comment_form,
        # 'post_comment': post_comment
    })