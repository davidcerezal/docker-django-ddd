from django import forms
from odds.models import DemoModel


class SomeForm(forms.ModelForm):
    class Meta:
        model = DemoModel
        fields = '__all__'

    def save(self, commit=True):
        image = self.cleaned_data.pop('image')
        instance = super().save(commit=True)
        # instance.save_m2m()
        print(image)
        instance.image = image
        instance.save()
        return instance
