def partition_problem_dp(S):
    n = len(S)                       
    total_sum = sum(S)                
    
    if total_sum % 2 != 0:
        return False, [], []

    target = total_sum // 2
    
    DP = [[False] * (target + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        DP[i][0] = True

    for i in range(1, n + 1):           
        for j in range(target + 1):     
            
            DP[i][j] = DP[i-1][j]
                        
            if j >= S[i-1]:
 
                DP[i][j] = DP[i][j] or DP[i-1][j - S[i-1]]

    if not DP[n][target]:
        return False, [], []

    subset1 = []   
    subset2 = []   
    i, j = n, target
    
    while i > 0:    
        if DP[i-1][j]:
            subset2.append(S[i-1])   
        else:
            subset1.append(S[i-1])
            j -= S[i-1]              
        i -= 1
    
    return True, subset1, subset2


def partition_problem_dp_otimizado(S):
    total_sum = sum(S)
    if total_sum % 2 != 0:
        return False, [], []
    
    target = total_sum // 2
    DP = [False] * (target + 1)
    DP[0] = True                  

    for num in S:
        for j in range(target, num - 1, -1):
            if DP[j - num]:            
                DP[j] = True           
    
    return DP[target], [], []          

if __name__ == "__main__":
    print("="*70)
    print("PARTIÇÃO DE CONJUNTOS – PROGRAMAÇÃO DINÂMICA (Cormen p. 404)")
    print("="*70)

    exemplos = [
        [1, 5, 11, 5],         
        [1, 2, 5],             
        [3, 1, 1, 2, 2, 1],    
        [2, 3, 7, 8, 10]       
    ]

    for i, conjunto in enumerate(exemplos, 1):
        print(f"\nExemplo {i}: {conjunto} → Soma total = {sum(conjunto)}")
        existe, A, B = partition_problem_dp(conjunto)
        if existe:
            print(f"Partição encontrada!")
            print(f"   Subconjunto 1: {A} → soma = {sum(A)}")
            print(f"   Subconjunto 2: {B} → soma = {sum(B)}")
        else:
            print("Impossível particionar.")
        
        print(f"   [Otimizado] Existe partição? {'Sim' if partition_problem_dp_otimizado(conjunto)[0] else 'Não'}")