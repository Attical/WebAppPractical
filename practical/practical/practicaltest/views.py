from django.shortcuts import render
from django.http import HttpResponse
from practicaltest.models import Course

def index(request):
    category_list = Course.objects.all()

    context_dict = {}
    context_dict['Courses'] = category_list

    return render(request, 'practicaltest/index.html', context=context_dict)

