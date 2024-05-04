import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit {
  title = 'fetch';
  zoom = 12;
  center: google.maps.LatLngLiteral = {
    lat: 40.7831,
    lng: -73.9712
  };
  options: google.maps.MapOptions = {
    mapTypeId: 'roadmap',
    zoomControl: true,
    scrollwheel: true,
    disableDoubleClickZoom: false,
    clickableIcons: false
  };
  markers: any[] = [];

  ngOnInit() {}

  addMarker() {
    var lat = this.center.lat + ((Math.random() - 0.5) * 2) / 10;
    var lng = this.center.lng + ((Math.random() - 0.5) * 2) / 10;
    var myLatlng = new google.maps.LatLng(lat, lng);
    this.markers.push({
      position: myLatlng,
      title: 'Marker title ' + (this.markers.length + 1)
    })
  }
}
