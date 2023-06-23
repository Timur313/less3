if __name__ == '__main__':

    len_list = input("Введите количество элементов будущего списка: ")

    if len_list.isdigit():
        my_list = []
        len_list = int(len_list)

        while len(my_list) < len_list:
            val = input("Введите целое любое число: ")
            if val.isdigit():
                my_list.append(int(val))
            else:
                print(f"Введенное значение {val} - не является целым числом")
        my_list.sort()
        print(f"Вывод: {my_list}")
    else:
        print(f"Введенное значение {len_list} - не является целым числом")

