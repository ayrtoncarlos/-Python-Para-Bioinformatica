'''
n = número de meses
pares = ?

A gente começa com 1 par de coelhos, e em cada geração,
1 par produz k pares de coelhos.

n = 5, k = 3

Fn = número de coelhos na geração n

F1 = 1
F2 = 1
F3 = 1 + 3 * 1 = 4
F4 = 4 + 3 * 1 = 7
F5 = 7 + 4 * 3 = 19 Coelhos

Fórmula:

    Fn = F(n-1) + k * F(n-2)

'''

# Método 1

def population(n, k):

    rabbits_populations = []

    for i in range(n):

        if i < 2:

            rabbits_populations.append(1)

        else:

            rabbits_populations.append(rabbits_populations[-1] + rabbits_populations[-2] * k)

    return rabbits_populations


# Método 2: Recursivo

def population_recursive(n, k):

    if n == 1:

        return 1

    elif n == 2:

        return 1

    else:

        return population_recursive(n-1, k) + k * population_recursive(n-2, k)

# Método 3: Memoização

memo = {}

def population_memoization(n, k):

    args = (n, k)

    if args in memo:

        return memo[args]
    
    if n == 1:

        ans = 1

    elif n == 2:

        ans = 1

    else:

        ans = population_memoization(n-1, k) + k * population_memoization(n-2, k)

    memo[args] = ans

    return ans

n = 5
k = 3

out1 = population(n, k)
out2 = population_recursive(n, k)
out3 = population_memoization(n, k)
print(out1)
print(out2)
print(out3)
