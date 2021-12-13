#Блоки и их хеширование в питоне
#код для хеширования блока будет выглядеть примерно так

import hashlib as hl

block = {
    'nonce': 0
}

hash_block = hl.sha256(str(block).encode()).hexdigest()

print(hash_block)
