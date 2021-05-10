
import config as cf
from storages.factory import StorageFactory

results1 = []

results2 = []
for row in cf.credit_card_details:
    normalized_row = []
    for index, value in enumerate(row):

        _min, _max = cf.get_min_and_max(data=cf.credit_card_details, index=index)
        normalized = (float(value) - _min) / (_max - _min)
        normalized_row.append(normalized)

    results1.append(normalized_row)

Storage1 = StorageFactory.factory('txt')
Storage2 = StorageFactory.factory('txt')
storage1 = Storage1()
storage2 = Storage2()
storage1.save('australian', data=results1)
storage2.save('wpbc', data=results2)


