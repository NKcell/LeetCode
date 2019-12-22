package leetcode

func isLongPressedName(name string, typed string) bool {
    if len(name)>len(typed){
		return false
	}
	pre := 0
	namelist := make([]string, 0)
	for i:=0; i<len(name)-1; i++{
		if name[i] != name[i+1]{
			namelist = append(namelist, name[pre:i+1])
			pre = i+1
		}
	}

	pre = 0
	typedlist := make([]string, 0)
	for i:=0; i<len(typed)-1; i++{
		if typed[i] != typed[i+1]{
			typedlist = append(typedlist, typed[pre:i+1])
			pre = i+1
		}
	}

	if len(typedlist)!=len(namelist){
		return false
	}

	for i:=0; i<len(namelist); i++{
		if len(typedlist[i])<len(namelist[i]) || typedlist[i][0] != namelist[i][0]{
			return false
		}
	}

	return true
}

func isLongPressedName1(name, typed string) bool {
	if name == typed {
		return true
	}
	nameSize := len(name)
	typedSize := len(typed)
	i, j := 0, 0
	for i < nameSize {
		c := name[i]
		pressMore := 0
		for i < nameSize && name[i] == c {
			i++
			pressMore--
		}
		for j < typedSize && typed[j] == c {
			j++
			pressMore++
		}
		if pressMore < 0 {
			return false
		}
	}
	return j == typedSize
}