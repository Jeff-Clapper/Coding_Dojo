function sweatshirtPricing(num) {
    var discount=0
    var price=20
    if (num > 3) {
        discount=.35
    }
    else if (num = 3) {
        discount =.19
    }
    else if (num = 2) {
        discount =.09
    }
    var total = Math.ceil(num*(price-(price*discount)))
    return total
}




console.log(sweatshirtPricing(4))