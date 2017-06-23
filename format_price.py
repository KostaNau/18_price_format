import sys


def format_price(price):
    try:
        is_digit = round(float(price))
        output_price = "{:,.0f}".format(is_digit).replace(",", " ")
        return output_price
    except (ValueError, TypeError):
        return None


if __name__ == '__main__':
    user_input = sys.argv[1]
    print(format_price(user_input))
