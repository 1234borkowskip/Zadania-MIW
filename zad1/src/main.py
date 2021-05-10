import csv
import config as cf
from storages.factory import StorageFactory

def get_min_and_max(data=None, index=None):
    row = [i for i in zip(*data)][index]
    row = [float(i) for i in row]

    return min(row), max(row)


with open('../datasets/australian.dat') as f:
    reader = csv.reader(f, delimiter=' ')

    credit_card_details = []
    for row in reader:
        credit_card_details.append(row)

with open('../datasets/crx.data') as f:
    reader = csv.reader(f, delimiter=',')
    credit_approval = []
    row_after_mapping = []
    for row in reader:
        for index, element in enumerate(row):
            mapped = cf.mapping_crx.get(index, {}).get(element)
        if mapped:
            element = mapped
            row_after_mapping.append(element)
        credit_approval.append(row_after_mapping)



with open('../datasets/breast-cancer-wisconsin.data') as f:
    reader = csv.reader(f, delimiter=',')

    breast_cancer_wisconsin = []
    for row in reader:
        breast_cancer_wisconsin.append(row)



results1 = []

results2 = []
for row in credit_card_details:
    normalized_row = []
    for index, value in enumerate(row):

        _min, _max = get_min_and_max(data=credit_card_details, index=index)
        normalized = (float(value) - _min) / (_max - _min)
        normalized_row.append(normalized)

    results1.append(normalized_row)

# for row in cf.credit_card_details:
#     normalized_row = []
#     for index, value in enumerate(row):
#
#         _min, _max = cf.get_min_and_max(data=cf.credit_approval, index=index)
#         normalized = (float(value) - _min) / (_max - _min)
#         normalized_row.append(normalized)
#
#     results1.append(normalized_row)


Storage1 = StorageFactory.factory('txt')
Storage2 = StorageFactory.factory('txt')
storage1 = Storage1()
storage2 = Storage2()
storage1.save('australian', data=results1)
storage2.save('wpbc', data=results2)

for row in credit_approval:
    print(row)
