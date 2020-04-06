class Solution:
    def letterCombinations(self, digits: str):
        if len(digits) == 0:
            return []
        myDict = dict()
        myDict['2'] = ['a', 'b', 'c']
        myDict['3'] = ['d', 'e', 'f']
        myDict['4'] = ['g', 'h', 'i']
        myDict['5'] = ['j', 'k', 'l']
        myDict['6'] = ['m', 'n', 'o']
        myDict['7'] = ['p', 'q', 'r', 's']
        myDict['8'] = ['t', 'u', 'v']
        myDict['9'] = ['w', 'x', 'y', 'z']
        
        res = [""]

        return self.dfs(myDict, res, digits, 0)

        
    def dfs(self, myDict, res, digits, index):
        if index>=len(digits):
            return res

        newres = list()
        while res:
            tmp = res.pop()
            for i in myDict[digits[index]]:
                newres.append(tmp+i)
        
        return self.dfs(myDict, newres, digits, index+1)

    def letterCombinations1(self, digits):
        interpret_digit = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '}
        all_combinations = [''] if digits else []
        for digit in digits:
            current_combinations = list()
            for letter in interpret_digit[digit]:
                for combination in all_combinations:
                    current_combinations.append(combination + letter)
            all_combinations = current_combinations
        return all_combinations


a = Solution()
print(a.letterCombinations("23"))


