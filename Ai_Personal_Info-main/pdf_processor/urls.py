from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_and_analyze_pdf, name='upload_pdf'),
    path('result/<int:pk>/', views.analysis_result, name='analysis_result'),
]
