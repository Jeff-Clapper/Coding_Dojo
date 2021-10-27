function max(max_arr){
    //returns the maximum of an array
    
    return max
}

function min(min_arr){
    //returns the mininum of an array
    while (min_arr.length > 1){
        if(min_arr[0] < min_arr[(min_arr.length)-1]){
            min_arr.pop()
        }
        else{
            var x = min_arr[0]
            min_arr[0] = min_arr[(min_arr.length)-1]
            min_arr[(min_arr.length)-1] = x
            min_arr.pop()
        }
    }
    var min = min_arr[0]
    return min
}

function ave(ave_arr){
    //returns the average of an array
    average = 0
    for(var i=0;i<ave_arr.length;i++){
        average = average + ave_arr[i]
    }
    average = average/(ave_arr.length)
    return average
}

function max_min_ave(arr){
    //Creates a new array that contains the max, the min, and the ave
    var max_arr = arr;
    var min_arr = arr;
    var ave_arr = arr;
    while (max_arr.length > 1){
        if(max_arr[0] > max_arr[(max_arr.length)-1]){
            max_arr.pop()
        }
        else{
            var x = max_arr[0]
            max_arr[0] = max_arr[(max_arr.length)-1]
            max_arr[(max_arr.length)-1] = x
            max_arr.pop()
        }
    }
    var max = max_arr[0]

var test = max_min_ave([2,8,19,-2,6,10,1])
console.log(test)