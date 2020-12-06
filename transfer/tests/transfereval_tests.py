from django.test import Client
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from ..models.model_major import Major
from ..models.model_course import Course
from ..models.model_approver import Approver
from ..models.model_major_requirement import Major_Requirement
from ..models.model_transfereval import Transfereval

class TransferevalTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        major_req = Major_Requirement.objects.create(description='Systems')
        approver = Approver.objects.create(approver_name='Approver Object (1)')
        cls.transfereval = Transfereval.objects.create(
            major_req_id=major_req,sem_year_taken ='sp 20', expiration_date='2020-10-20 00:00:00', approver_id=approver).pk

    def test_string_representation(self):
        transfereval = Transfereval.objects.get(transfer_eval_id=self.transfer_eval_id)
        self.assertEqual(str(transfereval), transfereval.sem_year_taken)
