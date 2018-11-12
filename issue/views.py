from django.http import HttpResponse
from django.shortcuts import render
# from django.template import loader

from issue.models import IssueModel


def index(request):
    latest_question_list = IssueModel.objects.order_by('-create_date')[:5]
    # template = loader.get_template('issue/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))
    context = {'latest_question_list': latest_question_list}
    return render(request, 'issue/index.html', context)


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
