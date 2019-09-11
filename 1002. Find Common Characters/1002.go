package main

import(
	"fmt"
	"math"
	"strings"
)

func main(){
	fmt.Println(commonChars([]string{"ellab", "allbe", "llekf"}))
}

func commonChars(A []string) []string {
	myDict := make(map[byte]int, len(A[0]))
	for i:=0; i<len(A[0]); i++{
		v,ok := myDict[A[0][i]]
		if !ok{
			myDict[A[0][i]] = 1
		}else{
			myDict[A[0][i]] = v+1
		}
	}

	for i:=1; i<len(A); i++{
		tmpDict := make(map[byte]int)
		for j:=0; j<len(A[i]); j++{
			v,ok := tmpDict[A[i][j]]
			if !ok{
				tmpDict[A[i][j]] = 1
			}else{
				tmpDict[A[i][j]] = v+1
			}
		}


		for k, v := range myDict{
			tmpv, ok := tmpDict[k]
			if !ok{
				myDict[k] = 0
			}else{
				if tmpv<v{
					myDict[k] = tmpv
				}
			}
		}
	} 
	

	var myre []string
	for k, v := range myDict{
		if v != 0{
			for i:=0; i<v; i++{
				myre = append(myre, string(k))
			}
		}
	}
	return myre
}

// 下面这个方法没用到字典，整体思路也很清晰，充分利用来只有小写字母这一条件
func commonChars1(A []string) []string {
    cnt := countChars(A[0])
    for _, word := range(A[1:]) {
        wcnt := countChars(word)
        takeMin(cnt, wcnt)
    }
    return reconstruct(cnt)
}

func countChars(word string) *[]int {
    cnts := make([]int, 26)
        for _, c := range(word) {
        cnts[c-'a']++
    }
    return &cnts
}

func takeMin(a, b *[]int) {
    for i, c := range(*a) {
        if (*b)[i] < c {
            (*a)[i] = (*b)[i]
        }
    }
}

func reconstruct(cnts *[]int) []string {
    res := []string{}
    for c, n := range(*cnts) {
        for j := 0; j < n; j++ {
            res = append(res, string(c+'a'))
        }
    }
    return res
}

// 这个方法和上面的方法基本一样
func commonChars2(A []string) []string {
    tmp := make([]int,26)
    for i:=range tmp{
        tmp[i]=math.MaxInt32
    }
    tmp2 := make([]int,26)
    for _,str := range A {
        for _,c := range []byte(str){
            tmp2[c-byte('a')]++
        }
        for i:=0;i<26;i++{
            tmp[i]=min(tmp[i],tmp2[i])
        }
        for i:=0;i<26;i++{
            tmp2[i]=0
        }
    }
    var rst []string
    for i,v := range tmp{
        for k:=0;k<v;k++{
            rst = append(rst,string([]byte{byte(i)+byte('a')}))
        }
    }
    return rst
}
func min(i,j int)int{
    if i<j {
        return i
    }
    return j
}

//这个方法看起来好麻烦...但实际比我的方法快很多啊...简直不是一个数量级
func commonChars3(A []string) []string {
	res := []string{}
	for i := range A[0] {
		currentString := A[0][i : i+1]
		find := true
		for j := 1; j < len(A); j++ {
			if strings.Index(A[j], currentString) == -1 {
				find = false
				break
			}
		}
		if find  {
			// 消耗一个
			res = append(res, currentString)

			for j := 1; j < len(A); j++ {
				currentStringIndex := strings.Index(A[j], currentString)
				A[j] = A[j][:currentStringIndex] + A[j][currentStringIndex+1:]
			}
		}
	}
	return res
}