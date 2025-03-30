from django import forms
from .models import Post , CommentPost

class PostForm(forms.Form):
    class Meta:
        model = Post
        fields = ['title' , 'content' , 'image']


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentPost
        fields = ['comment'] # add comment to the post