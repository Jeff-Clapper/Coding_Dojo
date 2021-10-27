// Predict 1: 
// This will print 8, then print 6, then 7, etc. until it finishs printing 9 

var arr = [8,6,7,5,3,0,9]
for(var i = 0; i < arr.length; i++){    
    console.log(arr[i]);
}

//Predict 2:
//This will print (one per line): That is odd, that is odd, 8, 4, 2, 0, that is odd

var arr = [7,3,8,4,2,0,1];
for(var i = 0; i < arr.length; i++){ 
    if(arr[i] % 2 == 0){
        console.log(arr[i]);
    } 
    else{
        console.log("That is odd!");
    }
}

//Predict 3:
//I think this will produce: 
//[ -1, -3, -8, zero, -4]
//[5, 2, 1]
//PS: I got this one wrong as I did pop instead of push

var arr = [1,3,8,-5,0,-2,4,-1];
var newArr = [];
for(var i = 0; i< arr.length; i++){
    if(arr[i] < 0){
        newArr.push(arr[i]);
        arr[i] = arr[i] * -1;
    }
    else if(arr[i] == 0){
        arr[i] = "Zero";
    }
    else{
        arr[i] = arr[i] * -1;
    }
}
console.log(arr);
console.log(newArr);


