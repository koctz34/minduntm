import os
from PIL import Image

# Папка, где находится скрипт
script_dir = os.path.dirname(os.path.abspath(__file__))

# Папка для готовых спрайтов
output_dir = os.path.join(script_dir, 'sprites')
os.makedirs(output_dir, exist_ok=True)

# Желаемый размер 32x32
target_size = (32, 32)

# Обработка файлов .png в текущей папке
for filename in os.listdir(script_dir):
    if filename.lower().endswith('.png') and os.path.isfile(os.path.join(script_dir, filename)):
        src_path = os.path.join(script_dir, filename)
        dst_path = os.path.join(output_dir, filename)

        with Image.open(src_path) as img:
            img = img.convert('RGBA')
            resized = img.resize(target_size, Image.NEAREST)
            resized.save(dst_path)
