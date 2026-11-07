import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearchByTitle(unittest.TestCase):
    def test_case_insensitive(self):
        items = [DigitalVideoDisc("The Lion King"), DigitalVideoDisc("Aladdin")]
        self.assertEqual([d.title for d in search_by_title(items, "lion")], ["The Lion King"])
        self.assertEqual([d.title for d in search_by_title(items, "LION")], ["The Lion King"])
        self.assertEqual(search_by_title(items, "xyz"), [])


if __name__ == "__main__":
    unittest.main()
