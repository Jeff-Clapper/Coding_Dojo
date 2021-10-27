function compare_arr(y,arr){
    var count = 0
    for (i = 0; i < arr.length;i++){
        if (arr[i] > y){
            count = count +1
        }
    }
    return count
}

test = compare_arr(3,[1,2,5,7])
console.log(test)