from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)
        widgets = {
            "body": forms.Textarea(attrs={"rows": 4, "placeholder": "Enter your comment here..."}),
        }

    def clean_body(self):
        body = self.cleaned_data.get("body")
        if not body or not body.strip():
            raise forms.ValidationError("Comment cannot be empty.")
        return body
