from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from post.models import Post
from post.forms import CreateCommentForm
from django.contrib.auth.decorators import login_required

@login_required
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    user_posts = Post.objects.filter(author=user)
    
    if request.method == "POST":
        create_comment_form = CreateCommentForm(request.POST)
        
        if 'create_comment' in request.POST and create_comment_form.is_valid():
            post_id = request.POST.get('post_id')
            post = get_object_or_404(Post, id=post_id)
            create_comment = create_comment_form.save(commit=False)
            create_comment.user = request.user
            create_comment.post = post
            create_comment_form.save()
            
            return redirect('user_profile:user_profile', user.username)
        
        if 'add_friend' in request.POST:
            pass
    
    else:
        create_comment_form = CreateCommentForm()
    
    return render(request, 'user_profile.html', {
        'user': user,
        'user_posts': user_posts,
        'create_comment_form': create_comment_form,
    })