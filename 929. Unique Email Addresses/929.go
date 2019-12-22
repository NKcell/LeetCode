package leetcode

import(
	"strings"
)

func numUniqueEmails(emails []string) int {
	res := make(map[string]bool, 0)
	for _,v := range emails{
		tmp := strings.Split(v, "@")
		local := tmp[0]
		domain := tmp[1]
		local = strings.Split(local, "+")[0]
		local = strings.Join(strings.Split(local, "."), "")
		res[strings.Join([]string{local, domain},"@")] = true
	}
	return len(res)
}