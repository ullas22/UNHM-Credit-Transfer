from django.contrib import admin
from django.urls import path
from .views.major_requirement_views import (
    Major_requirementCreateView,
    Major_requirementListView,
    Major_requirementUpdateView,
    Major_requirementDeleteView,
    Major_requirementDetailView,
 )
from .views.school_views import (
    SchoolListView,
    SchoolCreateView,
    HomeListView,
    SchoolDetailView,
    SchoolUpdateView,
    SchoolDeleteView,
    )
from .views.major_views import (
    MajorCreateView,
    MajorListView,
    MajorDetailView,
    major_update,
    major_delete,
    )
from .views.course_views import (
    course_list,
    course_create,
    course_delete,
    course_update,
    course_detail,
    )
from .views.transfer_evaluation_views import (
    transfereval_list,
    transfereval_create,
    transfereval_delete,
    transfereval_update,
    transfereval_detail,
    )
from .views.approver_views import (
    ApproverCreateView,
    ApproverListView,
    ApproverDetailView,
    ApproverUpdateView,
    ApproverDeleteView,
    )
from .views.import_excel import import_file
from .views.result_views import result
from .views.search_view import search
urlpatterns = [
    path('import', import_file, name='import'),
    path('', HomeListView.as_view(), name='home'),
    path('result/', result),
    #approver resources
    path('approver/', ApproverListView.as_view(), name='approver_home'),
    path('approver/<int:pk>/', ApproverDetailView.as_view(),
         name='approver_detail'),
    path('approver-create', ApproverCreateView.as_view(), name='approver_new'),
    path('approver-update/<int:pk>/', ApproverUpdateView.as_view(),
         name='approver_update'),
    path('approver-delete/<int:pk>/', ApproverDeleteView.as_view(),
         name='approver_delete'),
    #school resources
    path('school/', SchoolListView.as_view(), name='school_home'),
    path('school/<int:pk>/', SchoolDetailView.as_view(), name='school_detail'),
    path('school-create', SchoolCreateView.as_view(), name='school_new'),
    path('school-update/<int:pk>/', SchoolUpdateView.as_view(),
         name='school_update'),
    path('school-delete/<int:pk>/', SchoolDeleteView.as_view(),
         name='school_delete'),

    ### search
    path('course/search/', search, name='course_home'),

    #major resources
    path('major/', MajorListView.as_view(), name='major_home'),
    path('major-update/<int:pk>/', major_update, name='major_update'),
    path('major-delete/<int:pk>/', major_delete, name='major_delete'),
    path('major/<int:pk>/', MajorDetailView.as_view(), name='major_detail'),
    path('major-create', MajorCreateView.as_view(), name='major_new'),
    #course resources
    path('course/', course_list, name='course_home'),
    path('course/<int:pk>/', course_detail, name='course_detail'),
    path('course-update/<int:pk>/', course_update, name='course_update'),
    path('course-delete/<int:pk>/', course_delete, name='course_delete'),
    path('course-create', course_create, name='course_new'),

    #### transfer evaluation
    path('transfereval/', transfereval_list, name='transfereval_home'),
    path('transfereval/<int:pk>/', transfereval_detail,
         name='transfereval_detail'),
    path('transfereval-update/<int:pk>/', transfereval_update,
         name='transfereval_update'),
    path('transfereval-delete/<int:pk>/', transfereval_delete,
         name='transfereval_delete'),
    path('transfereval-create', transfereval_create, name='transfereval_new'),

    #major_requirement resources
    path('major_requirement/', Major_requirementListView.as_view(),
         name='major_requirement_home'),
    path('major_requirement/<int:pk>/', Major_requirementDetailView.as_view(),
         name='major_requirement_detail'),
    path('major_requirement-create', Major_requirementCreateView.as_view(),
         name='major_requirement_new'),
    path('major_requirement-update/<int:pk>/', Major_requirementUpdateView.as_view(),
         name='major_requirement_update'),
    path('major_requirement-delete/<int:pk>/', Major_requirementDeleteView.as_view(),
         name='major_requirement_delete'),
]
