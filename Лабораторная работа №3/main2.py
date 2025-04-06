# TODO Напишите функцию find_common_participants
def find_common_participants(a,b,x=','):
    d = set(a.split(x)) # Разделяю первую группу и превращаю во множество
    v = set(b.split(x)) # Разделяю вторую группу и превращаю во множество
    f = d.intersection(v) # Поиск пересечений множеств
    g = list(f) # Превращение в список
    w = sorted(g) # Сортировка списка по алфавиту
    return w

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Проверьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group,participants_second_group,'|'))