// Lat first then longitude
const token = document.getElementsByName("csrfmiddlewaretoken")[0];

var logVar = "";
var latVar = "";

function templateLoad(data) {
  let popupContent = document.querySelector("#popup-content");
  popup = document.createElement("div");
  templateContent = popupContent.content.cloneNode(true);
  popup.appendChild(templateContent);
  popupName = popup.querySelector(".popup-name");
  popupName.innerHTML = data.name;
  popupMass = popup.querySelector(".popup-mass");
  popupMass.innerHTML = data.mass;
  popupFound = popup.querySelector(".popup-found");
  popupFound.innerHTML = data.found;
  popupDate = popup.querySelector(".popup-date");
  popupDate.innerHTML = data.date;
  popupLatitude = popup.querySelector(".popup-latitude");
  popupLatitude.innerHTML = data.latitude;
  popupLongitude = popup.querySelector(".popup-longitude");
  popupLongitude.innerHTML = data.longitude;
  return popup;
}

// function for adding lat and long to the marker
const addMarker = (data) => {
  L.marker([parseInt(latVar), parseInt(logVar)])
    .addTo(map)
    .bindPopup(templateLoad(data));
};

// axios call for json data
axios({
  headers: {
    "Content-Type": "application/json",
    "X-CRFToken": token,
  },
  // params: {

  // },
  xsrfHeaderName: "X-CRFToken",
  method: "GET",
  url: "/event_retrieve",
}).then(function (response) {
  // for loop taking the lat and long out of the array
  for (let i = 0; i < response.data.length; i++) {
    logVar = response.data[i].longitude;
    latVar = response.data[i].latitude;
    let data = response.data[i];
    addMarker(data);
  }
});




// get year, month, day