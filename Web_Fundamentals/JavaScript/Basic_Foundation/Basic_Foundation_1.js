function makeArray() {
    var arr = []
    for(var i = 1; i < 256; i++) {
        arr.push(i);
    }
    return arr;
}

function sumEvens() {
    var sum = 0
    for(var i = 0; i < 1001; i=i+2) {
        sum = sum + i;
    }
    return sum;
}

function sumOdds() {
    var sum = 0
    for(var i = 1; i < 5000; i=i+2) {
        sum = sum + i;
    }
    return sum;
}

function sumArray(arr) {
    var sum = 0;
    for(var i = 0; i < arr.length; i++) {
        sum = sum + arr[i];
    }
    return sum;
}

function arrayMax(arr) {
    while (arr.length > 1) {
        if(arr[0] > arr[(arr.length)-1]) {
            arr.pop();
        }
        else {
            arr.shift();
        }
    }
    var max = arr[0]
    return max;
}

function arrayAverage(arr) {
    var average = 0;
    for(var i = 0; i < arr.length; i++) {
        average = average + arr[i];
    }
    average = average/(arr.length);
    return average;
}

function arrayOdds(arr) {
    var odds = [];
    for(var i =0; i < arr.length; i++) {
        if(arr[i] % 2 != 0) {
            odds.push(arr[i]);
        }
    }
    return odds;
}

function greaterThan(y, arr) {
    var greaterArr = [];
    for(var i = 0; i < arr.length; i++) {
        if(arr[i] > y) {
            greaterArr.push(arr[i]);
        }
    }
    return greaterArr
}

function arrayValueSquared(arr) {
    for(var i = 0; i < arr.length; i++) {
        arr[i] = arr[i]*arr[i];
    }
    return arr;
}

function removeNegatives(arr) {
    for(var i = 0; i < arr.length; i++){
        if(arr[i] < 0) {
            arr[i] = 0
        }
    }
    return arr
}

function maxMinAvg(arr) {
    var minArray = []
    var avg = 0
    for(var i = 0; i < arr.length; i++) {
        avg += arr[i]
    }
    avg = avg/(arr.length)
    
    while(arr.length > 1){
        if(arr[0] > arr[(arr.length)-1]) {
            minArray.push(arr[(arr.length)-1]);
            arr.pop()
        }
        else {
            minArray.push(arr[0])
            arr.shift()
        }
    }
    var max = arr[0]
    
    while(minArray.length > 1){
        if(minArray[0] < minArray[(minArray.length)-1]) {
            minArray.pop()
        }
        else {
            minArray.shift()
        }
    }
    var min = minArray[0]
    var newArray = [max, min, avg]
    return newArray
}

function swapValues(arr) {
    var holder = arr[0];
    arr[0] = arr[(arr.length)-1]
    arr[(arr.length)-1] = holder
    return arr
}

function noNegatives(arr){
    for(var i = 0; i < arr.length; i++) {
        if(arr[i] < 0) {
            arr[i] = 'Dojo'
        }
    }
    return arr
}