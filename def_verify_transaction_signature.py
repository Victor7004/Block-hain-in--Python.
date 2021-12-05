#Проверка подписей транзакций в python
#Код такой-же, как в ранее пройденном уроке

def verify(transaction, signature):
    key = transaction['user']['public_key']
    return rsa.verify(message=str(transaction).encode(), signature=signature, pub_key=key)
