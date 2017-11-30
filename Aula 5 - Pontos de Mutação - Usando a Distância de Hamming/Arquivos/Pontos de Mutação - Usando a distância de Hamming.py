def hamming(dna1, dna2):

    total = 0

    for i in range(len(dna1)):

        if dna1[i] != dna2[i]:

            total += 1

    return total

dna1 = "GAGCCTACTAACGGGAT"
dna2 = "CATCGTAATGACGGCCT"

total = hamming(dna1, dna2)
print(total)
