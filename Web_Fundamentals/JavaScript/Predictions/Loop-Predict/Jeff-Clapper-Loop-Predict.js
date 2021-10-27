// Predict 1:
// a count from 0 to 14

// Predict 2:
// a count containing 3,6,9

// Predict 3:
// prints 1,4,5,8,12,13,16

console.log("Predict 1 Results")
for(var num = 0; num < 15; num++){
    console.log(num);
}

console.log("")
console.log("Predict 2 Results")
for(var i = 1; i < 10; i+=2){
    if(i % 3 == 0){
        console.log(i);
    }
}

console.log("")
console.log("Predict 3 Results")
for(var j = 1; j <= 15; j++){
    if(j % 2 == 0){
        j+=2;
    }
    else if(j % 3 == 0){
        j++;
    }
    console.log(j);
}
