var map;
function create_map(center, zoom){

    if (document.querySelector('#jsonData') != null ){
        var jsonData = JSON.parse(document.querySelector('#jsonData').getAttribute('data-json'));
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



        var Icon = new L.Icon({
          iconUrl: '/static/Subdivisions/images/icons8-home-64.png',
          iconSize: [30, 30],
    });

    if (document.querySelector('#jsonData') != null){
    for (let i = 0; i < jsonData.length; i++) {
        var marker = new L.Marker([jsonData[i].latitude, jsonData[i].longitude], {icon: Icon});

        var abbreviation = jsonData[i].abbreviation;
        var description = jsonData[i].description;
        var address = jsonData[i].address;

        var full_description = "<b>Aббревиатура: </b>" + abbreviation + '<br/>' + "<b>Описание подразделения: </b>" + description + '<br/>'+ "<b>Адрес подразделения: </b>" + address;
        marker.bindPopup(full_description).openPopup();
        marker.addTo(map);
        }
    }



       var featureGroup = L.featureGroup(baseMap);
       featureGroup.addTo(map);
       L.control.scale().addTo(map);
       //map.scrollWheelZoom.disable();
//    L.control.layers(railwayLayer, baseMap).addTo(map);
};

