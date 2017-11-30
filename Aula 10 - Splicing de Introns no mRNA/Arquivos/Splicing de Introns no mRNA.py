import re

f = open("rna_codon_table.txt")

table = {}

for line in f:

    line = line.strip()
    line = [ (codon.split(' ')[0], codon.split(' ')[1]) for codon in re.split(r'[ ]{2,3}', line) if codon]

    for r in line:

        table[r[0]] = r[1]

f.close()

def transcription(dna):

    return dna.replace('T', 'U')

def translation(rna):

    protein = ""

    for start in range(0, len(rna),3):

        if table[rna[start:start+3]] != "Stop":

            protein += table[rna[start:start+3]]

    return protein

def splicing(mRNA, introns):

    for intron in introns:

        mRNA = mRNA.replace(intron, '')

    return mRNA

f = open("rosalind_splc.txt")

content = f.read()

lines = []

for data in content.split('>'):

    line = ''.join(data.split('\n')[1:]).replace('\n', '')

    if line:

        lines.append(transcription(line))

exons = splicing(lines[0], lines[1:])

print(translation(exons))

f.close()

