<template>

<div style="height: 500px; width: 100%">
    <l-map :zoom="zoom" :center="center" :options="mapOptions" style="height: 80%" @update:center="centerUpdate" @update:zoom="zoomUpdate">
        <l-tile-layer :url="url" :attribution="attribution"/>
            <template v-for="(point, index) in points">
                <l-marker :lat-lng="latLng(point[0], point[1])" :key="point + index" @click="agregarInd(index)"></l-marker>
            </template>
            <template v-for="(line, index) in lines">
                <l-polyline :lat-lngs="lines[index].latlngs" :color="lines[index].color" :key="line + index"></l-polyline>
            </template>
            <template v-if = "this.minPath.latlngs.length >= 2">
                <l-polyline :lat-lngs="this.minPath.latlngs" :color="this.minPath.color"></l-polyline>
            </template>
    </l-map>
    <button @click="borrarPuntos()">Borrer puntos</button>
    <br>
    {{this.indexes}}
    <br>
    {{this.arrNodes}}
    <br>
    {{this.minPath.latlngs}}
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
            indexes:[],
            MX: 300,
            INF: 1e10,
            d: [],
            parent: [],
            arrNodes: [],
            path:[]
        };
    },
    created: function(){
        for(let i = 0; i < this.MX; i++) {
            this.d.push([]);
            this.parent.push([]);
            for (let j = 0; j < this.MX; j++) {
                this.d[i].push(null);
                this.parent[i].push(null);
            }
        }

        for (let i = 0; i < 4; i++){
            for (let j = 0; j < 4; j++){
                this.d[i][j] = this.INF
                this.parent[i][j] = -1
            }
        this.d[i][i] = 0
        }

        this.addEdge(1, 2, 3)
        this.addEdge(2, 4, 4)
        this.addEdge(1, 3, 5)
        this.addEdge(3, 4, 7)

        this.floydWarshall(4)
    },
    methods: {
        zoomUpdate(zoom) {
            this.currentZoom = zoom;
        },
        centerUpdate(center) {
            this.currentCenter = center;
        },
        agregarInd(index){
            if (this.indexes.length < 2) this.indexes.push(index+1);
            if (this.indexes.length == 2){
                this.arrNodes = this.getPath(this.indexes[0], this.indexes[1])
                for (let value of this.arrNodes){
                    this.minPath.latlngs.push(this.points[value-1]);
                }
            }
        },
        borrarPuntos(){
            this.indexes = []
        },
        addEdge(u, v, w){
            u = u - 1
            v = v - 1
            
            if(this.d[u][v] > w) this.d[u][v] = w;
            if(this.d[v][u] > w) this.d[v][u] = w;

            this.parent[u][v] = u
            this.parent[v][u] = v
        },
        floydWarshall(n){
            for (let k = 0; k < n; k++){
                for (let u = 0; u < n; u++){
                    for (let v = 0; v < n; v++){
                        if(this.d[u][k] == this.INF) continue;
                        if(this.d[k][v] == this.INF) continue;
                        if(this.d[u][k] + this.d[k][v] < this.d[u][v]){
                            this.d[u][v] = this.d[u][k] + this.d[k][v]
                            this.parent[u][v] = this.parent[k][v]
                        }
                    }
                }
            }
        },
        getPath(u,v){
            u = u - 1
            v = v - 1

            this.path = []

            while(v != -1){
                this.path.push(v + 1)
                v = this.parent[u][v]
            }
            this.path.reverse()
            
            return this.path
        },
        latLng
    },
};
</script>

<style>

</style>