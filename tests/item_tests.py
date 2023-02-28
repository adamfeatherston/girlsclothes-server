import json
from rest_framework import status
from rest_framework.test import APITestCase
from girlsclothesapi.models import ClothingUse, ClothingType, Kid


class ItemTests(APITestCase):

    # Add any fixtures you want to run to build the test database
    fixtures = ['clothing_items', 'tokens', 'clothing_types', 'clothing_uses', 'item_uses', 'kids', 'outfit_items', 'outfits', 'users']

    def test_create_item(self):
        """
        Ensure we can create a new item.
        """
        # Define the endpoint in the API to which
        # the request will be sent
        url = "/clothingitems"

        # Define the request body
        data = {
            "item_description": "Test Shirt",
            "clothing_type": 1,
            "kid": 5,
            "size": "4T",
            "clean_or_dirty": True,
            "item_fits": True,
            "sibling_has_match": False,
            "item_image": "",
            "clothing_uses": [1,2,3]
        }

        # Initiate request and store response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the properties on the created resource are correct
        self.assertEqual(json_response["item_description"], "Test Shirt")
        self.assertEqual(json_response["size"], "4T")
        self.assertEqual(json_response["clean_or_dirty"], True)
        self.assertEqual(json_response["item_fits"], True)
        self.assertEqual(json_response["sibling_has_match"], False)
        self.assertEqual(json_response["item_image"], "")