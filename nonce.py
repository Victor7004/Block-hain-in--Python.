#Блоки и их хеширование в питоне
#Цикл для нахождения nonce
import hashlib as hl
complexity = 2

block = {
    'nonce': 0
}
hash_block = hl.sha256(str(block).encode()).hexdigest()
# print(hash)
while hash_block[0:complexity] != '0'*complexity:
    block['nonce'] += 1
    hash_block = hl.sha256(str(block).encode()).hexdigest()

print(block['nonce'])
print(hash_block)
