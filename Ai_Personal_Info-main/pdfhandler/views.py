from django.shortcuts import render
from django.http import HttpResponse
from pdfhandler import views

def home(request):
    return HttpResponse("Hello, this is the PDF handler app!")

def main_page(request):
    return render(request, 'main_page.html')  # main_page.html은 템플릿 파일