function arr_ave(arr){
    var sum =0;
    for(var i = 0; i < arr.length; i++){
        sum = sum + arr[i];
    }
    var aver = sum/(arr.length);
    return(aver)
}

test = arr_ave([19,3,8,33,-12,2])
console.log(test)