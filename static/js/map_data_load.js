// Lat first then longitude

const token = document.getElementsByName("csrfmiddlewaretoken")[0];

var logVar = "";
var latVar = "";

const addMarker = () => {
  L.marker([parseInt(latVar), parseInt(logVar)])
    .addTo(map)
    .bindPopup("A pretty CSS3 popup.<br> Easily customizable.")
    .openPopup();
};

axios({
  headers: {
    "Content-Type": "application/json",
    "X-CRFToken": token,
  },
  xsrfHeaderName: "X-CRFToken",
  method: "GET",
  url: "/event_retrieve",
}).then(function (response) {
    console.log(response.data)
  for (let i = 0; i < response.data.length; i++) {
    console.log(response.data.length)
    logVar = response.data[i].longitude;
    latVar = response.data[i].latitude;
    addMarker();
  }
});
//   .then(function (results) {
//     addMarker();
//   });
