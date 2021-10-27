function replace_neg(arr){
    for(var i = 0;i < arr.length;i++){
        if(arr[i] < 0){
            arr[i] = 'Dojo'
        }
    }
    return arr
}

test = replace_neg([1,3,-8,22,17,-33,7,-1])
console.log(test)