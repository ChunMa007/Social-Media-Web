from django import forms
from .models import Post, Comment

class CreatePostForm(forms.ModelForm):
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control form-control-lg', 'rows': '1', 'placeholder': "What's on your mind?"}),
        label="",
        )
    
    class Meta:
        model = Post
        fields = ['content']

class CreateCommentForm(forms.ModelForm):
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '1', 'cols': '100', 'placeholder': 'Comment'}),
        label = ""
    )
    
    class Meta:
        model = Comment
        fields = ['content']