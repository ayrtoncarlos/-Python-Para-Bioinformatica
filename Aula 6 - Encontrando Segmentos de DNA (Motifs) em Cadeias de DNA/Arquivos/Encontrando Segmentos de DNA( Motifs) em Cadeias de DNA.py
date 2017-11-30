import re

def locations(segmento, dna):

    pattern = re.compile(r'(?=%s)' % segmento)

    for padrao in pattern.finditer(dna):

        print(padrao.start() + 1, padrao.group())
    
dna1 = "GATATATGCATATACTT"
segmento1 = "ATAT"

print("Caso #1")
locations(segmento1, dna1)



