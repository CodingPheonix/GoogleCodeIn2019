const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric'};

function parse_query_string(query) {
    var vars = query.split("&");
    var query_string = {};
    for (var i = 0; i < vars.length; i++) {
      var pair = vars[i].split("=");
      var key = decodeURIComponent(pair[0]);
      var value = decodeURIComponent(pair[1]);
      if (typeof query_string[key] === "undefined") {
        query_string[key] = decodeURIComponent(value);
      } else if (typeof query_string[key] === "string") {
        var arr = [query_string[key], decodeURIComponent(value)];
        query_string[key] = arr;
      } else {
        query_string[key].push(decodeURIComponent(value));
      }
    }
    return query_string;
}

var parsed = parse_query_string(window.location.search.substring(1));
var locName = document.getElementById("name");
var Temp = document.getElementById("temp");
var Pressure = document.getElementById("pressure");
var WindSpeed = document.getElementById("windspeed");
var WindDeg = document.getElementById("winddeg");
var Sunrise = document.getElementById("sunrise");
var Sunset = document.getElementById("sunset");
var Humidity = document.getElementById("humidity");
var CloudImage = document.getElementById("icon");
var Date_Time = document.getElementById("date");

var request = new XMLHttpRequest();

request.open('GET', 'https://cors-anywhere.herokuapp.com/http://api.openweathermap.org/data/2.5/weather?q='+parsed["name"]+'&APPID=8cf34526c8b32918d7726e300d9e6113', true)
request.onload = function() {
// Begin accessing JSON data here
  var data = JSON.parse(this.response);

  if (request.status >= 200 && request.status < 400) {
    locName.innerHTML = data.name;
  
    var d = new Date();
    var utc = d.getTime() + (d.getTimezoneOffset() * 60000);
    var nd = new Date(utc + (1000*data.timezone));
    Date_Time.innerHTML=nd.toLocaleDateString('en-EN', options);
    
    var date = new Date(data.sys.sunrise*1000);
    var hours = date.getHours();
    var minutes = "0" + date.getMinutes();
    var seconds = "0" + date.getSeconds();
    Sunrise.innerHTML = "Sunrise: " + hours + ':' + minutes.substr(-2) + ':' + seconds.substr(-2);

    date = new Date(data.sys.sunset*1000);
    hours = date.getHours();
    minutes = "0" + date.getMinutes();
    seconds = "0" + date.getSeconds();
    Sunset.innerHTML = "Sunset: " + hours + ':' + minutes.substr(-2) + ':' + seconds.substr(-2);

    WindSpeed.innerHTML = "Wind Speed: "+data.wind.speed;
    if (data.wind.def != undefined){ 
      WindDeg.innerHTML =  "Wind Degrees: "+data.wind.deg;
    } else {
      WindDeg.innerHTML =  "Wind Degrees: 0";
    }
    Humidity.innerHTML = "Humidity: " + data.main.humidity;
    Temp.innerHTML = "Temperature: " + Math.round(data.main.temp_min-273.15) + "°C | " + Math.round(data.main.temp_max-273.15) + "°C";
    Pressure.innerHTML = "Pressure: " + data.main.pressure;

    CloudImage.src = "http://openweathermap.org/img/wn/"+data.weather[0].icon+"@2x.png";
    if ((Array.from(data.weather[0].icon))[1] == "1"){
        document.body.style.backgroundImage = "url('ClearSky.jpg')"
    } else if((Array.from(data.weather[0].icon))[1] == "9" || 
              (Array.from(data.weather[0].icon))[0]+(Array.from(data.weather[0].icon))[1] == "10"){
        document.body.style.backgroundImage = "url('Rain.jpg')"
    } else if((Array.from(data.weather[0].icon))[0] + (Array.from(data.weather[0].icon))[1] == "11"){
        document.body.style.backgroundImage = "url('Thunder.jpg')"
    } else if((Array.from(data.weather[0].icon))[0] + (Array.from(data.weather[0].icon))[1] == "13"){
        document.body.style.backgroundImage = "url('Snow.jpg')"
    } else if((Array.from(data.weather[0].icon))[0] + (Array.from(data.weather[0].icon))[1] == "50"){
        document.body.style.backgroundImage = "url('Mist.jpg')"
    } else {
        document.body.style.backgroundImage = "url('Cloud.jpg')"
    }
  } else {
    console.log('An error occured');
    console.log('Redirecting user')
    window.location.href = "index.html"
  }
}

request.send()