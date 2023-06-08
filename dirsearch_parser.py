## USAGE: python dirsearch_parser.py  -i <input_file_name.txt> o <output_file_name.txt>

## BU SAYEDEDE AZ DİĞER SCRİPTİ ÇALIŞTIRARAK URL LİSTESİNDEKİ HER URL'İ YENİ SEKMEDE AÇABİLİRİZ.

import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='Girdi dosyası')
parser.add_argument('-o', '--output', help='Çıktı dosyası')
args = parser.parse_args()

input_file = args.input
output_file = args.output

with open(input_file, 'r') as file:
    content = file.readlines()

# '302     0B   http://domain.com:80/6I/    -> REDIRECTS TO:' kısmını silmek için,
updated_content = []
for line in content:
    if line.startswith('302     0B   http://domain.com:80/') and '-> REDIRECTS TO:' in line:
        line = line.split('-> REDIRECTS TO:')[1].strip() + '\n'
    updated_content.append(line)

with open(output_file, 'w') as file:
    file.writelines(updated_content)

print(f"Güncellenmiş içerik '{output_file}' adlı dosyaya yazıldı.")
