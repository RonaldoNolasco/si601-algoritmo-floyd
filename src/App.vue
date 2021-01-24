<template>

<div style="height: 500px; width: 100%">
    <l-map :zoom="zoom" :center="center" :options="mapOptions" style="height: 80%" @update:center="centerUpdate" @update:zoom="zoomUpdate">
        <l-tile-layer :url="url" :attribution="attribution"/>
            <template v-for="(point, index) in points">
                <l-marker :lat-lng="latLng(point)" :key="index" @click="agregar(point)"></l-marker>
            </template>
            <template v-for="(line, index) in lines">
                <l-polyline :lat-lngs="lines[index].latlngs" :color="lines[index].color" :key="index"></l-polyline>
            </template>
            <template v-if = "this.minPath.latlngs.length >= 2">
                <l-polyline :lat-lngs="this.minPath.latlngs" :color="this.minPath.color"></l-polyline>
            </template>
    </l-map>
    {{this.minPath}}
</div>

</template>

<script>
import { latLng } from "leaflet";
import { LMap, LTileLayer, LMarker, LPolyline } from "vue2-leaflet";

export default {
    name: "Example",
    components: {
        LMap,
        LTileLayer,
        LMarker,
        LPolyline
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
                [47.41422, -1.250482],
                [47.41122, -1.230482],
                [47.42022, -1.230482],
                [47.41222, -1.210482]
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
            minPath:{
                latlngs: [],
                color: 'red'
            },
        };
    },
    methods: {
        zoomUpdate(zoom) {
            this.currentZoom = zoom;
        },
        centerUpdate(center) {
            this.currentCenter = center;
        },
        agregar(point){
            this.minPath.latlngs.push(point);
        },
        latLng
    },
};
</script>

<style>

</style>