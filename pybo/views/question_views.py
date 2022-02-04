from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question


@login_required(login_url='common:login')
def question_create(request):
    pass


@login_required(login_url='common:login')
def question_modify(request, question_id):
    pass


@login_required(login_url='common:login')
def question_delete(request, question_id):
    pass