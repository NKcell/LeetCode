package leetcode

func checkStraightLine(coordinates [][]int) bool {
	var flag bool 
	if coordinates[0][1] == coordinates[1][1]{
		flag = true
	}
	rate := (float64(coordinates[0][0])-float64(coordinates[1][0]))/(float64(coordinates[0][1])-float64(coordinates[1][1]))
	for i:=2; i<len(coordinates); i++{
		if flag{
			if coordinates[i][1] != coordinates[0][1]{
				return false
			}
		}else{
			if coordinates[i][1] == coordinates[0][1]{
				return false
			}
			if (float64(coordinates[0][0])-float64(coordinates[i][0]))/(float64(coordinates[0][1])-float64(coordinates[i][1])) != rate{
				return false
			}
		}
	}
	return true
}