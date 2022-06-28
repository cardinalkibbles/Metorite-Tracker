// Lat first then longitude

const token = document.getElementsByName("csrfmiddlewaretoken")[0];


var logVar = "";
var latVar = "";

// function for adding lat and long to the marker
const addMarker = () => {
  L.marker([parseInt(latVar), parseInt(logVar)])
    .addTo(map)
    .bindPopup("Meteorite popup")
    .openPopup();
};



// axios call for json data
axios({
  headers: {
    "Content-Type": "application/json",
    "X-CRFToken": token,
  },
  xsrfHeaderName: "X-CRFToken",
  method: "GET",
  url: "/event_retrieve",
}).then(function (response) {
    // for loop taking the lat and long out of the array
  for (let i = 0; i < response.data.length; i++) {
    logVar = response.data[i].longitude;
    latVar = response.data[i].latitude;
    addMarker();
  }
});