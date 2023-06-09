import unittest

import one


class Test(unittest.TestCase):
    def testDeleteFirstLastFunc(self):
        self.assertEqual(one.delete_first_last_char("hello"), "ell")
        self.assertEqual(one.delete_first_last_char("a"), "")
        self.assertEqual(one.delete_first_last_char(""), "")
        self.assertEqual(one.delete_first_last_char("12345"), "234")

    def testAddFunc(self):
        self.assertEqual((one.add(105, 205)), 310)
        self.assertEqual((one.add(-50, 20)), -30)

    def testReverse(self):
        self.assertNotEqual((one.reverse("f")), "h")
        self.assertEqual((one.reverse("salam")), "malas")

    def testSubFunc(self):
        self.assertEqual((one.sub(-10, -10)), 0)


if __name__ == "__main__":
    unittest.main()
