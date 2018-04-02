from django import forms
from crispy_forms.helper import FormHelper
from core.models import Post
from crispy_forms.layout import Submit, Layout, Div, HTML

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text','title']
        exclude = ('author', 'author_photo', 'created_date', 'published_date')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "post_form";
        self.helper.include_media = False
        self.helper.add_input(Submit('submit', 'Salva', css_class="pull-right"))
        self.helper.layout = Layout(
            Div(
                Div('title', css_class='uk-form-width-large'),
                css_class='uk-form-controls'
            ),
            Div(
                Div('text', css_class='uk-form-width-large'),
                css_class='uk-form-controls'
            ),
        )

    def save(self):
        return super(PostForm, self).save()
