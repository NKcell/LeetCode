"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        myDict = {}
        for i in employees:
            myDict[i.id] = [i.importance, i.subordinates]
        
        res = 0
        def getres(myDict, id, res):
            res += myDict[id][0]
            if myDict[id][1]:
                for i in myDict[id][1]:
                    res = getres(myDict, i, res)
            return res

        return getres(myDict, id, res)

    def getImportance1(self, employees, id):
        # Time: O(n)
        # Space: O(n)
        emps = {employee.id: employee for employee in employees}
        def dfs(id):
            subordinates_importance = sum([dfs(sub_id) for sub_id in emps[id].subordinates])
            return subordinates_importance + emps[id].importance
        return dfs(id) 
