from django import forms
from .models import Post,Notice_category,Word_filtering,Comment,File,Imges
from ckeditor.widgets import CKEditorWidget

from ckeditor.fields import RichTextField
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','content']
        widgets = {
            'title':forms.TextInput(attrs={'class': 'title form-control','id': 'title', 'placeholder': '제목을 입력하세요'}),
            'content':forms.CharField(widget=CKEditorWidget()),
        }
        labels = {
            'title': '제목',
            'content': '내용',
        }
class FlieForm(forms.ModelForm):
    class Meta:
        model =File
        fields =['file',]
        widgets = {
            'file': forms.FileInput(attrs={'class' :' file'}),
        }
        labels = {
            'file': ''
        }

class ImgesForm(forms.ModelForm):
    class Meta:
        model =Imges
        fields =['imges',]
        widgets = {
            'imges': forms.FileInput(attrs={'class' :'imges','accept':'image/*'}),
        }
        labels = {
            'imges': ''
        }
      
class Word_filteringForm(forms.ModelForm):
    class Meta:
        model = Word_filtering
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'text form-control',  'row': 0, 'cols': 100,'style': 'resize:none;'}),
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class':'comment form-control', 'placeholder': '댓글 을 입력해주세요','row':0,'cols':100,'style':'resize:none;'}),
        }
        labels = {
            'text':'댓글'
        }

class Notice_categoryForm(forms.ModelForm):
    class Meta:
        model = Notice_category
        fields = ['title','list_auth','detail_auth','writer_auth']
        widgets = {
            'title': forms.TextInput(attrs={'class':'title form-control' }),
            'list_auth':forms.Select(attrs={'class':'list_auth form-control'}),
            'detail_auth': forms.Select(attrs={'class': 'detail_auth form-control'}),
            'writer_auth': forms.Select(attrs={'class': 'writer_auth form-control'}),
        }

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='search_word',widget=forms.TextInput(attrs={'class':'form-control','placeholder': '검색어를 입력해주세요'}))
