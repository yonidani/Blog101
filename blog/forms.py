from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title',  'title_tag', 'author', 'body', 'header_image')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'This is title on your post '}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is what will go on your tab'}),
           	'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }