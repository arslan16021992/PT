# -*- coding: utf-8 -*-
def shell_sort(array):
    step = len(array) // 2
    while step > 0:
        for start in range(step):
            for i in range(start + step, len(array), step):
                current_item = array[i]

                while i >= step and array[i - step] > current_item:
                    array[i] = array[i - step]
                    i -= step

                array[i] = current_item
        step //= 2


if __name__ == '__main__':
    while True:
        try:
            data = [int(x) for x in input('Введите последовательность чисел для сортировки методом Шелла:').split(',')]
        except ValueError:
            print("Последовательность должна содержать цифры, разделенные через запятую!")
        except ZeroDivisionError:
            print("Введите непустую последовательность!")
        except KeyboardInterrupt:
            print("Неправильный ввод с клавитуры.")
        except:
            print('Что-то пошло не так.')
        else:
            shell_sort(data)
            print(data)
            break
