from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models


# Create your views here.

def importExcel(request):
    return HttpResponse('test')

