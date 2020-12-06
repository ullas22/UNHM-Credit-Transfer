from ..models.model_course import Course
import django_filters

class SchoolFilter(django_filters.FilterSet):
    school_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Course
        fields = ['school_id']
