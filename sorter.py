#MADE BY FRUIZZ NIGGA

import os
import sys

if getattr(sys, 'frozen', False):
    app_dir = os.path.dirname(sys.executable)
else:
    app_dir = os.path.dirname(os.path.abspath(__file__))

folder = input("Введите путь к папке с текстовыми файлами :\n").strip().strip('"')

if not os.path.isdir(folder):
    print("Папка не найдена")
    input("Нажмите Enter для выхода...")
    raise SystemExit


result_dir = os.path.join(app_dir, 'result')
os.makedirs(result_dir, exist_ok=True)
output_file = os.path.join(result_dir, 'result.txt')

unique_elements = set()

for root, dirs, files in os.walk(folder):
    for file_name in files:
        if file_name.endswith('.txt') and file_name != 'result.txt':
            path = os.path.join(root, file_name)
            with open(path, 'r', encoding='utf-8') as f:
                unique_elements.update(f.read().split())

sorted_elements = sorted(unique_elements)

lines = []
for i in range(0, len(sorted_elements), 3):
    lines.append(" ".join(sorted_elements[i:i + 3]))

with open(output_file, 'w', encoding='utf-8') as f:
    f.write("\n".join(lines))

print(f"Готово: {len(sorted_elements)} уникальных слов записано в {output_file}")
input("Нажмите Enter для выхода...")