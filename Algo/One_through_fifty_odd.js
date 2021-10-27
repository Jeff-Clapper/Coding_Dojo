function odd_numbers(){
    var odds = []
    for (var i = 1; i<50;i = i+2){
        odds.push(i)
    }
    return odds
}

test = odd_numbers()
console.log(test)