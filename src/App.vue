<template>

<div style="height: 500px; width: 100%">
    <l-map :zoom="zoom" :center="center" :options="mapOptions" style="height: 80%" @update:center="centerUpdate" @update:zoom="zoomUpdate">
        <l-tile-layer :url="url" :attribution="attribution"/>
            <template v-for="(point, index) in points">
                <l-marker :lat-lng="latLng(point[0], point[1])" :key="point + index" @click="agregarInd(index)" :draggable="true">
                    <l-tooltip :options="{ permanent: true }">{{index + 1}}</l-tooltip>
                </l-marker>
            </template>
            <template v-for="(line, index) in relationsLine">
                <l-polyline :lat-lngs="relationsLine[index].latlngs" :color="relationsLine[index].color" :key="relationsLine + index"></l-polyline>
            </template>
            <template v-if = "this.minPath.latlngs.length >= 2">
                <l-polyline :lat-lngs="this.minPath.latlngs" :color="this.minPath.color"></l-polyline>
            </template>
    </l-map>
    <br>
    <center>
        <button @click="borrarPuntos()" align="center">Borrar selección</button>
        <!--<center><h3>Camino mínimo:</h3>
        <template v-for="(value, index) in path">
            <h4 :key="value + index">{{value + " - "}}</h5>
        </template>-->
        <h3>Camino mínimo: {{this.path}}</h3>
    </center>
</div>

</template>

<script>
import { latLng } from "leaflet";
import { LMap, LTileLayer, LMarker, LPolyline, LTooltip } from "vue2-leaflet";

export default {
    name: "Example",
    components: {
        LMap,
        LTileLayer,
        LMarker,
        LPolyline,
        LTooltip
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
            /*Coordenadas de los nodos*/
            points:[
                [47.41422, -1.250482],
                [47.41122, -1.230482],
                [47.42022, -1.230482],
                [47.41022, -1.207482],
                [47.40522, -1.200482],
                [47.39822, -1.225482],
                [47.41922, -1.200482],
                [47.39822, -1.250282],
            ],
            /*Matriz de relaciones entre los nodos*/
            relationsPair:[
                [1,2], [1,3], [2,4], [3,4], [2,5], [4,5], [1,6], [2,6], [5,6], [3,7], [4,7], [5,7], [1,8], [6,8]
            ],
            /*Numero de nodos*/
            nodesNumber: 0,
            relationsLine: [],
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
        /*Inicializando el d y el parent */
        for(let i = 0; i < this.MX; i++) {
            this.d.push([]);
            this.parent.push([]);
            for (let j = 0; j < this.MX; j++) {
                this.d[i].push(null);
                this.parent[i].push(null);
            }
        }

        this.nodesNumber = this.points.length //Hallando el numero de nodos

        /*Asignando -1 a las diagonales e infinito a los restantes*/
        for (let i = 0; i < this.nodesNumber; i++){
            for (let j = 0; j < this.nodesNumber; j++){
                this.d[i][j] = this.INF
                this.parent[i][j] = -1
            }
        this.d[i][i] = 0
        }

        /*Hallando las lineas de todas las relaciones*/
        for(let value of this.relationsPair){
            this.relationsLine.push(
                {
                    latlngs: [this.points[value[0]-1], this.points[value[1]-1]],
                    color: "blue"
                }
            )
        }

        /*Hallando la distancia pitagórica de todos los caminos y agregandola a la matriz*/
        for(let value of this.relationsPair){
            this.addEdge(value[0], value[1], Math.sqrt(Math.pow(this.points[value[0]-1][0] - this.points[value[1]-1][0], 2) + Math.pow(this.points[value[0]-1][1] - this.points[value[1]-1][1], 2) ) )
        }

        this.floydWarshall(this.nodesNumber)
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
            this.arrNodes = []
            this.minPath.latlngs = [],
            this.path = []
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