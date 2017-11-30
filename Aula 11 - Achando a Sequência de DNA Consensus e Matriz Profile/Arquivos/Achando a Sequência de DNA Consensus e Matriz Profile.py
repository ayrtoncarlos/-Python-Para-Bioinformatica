f = open("sequences.txt")

content = f.read()

lines = []

for data in content.split('>'):

    line = ''.join(data.split('\n')[1:]).replace('\n', '')

    if line:

        lines.append(line)

f.close()

'''
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
'''

result = []

for idx, n in enumerate(['A', 'C', 'G', 'T']):

    result.append([])
    result[idx].append(n + ':')

    for i in range(len(lines[0])):

        total = 0

        for dna in lines:

            if dna[i] == n:

                total += 1

        result[idx].append(total)

consensus = ""

for i in range(len(lines[0])):

    column = []

    for row in result:

        column.append(row[1:][i])

    maximum = column.index(max(column))
    consensus += ['A', 'C', 'G', 'T'][maximum]

print(consensus)

for row in result:

    print(' '.join(map(str,row)))

