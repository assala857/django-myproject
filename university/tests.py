from django.test import TestCase
from django.urls import reverse
from .models import University

class UniversityModelTest(TestCase):
    def test_university_creation(self):
        """Test que l'université peut être créée"""
        university = University.objects.create(
            name="Harvard University",
            city="Cambridge"  # Utilisez 'city' au lieu de 'location'
        )
        self.assertEqual(str(university), "Harvard University")
        self.assertEqual(university.city, "Cambridge")

class UniversityViewTest(TestCase):
    def test_university_list_view(self):
        """Test de la vue liste des universités"""
        response = self.client.get('/university/getAll/')
        self.assertEqual(response.status_code, 200)