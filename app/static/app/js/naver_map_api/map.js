var HOME_PATH = window.HOME_PATH || '.';
var MARKER_SPRITE_X_OFFSET = 29,
    MARKER_SPRITE_Y_OFFSET = 50;

//지도 생성 시에 옵션을 지정 가능
var map = new naver.maps.Map('map', {
    center: new naver.maps.LatLng(36.967999, 127.8710230), //지도의 초기 중심 좌표
    zoom: 12, //지도의 초기 줌 레벨
    minZoom: 1 //지도의 최소 줌 레벨
});

//지도 인터랙션 끄기
// map.setOptions({ 
//     draggable: false, //지도 드래그 이동 사용 여부
//     pinchZoom: true, //핀치 줌 사용 여부
//     scrollWheel: false, //마우스 휠로 확대 축소 사용 여부
//     keyboardShortcuts: false, //키보드 단축키 사용 여부
//     disableDoubleTapZoom: true,
//     disableDoubleClickZoom: true, //더블클릭 중심으로 확대 사용 여부
//     disableTwoFingerTapZoom: true
// });

var bounds = map.getBounds(),
    southWest = bounds.getSW(),
    northEast = bounds.getNE(),
    lngSpan = northEast.lng() - southWest.lng(),
    latSpan = northEast.lat() - southWest.lat();

var markers = [],
    infoWindows = [];

var positions = [
    new naver.maps.LatLng(36.967099, 127.8710230),
    new naver.maps.LatLng(36.967199, 127.8711230),
    new naver.maps.LatLng(36.967299, 127.8712230),
    new naver.maps.LatLng(36.967399, 127.8713230),
    new naver.maps.LatLng(36.967499, 127.8714230),
    new naver.maps.LatLng(36.967599, 127.8715230),
    new naver.maps.LatLng(36.967699, 127.8716230),
    new naver.maps.LatLng(36.967799, 127.8717230),
    new naver.maps.LatLng(36.967899, 127.8718230),
    new naver.maps.LatLng(36.967999, 127.8719230),
]

for (var i=0; i<positions.length; i++) {

    var position = positions[i];

    var marker = new naver.maps.Marker({
        map: map,
        position: position,
        title: i+1,
        icon: {
            url: HOME_PATH +'/img/example/sp_pins_spot_v3.png',
            size: new naver.maps.Size(24, 37),
            anchor: new naver.maps.Point(12, 37),
            origin: new naver.maps.Point(MARKER_SPRITE_X_OFFSET, MARKER_SPRITE_Y_OFFSET)
        },
        zIndex: 100,
        animation: naver.maps.Animation.BOUNCE
    });

    var infoWindow = new naver.maps.InfoWindow({
        content: '<div style="width:150px;text-align:center;padding:10px;">여기는 <b>"'+ (i+1).toString() +'"</b> 입니다.</div>'
    });

    markers.push(marker);
    infoWindows.push(infoWindow);
};

naver.maps.Event.addListener(map, 'idle', function() {
    updateMarkers(map, markers);
});

function updateMarkers(map, markers) {

    var mapBounds = map.getBounds();
    var marker, position;

    for (var i = 0; i < markers.length; i++) {

        marker = markers[i]
        position = marker.getPosition();

        if (mapBounds.hasLatLng(position)) {
            showMarker(map, marker);
        } else {
            hideMarker(map, marker);
        }
    }
}

function showMarker(map, marker) {

    if (marker.setMap()) return;
    marker.setMap(map);
}

function hideMarker(map, marker) {

    if (!marker.setMap()) return;
    marker.setMap(null);
}

// 해당 마커의 인덱스를 seq라는 클로저 변수로 저장하는 이벤트 핸들러를 반환합니다.
function getClickHandler(seq) {
    return function(e) {
        var marker = markers[seq],
            infoWindow = infoWindows[seq];

        if (infoWindow.getMap()) {
            infoWindow.close();
        } else {
            infoWindow.open(map, marker);
        }
    }
}

for (var i=0, ii=markers.length; i<ii; i++) {
    naver.maps.Event.addListener(markers[i], 'click', getClickHandler(i));
}