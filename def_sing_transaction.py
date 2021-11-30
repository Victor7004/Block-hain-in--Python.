#Подписание транзакции в python.
#Пишем функцию для этого:

def sing_transaction(transaction):
    global key
    signature = rsa.sign(message=str(transaction).encode(), priv_key=key[1], hash_method='SHA-256')
    return signature
#Нужно сохранять/получать ключи из файлов,

#для этого также пешим две функции, для генерации и записи

def save_key(key, fp):
    pubkey, privkey = key[0], key[1]
    pubkey_pem = pubkey.save_pkcs1(format='PEM')  #  (format='PEM')
    privkey_pem = privkey.save_pkcs1(format='PEM')
    print(pubkey_pem)
    print(privkey_pem)
    with open(fp + 'PublicKey', 'w') as file:
        file.write(pubkey_pem.decode())
    with open(fp + 'PrivateKey', 'w') as file:
        file.write(privkey_pem.decode())
#для чтения из файла

def get_key(fp):
    global key
    puk = fp + 'PublicKey'
    prk = fp + 'PrivateKey'
    with open(puk, 'r') as file:
        key.append(rsa.PublicKey.load_pkcs1(file.read().encode(), 'PEM'))
    with open(prk, 'r') as file:
        key.append(rsa.PrivateKey.load_pkcs1(file.read().encode(), 'PEM'))

        
#Проверка подписи транзакции в python.

def verify(transaction, signature):
    key = transaction['user']['public_key']
    print(str(transaction).encode())
    print(signature)
    return rsa.verify(message=str(transaction).encode(), signature=signature, pub_key=key)
