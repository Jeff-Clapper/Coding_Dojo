function return_max(arr){
    var keep = 0;
    while (arr.length > 1){
        if (arr[0] >= arr[(arr.length)-1]){
            arr.pop()
        }
        else {
            var x = arr[(arr.length)-1]
            arr[(arr.length)-1] = arr[0]
            arr[0] = x
            arr.pop()
            }
    keep = arr[0]
    }
    return keep
}

test = return_max([1,5,-300,16,-2,19,12])
console.log(test)
