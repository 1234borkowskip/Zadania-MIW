import csv
import math


def normalize(data=None, index=None):
    row = [i for i in zip(*data)][index]
    row = [float(i) for i in row]
    min_row = min(row)
    max_row = max(row)
    return (float(row[index]) - min_row) / (max_row - min_row)

def get_min_and_max(data=None, index=None):
    row = [i for i in zip(*data)][index]
    row = [float(i) for i in row]

    return min(row), max(row)

def euclidean(row1, row2):
    distance = 0.0
    for i in range(len(row1)):
        distance += (row1[i] - row2[i])**2

    return math.sqrt(distance)

def manhattan(row1, row2):
    distance = 0.0
    for i in range(len(row1)):
        distance = abs(row1[i] - row2[i])

    return distance

def logarithm(row1, row2):
    distance = 0.0
    for i in range(len(row1)):
        if row1[i] <= 0:
            value1 = 0
        else:
            value1 = math.log(row1[i])
        if row2[i] <= 0:
            value2 = 0
        else:
            value2 = math.log(row1[i])
        distance = abs(value1-value2)

    return distance

def czebyszew(row1, row2):
    distance = 0.0
    for i in range(len(row1)):
        distance = max(abs(row1[i] - row2[i]))

    return distance

def minkowski(row1, row2, p):
    distance = 0.0
    for i in range(len(row1)):
        distance = ((abs(row1[i] - row2[i])**p))**(1/p)
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
    for index, value in enumerate(row):
        if index in class_index:
            normalized_row.append(value)
            continue
        _min, _max = get_min_and_max(data=iris, index=index)
        normalized = (float(value) - _min) / (_max - _min)
        normalized_row.append(normalized)
    normalized_iris.append(normalized_row)

testrow = [1, 1, 1, 1]
distances = []
for row in normalized_iris:
    distance_row = []
    for index, value in enumerate(row):
        if index in class_index:
            distance_row.append(value)
            continue
    distance = euclidean(testrow, row)
    distance_row.append(distance)
    distances.append(distance_row)

for row in distances:
    print(row)

k = 3


def knn1(distances, k):
    knn=[]
    i=0
    distances.sort(key=lambda value: value[1])
    while i < k:
        for row in distances:
            knn.append(row)
            i += 1
    return knn

def knn2(distances, k):
    knn = []
    distances.sort(key=lambda value: value[1])

knn = knn1(distances, k)

# for row in normalized_iris:
#     print(row)

# for row in knn:
#     print(row)
