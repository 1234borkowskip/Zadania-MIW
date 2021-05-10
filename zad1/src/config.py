import csv


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


def get_min_and_max(data=None, index=None):
    row = [i for i in zip(*data)][index]
    row = [float(i) for i in row]

    return min(row), max(row)


crx_valuesA1 = {"a": 0, "b": 1}

crx_valuesA4 = {"p": 1, "g": 2, "gg": 3}

crx_valuesA5 = {"ff": 1, "d": 2, "i": 3, "k": 4, "j": 5, "aa": 6, "m": 7, "c": 8, "w": 9, "e": 10, "q": 11, "r": 12,
                "cc": 13, "x": 14}
crx_valuesA6 = {"ff": 1, "dd": 2, "j": 3, "bb": 4, "v": 5, "n": 6, "o": 7, "h": 8, "z": 9}

crx_valuesA8A9A11 = {"t": 0, "f": 1}

crx_valuesA12 = {"s": 1, "g": 2, "p": 3}

crx_valuesA15 = {"+": 1, "-": 2}

breast_cancer_wisconsin_values = {"?": None}

with open('../datasets/australian.dat') as f:
    reader = csv.reader(f, delimiter=' ')

    credit_card_details = []
    for row in reader:
        credit_card_details.append(row)

with open('../datasets/crx.data') as f:
    reader = csv.reader(f, delimiter=',')

    credit_approval = []
    for row in reader:
        credit_approval.append(row)

with open('../datasets/breast-cancer-wisconsin.data') as f:
    reader = csv.reader(f, delimiter=',')

    breast_cancer_wisconsin = []
    for row in reader:
        breast_cancer_wisconsin.append(row)
