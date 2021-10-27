function iterArr(arr) {
   var sum = 0
   for (var i = 0; i < arr.length; i++){
       sum = sum + arr[i]
   }
   return sum; 
}

test = iterArr([2,5,8,-2,-3,9])
console.log(test)