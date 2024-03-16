import unittest
from unittest.mock import patch
from tracker import track_bus_location

class TestTracker(unittest.TestCase):
    @patch('requests.get')
    def test_track_bus_location_success(self, mock_get):
        # Mock the response from the GET request
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = '<body onload="initialize_map(); add_map_point(37.123, -122.456);">'

        # Call the function with a sample bus route number
        latitude, longitude = track_bus_location(123)

        # Assert that the expected latitude and longitude values are returned
        self.assertEqual(mock_get.call_args[0][0], 'https://trac.suveechi.com/k/mmap.php?k=CHK-R123')
        self.assertEqual(mock_get.return_value.status_code, 200)
        self.assertEqual(latitude, 37.123)
        self.assertEqual(longitude, -122.456)
        self.assertEqual(mock_get.call_count, 1)

    @patch('requests.get')
    def test_track_bus_location_failure(self, mock_get):
        # Mock the response from the GET request
        mock_get.return_value.status_code = 404

        # Call the function with a sample bus route number
        latitude, longitude = track_bus_location(456)

        # Assert that the failure message is returned
        self.assertEqual(mock_get.call_args[0][0], 'https://trac.suveechi.com/k/mmap.php?k=CHK-R456')
        self.assertEqual(mock_get.return_value.status_code, 404)
        self.assertIsNone(latitude)
        self.assertIsNone(longitude)

if __name__ == '__main__':
    unittest.main()
