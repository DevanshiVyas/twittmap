mapboxgl.accessToken = 'pk.eyJ1IjoiZGV2YWlzY29vbCIsImEiOiJjaWxkZ3J4ODQwZWN2dnJtMDV2aDh3N2JjIn0.IQLMiABHeyes0L1q6p7gmw';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v8',
    center: [0,0],
    zoom: 2
});

var buildFeature = function(coord) {
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": coord
        },
        "properties": {
            "marker-symbol": "monument"
        }
    }
};

var features = coords.map(function(c) {
    return buildFeature(c)
});

map.on('style.load', function () {
    map.addSource("markers", {
        "type": "geojson",
        "data": {
            "type": "FeatureCollection",
            "features": features
        }
    });

    map.addLayer({
        "id": "markers",
        "type": "symbol",
        "source": "markers",
        "layout": {
            "icon-image": "{marker-symbol}-15",
            "text-field": "{title}",
            "text-offset": [0, 0.6],
            "text-anchor": "top"
        }
    });
});


var btn = document.getElementById("submit");
btn.addEventListener("click", function(){
    var q = document.getElementById("search");
    window.location = "/?q=" + q.value;
});
