from django.contrib import admin

# Register your models here.
from issue.models import IssueModel


class IssueAdminModel(admin.ModelAdmin):
    list_display = ['issue_id', 'issue_name', 'choice']
    search_fields = ['issue_id', 'issue_name']
    list_display_links = ['issue_id', 'issue_name']


admin.site.register(IssueModel, IssueAdminModel)
