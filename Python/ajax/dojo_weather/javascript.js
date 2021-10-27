async function getTampaWeather(city) {
    var response = await fetch("https://api.openweathermap.org/data/2.5/weather?q=Tampa&units=imperial&appid={}")
    var CityWeather = await response.json()

    var currTemp = CityWeather.main['temp']
    var maxTemp = CityWeather.main['temp_max']
    var minTemp = CityWeather.main['temp_min']
    var weather = CityWeather.weather['0']['description']
    var city = CityWeather.name
    variables = [currTemp,maxTemp,minTemp, weather]
    
    // var displayVariable = document.createElement("p")
    // displayVariable.innerText =currTemp
    
    document.querySelector(".city").innerText = city 
    console.log(currTemp)
    document.querySelector(".city_weather_temp").innerText = "CURRENT TEMP: " + currTemp + "degrees F"
    document.querySelector(".city_weather_temp_range").innerText ="TEMP RANGE: " + minTemp + "degrees F" + " - " + maxTemp + "degrees F"
    document.querySelector(".city_weather").innerText = "WEATHER: " + weather

    return CityWeather
}

async function getChicagoWeather(city) {
    var response = await fetch("https://api.openweathermap.org/data/2.5/weather?q=Chicago&units=imperial&appid=34a2bfc3e1a5b157f66e325147513649")
    var CityWeather = await response.json()

    var currTemp = CityWeather.main['temp']
    var maxTemp = CityWeather.main['temp_max']
    var minTemp = CityWeather.main['temp_min']
    var weather = CityWeather.weather['0']['description']
    var city = CityWeather.name
    variables = [currTemp,maxTemp,minTemp, weather]
    
    // var displayVariable = document.createElement("p")
    // displayVariable.innerText =currTemp
    
    document.querySelector(".city").innerText = city 
    document.querySelector(".city_weather_temp").innerText = "CURRENT TEMP: " + currTemp + "degrees F"
    document.querySelector(".city_weather_temp_range").innerText ="TEMP RANGE: " + minTemp + "degrees F" + " - " + maxTemp + "degrees F"
    document.querySelector(".city_weather").innerText = "WEATHER: " + weather

    return CityWeather
}

async function getBurbankWeather(city) {
    var response = await fetch("https://api.openweathermap.org/data/2.5/weather?q=Burbank&units=imperial&appid=34a2bfc3e1a5b157f66e325147513649")
    var CityWeather = await response.json()

    var currTemp = CityWeather.main['temp']
    var maxTemp = CityWeather.main['temp_max']
    var minTemp = CityWeather.main['temp_min']
    var weather = CityWeather.weather['0']['description']
    var city = CityWeather.name
    variables = [currTemp,maxTemp,minTemp, weather]
    
    // var displayVariable = document.createElement("p")
    // displayVariable.innerText =currTemp
    
    document.querySelector(".city").innerText = city 
    document.querySelector(".city_weather_temp").innerText = "CURRENT TEMP: " + currTemp + "degrees F"
    document.querySelector(".city_weather_temp_range").innerText ="TEMP RANGE: " + minTemp + "degrees F" + " - " + maxTemp + "degrees F"
    document.querySelector(".city_weather").innerText = "WEATHER: " + weather

    return CityWeather
}


async function getDallasWeather(city) {
    var response = await fetch("https://api.openweathermap.org/data/2.5/weather?q=Dallas&units=imperial&appid=34a2bfc3e1a5b157f66e325147513649")
    var CityWeather = await response.json()

    var currTemp = CityWeather.main['temp']
    var maxTemp = CityWeather.main['temp_max']
    var minTemp = CityWeather.main['temp_min']
    var weather = CityWeather.weather['0']['description']
    var city = CityWeather.name
    variables = [currTemp,maxTemp,minTemp, weather]
    
    // var displayVariable = document.createElement("p")
    // displayVariable.innerText =currTemp
    
    document.querySelector(".city").innerText = city 
    document.querySelector(".city_weather_temp").innerText = "CURRENT TEMP: " + currTemp + "degrees F"
    document.querySelector(".city_weather_temp_range").innerText ="TEMP RANGE: " + minTemp + "degrees F" + " - " + maxTemp + "degrees F"
    document.querySelector(".city_weather").innerText = "WEATHER: " + weather

    return CityWeather
}