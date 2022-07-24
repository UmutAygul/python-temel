def q1():

    listem = [[1, 2, 3], [True, False], [6.1, 7.3, 8.0], ['a', 'b', 'c'],[[[[3]]]],4,[["a"],2,4]]
    joinedlist = lambda listem:[c for i in listem for c in joinedlist(i)] if type(listem) is list else [listem]

    print(joinedlist(listem))

q1()


def q2():
    inputlist= [[1, 2], [3, 4], [5, 6, 7],["aa","b"]]

    for i in range(len(inputlist)):
        for j in range(1):
            inputlist[i].reverse()


    inputlist.reverse()
    print(inputlist)
q2()