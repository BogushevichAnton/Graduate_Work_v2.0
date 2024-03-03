var map;
function create_map(center, zoom){

    map = L.map('map').setView(center,zoom);

    var baseMap = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution:  ''
     }).addTo(map);

    var railwayLayer = L.tileLayer('http://{s}.tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png', {
        attribution:  '©OpenRailwayMap'
    }).addTo(map);

    var jsonData = JSON.parse(document.querySelector('#jsonData').getAttribute('data-json'));
    console.log(jsonData);

    var description = jsonData.map((item) => item.description);
    console.log(description);

    var marker = new L.Marker(center);
    marker.bindPopup(description.toString()).openPopup();
    marker.addTo(map);

       var featureGroup = L.featureGroup([railwayLayer, baseMap]);
       featureGroup.addTo(map);
       L.control.scale().addTo(map);
       //map.scrollWheelZoom.disable();
//    L.control.layers(railwayLayer, baseMap).addTo(map);
};

