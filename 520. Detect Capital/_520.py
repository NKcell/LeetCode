class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        tmp1 = word
        tmp2 = word
        tmp3 = word
        if tmp1.upper() == word or tmp2.lower() == word or tmp3.capitalize()==word:
            return True
        return False

    def detectCapitalUse1(self, word):
        return word.isupper() or word.islower() or word.istitle()

    def detectCapitalUse2(self, word):
        return word[1:]==word[1:].lower() or word==word.upper()