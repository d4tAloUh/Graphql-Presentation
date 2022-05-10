from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Author(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=_('Name')
    )
    surname = models.CharField(
        max_length=255,
        verbose_name=_('Surname')
    )
    birth_date = models.DateField(
        verbose_name=_("Birth date"),
    )

    class Meta:
        unique_together = ('name', 'surname')

    def __str__(self):
        return f"{self.name} {self.surname}"


class Book(models.Model):
    isbn = models.CharField(
        verbose_name=_('ISBN'),
        max_length=13,
        validators=[MinLengthValidator(13)],
        primary_key=True
    )

    title = models.CharField(
        max_length=255,
        verbose_name=_('Title'),
    )
    description = models.CharField(
        max_length=512,
        verbose_name=_('Description'),
    )
    authors = models.ManyToManyField(
        Author,
        verbose_name=_('Authors'),
        related_name='books',
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Created at")
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Updated at")
    )

    def __str__(self):
        return f"{self.isbn} : {self.title}"


class Review(models.Model):
    rating = models.PositiveIntegerField(
        verbose_name=_('Rating'),
    )
    user = models.ForeignKey(
        User,
        verbose_name=_('User'),
        related_name='reviews',
        on_delete=models.CASCADE
    )
    book = models.ForeignKey(
        Book,
        verbose_name=_('Book'),
        related_name='reviews',
        on_delete=models.CASCADE
    )
    description = models.CharField(
        max_length=512,
        verbose_name=_('Description'),
    )

    def __str__(self):
        return f"{self.rating} review on {self.book.title}"
