from django.db import models
from .model_school import School

class Course(models.Model):
    """

    table name is Course
    course_id is the Primarykey
    school_id is ForeignKey
    approver_id is ForgeinKey
    major_req_id is Forgeinkey

    """
    course_id = models.AutoField(primary_key=True)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE, null=True, default=None)
    subject_number = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)


def __str__(self):
    return self.course_id
