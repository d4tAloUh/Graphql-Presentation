from django import forms

from books.models import Book, Author, Review


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('isbn', 'title', 'description',
                  'authors')


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name',)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'user', 'book',
                  'description')
