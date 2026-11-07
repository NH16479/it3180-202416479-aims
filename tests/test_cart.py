import unittest

from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(MAX_NUMBERS_ORDERED):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {i}", cost=1.0)))
        # đĩa thứ 21 phải bị từ chối
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("Extra", cost=1.0)))

    def test_total_cost(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("A", cost=1.5))
        cart.add_dvd(DigitalVideoDisc("B", cost=2.5))
        self.assertAlmostEqual(cart.total_cost(), 4.0)


if __name__ == "__main__":
    unittest.main()
