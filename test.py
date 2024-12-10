d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

def fonc(d1,d2):
    d3={}
    for k in d1.keys():
        d3[k] = d1[k]
    for k in d2.keys():
        if k not in d3.keys():
            d3[k] = d2[k]
        else:
            d3[k] = d3[k]+d2[k]

    return d3
            
print(fonc(d1,d2))

