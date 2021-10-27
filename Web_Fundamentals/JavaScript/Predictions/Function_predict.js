//Predict1:
//This will print World and will then print Hello
function greeting(){
    return "Hello";
    console.log("World");
}
var word = greeting();
console.log(word);

//Predict2:
//This will print 8, and then will print 11
function add(num1, num2){
    console.log("Summing Numbers!");
    console.log("num1 is: " + num1);
    console.log("num2 is: " + num2);
    var sum = num1 + num2;
    return sum;
}
var result1 = add(3,5);
var result2 = add(4,7);
console.log(result1);
console.log(result2);

//Predict3:
//This will  do nothing as the function is not called
function highFive(num){
    for(var i=0; i<num; i++){
        if(i == 5){
            console.log("High Five!");
        }
        else{
            console.log(i);
        }
    }
}
    