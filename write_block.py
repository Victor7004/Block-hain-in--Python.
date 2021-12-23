#Создание цепочки блоков программой
#Запись в файл блока
#Код крайне простой и не требует комментариев:

fp = 'blocks//'


def write_block(block, fp):
    fp = fp + str(block['name']) + '.json'
    with open(fp, 'w', encoding='UTF8') as file:
        json.dump(block, file, indent=2)
#И также меняем код для вывода, на код для записи:

block = generate_block(1, None)
write_block(block, fp)
