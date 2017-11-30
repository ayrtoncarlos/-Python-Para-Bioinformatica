import re

f = open("sample.txt")

maxest = [-1, -1]

for fasta in re.split(r'>', f.read()[1:]):

    label= fasta.split("\n")[0]
    dna = ''.join([code.strip() for code in fasta.split("\n")[1:]])
    gc_content = (dna.count('G') + dna.count('C')) / float(len(dna))

    if gc_content > maxest[1]:

        maxest[0] = label
        maxest[1] = gc_content

print(maxest[0])
print("%.6f" % (maxest[1] * 100))

f.close()
