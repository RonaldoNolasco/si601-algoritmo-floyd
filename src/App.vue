<template>

<div style="height: 500px; width: 100%">
    <l-map :zoom="zoom" :center="center" :options="mapOptions" style="height: 80%" @update:center="centerUpdate" @update:zoom="zoomUpdate">
        <l-tile-layer :url="url" :attribution="attribution"/>
            <template v-for="(point, index) in points">
                <l-marker :lat-lng="point" :key="index" @click="agregar">
                    <l-popup> {{point}} </l-popup>
                </l-marker>
            </template>
            <template v-for="(line, index) in lines">
                <l-polyline :lat-lngs="lines[index].latlngs" :color="lines[index].color" :key="index"></l-polyline>
            </template>
    </l-map>
    {{prueba}}
</div>

</template>

<script>
import { latLng } from "leaflet";
import { LMap, LTileLayer, LMarker, LPolyline, LPopup} from "vue2-leaflet";

export default {
    name: "Example",
    components: {
        LMap,
        LTileLayer,
        LMarker,
        LPolyline,
        LPopup
    },
    data() {
        return {
            zoom: 13,
            center: latLng(47.41322, -1.219482),
            url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
            attribution:
                '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            currentZoom: 11.5,
            currentCenter: latLng(47.41322, -1.219482),
            showParagraph: false,
            mapOptions: {
                zoomSnap: 0.5
            },
            points:[
                latLng(47.41422, -1.250482),
                latLng(47.41122, -1.230482),
                latLng(47.42022, -1.230482),
                latLng(47.41222, -1.210482)
            ],
            lines: [
                {
                    latlngs: [[47.41422, -1.250482], [47.41122, -1.230482]],
                    color: 'blue'
                },
                {
                    latlngs: [[47.41422, -1.250482], [47.42022, -1.230482]],
                    color: 'blue'
                },
                {
                    latlngs: [[47.42022, -1.230482], [47.41222, -1.210482]],
                    color: 'blue'
                },
                {
                    latlngs: [[47.41122, -1.230482], [47.41222, -1.210482]],
                    color: 'blue'
                }
            ],
            prueba:[]
        };
    },
    methods: {
        zoomUpdate(zoom) {
            this.currentZoom = zoom;
        },
        centerUpdate(center) {
            this.currentCenter = center;
        },
        showLongText() {
            this.showParagraph = !this.showParagraph;
        },
        innerClick() {
            alert("Click!");
        },
        agregar(){
            this.prueba.push(1);
        }
    }
};
</script>

<style>

</style>
