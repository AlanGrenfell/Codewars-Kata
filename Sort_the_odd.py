list = []
odd_index_list = []

odds = sorted([n for n in list if n%2])

def index_grabber(odds):
        for n in odds:
            list.index(n)
            odd_index_list.append(list.index(n))

def odd_attempter(list):
    for index, num in zip(sorted(odd_index_list), odds):
        list[index] = num

def sort_array(list):
    if len(list) == 0:
        print(list)
    else:
        index_grabber(odds)
        odd_attempter(list)
        print(list)

sort_array(list)
