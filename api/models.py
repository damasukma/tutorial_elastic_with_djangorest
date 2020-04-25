from django.db import models

# Create your models here.

class ProjectApplication(models.Model):

    project_name = models.CharField(max_length=100)
    path_file = models.CharField(max_length=255)
    status_log = models.CharField(max_length=15)

    class Meta:
        def __unicode__(self):
            return self.project_name
