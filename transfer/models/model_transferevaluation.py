
from django.db import models
from .model_course import Course
from .model_major_requirement import Major_requirement
from .model_approver import Approver

class Transferevaluation(models.Model):
    """

    table name is Transferevaluation
    transfer_eval_id( is the Primarykey
    school_id is ForeignKey
    approver_id is ForgeinKey
    major_req_id is Forgeinkey

    """
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    major_req_id = models.ForeignKey(Major_requirement, on_delete=models.CASCADE)
    sem_year_taken = models.CharField(max_length=8, blank=True, null=True)
    expiration_date = models.DateField()
    approved_status = models.CharField(max_length=1, blank=True, null=True)
    comment = models.CharField(max_length=150, blank=True, null=True)
    approver_id = models.ForeignKey(Approver, on_delete=models.CASCADE)

def __str__(self):
    return self.course_id
