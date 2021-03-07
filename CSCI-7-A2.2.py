# TODO: Write a Python program to draw a three stage rocket. Here is mine - make yours different!

rocket_array = ["|", "*", "="]


def rocket_test():
    print(" " * 2, rocket_array[1], " " * 2)
    print(rocket_array[1], " " * 3, rocket_array[1])
    print(rocket_array[2] * 7)
    for i in range(3):
        print(rocket_array[0], " " * 3, rocket_array[0])
        print(rocket_array[1], " " * 3, rocket_array[1])
        print(rocket_array[2]*7)
    return


rocket_test()
