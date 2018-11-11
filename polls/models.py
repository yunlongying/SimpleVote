from django.db import models

# Create your models here.
from issue.models import IssueModel


class PollsModel(models.Model):
    class Meta:
        db_table = 'POLLS'

    vote_id = models.CharField(db_column='VOTE_ID', max_length=200, primary_key=True)
    issue = models.ForeignKey(IssueModel, on_delete=models.CASCADE)
    user = models.CharField(db_column='USER', max_length=200, blank=True, null=True)
    email = models.CharField(db_column='EMAIL', max_length=200, blank=True, null=True)
    vote_choice = models.IntegerField(default=0)
    vote_date = models.DateTimeField(db_column='VOTE_DATE')

    def __str__(self):
        return self.vote_id
