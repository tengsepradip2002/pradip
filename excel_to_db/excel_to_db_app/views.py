import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer

class UploadExcelView(APIView):
    def post(self, request, format=None):
        excel_file = request.FILES.get('file')

        if not excel_file:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            df = pd.read_excel(excel_file)

            for _, row in df.iterrows():
                employee_data = {
                    'name': row['name'],
                    'age': row['age'],
                    'department': row['department'],
                    'joining_date': row['joining_date'],
                }

                serializer = EmployeeSerializer(data=employee_data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({"message": "Employees saved successfully"}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from openpyxl import Workbook
from django.apps import apps
import datetime


# ✅ All imports must go at the top of the file
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from openpyxl import Workbook
from .models import Employee  # Adjust as per your app
import datetime

# @csrf_exempt
from django.http import HttpResponse
from openpyxl import Workbook
from .models import Employee
from django.views.decorators.csrf import csrf_exempt  # ✅ add this

@csrf_exempt  # ✅ disable CSRF for testing in Postman
def export_employee_excel(request):
    if request.method == 'POST':
        workbook = Workbook()
        worksheet = workbook.active
        worksheet.title = 'Employees'

        headers = ['name', 'age', 'department', 'joining_date']
        worksheet.append(headers)

        employees = Employee.objects.all()
        for emp in employees:
            worksheet.append([
                emp.name,
                emp.age,
                emp.department,
                emp.joining_date.strftime('%Y-%m-%d') if emp.joining_date else ''
            ])

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=employee_data.xlsx'
        workbook.save(response)
        return response

    return HttpResponse('Only POST allowed', status=405)
