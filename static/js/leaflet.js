let bounds = new L.LatLngBounds(new L.LatLng(-90, -180), new L.LatLng(90, 180));


let map = L.map("map", {
  minZoom: 1.5,
  maxBounds: bounds,
  maxBoundsViscosity: 1.0,
}).setView([48, 2], 0);


L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  // maxZoom: 19,
  attribution: "© OpenStreetMap",
  noWrap: true,
}).addTo(map);

L.control.scale().addTo(map);
