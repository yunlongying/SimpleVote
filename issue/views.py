from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from issue.models import IssueModel


def index(request):
    latest_question_list = IssueModel.objects.order_by('-create_date')[:5]
    # output = ', '.join([q.issue_name for q in latest_question_list])
    template = loader.get_template('issue/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    tmp = template.render(context, request)
    return HttpResponse(template.render(context, request))
    # return HttpResponse(output)


def list_issue(request):
    resp = 'List all questions successfully!'
    return HttpResponse(content=resp, status=200)


def add_issue(request):
    resp = 'Add question(%s) successfully!' % 11
    return HttpResponse(content=resp, status=200)


def get_issue(request, issue_id):
    resp = 'Get question(%s) successfully!' % issue_id
    return HttpResponse(content=resp, status=200)


def update_issue(request, issue_id):
    resp = 'Update question(%s) successfully!' % issue_id
    return HttpResponse(content=resp, status=200)


def delete_issue(request, issue_id):
    resp = 'Delete question(%s) successfully!' % issue_id
    return HttpResponse(content=resp, status=200)
