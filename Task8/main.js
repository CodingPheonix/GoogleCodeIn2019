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

var parsed_qs = parse_query_string(window.location.search.substring(1));

if(parsed_qs["search"] != undefined){
  var request = new XMLHttpRequest();

  request.open('GET', 'https://cors-anywhere.herokuapp.com/http://api.openweathermap.org/data/2.5/weather?q='+parsed_qs["search"]+'&APPID=8cf34526c8b32918d7726e300d9e6113', true)
  request.onload = function() {
  // Begin accessing JSON data here
    var data = JSON.parse(this.response);

    if (request.status >= 200 && request.status < 400) {
      window.location.href = "forecast.html?name="+data.name;
    } else {
      console.log('error');
      //Invalid location message here
    }
  }

  request.send()
}