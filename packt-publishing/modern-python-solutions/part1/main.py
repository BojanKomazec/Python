import sys

def video_02_creating_meaningful_names_and_using_variables():
    # naming convention:
    #   name parts go from specific to general
    #   use CamelCase for class names
    #   use snake_case for variable and method names
    circumference_diameter_ratio = 355/113
    target_color_name = 'FireBrick'
    target_color_rgb = (178, 34, 34)
    print("circumference_diameter_ratio =", circumference_diameter_ratio)
    print("target_color_name =", target_color_name)
    print("target_color_rgb =", target_color_rgb)

    # assigning value to multiple variables
    target_color_name = first_color_name = 'FireBrick'

    # id() built-in function
    # http://stackoverflow.com/questions/15667189/what-does-id-function-used-for
    # Return the “identity” of an object. This is an integer (or long integer)
    # which is guaranteed to be unique and constant for this object during its lifetime.
    are_same = id(target_color_name) == id(first_color_name)
    print("are_same =", are_same)
    id1 = id(target_color_name)
    print("id1 =", id1)

    total_count = 0
    total_count += 5
    total_count += 6
    print("total_count =", total_count)

def video_03_working_with_large_and_small_integers():
    int1 = 2
    print("int1 =", int1)

    # hexadecimal number
    int2 = 0xff
    print("int2 =", int2)

    # one byte sequence
    int3 = b'\xfe'
    print("int3 =", int3)

    # 2 to the power or 20148
    int4 = 2 ** 2048
    print("int4 =", int4)

    import math

    # 52 factorial
    print("52! =", math.factorial(52))

    # The largest positive integer supported by the platform's Py_ssize_t type
    print("sys.maxsize = ", sys.maxsize)

    # logarithm of number to base 2
    print("math.log(sys.maxsize, 2) =", math.log(sys.maxsize, 2))

    # A struct sequence that holds information about Python’s
    # internal representation of integers (Python 3.1+)
    print(sys.int_info)

    print("id(1) =", id(1))
    print("id(2) =", id(2))
    print("id(1+1) =", id(1+1))

    # Return a string containing a nicely printable representation of an object.
    print("str(2**2048) =", str(2**2048))

    # Return the length (the number of items) of an object. The argument may be
    # a sequence (such as a string, bytes, tuple, list, or range) or
    # a collection (such as a dictionary, set, or frozen set).
    print("len(str(2**2048)) =", len(str(2**2048)))

    # ^ - eXclusive OR
    xor = 0b0011 ^ 0b0101
    # Convert an integer number to a binary string
    print("bin(xor) =", bin(xor))

    composite_byte = 0b01101100
    # get 2 most significant bits in a 8-bit number
    print("bin(composite_byte >> 6) =", bin(composite_byte >> 6))

    bottom_6_mask = 0b00111111
    # get 6 least significant bits in a 8-bit number
    print("bin(composite_byte & bottom_6_mask) =", bin(composite_byte & bottom_6_mask))

def video_04_choosing_between_float_decimal_and_fraction():
    # When working with currencies, use Decimal, not built-in float as
    # the latter has problems with rounding and truncations.
    # decimal module provides support for decimal floating point arithmetic
    # https://docs.python.org/2/library/decimal.html
    from decimal import Decimal
    # Decimal instances can be constructed from integers, strings, floats, or tuples.
    tax_rate = Decimal('7.25')/Decimal(100)
    purchase_amount = Decimal('2.95')
    val1 = tax_rate * purchase_amount
    print("tax_rate * purchase_amount = ", val1)

    # Avoid mixing Decimal and floating point variables
    f_tax_rate = 7.25/100
    f_purchase_amount = 2.95
    f_val1 = f_tax_rate * f_purchase_amount
    print("f_tax_rate * f_purchase_amount = ", f_val1)

    penny = Decimal('0.01')
    total_amount = purchase_amount + tax_rate * purchase_amount
    print("total_amount = ", total_amount)

    #  quantize() method rounds a number to a fixed exponent
    print("total_amount.quantize(penny) = ", total_amount.quantize(penny))

    # We can set different rounding rule
    import decimal
    print("total_amount.quantize(penny, decimal.ROUND_UP) = ",
          total_amount.quantize(penny, decimal.ROUND_UP))

    # For fractions/rationsal numbers, use fractions module.
    # The fractions module provides support for rational number arithmetic
    from fractions import Fraction

    # Fraction instance can be constructed from a pair of integers, another
    # rational number, from a string, float or decimal.Decimal
    sugar_cups = Fraction('2.5')
    scale_factor = Fraction(5/8)
    val2 = sugar_cups * scale_factor
    print("sugar_cups * scale_factor = ", val2)

    # auto-scaling
    val3 = Fraction(24, 16)
    print("Fraction(24, 16) = ", val3)

    # float approximation introduces error
    val4 = (19/155) * (155/19)
    print("(19/155) * (155/19) = ", val4)
    val5 = round(val4, 3)
    print("round((19/155) * (155/19), 3) = ", val5)

    # Don't compare floating point values for exact equality
    val6 = 1 - val4
    print("1 - (19/155) * (155/19) = ", val6)

    # Converting Decimal to float
    print("float(total_amount) = ", float(total_amount))

    # Converting Fraction to float
    print("float(sugar_cups * scale_factor) = ", float(sugar_cups * scale_factor))

    # Converting float to Fraction (exposes float truncation error)
    print("Fraction(19/155) = ", Fraction(19/155))

    # Converting float to Decimal (exposes float truncation error)
    print("Decimal(19/155) = ", Decimal(19/155))

    # base 10
    val7 = 8.066e+67
    print(val7)

    val8 = 6737037547376141/2**53*2**226
    print(val8)

    import math
    print("math.frexp(8.066e+67) = ", math.frexp(8.066e+67))

    print("((19/155) * (155/19)) == 1: ", ((19/155) * (155/19)) == 1)
    print("math.isclose((19/155) * (155/19), 1): ", math.isclose((19/155) * (155/19), 1))

    val9 = math.sqrt(-2)
    print(val9)

    # support for complex numbers
    import cmath

    val10 = cmath.sqrt(-2)
    print(val10)


def main():
    # video_02_creating_meaningful_names_and_using_variables()
    # video_03_working_with_large_and_small_integers()
    video_04_choosing_between_float_decimal_and_fraction()

main()
