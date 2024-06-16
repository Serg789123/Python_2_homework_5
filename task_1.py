# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция возвращает кортеж
# из трёх элементов: путь, имя файла, расширение файла.

absolute_path = 'https://img.razrisyika.ru/kart/2/4816-kotik-12.jpg'

def split_(path):
    *path_, x = path.split('/')
    name, extension = x.split('.')
    res = ('/'.join(path_), name, extension)
    return res


print(split_(absolute_path))