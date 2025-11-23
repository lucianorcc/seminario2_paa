def partition_backtracking(S):
    S = sorted(S, reverse=True)
    total = sum(S)
   
    if total % 2 != 0:
        return False, [], []
   
    target = total // 2
   
    def bt(pos, sum1, grupo1):
        if pos == len(S):
            return sum1 == target, grupo1[:]
       
        num = S[pos]
       
        if sum1 + num <= target:
            grupo1.append(num)
            encontrou, solucao = bt(pos + 1, sum1 + num, grupo1)
            if encontrou:
                return True, solucao
            grupo1.pop()
       
        remaining = sum(S[pos+1:])
        if sum1 + remaining >= target:
            encontrou, solucao = bt(pos + 1, sum1, grupo1)
            if encontrou:
                return True, solucao
       
        return False, []
   
    encontrou, parte1 = bt(0, 0, [])
    if not encontrou:
        return False, [], []
   
    parte2 = [x for x in S if x not in parte1]
    return True, sorted(parte1), sorted(parte2)

if __name__ == "__main__":
    testes = [
        [1, 5, 11, 5],
        [1, 2, 3, 6],
        [1, 2, 5],
        [3, 1, 1, 2, 2, 1],
        [4, 5, 6, 7, 8]
    ]
   
    print("BACKTRACKING CORRETO – Problema da Partição (Cormen p. 404)\n")
    for i, conjunto in enumerate(testes, 1):
        print(f"Teste {i}: {conjunto} → soma = {sum(conjunto)}")
        ok, A, B = partition_backtracking(conjunto)
        if ok:
            print(f" Partição: {A} | {B} → {sum(A)} = {sum(B)}")
        else:
            print(" Impossível particionar")
        print()