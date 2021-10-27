function replace_first_last(arr){
    var x = arr[0]
    arr[0] = arr[(arr.length)-1]
    arr[(arr.length)-1] = x
    return arr
}

test = replace_first_last([-1,13,-8,4,110,84,-1,2])
console.log(test)
