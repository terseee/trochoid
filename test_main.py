from unittest import TestCase
from main import get_count


class Test(TestCase):
    def test_get_trochoid(self):
        count = get_count(100, 50)
        assert count == 2
        count = get_count(100, 30)
        assert count == 10
