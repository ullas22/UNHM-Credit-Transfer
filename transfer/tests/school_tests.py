from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from ..models.model_school import School

class SchoolTests(TestCase):
    def setup(cls):
        super().setup()
        cls.school_id = School.objects.create(school_name = 'UNH').pk

    def test_string(self):
        school = School.objects.get(school_id=self.school_id)
        self.assertEqual(str(school), school.school_name)

    def test_url(self):
        school = School.objects.get(school_id = self.school_id)
        self.assertEqual(f'/school/{self.school_id}', school.get_absolute_url())
