from django.contrib import admin

# Register your models here.
from polls.models import PollsModel


class PollsAdminModel(admin.ModelAdmin):
    list_display = ['vote_id', 'issue', 'user', 'email', 'vote_choice', 'vote_date']
    search_fields = ['vote_id', 'issue', 'user', 'email', 'vote_choice', 'vote_date']
    list_display_links = ['vote_id', 'user']


admin.site.register(PollsModel, PollsAdminModel)
