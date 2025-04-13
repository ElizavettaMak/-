# TODO импортировать необходимые модули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task(filename_csv, filename_json) -> None:
    with open(filename_csv, "r", encoding="utf-8") as file_csv:
        reader = csv.DictReader(file_csv)
        indent = 4
        ensure_ascii = False
        list_ = []
        for i in reader:
            list_.append(i)
        with open(filename_json, "w", encoding="utf-8") as file_json:
            json.dump(list_, file_json, indent=indent, ensure_ascii=ensure_ascii)
            #json_data = json.dumps(list_, indent=indent, ensure_ascii=ensure_ascii)
            #file_json.write(json_data)

if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")
