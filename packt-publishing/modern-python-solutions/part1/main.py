import sys
import math

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

def main():
    #video_02_creating_meaningful_names_and_using_variables()
    video_03_working_with_large_and_small_integers()

main()
