from django.db import models
from .model_major import Major

class School(models.Model):
    """
    table name is school
    school_id is the Primarykey
    """
    school_id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=100)
    state_name = models.CharField(max_length=100)

    def __str__(self):
        return self.school_name

    def get_absolute_url(self):
        '''
        Returns the url for school_name
        '''
        return reverse('school_name', args=[str(self.id)])
