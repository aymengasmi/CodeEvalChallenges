import sys


def  gray_to_binary(num_input):
    list_num = [x for x in num_input]
    res = []
    k = 0
    for num in list_num :
        if k == 0 : 
            res.append(num)
            k+=1
            continue
        else : 
            if num == '0':
                res.append(res[k-1])
            else :
                if res[k-1] == '1':
                    res.append('0')
                else : res.append('1')
            k += 1
    return ''.join(res)

with open(sys.argv[1], 'r') as test_cases:  
    for line in test_cases:
        line = line.rstrip('\n')
        line = line.split(' | ')
        line = [str(int(gray_to_binary(x),2)) for x in line ]
        print ' | '.join(line)
