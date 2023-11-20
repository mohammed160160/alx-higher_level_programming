#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    final_list = []
    for i in range(list_length):
        try:
            X = my_list_1[i] / my_list_2[i]
            final_list.append(X)
        except TypeError:
            final_list.append(0)
            print("wrong type")
        except IndexError:
            final_list.append(0)
            print("out of range")
        except ZeroDivisionError:
            final_list.append(0)
            print("division by 0")
    return(final_list)
