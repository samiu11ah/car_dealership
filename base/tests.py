from django.test import TestCase
from django.urls import reverse
from base.models import Car

class CarTestCase(TestCase):
    def setUp(self):
        for i in range(10):
            Car.objects.create(
                make=f"test_make_{str(i)}", 
                model=f"test_model_{str(i)}",
                model_year="1995",
                price=34343.0,
                condition="old",
                condition_rating="9",
                description=f"test_description_{str(i)}",
                address=f"test_address_{str(i)}"
                )

    def test_cars_have_make_and_model(self):
        """Cars that are correctly identified"""
        test_make_5 = Car.objects.get(make="test_make_5")
        test_model_2 = Car.objects.get(model="test_model_2")
        self.assertEqual(test_make_5.get_make(), 'test_make_5')
        self.assertEqual(test_model_2.get_model(), 'test_model_2')

    def test_home_url_exists(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_cars_url_exists(self):
        response = self.client.get("/cars/")
        self.assertEqual(response.status_code, 200)

    def test_enquiry_url_exists(self):
        response = self.client.get("/enquiry/")
        self.assertEqual(response.status_code, 200)

    def test_cars_url_accessible_by_name(self):
        response = self.client.get(reverse('cars'))
        self.assertEqual(response.status_code, 200)


    def test_register_url_accessible_by_name(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_user_login_url_accessible_by_name(self):
        response = self.client.get(reverse('user_login'))
        self.assertEqual(response.status_code, 200)

    def test_cars_url_accessible_by_name(self):
        response = self.client.get(reverse('cars'))
        self.assertEqual(response.status_code, 200)

    def test_inquiry_url_accessible_by_name(self):
        response = self.client.get(reverse('inquiry'))
        self.assertEqual(response.status_code, 200)


    def test_cars_uses_correct_template(self):
        response = self.client.get(reverse('cars'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/cars.html')


    def test_inquiry_uses_correct_template(self):
        response = self.client.get(reverse('inquiry'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/inquiry.html')
