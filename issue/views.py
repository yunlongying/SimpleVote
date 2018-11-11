from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


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
