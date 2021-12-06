#Создание дерева Меркла в блокчейне
#Считывание транзакций и их подписей из файлов в python
def read_transactions(fp):  # Считываем цепочку уже созданных транзакций
    fp_transaction = fp + 'transaction' + '*' + '.json'
    fp_signature = fp + 'signatue' + '*' + '.dat'
    files_transactions = glob(fp_transaction)
    files_signatures = glob(fp_signature)
    if len(files_signatures) == len(files_transactions):
        pass
    else:
        raise Exception('Not all transactions were signed')

    transactions = []
    for i, file_name_transction in enumerate(files_transactions):
        file_name_signatures = files_signatures[i]
        with open(file_name_transction, 'r', encoding='UTF8') as file:
            transactions.append([json.load(file)])
            transactions[-1][0]['user']['public_key'] = rsa.PublicKey(
                transactions[-1][0]['user']['public_key'][0],
                transactions[-1][0]['user']['public_key'][1]
            )
        with open(file_name_signatures, 'rb') as bytes_code:
            transactions[-1].append(bytes_code.read())
    return transactions
