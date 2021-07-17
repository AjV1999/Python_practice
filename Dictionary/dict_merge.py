def dictionary_merge(*dicts):
    res = dict()
    #print(dicts)
    for i in dicts:
        res.update(i)
    return res
car1 = {'Audi':1, 'Mercedes':2, 'BMW':3}
car2 = {'Ferrari':10, 'Bentley':20, 'Porsche':30}
print("Dictionaries with cars: ")
print(car1)
print(car2)
print("Merged Dictionaries: ")
print(dictionary_merge(car1, car2))
