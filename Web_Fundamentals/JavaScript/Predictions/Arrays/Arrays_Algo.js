var testArr = [6,3,5,1,2,4]
var sum = 0
for(var i = 0; i < testArr.length; i++) {
    sum += testArr[i];
    console.log('Num', testArr[i], 'Sum', sum)
}
for(var a = 0; a < testArr.length; a++) {
    testArr[a] = testArr[a] * a; 
}
console.log(testArr)