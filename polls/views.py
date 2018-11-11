from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def list_polls(request):
    resp = 'List all questions successfully!'
    return HttpResponse(content=resp, status=200)


def add_polls(request):
    resp = 'Add question(%s) successfully!' % 11
    return HttpResponse(content=resp, status=200)


def get_polls(request, polls_id):
    resp = 'Get question(%s) successfully!' % polls_id
    return HttpResponse(content=resp, status=200)


def update_polls(request, polls_id):
    resp = 'Update question(%s) successfully!' % polls_id
    return HttpResponse(content=resp, status=200)


def delete_polls(request, polls_id):
    resp = 'Delete question(%s) successfully!' % polls_id
    return HttpResponse(content=resp, status=200)
