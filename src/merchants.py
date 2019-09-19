"""
CSAPX Lab 3: Merchants of Venice

Given a list of merchants at integer locations on a road, find the optimal
location to place a new merchant, such that the sum of the distances the
new merchant must travel to all other merchants is minimized.

$ python3 merchants.py [slow|fast] input-file

Author: Sean Strout @ RIT CS
Author: Ayane Naito
"""
import collections      # namedtuple
import sys              # arg
import time             # clock
import random           # random

from typing import List # List
from typing import Tuple

"""
Merchant:
    name (str): Merchant's name
    loc (int): Merchant's location on the Grand Canal
"""
Merchant = collections.namedtuple('Merchant', ['name', 'loc'])

def read_merchants(filename: str) -> List[Merchant]:
    """
        Read merchants from a file into a list of Person namedtuples.
        :param filename: The name of the file
        :return: A list of Person
        """
    merchants = list()
    with open(filename) as f:
        for line in f:
            fields = line.split()
            merchants.append(Merchant(
                name=fields[0],
                loc=int(fields[1]),
            ))
    return merchants

def _partition(data: List[Merchant], pivot: Merchant) \
      -> Tuple[List[Merchant], List[Merchant], List[Merchant]]:
    """
    Three way partition the data into smaller, equal and greater lists,
    in relationship to the pivot
    :param data: The data to be sorted (a list)
    :param pivot: The value to partition the data on
    :return: Three list: smaller, equal and greater
    """
    less, equal, greater = [], [], []
    for element in data:
        if element.loc < pivot.loc:
            less.append(element)
        elif element.loc > pivot.loc:
            greater.append(element)
        else:
            equal.append(element)
    return less, equal, greater

def quick_sort(data: List[Merchant]) -> List[Merchant]:
    """
    Performs a quick sort and returns a newly sorted list
    :param data: The data to be sorted (a list)
    :return: A sorted list
    """
    if len(data) == 0:
        return []
    else:
        pivot = data[0]
        less, equal, greater = _partition(data, pivot)
        return quick_sort(less) + equal + quick_sort(greater)



def main() -> None:
    """
    The main function.
    :return: None
    """
    merchants = read_merchants(sys.argv[1])
    start = time.perf_counter()
    sorted_merchants = quick_sort(merchants)

if __name__ == '__main__':
    main()