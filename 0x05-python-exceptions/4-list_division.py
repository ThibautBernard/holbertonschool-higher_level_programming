#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_tab = []
    try:
        for i in range(0, list_length):
            try:
                new_tab.append(my_list_1[i] / my_list_2[i])
            except ZeroDivisionError:
                new_tab.append(0)
                print("division by 0")
            except TypeError:
                new_tab.append(0)
                print("wrong type")
            except IndexError:
                new_tab.append(0)
                print("out of range")
    except:
        return
    finally:
        return new_tab
