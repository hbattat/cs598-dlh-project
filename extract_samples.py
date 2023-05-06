import re


ids = []
output_file = open('samples.csv', 'a')

with open('listfile.csv', 'r') as file:
    lines = file.readlines()[1:]
    for line in lines:
        id = re.search(r'^(\d+)_.*?', line).group(1)
        if (len(ids) < 400):
            ids.append(id)
        elif id in ids:
            output_file.write(line)

print(len(ids))
output_file.close()
