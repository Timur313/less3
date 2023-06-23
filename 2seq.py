if __name__ == '__main__':

    my_arr = input("Введите элементы списка через разделитель ( , или ; или / ): ")

    sep_val = ","
    if ";" in my_arr:
        sep_val = ";"
    elif "/" in my_arr:
        sep_val = "/"
    my_arr = my_arr.split(sep_val)

    new_arr = [v for v in l if l.count(v) <= 1]

    print(new_arr)
