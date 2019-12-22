package leetcode

func uniqueMorseRepresentations(words []string) int {
	morse := []string{".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."}
	res := make(map[string]bool, 0)

	for _,word := range words{
		tmp := ""
		for _, v := range word{
			tmp += morse[v-'a']
		}
		res[tmp] = true
	}
	return len(res)
}