from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from ..models.model_approver import Approver

class ApproverTests(TestCase):
    def setup(cls):
        super().setup()
        cls.approver_id = Approver.objects.create(approver_name = 'paul').pk

    def test_string(self):
        approver = Approver.objects.get(approver_id=self.approver_id)
        self.assertEqual(str(approver), approver.approver_name)

    def test_url(self):
        approver = Approver.objects.get(Approver_id = self.approver_id)
        self.assertEqual(f'/approver/{self.approver_id}', approver.get_absolute_url())
