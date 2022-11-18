import os


labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
          'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
for i in labels:
    os.mkdir(str(i))


# # Load the labels
# class_names = open('Model/labels.txt', 'r').readlines()
# print(class_names[1])
# for i in class_names:
#     line = i.strip("\n")
#     print(line, list(line)[-1])


# lables = [list(i.strip("\n"))[-1] for i in class_names]

# print(lables)
