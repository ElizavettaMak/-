# TODO решите задачу
import json

def task(filename) -> float:
    # Чтение данных из файла в формате JSON
    with open(filename, encoding="utf-8") as file:
        data = json.load(file)
    list_ = []
    for i in data:
        n = i['score'] * i['weight']
        list_.append(n)
    return round(sum(list_),3)

file_name = 'input.json'
print(task(file_name))
