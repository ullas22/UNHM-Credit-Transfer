from ..models.model_course import Course
from django.shortcuts import render
from ..filters.school_filter import SchoolFilter

def search(request):
    school_list = Course.objects.all()
    school_filter = SchoolFilter(request.GET, queryset=school_list)
    return render(request, 'course_html/course_search.html', {'filter': school_filter})
