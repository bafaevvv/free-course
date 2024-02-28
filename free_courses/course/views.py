from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import Q

def index(request):
      course_list = Course.objects.all().order_by('?')
      context = {
            'course_list': course_list
      }
      return render(request, 'course/index.html', context)
      
def course(request):
      course_name = request.GET.get('search')
      course = Course.objects.all()
      print(course_name)
      if course_name != '' and course_name is not None:
            course = course.filter(Q(title__icontains=course_name))
      return render(request, 'course/courses.html', {'course':course})

def course_detail(request, course_id):
      course = Course.objects.get(pk=course_id)
      context = {
            'course': course
      }
      return render(request, 'course/course_detail.html', context)

def category(request):
      return HttpResponse('<h1>This is an category view!</h1>')

def category_detail(request, pk):
      category_list = Category.objects.get(pk=pk)
      course_set = Course.objects.all()
      context = {
            'category_list': category_list,
            'course_set': course_set
      }
      return render(request, 'course/category_detail.html', context)


