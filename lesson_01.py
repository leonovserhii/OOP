class Point:
    """ Краткое описание класса """
    color = 'red'
    circle = 2


Point.color = 'blue'
print(Point.color)
print(Point.circle)
print(Point.__dict__)
a = Point()
b = Point()
print(a.circle)
print(a.color)
print(a.__dict__)
print(b.circle)
b.color = 'white'
print(b.color)
print(a.color)
print(Point.color)
print(f"Type: {type(a)} / address: {id(a)}")
print(f"Type: {type(b)} / address: {id(b)}")

# -------------

print(setattr(Point, 'prop', 1))  # возвращает значение атрибута объекта;
print(getattr(Point, 'a', False))  # проверяет на наличие атрибута name в obj; False - если не существует
print(getattr(Point, 'prop', False))  # проверяет на наличие атрибута name в obj; значение - если существует

hasattr(Point, 'circle')  # есть ли атрибут

delattr(Point, 'type_pt')  # удаляем аттрибут
