import unittest
from format_price import format_price


class TestFormatPrice(unittest.TestCase):
    def test_int_var_case(self):
        int_price = format_price(12312)
        self.assertEqual(int_price, "12 312")

    def test_float_var_case(self):
        float_price = format_price(234.0431231)
        long_float_price = format_price(546789.964305)
        self.assertEqual(float_price, "234")
        self.assertEqual(long_float_price, "546 790")

    def test_alphanumeric_case(self):
        alphanumeric_1 = format_price("123.550FAFFA")
        alphanumeric_2 = format_price("asdaKJHJKHFkafsdf")
        alphanumeric_3 = format_price("*(&*(^&*(^@#$&*%^&*$")
        self.assertIsNone(alphanumeric_1)
        self.assertIsNone(alphanumeric_2)
        self.assertIsNone(alphanumeric_3)

    def test_built_in_datatype_case(self):
        list_type = format_price([1234])
        dict_type = format_price({'price': 1235.895})
        tuple_type = format_price((123.553,))
        self.assertIsNone(list_type)
        self.assertIsNone(dict_type)
        self.assertIsNone(tuple_type)


if __name__ == "__main__":
    unittest.main()
