#Создание блока с хешем прошлого
#Сначала, напишем небольшую функцию для генерации блока
#Что-бы создавать блок, надо определится как он будет выглядеть. Например так:

{
  "number": 0,
  "name": "block_name",
  "nonce": 0,
  "hash_last_one": None,
  'transactions_mercls_tree': None,
  "complexity": 50
}
#Функция будет выглядеть примерно так:

def generate_block(number, last_one, mercls_tree):  # Генерируем новый блок
    global complexity, blocks_name
    if last_one is None:
        hash_last_one = None
    else:
        hash_last_one = last_one["hash"]
    name = blocks_name
    block_name = name + str(number)
    block = {
        "number": number,
        "name": block_name,
        "nonce": 0,
        "hash_last_one": hash_last_one,
        'transactions_mercls_tree': mercls_tree,
        "complexity": complexity
    }
    hash = hl.sha256(str(block).encode()).hexdigest()
    while hash[0:complexity] != '0' * complexity:
        block['nonce'] += 1
        hash = hl.sha256(str(block).encode()).hexdigest()
    block['hash'] = hash
    # print(json.dumps(block, indent=4))
    return block
#    Можно дописать: 

print(json.dumps(bg.generate_block(0, None, None), indent = 4))
# вызвав функцию получим блок:

{
    "number": 0,
    "name": "block0",
    "nonce": 188,
    "hash_last_one": null,
    "transactions_mercls_tree": null,
    "complexity": 2,
    "hash": "00a97c04e82f5d625f656010be5130134889b40a496e9646e0b8d613edd79208"
}
# но как сделать чтобы он сохранялся?
