def video_02_creating_meaningful_names_and_using_variables():
    # naming convention:
    #   name parts go from specific to general
    #   use CamelCase for class names
    #   use snake_case for variable and method names
    circumference_diameter_ratio = 355/113
    target_color_name = 'FireBrick'
    target_color_rgb = (178, 34, 34)
    print "circumference_diameter_ratio =", circumference_diameter_ratio
    print "target_color_name =", target_color_name
    print "target_color_rgb =", target_color_rgb

    # assigning value to multiple variables
    target_color_name = first_color_name = 'FireBrick'

    # id() operator
    # http://stackoverflow.com/questions/15667189/what-does-id-function-used-for
    are_same = id(target_color_name) == id(first_color_name)
    print "are_same =", are_same
    id1 = id(target_color_name)
    print "id1 =", id1

    total_count = 0
    total_count += 5
    total_count += 6
    print "total_count =", total_count

def main():
    video_02_creating_meaningful_names_and_using_variables()

main()
