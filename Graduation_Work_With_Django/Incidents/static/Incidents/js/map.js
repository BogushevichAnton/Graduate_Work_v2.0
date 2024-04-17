var map;
function create_map(center, zoom){
    if (document.querySelector('#jsonData') != null ){

        var jsonData = JSON.parse(document.querySelector('#jsonData').getAttribute('data-json'));
        console.log(jsonData);
        console.log(jsonData.length);
        if (jsonData.length == 1){
            center[0] = jsonData[0].latitude;
            center[1] = jsonData[0].longitude;
            zoom = 12;
        } else {
        zoom = 7
        }

    }
    map = L.map('map').setView(center,zoom);

    var baseMap = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution:  ''
     }).addTo(map);

    var railwayLayer = L.tileLayer('http://{s}.tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png', {
        attribution:  '©OpenRailwayMap'
    }).addTo(map);

    if (document.querySelector('#jsonData') != null){
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
    }

    if (document.querySelector('#jsonData') != null){
    var markers = L.markerClusterGroup();

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
        var description = jsonData[i].description;
        var time_create = jsonData[i].time_create;
        var address = jsonData[i].address;
        var specification = jsonData[i].specification__pattern;
        var user_create = jsonData[i].user_create__surname + ' '+ jsonData[i].user_create__name +' '+ jsonData[i].user_create__lastname;

        var full_description = "<b>Описание: </b>" + description + '<br/>' + "<b>Адрес: </b>" + address + '<br/>' + "<b>Дата и время обнаружения: </b>" + time_create + '<br/>'+ "<b>Спецификация происшествия: </b>" + specification + '<br/>'+ "<b>Обнаружитель происшествия: </b>" + user_create;
        marker.bindPopup(full_description).openPopup();
        marker.addTo(markers);

    }
        map.addLayer(markers);
        markers.addTo(map);
    }


       var featureGroup = L.featureGroup([railwayLayer, baseMap]);
       featureGroup.addTo(map);
       L.control.scale().addTo(map);
       //map.scrollWheelZoom.disable();
//    L.control.layers(railwayLayer, baseMap).addTo(map);
};

