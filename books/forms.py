from django import forms

from books.models import Book, Author, Review


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
