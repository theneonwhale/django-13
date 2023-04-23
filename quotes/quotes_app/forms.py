from django.db.models import ForeignKey, CASCADE
from django.forms import ModelForm, CharField, TextInput, ModelMultipleChoiceField, SelectMultiple, ChoiceField, Select, \
    ModelChoiceField

from .models import Tag, Quote, Author


class TagForm(ModelForm):
    tag = CharField(max_length=100, widget=TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Tag
        fields = ['tag']


class AuthorForm(ModelForm):
    fullname = CharField(max_length=1000, required=True, widget=TextInput(attrs={"class": "form-control"}))
    born_date = CharField(max_length=1000, widget=TextInput(attrs={"class": "form-control"}))
    born_location = CharField(max_length=1000, widget=TextInput(attrs={"class": "form-control"}))
    description = CharField(max_length=1000, widget=TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(ModelForm):
    quote = CharField(max_length=1500, widget=TextInput(attrs={"class": "form-control"}))
    tags = ModelMultipleChoiceField(
        queryset=Tag.objects.all().order_by('tag'),
        to_field_name="tag",
        widget=SelectMultiple(attrs={"class": "form-select"})
    )
    author = ModelChoiceField(
        queryset=Author.objects.all().order_by('fullname'),
        to_field_name="id",
        widget=Select(attrs={"class": "form-select"})
    )

    class Meta:
        model = Quote
        fields = ['quote', 'tags', 'author']
