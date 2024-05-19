



// script.js

const url = "https://api.openweathermap.org/data/2.5/weather";
const apiKey = "2ab92ea8f83687950a43795cb8d5f2c0";

const getResults = () => {
    let query = `${url}?q=Izmir&appid=${apiKey}&units=metric&lang=tr`;
    fetch(query)
        .then(weather => weather.json())
        .then(displayResults);
}

const displayResults = (response) => {
    let city = response.name;
    let temp = Math.round(response.main.temp);
    let desc = response.weather[0].description;
    let capitalizedDesc = desc.charAt(0).toUpperCase() + desc.slice(1);
    let icon = response.weather[0].icon;
    let image = "http://openweathermap.org/img/wn/" + icon + "@2x.png";
    let country = response.sys.country;
    let min = Math.round(response.main.temp_min);
    let max = Math.round(response.main.temp_max);
    document.querySelector(".image").style.display = "block";

    let cityElements = document.getElementsByClassName("city");
    let tempElements = document.getElementsByClassName("temp");
    let descElements = document.getElementsByClassName("description");
    let imageElements = document.getElementsByClassName("image");
    let minMaxElements = document.getElementsByClassName("min_max");

    for (let i = 0; i < cityElements.length; i++) {
        cityElements[i].innerText = city + ", " + country;
        tempElements[i].innerText = temp;
        descElements[i].innerText = capitalizedDesc;
        imageElements[i].children[0].src = image; 
        minMaxElements[i].innerText = min + "°C / " + max + "°C";
    }
}

window.addEventListener("load", getResults);

