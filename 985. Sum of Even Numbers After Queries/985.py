class Solution:
    def sumEvenAfterQueries(self, A, queries) :
        sum = 0
        for value in A:
            if value % 2 == 0:
                sum += value

        relist = list()
        for i in queries:
            if A[i[1]]%2 == 0:
                if i[0]%2 == 0:
                    sum += i[0]
                else:
                    sum -= A[i[1]]
                A[i[1]] = A[i[1]] + i[0]
            else:
                A[i[1]] = A[i[1]] + i[0]
                if i[0]%2 != 0:
                    sum += A[i[1]]    
            relist.append(sum)
        
        return relist

    def sumEvenAfterQueries1(self, A, queries):
        cur_sum = sum([num for num in A if not num & 1]) #列表表达式和与的用法
        res = []
        for val,idx in queries: # 这个写法很好啊
            if A[idx] & 1 and val & 1:
                cur_sum += A[idx] + val
            elif not A[idx] & 1 and val & 1:
                cur_sum -= A[idx]
            elif not A[idx] & 1 and not val & 1:
                cur_sum += val
            A[idx] += val
            res.append(cur_sum)
        return res

a = Solution()
print(a.sumEvenAfterQueries([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]]))