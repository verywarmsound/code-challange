from django.test import TestCase
from rest_framework.test import APITestCase, APIClient


class TestSimulationApiView(APITestCase):
    def test_get_result_for_location(self):
        location = [52.5074, 13.4253, 52.423360425382036, 13.459703138203825]
        client = APIClient()
        response = client.get(f"api/simulation?location={location}")
        assert response.status_code == 200