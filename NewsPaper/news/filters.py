from django_filters import FilterSet, ModelChoiceFilter, DateTimeFilter
from .models import Post, Category
from django.forms import DateTimeInput


class PostFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label='Пост не ранее',
        widget=DateTimeInput(
            format='%y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    categoryType = ModelChoiceFilter(
        field_name='categoryType',
        queryset=Category.objects.all(),
        label='Категория',
        empty_label='всё'
    )

    class Meta:
        model = Post
        fields = ['title']



