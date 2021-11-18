from django import forms
from .models import *

class PostForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['category'].empty_label = "Категория не выбрана"
        self.fields['author'].empty_label = "Автор не выбран"

    class Meta:
        model = Post
        fields = ('title', 'snippet', 'author', 'body', 'category', 'photo', )
        widgets = {
        'title': forms.TextInput(attrs={'class':'form-control'}),
        'snippet': forms.TextInput(attrs={'class':'form-control'}),
        'body': forms.Textarea(attrs={'class':'form-control'}),
        'author': forms.Select(attrs={'class':'form-control'}),
        'category': forms.Select(attrs={'class':'form-control'})
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'photo', 'snippet')
        widgets = {
        'title': forms.TextInput(attrs={'class':'form-control'}),
        'snippet': forms.TextInput(attrs={'class':'form-control'}),
        'body': forms.Textarea(attrs={'class':'form-control'}),
        'author': forms.Select(attrs={'class':'form-control'})
        }

class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
        'name': forms.TextInput(attrs={'class':'form-control'}),
        'body': forms.Textarea(attrs={'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].label = "Ваше имя"
        self.fields['body'].label = "Текст комментария"
        