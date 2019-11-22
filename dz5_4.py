file_a = open('dz4.txt', encoding='UTF-8')
file_b = open('dz4_new.txt', 'w', encoding='UTF-8')
list_rus = ['Один', 'Два', 'Три', 'Четыре']
line_b = list()
for line_a in file_a:
    line_c = list()
    line_b = list(line_a.split())
    if line_b[0] == 'One':
        line_c.append(list_rus[0])
    elif line_b[0] == 'Two':
        line_c.append(list_rus[1])
    elif line_b[0] == 'Three':
        line_c.append(list_rus[2])
    elif line_b[0] == 'Four':
        line_c.append(list_rus[3])
    line_c.append(' ')
    line_c.append(line_b[1])
    line_c.append(' ')
    line_c.append(line_b[2])
    line_c.append('\n')
    file_b.writelines(line_c)
file_a.close()
file_b.close()
