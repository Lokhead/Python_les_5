file_a = open('dz2.txt', encoding='UTF-8')
for ind, line_a in enumerate(file_a, 1):
    print(f'строка {ind}: слов в строке {len(line_a.split())}')
file_a.close()
