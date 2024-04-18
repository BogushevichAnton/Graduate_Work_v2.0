var map;
function create_map(center, zoom){
    console.log(document.querySelector('#jsonData'));
    if (document.querySelector('#jsonData') != null ){
        var jsonData = JSON.parse(document.querySelector('#jsonData').getAttribute('data-json'));
        console.log(jsonData);
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

        var full_description = "<table id='table-auto'>" + "<thead id='thead'><tr id='tr' ><th id='th'>Поле объекта</th><th id='th'>Значения</th></tr id='tr'></thead><tbody><tr id='tr'><td id='td'><b>Aббревиатура:</b></td><td id='td'>" + abbreviation + "</td></tr id='tr'>"+
        "<tr id='tr' id='tr id='tr''><td id='td'><b>Описание подразделения:</b></td><td id='td'>" + description + "</td></tr id='tr'>"+
        "<tr id='tr'><td id='td'><b>Адрес подразделения:</b></td><td id='td'>" + address + "</td></tr id='tr'>";




        marker.bindPopup(full_description, {
    maxWidth : 270
}).openPopup();
        marker.addTo(map);
        }
    }



       var featureGroup = L.featureGroup(baseMap);
       featureGroup.addTo(map);
       L.control.scale().addTo(map);
       //map.scrollWheelZoom.disable();
//    L.control.layers(railwayLayer, baseMap).addTo(map);
};

