package leetcode

func maxArea(height []int) int {
	maxarea, l, r := 0, 0, len(height)-1
	for l<r{
		heighttmp := r-l
		var edge int
		if height[l]>height[r]{
			edge = height[r]
			r--
		}else{
			edge = height[l]
			l++
		}

		if maxarea < edge*heighttmp{
			maxarea = edge*heighttmp
		}
	}
	return maxarea
}