# Graduate work: Development of an information system for Russian Railways emergency services
___
The information system allows you to access information about incidents, for example, 
a broken communication line, track defects, automate the process of adding detected incidents, 
editing, deleting and recording measures to eliminate incidents.
# Technologies
___
- Django
- Leaflet
- SQLite
- JS

# Development
___
### Database
Take a backup of the database from the __DB__ folder.
### Project
To authorize, you need to create a user using the `python manage.py createsuperuser` command.
Go to the site and enter your username and password.

<p align="center">
<img src="https://github.com/nemooo-trash/Graduate_Work_v2.0/assets/56976574/76194140-89ce-4f31-b4b3-62313ea06037">
</p>

### map
Emergency situations will be classified by color (markers on the map), depending on the severity of the incident.


<p align="center">
<img src="https://github.com/nemooo-trash/Graduate_Work_v2.0/assets/56976574/963c090c-5f59-4058-9b61-a881dedbb2fc">
</p>




### Leaflet.markercluster
The site implements Leaflet Clusters.
```js
 var markers = L.markerClusterGroup();
 var full_description =
        "<table id='table-auto'>" + "<thead id='thead'><tr id='tr' ><th id='th'>Поле объекта</th><th id='th'>Значения</th></tr id='tr'></thead><tbody><tr id='tr'><td id='td'><b>Описание:</b></td><td id='td'>" + jsonData[i].description + "</td></tr id='tr'>"+
        "<tr id='tr' id='tr id='tr''><td id='td'><b>Дата обнаружения:</b></td><td id='td'>" + jsonData[i].time_create + "</td></tr id='tr'>"+
        "<tr id='tr'><td id='td'><b>Адрес:</b></td><td id='td'>" + jsonData[i].address + "</td></tr id='tr'>"+
        "<tr id='tr'><td id='td'><b>Спецификация происшествия:</b></td><td id='td'>" + jsonData[i].specification__pattern + "</td></tr id='tr'>"+
        "<tr id='tr'><td id='td'><b>Обнаружитель:</b></td><td id='td'>" + jsonData[i].user_create__surname + ' '+ jsonData[i].user_create__name +' '+ jsonData[i].user_create__lastname + "</td></tr id='tr'>";
 marker.bindPopup(full_description, {
        maxWidth : 270
 }).openPopup(); 
 marker.addTo(markers);
 map.addLayer(markers);
 ```
<p align="center">
<img src="https://github.com/nemooo-trash/Graduate_Work_v2.0/assets/56976574/91980fd7-2a80-45c9-a9c8-9243b383f5e9">
</p>

### Descriptions of incidents
Description of incidents on the map.
<p align="center">
<img src="https://github.com/nemooo-trash/Graduate_Work_v2.0/assets/56976574/aae24494-f4d0-4eb4-b11a-5419897f139a">
</p>

<p align="center">
<img src="https://github.com/nemooo-trash/Graduate_Work_v2.0/assets/56976574/0f5647cb-0651-4281-ae12-80480510256f">
</p>

___


