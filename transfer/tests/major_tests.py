from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from ..models.model_major import Major

class MajorTests(TestCase):
    def setup(cls):
        super().setup()
        cls.major_id = Major.objects.create(major_name ='Biological Sciences').pk

    def test_string(self):
        major = Major.objects.get(major_id = self.major_id)
        self.assertEqual(str(major), major.major_name)

    def test_url(self):
        major = Major.objects.get(major_id = self.major_id)
        self.assertEqual(f'/major/{self.major_id}', '/major/1')
