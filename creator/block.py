import os

# Папка, в которой находится сам скрипт
script_dir = os.path.dirname(os.path.abspath(__file__))

# Папка для .hjson файлов
output_dir = os.path.join(script_dir, 'blocks')

# HJSON шаблон
hjson_template = '''{
    type: Floor
    category: power
    placeableOn: true
    solid: false
    variants: 0
    drawEdgeOut: false
    requirements:
    [
        copper/1
    ]
}'''

# Создание папки blocks, если её нет
os.makedirs(output_dir, exist_ok=True)

# Проход только по файлам в текущей папке
for file in os.listdir(script_dir):
    if file.lower().endswith('.png') and os.path.isfile(os.path.join(script_dir, file)):
        name_without_ext = os.path.splitext(file)[0]
        hjson_path = os.path.join(output_dir, name_without_ext + '.hjson')

        # Запись HJSON файла
        with open(hjson_path, 'w', encoding='utf-8') as f:
            f.write(hjson_template)

print("Готово: создано .hjson файлов:", len(os.listdir(output_dir)))
