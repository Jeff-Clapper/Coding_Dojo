async function getCoderData() {
    var response = await fetch("https://api.github.com/users/adion81")
    var coderData = await response.json()
    
    var container = document.querySelector('#test')
    var image = document.createElement("img")
    image.setAttribute('src',coderData.avatar_url)
    
    var paragraph = document.createElement("p")
    paragraph.innerText=coderData.name
    

    container.before(image)
    document.querySelector("#test").innerText = coderData.name + " has " + coderData.followers + " followers!"
    return coderData
}






// function userData() {
//     var coderData = getCoderData();
//     var name = getName(coderData);
//     var followerCount = getFollowers(coderData)
//     document.querySelector("#test").innerText = coderData.name
//     document.querySelector("#test").innerText = coderData.avatar_url
//     document.querySelector("#test").innerText = coderData.followers

// }