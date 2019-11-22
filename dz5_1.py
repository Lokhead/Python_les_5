file_a = open('dz1_new.txt', 'w', encoding='UTF-8')
str_a = ' '
while len(str_a) > 0:
    str_a = list(input('Введите строку. Для завершения оставьте строку пустой'))
    if len(str_a) > 0:
        str_a.append('\n')
        file_a.writelines(str_a)
file_a.close()
