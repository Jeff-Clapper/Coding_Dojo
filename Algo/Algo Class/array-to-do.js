//Push Front: givna array and addition value, insert value at the begining of array. (without builtin functions)
function pushFront(arr,num) {
    arr.length = arr.length + 1
    for(var ind=arr.length-1; ind > 0; ind--) {
        arr[ind] = arr[ind-1]
    }
    arr[ind] = num
    return arr
} 

//Pop Front: ginen array, remoave and return value at beginning. do this without builtins except for pop
function popFront(arr) {
    var temp = arr[0]
    for (var ind = 0; ind < arr.length-1; ind++) {
        arr[ind] = arr[ind+1]
    }
    arr.pop()
    return temp
} 

//Insert At: given array, index, and additional value, insert value into array at index. Do this without built in array methods.
function insertAt(arr,index,value) {
    arr.length += 1
    if (index > arr.length){
        return "index is outside of array (array length < index)"
    }
    for (var ind = arr.length-1; ind > index; ind--) {
        arr[ind] = arr[ind-1]
    }
    arr[ind] = value
    return arr
}

//Remove At: given array and index, remove and return array value at index. dont use any other built-in array methods except pop
function removeAt(arr,index) {
    if (index > arr.length){
        return "index is outside of array (array length < index)"
    }
    var holder = arr[index]
    for (var ind = index; ind < arr.length ; ind++) {
        arr[ind] = arr[ind+1]
    }
    arr.length = arr.length-1
    return holder
}

//Swap Pairs: given array, swap positions of successive pairs. if length is odd, do not change final element. dont use builtins
function swapPairs(arr) {
    var holder;
    for (var ind = 1; ind < arr.length; ind += 2) {
        holder = arr[ind];
        arr[ind] = arr[ind-1];
        arr[ind-1] = holder;
    }
    return arr
}

//Remove Duplicates: given sorted array, remove duplicate values. No built-ins
function removeDup(arr) {
    var compare;
    var newArr = []
    for (var ind = 0; ind < arr.length; ind++) {
        if (arr[ind] !== compare) {
            compare = arr[ind];
            newArr.length++;
            newArr[newArr.length-1] = compare;
        }
        else {
            continue
        }
    }
    return newArr
}

//Remove Duplicates+: given sorted array, remove duplicate values. No built-ins AND no nested loops
function removeDupB(arr1,arr2=[],comp=null) {
    var compare=comp;
    var newArr = arr2;
    if ((arr1.length > 0) && (compare !== arr1[arr1.length-1])) {
        compare = arr1[arr1.length-1];
        newArr.length++;
        newArr[newArr.length-1] = compare;
        arr1.length --;
        removeDupB(arr1,newArr,compare)
    }
    else if ((arr1.length > 0)) {
        arr1.length --;
        removeDupB(arr1,newArr,compare)
    }
    return newArr
}

