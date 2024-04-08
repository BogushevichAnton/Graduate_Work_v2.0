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

    var description = jsonData.map((item) => item.description);

        var redIcon = new L.Icon({
          iconUrl: '/static/images/marker-icon-2x-red.png',
          shadowUrl: '/static/images/marker-shadow.png',
          iconSize: [25, 41],
          iconAnchor: [12, 41],
          popupAnchor: [1, -34],
          shadowSize: [41, 41]
    });
        var greenIcon = new L.Icon({
          iconUrl: '/static/images/marker-icon-2x-green.png',
          shadowUrl: '/static/images/marker-shadow.png',
          iconSize: [25, 41],
          iconAnchor: [12, 41],
          popupAnchor: [1, -34],
          shadowSize: [41, 41]
    });
        var orangeIcon = new L.Icon({
          iconUrl: '/static/images/marker-icon-2x-orange.png',
          shadowUrl: '/static/images/marker-shadow.png',
          iconSize: [25, 41],
          iconAnchor: [12, 41],
          popupAnchor: [1, -34],
          shadowSize: [41, 41]
    });

    for (let i = 0; i < jsonData.length; i++) {
        switch (jsonData[i].specification__color) {
                case 'green':
                    var marker = new L.Marker([jsonData[i].latitude, jsonData[i].longitude], {icon: greenIcon});
                    break;
                case 'red':
                    var marker = new L.Marker([jsonData[i].latitude, jsonData[i].longitude], {icon: redIcon});
                    break;
                case 'orange':
                    var marker = new L.Marker([jsonData[i].latitude, jsonData[i].longitude], {icon: orangeIcon});
                    break;
                default:
                    var marker = new L.Marker([jsonData[i].latitude, jsonData[i].longitude]);
                    break;
                }
        marker.bindPopup(jsonData[i].description.toString()).openPopup();
        marker.addTo(map);
    }





    //L.marker([55.7429063961456, 37.662975621024664], {icon: redIcon}).addTo(map);

//    var marker = new L.Marker(center);
//    marker.bindPopup(description.toString()).openPopup();
//    marker.addTo(map);

       var featureGroup = L.featureGroup([railwayLayer, baseMap]);
       featureGroup.addTo(map);
       L.control.scale().addTo(map);
       //map.scrollWheelZoom.disable();
//    L.control.layers(railwayLayer, baseMap).addTo(map);
};

