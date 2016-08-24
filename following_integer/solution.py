import sys 
import itertools

def get_next(stuff,value):
    list1 = []
    irts = []
    irts = [item for item in itertools.permutations(stuff, len(stuff))]
    for item in irts : 
        list1.append( int(''.join(item)) )
    test = []
    test = list(set(list1))
    res = sorted (test)
    k = res.index(value)
    if k == len(res)-1 :
        return 'False'
    else :
        print res[k+1]
  
with open(sys.argv[1], 'r') as test_cases:
    for line in test_cases:  
        val = int(line)
        input = [x for x in str(val)]   
        stuff = input        
        if get_next(stuff,val) == 'False':
            input.append("0")
            get_next(input,val)