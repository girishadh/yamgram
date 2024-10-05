from django import forms
from .models import Post, Comments

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'content' : forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comments
        fields = ['content']

        widgets = {
            'content' : forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }