#Запись транзакции в файл python
#Вы можете заметить, что транзакции прошлось хранить в виде байт-кода в отдельных файлах, формата .dat.

def write_transaction(transaction, signature, fp):
    number = transaction["additional"]["number"]
    fp_transaction = fp + 'transaction' + str(number) + '.json'
    fp_signature = fp + 'signatue' + str(number) + '.dat'
    transaction['user']['public_key'] = [transaction['user']['public_key']['n'], transaction['user']['public_key']['e']]
    with open(fp_transaction, 'w', encoding='UTF8') as file:
        json.dump(transaction, file, indent=4)
    with open(fp_signature, 'wb') as file:
        file.write(signature)
