# -*- coding: utf-8 -*-

import os, uuid, json

def bsearch(lst, elt):
    left = 0
    right = len(lst) -1

    while True:
        if right < left:
            return False, left

        pivot = left + ((right - left) / 2)
        test = lst[pivot]
        if elt == test:
            return True, pivot
        elif elt < test:
            right = pivot - 1
        else:
            left = pivot + 1

class RawData(object):
    def __init__(self):
        self.idlist = []
        self.datalist = []

    def select(self, uid):
        found, index = bsearch(self.idlist, uid)
        if found:
            return uid, self.datalist[index]
        else:
            return None

    def insert(self, data):
        uid = uuid.uuid4().int
        _, index = bsearch(self.idlist, uid)
    
        self.idlist.insert(index, uid)
        self.datalist.insert(index, data)
        return uid

    def update(self, uid, data):
        found, index = bsearch(self.idlist, uid)
    
        if found:
            self.datalist[index] = data
            return True
        else:
            return False
    
    def delete(self, uid):
        found, index = bsearch(self.idlist, uid)
    
        if found:
            del self.idlist[index]
            del self.datalist[index]
            return True
        else:
            return False
    
    def search(self, pred):
        for index in (index for (index, elt) in enumerate(self.datalist) if pred(elt) == True):
            yield self.idlist[index], self.datalist[index]

    def dump(self):
        return [(uid, self.datalist[index]) for (index, uid) in enumerate(self.idlist)]

if __name__ == '__main__':
    database = RawData()

    apple = database.insert("apple")
    orange = database.insert("orange")
    banana = database.insert("banana")
    pineapple = database.insert("pineapple")

    print database.dump()

    print database.select(apple)
    print database.select(banana)
    print database.select(0)

    database.update(apple, "green apple")
    database.delete(banana)
    
    print database.dump()
    
    for (uid,data) in database.search(lambda data: data.find("apple") >= 0):
        print "found: %x %s" % (uid, data)


    database.insert({"menu":"spam","price":1000})
    database.insert({"menu":"egg","price":300})
    database.insert({"menu":"ikura","price":3000})

    for (uid, data) in database.search(lambda elt: type(elt) == dict and elt.get("price",0) > 500):
        print "found: %x %s" % (uid, data)

    print "end."
    
    
