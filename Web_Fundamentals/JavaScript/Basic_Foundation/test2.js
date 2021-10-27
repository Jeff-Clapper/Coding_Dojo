function reverseArray(arr) {
    // var end = arr.length-1;
    for(var index = 0; index < (arr.length/2); index++) {
        [arr[index], arr[arr.length-(index+1)]] = arr[arr.length-(index+1)], arr[index]];
        // end--;
    }
    return arr
}

var test = reverseArray([0,1,2,3,4,5]);
console.log(test)

//or

console.log(reverseArray([0,1,"threat",3,4,"cat"]))