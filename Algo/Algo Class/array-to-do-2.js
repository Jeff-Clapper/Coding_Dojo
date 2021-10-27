// given numerical array, reverse the order of values, in-place. rev. array should have the same length, with existing elements moved to other indices so that order of 
// elements is reversed. Working 'in-place' means that you cannot use a second array - move values within the array that you are given. no built-in array functions

function reverseArr(arr) {
    var ind2 = arr.length-1;
    var holder;
    for(var ind = 0; ind < (arr.length/2); ind++) {
        holder = arr[ind];
        arr[ind] = arr [ind2];
        arr[ind2] = holder;
        ind2--;
    }
    return arr
}

function reverseArr2(arr) {
    var ref
    var sums
    for(var ind = 0; ind < arr.length/2; ind++) {
        ref = arr[ind]
        sums = arr[ind] + arr[arr.length-(ind+1)]
        arr[ind] = sums-ref
        arr[arr.length-(ind+1)] = sums-arr[ind]
    }
    return arr
}


//Given array and offset value, shift arr's values to the right by that amount. "wrap-around" any values that shift off arrays's end to the other side, so that no data 
//is lost. operate in-place. NO BUILT-INS. 
//Second: allow neg shift (shift L or R)
//Third: minimize mem usage (no new aray, handles arrays/shits in the millions)
//minimize the touches of each element
function rotateArr(arr, shiftBy) {
    var is_neg
    if (shiftBy < 0) {
        shiftBy *= -1
        is_neg = true
    }
    if (shiftBy > arr.length) {
        shiftBy -= arr.length
    } 
    arr.length += shiftBy
    if(is_neg != true) {
        for(ind = arr.length-1; ind > shiftBy-1; ind--) {
            arr[ind] = arr[ind-shiftBy]
        }
        for(ind =1; ind <= shiftBy; ind++) {
            arr[shiftBy-ind] = arr[arr.length-ind];
        }
    }
    else {
        for(ind =1; ind <= shiftBy; ind++) {
            arr[arr.length-ind] = arr[shiftBy-ind];
        }
        for(ind = 0; ind < arr.length-shiftBy; ind++) {
            arr[ind] = arr[ind+shiftBy]
        }
        
    }
    arr.length -= shiftBy
    return arr
} 


//given array, min, and max, retain ony the array values between min and max. Work in-place; return the array you are gien, with values in original order
function filterRange1(arr,min,max) {
    for(ind=0; ind <= (max-min); ind++) {
        arr[ind] = arr[min+ind]
    }
    arr.length = (max-min+1)
    return arr
}

//possible understanding #2. Function moveToBack is for the actual solving 
function moveToBack(arr, ind){
    var holder
    for(ind = ind; ind < arr.length-1; ind++) {
        holder = arr[ind];
        arr[ind] = arr[ind+1];
        arr[ind+1] = holder;
    }
    return arr
}


function filterRange2(arr,min,max) {
    var count = 0
    for(ind = arr.length-1; ind >= 0; ind--) {
        if ((arr[ind] < min) || (arr[ind] > max)){
            moveToBack(arr,ind)
            count ++
        }
    }
    
    arr.length -= count
    return arr
}

//Replicate JavaScripts concat. create a standalone function that accepts two arrays. Return a
// new array containing the first array's elements, followed by the second array's elements. 
//Do not alter original arrays
function arrConcat(arr1,arr2) {
    var newArr = [];
    newArr.length = arr1.length + arr2.length

    var index = 0
    for(ind = 0; ind < arr1.length; ind++) {
        newArr[index] = arr1[ind];
        index++;
    }
    for(ind = 0; ind < arr2.length; ind++) {
        newArr[index] = arr2[ind];
        index++;
        }
    return newArr
}
