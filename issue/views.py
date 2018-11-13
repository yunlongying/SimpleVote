import json
import uuid
from datetime import datetime

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
    issues = IssueModel.objects.all()
    issue_list = []
    for issue in issues:
        issue_list.append({
            'issue_id': issue.issue_id,
            'issue_name': issue.issue_name,
            'choice': issue.choice,
            'create_data': str(issue.create_date)
        })
    resp = 'List all questions successfully!'
    return HttpResponse(content=json.dumps(issue_list), status=200)


def add_issue(request):
    issue_id = uuid.uuid4()
    data = json.loads(request.body)
    issue_name = data.get('issue_name')
    choice = data.get('choice')
    IssueModel.objects.create(issue_id=issue_id, issue_name=issue_name, choice=choice, create_date=datetime.now())
    resp = 'Add question(%s) successfully!' % issue_id
    return HttpResponse(content=resp, status=200)


def get_issue(request, issue_id):
    question = IssueModel.objects.get(issue_id=issue_id)
    context = {'question': question}
    return render(request, 'issue/issue_detail.html', context)


def update_issue(request, issue_id):
    resp = 'Update question(%s) successfully!' % issue_id
    return HttpResponse(content=resp, status=200)


def delete_issue(request, issue_id):
    resp = 'Delete question(%s) successfully!' % issue_id
    return HttpResponse(content=resp, status=200)
