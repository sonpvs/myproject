from django import forms
from .models import Post, Baby, Khaosat


class Post_Form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content')


class Baby_Form(forms.ModelForm):
    class Meta:
        model = Baby
        fields = ('age','weight')


class Khaosat_Form(forms.ModelForm):
    class Meta:
        model = Khaosat
        fields = '__all__'
