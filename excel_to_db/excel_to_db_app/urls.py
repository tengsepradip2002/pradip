from django.contrib import admin
from django.urls import path
from .views import UploadExcelView,export_employee_excel
urlpatterns = [
    path('upload-excel/', UploadExcelView.as_view(), name='upload-excel'),
    path('export/all/', export_employee_excel,name='export_all_tables_to_excel'),
]
