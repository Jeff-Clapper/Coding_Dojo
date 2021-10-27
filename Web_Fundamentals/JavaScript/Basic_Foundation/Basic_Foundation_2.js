function bigNum(arr){
    for(var index=0; index < arr.length; index++) {
        if(arr[index] > 0){
            arr[index] = 'big' 
        }
    }
    return arr
}

function printLowReturnHigh(arr) {
    var high = arr[0];
    var low = arr[0];
    for(var index=0; index<arr.length; index++){
        if(arr[index] > high) {
            high = arr[index];
        }
        else if (arr[index] < low) {
            low = arr[index];
        }
    }
    console.log(`low: ${low}`);
    return high;
}

function print2ndLastReturnOdd(arr) {
    var odd 
    var index = 0
    while (odd === undefined) {
        if(index == arr.length) {
            odd = "none";
        }
        else if(arr[index] % 2 != 0) {
            odd = arr[index];
        }
        else {
            index++;
        }
    }
    console.log(arr[(arr.length)-2]);
    return odd;
}

function doubleArray(arr){
    var doubledArr = [];
    for(var index=0; index<arr.length; index++) {
        doubledArr.push(arr[index]*2);
    }
    return doubledArr
}

function countPositives(arr){
    var count = 0;
    for(var index = 0; index < arr.length; index++){
        if(arr[index] > 0){
            count++
        }
    }
    arr[arr.length-1] = count;
    return arr
}

function evenOdd(arr){
    var even = 0;
    var odd = 0;
    for(var index = 0; index < arr.length; index++){
        if(arr[index] % 2 == 0) {
            even++;
            odd = 0;
            if(even==3) {
                console.log("Even more so!")
            }
        }
        else {
            odd++;
            even = 0;
            if(odd==3) {
                console.log("That's odd!")
            }
        }
    }
}

function everyOther(arr){
    for(var index=1;index < arr.length; index+=2){
        arr[index] +=1;
    }
    for(var index2=0; index2 < arr.length; index2++) {
        console.log(arr[index2]);
    }
    return arr
}

function previousLengths(arr) {
    for(var index = arr.length-1; index > 0; index--) {
        arr[index] = arr[index-1].length;
    }
    return arr
}

function addSeven(arr) {
    var dup_arr = [];
    for(var index=0; index < arr.length; index++) {
        dup_arr.push(arr[index] + 7);
    }
    return dup_arr
}

function terry(arr) {
    var back = arr.length-1;
    for(var index = 0; index < back; index++) {
        [arr[index], arr[back]] = [arr[back], arr[index]];
        back--;
    }
    return arr
}

function outlookNegative(arr) {
    var new_arr = [];
    for(var index = 0; index < arr.length; index++) {
        if(arr[index] < 0) {
            new_arr.push(arr[index]);
        }
        else {
            arr[index] = arr[index] * -1;
            new_arr.push(arr[index]);
        }
    }
    return new_arr
}

function alwaysHungry(arr) {
    counter = 0
    for(var index = 0; index < arr.length; index++) {
        if(arr[index] === 'food') {
            console.log("yummy");
            counter++
        }
    }
    if(counter === 0) {
        console.log("I'm Hungry")
    }
}

function swapTowardsCenter(arr) {
    [arr[0], arr[(arr.length)-1]] = [arr[(arr.length)-1], arr[0]];
    [arr[2], arr[(arr.length)-3]] = [arr[(arr.length)-3], arr[2]]
    return arr
}

function scaleArray(arr, num) {
    for(var index = 0; index < arr.length; index++) {
        arr[index] *= num;
    }
    return arr
}
