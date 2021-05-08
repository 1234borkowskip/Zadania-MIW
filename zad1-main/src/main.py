import csv

from storages.factory import StorageFactory


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


with open('../datasets/australian.dat') as f:
    reader = csv.reader(f, delimiter= ' ')

    credit_card_details = []
    for row in reader:
        credit_card_details.append(row)

with open('../datasets/crx.data') as f:
    reader = csv.reader(f, delimiter= ',')

    credit_approval = []
    for row in reader:
        credit_approval.append(row)

with open('../datasets/wpbc.data') as f:
    reader = csv.reader(f, delimiter= ',')

    breast_cancer_wisconsin = []
    for row in reader:
        breast_cancer_wisconsin.append(row)


results1 = []
results2 = []
indexes_australian = [1, 2, 6, 9, 12, 13]
indexes_cancer = [1, 2, 34, 35]
indexes_credit = [2, 3, 4]
for row in credit_card_details:
    normalized_row = []
    for index, _ in enumerate(row):
        if index not in indexes_australian:
            continue
        normalized = normalize(data=credit_card_details, index=index)
        normalized_row.append(normalized)
    results1.append(normalized_row)

for row in breast_cancer_wisconsin:
    normalized_row = []
    for index, _ in enumerate(row):
        if index in indexes_cancer:
            continue
        normalized = normalize(data=breast_cancer_wisconsin, index=index)
        normalized_row.append(normalized)
    results2.append(normalized_row)


# for row in credit_approval:
#     normalized_row = []
#     for index, _ in enumerate(row):
#         if index not in indexes_cancer:
#             continue
#         normalized = normalize(data=credit_approval, index=index)
#         normalized_row.append(normalized)
#     results2.append(normalized_row)

#
Storage1 = StorageFactory.factory('txt')
Storage2 = StorageFactory.factory('txt')
#Storage3 = StorageFactory.factory('txt')
storage1 = Storage1()
storage2 = Storage2()
# storage3 = Storage3()
storage1.save('australian', data=results1)
storage2.save('wpbc', data=results2)
#storage3.save('crx', data=results3)


