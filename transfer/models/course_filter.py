import django_filters
from .model_course import Course

class CourseFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Course
        fields = ['course_id', 'school_id', 'subject_number', 'title']
