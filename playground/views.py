from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    x=1
    y=1
    print('yes')
    return HttpResponse("hello mama")

from django.http import JsonResponse
from .models import FeeSet, Student

def get_fees_amount(request):
    fee_category_id = request.GET.get('fee_category_id')
    fee_set = FeeSet.objects.filter(pk=fee_category_id).first()
    print('mama')
    if fee_set:
        return JsonResponse({'fees_amount': fee_set.fee_amount})
    return JsonResponse({'fees_amount': None})

def get_fee_categories(request):
    student_id = request.GET.get('student_id')
    if student_id:
        try:
            student = Student.objects.get(pk=student_id)
            fee_categories = FeeSet.objects.filter(class_category=student.section)
            data = {str(category.id): str(category) for category in fee_categories}
            print(data)
            return JsonResponse(data)
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)
    else:
        return JsonResponse({'error': 'Student ID not provided'}, status=400)