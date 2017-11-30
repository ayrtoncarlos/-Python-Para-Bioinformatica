def long_mottif(data):

    substr = ""

    if len(data) > 1 and len(data[0]) > 0:

        for i in range(len(data[0])):

            for j in range(len(data[0]) - i + 1):

                if j > len(substr) and all(data[0][i:i+j] in x for x in data):

                    substr = data[0][i:i+j]
        
    return substr

f = open("rosalind_lcsm.txt")
content = f.read()

lines  = []

for data in content.split('>'):

    line = ''.join(data.split('\n')[1:]).replace('\n','')

    if line:

        lines.append(line)

print(long_mottif(lines))

f.close()
