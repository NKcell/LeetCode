def solution(n: int) -> int:
        mylist = [n]
        step = 0

        while True:
            step += 1
            tmp = set()
            while mylist:
                n = mylist.pop()
                for i in range(1, int(n**0.5)+1):
                    cha = n-i**2
                    if cha == 0:
                        return step
                    else:
                        tmp.add(cha)
            mylist = list(tmp)

        return step