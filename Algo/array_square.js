function arr_squared(arr){
    for (var i = 0; i < arr.length; i++){
        arr[i] = arr[i]*arr[i]
    }
    return arr
}

test = arr_squared([1,2,3,4,5,6,7,8,9])
console.log(test)