import csv
import math

def find_minimal(data=None):
    minimal = None
    for row in data:
        val = int(row[0])
        if not minimal:
            minimal = val
        elif val < minimal:
            minimal = val
    return minimal


def find_maximal(data=None):
    minimal = None
    for row in data:
        val = int(row[0])
        if not minimal:
            minimal = val
        elif val > minimal:
            minimal = val
    return minimal


def normalize(data=None, index=None):
    row = [i for i in zip(*data)][index]
    row = [float(i) for i in row]
    min_row = min(row)
    max_row = max(row)
    return (float(row[index]) - min_row) / (max_row - min_row)

def euclidean(row1, row2):
    distance = 0.0
    for i in range(len(row1)-1):
        distance += (row1[i] - row2[i])**2
    return math.sqrt(distance)

def manhattan(row1, row2):
    distance = 0.0
    for i in range(len(row1)-1):
        distance = abs(row1[i] - row2[i])
    return distance


with open('datasets/iris.txt') as f:
    reader = csv.reader(f, delimiter='	')

    iris = []
    for row in reader:
        iris.append(row)


with open('datasets/iris.txt') as f:
    reader = csv.reader(f, delimiter='	')

    iris_class = []
    for row in reader:
        iris_class.append(row[4])

normalized_iris = []

class_index = [4]
for row in iris:
    normalized_row = []
    for index, _ in enumerate(row):
        if index in class_index:
            normalized_row.append(iris_class[index])
            continue
        normalized = normalize(data=iris, index=index)
        normalized_row.append(normalized)
    normalized_iris.append(normalized_row)

# for row in normalized_iris:
#     print(row)
