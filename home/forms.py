from django import forms
from .models import comments,  video_upload

class video_upload_form(forms.ModelForm):
    class Meta:
        model = video_upload
        fields = ['title', 'description', 'video', 'thumbnail']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.video.name = f"{self.cleaned_data['title']}.mp4"

        # Handle thumbnail upload
        if 'thumbnail' in self.files:
            instance.thumbnail = self.files['thumbnail']
            instance.thumbnail.name = f"{self.cleaned_data['title']}_thumbnail.jpg"

        if commit:
            instance.save()
        return instance

class commentsform(forms.ModelForm):
    class Meta:
        model = comments
        fields = ['body']
   
