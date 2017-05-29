from django import forms
from django.contrib.auth.models import User
from rango.models import Page, Category, UserProfile


class CategoryForm(forms.ModelForm):
    name = forms.CharField(widget = forms.TextInput(attrs={'max_length': 128,
                                     'help_text': 'Please enter the category name.',
                                     'class': 'form-control',}))
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)
        # widgets = {  # to style the form in CSS
        #     # Apparently this may be bad practice due to mixing of presentation and business logic.
        #     'name': forms.CharField(attrs={'class': 'form-control'}),
        # }



class PageForm(forms.ModelForm):
    title = forms.CharField(widget = forms.TextInput(attrs={'max_length': 128,
                                     'help_text': 'Please enter the title of the page.',
                                     }))
    url = forms.URLField(widget = forms.TextInput(attrs={'help_text': 'Please enter the URL of the page.',
                                     'class': 'form-control',}))
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('category',)
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')
        # I think I should have done it as forms.URLField(widget = forms.TextInput(attrs={'max_length': 128})
        # 'url': forms.URLField(attrs={'class': 'form-control'})
        # widgets = {  # to style the form in CSS
        #     # Apparently this may be bad practice due to mixing of presentation and business logic.
        #     'title': forms.CharField(attrs={'class': 'form-control'}),
        #     'url': forms.URLField(attrs={'class': 'form-control'}),
        # }

    def clean(self):
        # I'm assuming this is equivalent to calling super.clean() first?
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 'http://', prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')