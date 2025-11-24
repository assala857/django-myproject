from django.test import TestCase
from django.urls import reverse
from .models import Student

class StudentModelTest(TestCase):
    def test_student_creation(self):
        """Test que l'étudiant peut être créé"""
        student = Student.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com"
        )
        self.assertEqual(str(student), "John Doe")
        self.assertEqual(student.email, "john.doe@example.com")

class StudentViewTest(TestCase):
    def test_student_list_view(self):
        """Test de la vue liste des étudiants"""
        response = self.client.get(reverse('student-list'))
        self.assertEqual(response.status_code, 200)
    
    def test_student_create_view(self):
        """Test de la création d'étudiant"""
        response = self.client.post(reverse('student-list'), {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'jane.smith@example.com'
        })
        self.assertEqual(response.status_code, 201)  # ou 200 selon votre API