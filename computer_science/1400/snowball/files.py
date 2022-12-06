import os

# os.remove('test.txt')
# os.mknod('test.txt')

# file = open("test.txt", "a")

# contents = [
#     "header",
#     "subheader",
#     "body",
#     "footer",
# ]

# for content in contents:
#     file.write(content + "\n")


# with open('test.txt') as file:
#     for line in file:
#         print(line)


snowballFile = open("sandbox.txt", "a")

contents = [
    "This is an exercise",
]

for line in contents:
    snowballFile.write("This is an exercise")

with open('sandbox.txt') as file:
    for line in file:
        print(line)