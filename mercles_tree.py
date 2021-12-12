#Рекурсивное вычисления главного хеша в дереве Меркла в python

def mercles_tree(hashs: list[str]) -> str:
    def balancing(hashs: list[str])  -> list[str]:
        if len(hashs) % 2 == 0:
            return hashs

        hashs.append(hashs[-1])
        return hashs

    tmp_hashs = []
    if len(hashs) > 1:
        balance_hashs = balancing(hashs)
        for i in range(0, len(balance_hashs), 2):
            j = (i + 1)
            el1, el2 = hashs[i], hashs[j]
            sum = el1 + el2
            tmp_hashs.append(hl.sha256(sum.encode()).hexdigest())
        return mercles_tree(tmp_hashs)
    return hashs[0]
