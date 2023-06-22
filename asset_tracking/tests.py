from django.test import TestCase
from .models import Log, Employee, Device, Company
from datetime import datetime

class CompanyModelTest(TestCase):
    def test_company_creation(self):
        company = Company.objects.create(name='Example Company')
        self.assertEqual(company.name, 'Example Company')


class EmployeeModelTest(TestCase):
    def test_employee_creation(self):
        company = Company.objects.create(name='Example Company')
        employee = Employee.objects.create(company=company, name='John Doe')
        self.assertEqual(employee.company, company)
        self.assertEqual(employee.name, 'John Doe')


class DeviceModelTest(TestCase):
    def test_device_creation(self):
        company = Company.objects.create(name='Example Company')
        device = Device.objects.create(company=company, name='Phone', condition='Good')
        self.assertEqual(device.company, company)
        self.assertEqual(device.name, 'Phone')
        self.assertEqual(device.condition, 'Good')

class LogModelTest(TestCase):
    def test_log_creation(self):
        company = Company.objects.create(name='Example Company')
        employee = Employee.objects.create(company=company, name='John Doe')
        device = Device.objects.create(company=company, name='Phone', condition='Good')
        check_out_date = datetime.now()
        return_date = datetime.now()
        log = Log.objects.create(device=device, employee=employee, check_out_date=check_out_date, return_date=return_date)
        self.assertEqual(log.device, device)
        self.assertEqual(log.employee, employee)
        self.assertEqual(log.check_out_date, check_out_date)
        self.assertEqual(log.return_date, return_date)