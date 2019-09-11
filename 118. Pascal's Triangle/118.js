/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    var mylist = []
    if (numRows < 1){
        return mylist
    }
    mylist.push([1])
    for (i=1; i<numRows; i++){
        var right = mylist[i-1].slice()
        var left = mylist[i-1].slice()
        right.push(0)
        left.unshift(0)
        var tmp = []
        for (j=0; j<right.length; j++){
            tmp.push(right[j]+left[j])
        }
        mylist.push(tmp)
    }

    return mylist
};

console.log(generate(2))

/*
1.数组的复制，不能a = b，这样复制，操作a还是在操作b，用slice()进行复制
2.与python不同两个数组相加变为了字符串不再是数组
*/