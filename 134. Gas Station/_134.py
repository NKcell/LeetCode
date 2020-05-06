class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i,v in enumerate(gas):
            if v-cost[i]>=0:
                if self.isok(gas[i:]+gas[0:], cost[i:]+cost[0:]):
                    return i

        return -1


    def isok(self, gas, cost):
        tmp = 0
        for i,v in enumerate(gas):
            tmp += (v-cost[i])
            if tmp<0:
                return False

        return True

    def canCompleteCircuit1(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1

        start  = 0
        remain = 0

        for i,v in enumerate(gas):
            remain += (v-cost[i])
            if remain<0:
                start = i+1
                remain = 0
        
        return start