
from django.db import models

# Create your models here.
from jsonfield import JSONField


class IssueModel(models.Model):
    class Meta:
        db_table = 'ISSUE'

    issue_id = models.CharField(db_column='ISSUE_ID', max_length=200, primary_key=True)
    issue_name = models.CharField(db_column='ISSUE_NAME', max_length=200, blank=False, null=False)
    choice = JSONField(db_column='choice', default=[])
    create_date = models.DateTimeField(db_column='CREATE_DATE')

    def __str__(self):
        return self.issue_name
