from django.forms import DateInput, ModelForm, NumberInput, TextInput, URLInput

from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        widgets = {
            "title": TextInput(),
            "author": TextInput(),
            "publish_date": DateInput(attrs=dict(type="date")),
            "isbn": TextInput(),
            "page_num": NumberInput(),
            "cover_link": URLInput(),
            "publish_lang": TextInput(),
        }
