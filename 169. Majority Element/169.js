var majorityElement = function(nums) {
    var mymap = new Map()
    flag = nums.length/2
    for (i=0;i<nums.length;i++){
        count = mymap.get(nums[i])
        if (count == null){
            count = 1
            mymap.set(nums[i],count)
        }else{
            count++
        }
        if (count>flag){
            return nums[i]
        }
        mymap.set(nums[i],count)    
    }
};

var majorityElement1 = function(nums) {
    var obj = {};    
    for(var i = 0; i < nums.length; i++){
        obj[nums[i]] = obj[nums[i]] + 1 || 1;
        if(obj[nums[i]] > nums.length / 2)  return nums[i];
    }   
};

console.log(majorityElement([1,2,2]))