// set myNumber to 42, myName to your name, and swap both
var myNumber = 42
var myName = 'Jeff'
var myholder = myName
myName = myNumber
myNumber = myholder

// print ints from -52 to 1066 using a for loop
for (var index = -52; index < 1067; index++) {
    console.log(index)
}

//create beCheerful(). within it, console.log string "good morning!" Call it 98 times
function beCheerful() {
    console.log('good morning!')
}
for (x=0; x <= 98; x++) {
    beCheerful()
}

//using for, print multiples of 3 from 300 to 0. Skip -3 and -6
for (var x=-300; x < 1; x+=3) {
    if (x == -6 || x == -3) {
        continue
    }
    console.log(x)
}


//print ints from 2000 to 5280 using a while loop
var x = 2000
while (x < 5281) {
    console.log(x)
    x++
} 

//if 2 given numbers represent your birth month and day in either order, log "how did you know?", else log "Just another day..."
function isItMyBirthday(num1,num2) {
    if ((num1 ==12 || num2 == 12) && (num1 == 28 || num2 == 28)) {
        return 'How did you know?'
    }
    return 'Just another day....'
}

console.log(isItMyBirthday(28,11))
console.log(isItMyBirthday(28,12))
console.log(isItMyBirthday(12,28))
console.log(isItMyBirthday(27,12))
console.log(isItMyBirthday(22,11))

//write a function that determines whether a given year is a leap year. if a yearis divisible by 4, it is a leap year, unless it is divisible by 100. However, if it is divisible by 400, then it is a leap year
function isLeapYear(year) {
    var leapYear = true;
    if (year % 400 == 0) {
        return leapYear
    }
    else if (year % 100 == 0) {
        leapYear = false;
        return leapYear
    }
    else if (year % 4 == 0) {
        return leapYear
    }
    else {
        leapYear = false
        return leapYear
    }
}
console.log("this year is a leap year: " + isLeapYear(2020))
console.log("this year is a leap year: " + isLeapYear(3129))

//print all integer multiples of 5, from 512 to 4096. afterward, also log how many there were
function printAndCount() {
    count = 0
    for (x = 512; x < 4097; x++) {
        if (x % 5 == 0) {
            console.log(x)
            count ++
        }
    }
    console.log(`there were ${count} multiples of 5`)
}
printAndCount()

//Your function will be given an input parameter incoming. please console.log this value
function fun(incoming) {
    console.log(incoming)
}

fun([9,'pie',true,[1,2,3]])

function countOdd() {
    var count = 0
    for(var x = -299999; x < 300000; x += 2 ) {
        count += x 
    } 
    console.log(count, x)
}

countOdd()

//some kinda problem I'm not gonna write it oooot
function countDownGiven(lowNum,highNum,mult) {
    x = highNum
    while (x > lowNum) {
        if (x % mult == 0) {
            console.log(x)
            x -= mult
        }
        else {
            x--
        }
    }
}
countDownGiven(22,1678,17)