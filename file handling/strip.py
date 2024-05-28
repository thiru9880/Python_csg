# text = ' hello! '
# stripped_text = text.rstrip()
# print(stripped_text)

with open('data.txt', 'r') as file:
    content = file.readlines()

for line in content:
    print(line.strip())