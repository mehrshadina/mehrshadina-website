# blog/forms.py

from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"name":"author", "type":"text", "class": "form-control input-mf", "id":"inputName", "placeholder": "نام *"}
        ),
    )
    email = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"name":"email", "type":"email", "class": "form-control input-mf", "id":"inputEmail", "placeholder": "ایمیل *"}
        ),
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"name":"message", "class": "form-control input-mf", "id":"textMessage", "cols":"45", "rows":"8", "placeholder": "پیام خود را اینجا بنویسید *"}
        )
    )