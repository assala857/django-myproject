from django.test import TestCase
from django.urls import reverse
from .models import Student

class StudentModelTest(TestCase):
    def test_student_creation(self):
        """Test que l'étudiant peut être créé"""
        student = Student.objects.create(
            name="John Doe",  # Utilisez 'name' au lieu de 'first_name'
            address="123 Main Street"  # Utilisez 'address' au lieu de 'email'
        )
        self.assertEqual(str(student), "John Doe")
        self.assertEqual(student.address, "123 Main Street")

class StudentViewTest(TestCase):
    def test_student_list_view(self):
        """Test de la vue liste des étudiants"""
        # Utilisez le nom réel de votre URL
        response = self.client.get('/students/getAll/')
        self.assertEqual(response.status_code, 200)
    
    def test_student_create_view(self):
        """Test de la création d'étudiant"""
        response = self.client.post('/students/add/', {
            'name': 'Jane Smith',
            'address': '456 Oak Avenue'
        })
        self.assertEqual(response.status_code, 200)  # ou 201 selon votre vue