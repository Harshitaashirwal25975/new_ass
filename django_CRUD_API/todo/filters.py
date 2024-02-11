from django_filters import rest_framework as filters
from .models import Todo


# We create filters for each field we want to be able to filter on
class TodoFilter(filters.FilterSet):
    task = filters.CharFilter(lookup_expr='icontains')
    genre = filters.CharFilter(lookup_expr='icontains')
    no = filters.NumberFilter()
    date__gt = filters.NumberFilter(field_name='year', lookup_expr='gt')
    date__lt = filters.NumberFilter(field_name='year', lookup_expr='lt')
    owner__username = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Todo
        fields = ['task', 'genre', 'no', 'date__gt', 'date__lt', 'owner__username']

