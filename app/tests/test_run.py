from unittest import TestCase

from app import home


class TestHome(TestCase):
    def setUp(self) -> None:
        pass

    def test_home(self):
        expected_result = {"msg": "hello world"}

        result = home()
        self.assertEqual(result, expected_result)

    def test_home2(self):
        expected_result = {"msg": "hello world"}

        result = home()
        self.assertEqual(result, expected_result)

    def tearDown(self) -> None:
        pass