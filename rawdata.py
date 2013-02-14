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

def select(idlist, datalist, id):
    found, index = bsearch(idlist, id)
    if found:
        return datalist[index]
    else:
        return None

def insert(idlist, datalist, data):
    id = uuid.uuid4().int
    _, index = bsearch(idlist, id)

    idlist.insert(index, id)
    datalist.insert(index, data)
    return id

def update(idlist, datalist, id, data):
    found, index = bsearch(idlist, id)

    if found:
        datalist[index] = data
        return True
    else:
        return False

def delete(idlist, datalist, id):
    found, index = bsearch(idlist, id)

    if found:
        del idlist[index]
        del datalist[index]
        return True
    else:
        return False

def search(idlist, datalist, pred):
    for index in (index for (index, elt) in enumerate(datalist) if pred(elt) == True):
        yield idlist[index]
        
if __name__ == '__main__':
    idlist = []
    datalist = []

    apple = insert(idlist, datalist, "apple")
    orange = insert(idlist, datalist, "orange")
    banana = insert(idlist, datalist, "banana")
    pineapple = insert(idlist, datalist, "pineapple")

    print idlist
    print datalist

    print select(idlist, datalist, apple)
    print select(idlist, datalist, banana)
    print select(idlist, datalist, 0)

    update(idlist, datalist, apple, "green apple")
    delete(idlist, datalist, banana)
    
    print idlist
    print datalist

    for id in search(idlist, datalist, lambda data: data.find("apple") >= 0):
        print "found: %s" % select(idlist, datalist, id)


    insert(idlist,datalist,{"menu":"spam","price":1000})
    insert(idlist,datalist,{"menu":"egg","price":300})
    insert(idlist,datalist,{"menu":"ikura","price":3000})

    for id in search(idlist, datalist,lambda elt: type(elt) == dict):
        print select(idlist, datalist, id)

    print "end."
    
    
