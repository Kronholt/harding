import django_filters
from .models import Post
from django_filters import DateFilter, CharFilter


class PostFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="start_date", lookup_expr='gte'),
    end_date = DateFilter(field_name="end_date", lookup_expr='lte'),
    # tag = CharFilter(field_name="tags", lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['content_date_start','content_date_end', 'tags']
    