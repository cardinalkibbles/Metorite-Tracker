const token = document.getElementsByName("csrfmiddlewaretoken")[0];
var logVar = "";
var latVar = "";
var meteorIcon = L.icon({
  iconUrl: meteor,
  iconSize: [38, 95], // size of the icon
  iconAnchor: [22, 94], // point of the icon which will correspond to marker's location
  popupAnchor: [-3, -76], // point from which the popup should open relative to the iconAnchor
});


function templateLoad(data) {
  let popupContent = document.querySelector("#popup-content");
  let popup = document.createElement("div");

  templateContent = popupContent.content.cloneNode(true);

  popup.appendChild(templateContent);
  popupName = popup.querySelector(".popup-name");
  popupName.innerHTML = data.name;
  popupMass = popup.querySelector(".popup-mass");
  popupMass.innerHTML = `Mass: ${data.mass}`;
  popupDate = popup.querySelector(".popup-date");
  popupDate.innerHTML = `Date of impact: ${data.date}`;
  popupLatitude = popup.querySelector(".popup-latitude");
  popupLatitude.innerHTML = `Latitude: ${data.latitude}`;
  popupLongitude = popup.querySelector(".popup-longitude");
  popupLongitude.innerHTML = `Longitude: ${data.longitude}`;
  popupLongitude.setAttribute("class", "text-success");
  return popup;
}

// function for adding lat and long to the marker
const addMarker = (data) => {
  L.marker([parseInt(latVar), parseInt(logVar)], { icon: meteorIcon })
    .addTo(map)
    .bindPopup(templateLoad(data));
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
    if (i === 2400) {
      break;
    }
    logVar = response.data[i].longitude;
    latVar = response.data[i].latitude;
    let data = response.data[i];
    addMarker(data);
  }
});