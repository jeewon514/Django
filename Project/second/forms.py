# from django import forms
from django.forms import ModelForm
from second.models import Post
from django.utils.translation import gettext_lazy as _

# class PostForm(forms.Form):
#     # valid 체크(유효성)
#     title = forms.CharField(label='제목',max_length=20)  #max_length: 제목 20글자까지 입력 가능
#     content = forms.CharField(label='내용', widget=forms.Textarea)    #어떤 위젯 사용 할지(Textarea)


class PostForm(ModelForm):
    class Meta:     # ModelForm 안에 class Meta를 정의!!(외우기, 규칙임)
        model = Post
        fields = ['title', 'content']

        labels = {
            'title':_('제목'),    # 텍스트('제목') 가져올 때 '_' 사용
            'content':_('내용'),
        }
        help_text = {
            'title': _('제목을 입력해주세요.'),  
            'content': _('내용을 입력해주세요'),
        }
        error_message = {
            'max_length': _('제목이 너무 깁니다. 30자 이하로 해주세요.'),
        }