from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher

def students_list(request):
    template = 'school/students_list.html'
    data1 = Student.objects.all()
    context = {
        'students': data1,
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)

# class StudentView(ListView):
#     model = Student
#     template_name = 'school/students_list.html'





