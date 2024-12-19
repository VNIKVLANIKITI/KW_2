from rest_framework.test import APITestCase
from rest_framework import status


class HabiteTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_create_habite(self):
        """ Тест создания  """
        data = {
            "action_time": "15:00:00",
            "periodicity": "weekly",
            "time_long": 2,
            "myrevard": 3
        }
        response = self.client.post(
            'http://localhost:8000/habit/create/',
            data=data,
            )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
                {
                    "action_time": "15:00:00",
                    "is_nice": False,
                    "action_place": 1,
                    "periodicity": "weekly",
                    "time_long": 2,
                    "is_public": False
                }
        )

    def test_update_habite(self):
        """ Тест обновления привычки """
        updated_data = {
            "action_time": "16:00:00",
            "periodicity": "daily",
            "time_long": 3,
            "myrevard": 4
        }
        
        response = self.client.put(
            f'http://localhost:8000/habit/update/{self.id}/',
            data=updated_data,
            format='json'  # Убедитесь, что формат данных указан правильно
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        # Проверяем, что данные обновлены
        updated_habite = self.client.get(f'http://localhost:8000/habit/{self.id}/')
        
        self.assertEqual(updated_habite.json(), {
            **updated_data,
            "is_nice": False,
            "action_place": 1,
            "is_public": False
        })

    def test_delete_habite(self):
        """ Тест удаления привычки """
        
        response = self.client.delete(
            f'http://localhost:8000/habit/delete/{self.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        # Проверяем, что привычка действительно удалена
        response = self.client.get(f'http://localhost:8000/habit/{self.habite_id}/')
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
