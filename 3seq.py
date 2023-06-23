import sys

def get_arr(my_arr: str) -> list:
    res = None
    try:
        sep_val = ","
        if ";" in my_arr:
            sep_val = ";"
        elif "/" in my_arr:
            sep_val = "/"
        my_arr = my_arr.split(sep_val)
        res = [float(v) for v in my_arr]
    except BaseException as e:
        print(f"Что-то пошло не так, возможно вы ввели не просто цифры: {e}")
    return res


if __name__ == '__main__':

    inp_data = input("Введите элементы списка #1 через разделитель ( , или ; или / ): ")
    my_arr1 = get_arr(inp_data)
    if my_arr1 is None:
        sys.exit()
    
    inp_data = input("Введите элементы списка #2 через разделитель ( , или ; или / ): ")
    my_arr2 = get_arr(inp_data)
    if my_arr2 is None:
        sys.exit()

    res = set(my_arr1) - set(my_arr2)
    print(res)
