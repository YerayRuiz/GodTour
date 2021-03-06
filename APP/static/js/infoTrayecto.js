// The first parameter are the coordinates of the center of the map
// The second parameter is the zoom level

var latOrigen = document.getElementById("latOrigen").value;
var lonOrigen = document.getElementById("lonOrigen").value;
var latDestino = document.getElementById("latDestino").value;
var lonDestino = document.getElementById("lonDestino").value;
var dirOrigen = document.getElementById("dir_origen").value;
var dirDestino = document.getElementById("dir_destino").value;

var origenIcon = L.icon({
    iconUrl: 'http://localhost:5000/static/images/verde-marker.png',
    iconSize: [40, 40],
    iconAnchor:   [22, 40],
    popupAnchor:  [-3, -76]
});

var destinoIcon = L.icon({
    iconUrl: 'http://localhost:5000/static/images/rojo-flag.png',
    iconSize: [40, 40],
    iconAnchor:   [22, 40],
    popupAnchor:  [-3, -76]
});


var map = L.map('map');
var corner1 = L.latLng(latOrigen, lonOrigen),
corner2 = L.latLng(latDestino, lonDestino),
bounds = L.latLngBounds(corner1, corner2);
map.fitBounds(bounds);


// {s}, {z}, {x} and {y} are placeholders for map tiles
// {x} and {y} are the x/y of where you are on the map
// {z} is the zoom level
// {s} is the subdomain of cartodb
var layer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Now add the layer onto the map
// map.addLayer(layer);

let marcaOrigen = L.marker([latOrigen, lonOrigen], {icon : origenIcon}).addTo(map).bindPopup("Origen: " + dirOrigen);
let marcaDestino = L.marker([latDestino, lonDestino], {icon : destinoIcon}).addTo(map).bindPopup("Destino: " + dirDestino);