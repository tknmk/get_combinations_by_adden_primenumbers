# -*- coding: utf-8 -*-

import sys
import numpy as np
import itertools
import pprint

# input a base number from console.
argvs = sys.argv
pn = int(argvs[1])


def main():
    # print Prime Numbers and count them
    pn_nums = get_prime_nums(pn)
    pn_count = len(pn_nums)
    print('Prime numbers are {0}'.format(pn_nums))
    print('Prime numbers count: {0}'.format(pn_count))

    # print combinations
    pairs = get_combinations(pn_nums, pn)
    pairs_count = len(pairs)
    print('Combinations:')
    pprint.pprint(pairs)
    print('Combinations count: {0}'.format(pairs_count))

def get_prime_nums(pn):

    max = int(np.sqrt(pn))
    #print(max)
    seachList = [i for i in range(2,pn+1)]
    #print(seachList)
    
    primeNum = []
    while seachList[0] <= max:
        primeNum.append(seachList[0])
        tmp = seachList[0]
        seachList = [i for i in seachList if i % tmp != 0]
    primeNum.extend(seachList)
    return primeNum


def get_combinations(nums, base_num):

    #result = []
    result = [seq for i in range(len(nums), 0, -1) for seq in itertools.combinations(nums, i) if sum(seq) == base_num]
    return result

    #for i in range(len(nums), 0, -1):
    #        for seq in itertools.product(nums, repeat=i):
    #            if sum(seq) == base_num:
    #                result.append(seq)
    #    return result



if __name__ == '__main__':
    main()
