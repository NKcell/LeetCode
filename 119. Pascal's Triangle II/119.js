/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function(rowIndex) {
    var mylist = [1]
    for (i=0;i<rowIndex;i++){
        for (j=0;j<mylist.length-1;j++){
            mylist[j] = mylist[j] + mylist[j+1]
        }
        mylist.unshift(1)
    }
    return mylist
};

console.log(getRow(3))