<template>

<div style="height: 500px; width: 100%">
    <l-map :zoom="zoom" :center="center" :options="mapOptions" style="height: 125%" @update:center="centerUpdate" @update:zoom="zoomUpdate">
        <l-tile-layer :url="url" :attribution="attribution"/>
            <template v-for="(point, index) in points">
                <l-marker :lat-lng="latLng(point.coord1, point.coord2)" :key="point + index" @click="agregarInd(index)">
                    <l-tooltip :options="{ permanent: true }">{{point.name}}</l-tooltip>
                </l-marker>
            </template>
            <template v-for="(line, index) in relationsLine">
                <l-polyline :lat-lngs="relationsLine[index].latlngs" :color="relationsLine[index].color" :key="relationsLine + index"></l-polyline>
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
            center: latLng(-12.2833333, -76.2),
            url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
            attribution:
                '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            currentZoom: 11.5,
            currentCenter: latLng(-12.2833333, -76.2),
            showParagraph: false,
            mapOptions: {
                zoomSnap: 0.5
            },
            /*Coordenadas de los nodos*/
            points:[
                {name:"acachare", coord1:-12.2833333, coord2:-76.2},
                {name:"acopata", coord1:-10.685, coord2:-76.74638890000001},
                {name:"aguar", coord1:-10.835, coord2:-76.9858333},
                {name:"alcacoto", coord1:-11.7166667, coord2:-76.8833333},
                {name:"alip", coord1:-12.266666699999998, coord2:-75.7833333},
                {name:"almenares", coord1:-13.0666667, coord2:-76.33333329999998},
                {name:"alto peru", coord1:-11.1213889, coord2:-76.5366667},
                {name:"anchimaja", coord1:-11.8694444, coord2:-76.4352778},
                {name:"andajes", coord1:-10.7922222, coord2:-76.9094444},
                {name:"andamarca", coord1:-11.3, coord2:-76.7666667},
                {name:"antaullo", coord1:-12.806388900000002, coord2:-75.7802778},
                {name:"antucrun", coord1:-11.0069444, coord2:-76.705},
                {name:"apahuaique", coord1:-12.0666667, coord2:-76.4333333},
                {name:"aquicha", coord1:-12.4166667, coord2:-75.83333329999998},
                {name:"araya grande", coord1:-10.6666667, coord2:-77.6333333},
                {name:"araya grande hacienda", coord1:-10.6666667, coord2:-77.6333333},
                {name:"arcata", coord1:-10.85, coord2:-77.3166667},
                {name:"arcopampa", coord1:-12.7255556, coord2:-75.6227778},
                {name:"atun machay", coord1:-11.051666699999998, coord2:-76.65138890000001},
                {name:"atunpampa", coord1:-10.5177778, coord2:-76.87777779999998},
                {name:"ayllon", coord1:-10.7166667, coord2:-77.16666670000002},
                {name:"barranco", coord1:-12.15, coord2:-77.0333333},
                {name:"bella luz", coord1:-10.6880556, coord2:-76.7233333},
                {name:"bellavista", coord1:-10.8333333, coord2:-77.7166667},
                {name:"blanca rosa del mar", coord1:-12.766666699999998, coord2:-76.6},
                {name:"bravo grande", coord1:-12.05, coord2:-76.95},
                {name:"bunabamba", coord1:-11.435, coord2:-76.5725},
                {name:"cacal", coord1:-10.9, coord2:-77.5166667},
                {name:"cacan", coord1:-11.3902778, coord2:-76.6477778},
                {name:"calachota", coord1:-12.6308333, coord2:-75.97972220000003},
                {name:"caldera hacienda", coord1:-11.0833333, coord2:-77.4666667},
                {name:"callisca", coord1:-12.3166667, coord2:-75.6333333},
                {name:"camacho", coord1:-12.0833333, coord2:-76.9666667},
                {name:"campamento", coord1:-11.27, coord2:-76.9883333},
                {name:"campo florido", coord1:-12.9444444, coord2:-75.7508333},
                {name:"canchahuara", coord1:-12.0333333, coord2:-76.3166667},
                {name:"canchan", coord1:-12.7819444, coord2:-75.91638890000002},
                {name:"canchapata", coord1:-12.8272222, coord2:-75.7194444},
                {name:"canchapitca", coord1:-11.25, coord2:-76.8166667},
                {name:"canchipampa", coord1:-12.6041667, coord2:-75.9233333},
                {name:"canete", coord1:-13.0833333, coord2:-76.4},
                {name:"canta gallo", coord1:-12.841388900000002, coord2:-75.9777778},
                {name:"capash", coord1:-10.915, coord2:-76.82472220000002},
                {name:"capilla", coord1:-11.2091667, coord2:-76.5197222},
                {name:"capillapata", coord1:-10.9666667, coord2:-77.08333329999998},
                {name:"caral hacienda", coord1:-10.9, coord2:-77.5166667},
                {name:"carapilana", coord1:-11.7808333, coord2:-76.23527779999998},
                {name:"caraponga", coord1:-12.0, coord2:-76.8666667},
                {name:"carcapata", coord1:-12.8747222, coord2:-75.6322222},
                {name:"carhuac", coord1:-11.6655556, coord2:-76.4927778},
                {name:"casa blanca", coord1:-13.05, coord2:-76.4333333},
                {name:"casa blanca hacienda", coord1:-12.2166667, coord2:-76.8666667},
                {name:"casa pintada hacienda", coord1:-13.0333333, coord2:-76.3666667},
                {name:"casa vieja", coord1:-12.116666699999998, coord2:-76.8166667},
                {name:"catas", coord1:-12.5333333, coord2:-76.25},
                {name:"caullamancha", coord1:-12.2, coord2:-76.25},
                {name:"cebadacancha", coord1:-13.0333333, coord2:-75.83333329999998},
                {name:"cebada corral", coord1:-11.1011111, coord2:-76.6652778},
                {name:"cerro blanco hacienda", coord1:-10.616666699999998, coord2:-77.7833333},
                {name:"cerro pamparena", coord1:-12.2, coord2:-76.5333333},
                {name:"chacamarca", coord1:-12.8066667, coord2:-75.6880556},
                {name:"chaclla", coord1:-11.7427778, coord2:-76.6486111},
                {name:"chacra cerro hacienda", coord1:-11.9166667, coord2:-77.0666667},
                {name:"chagapata", coord1:-10.8622222, coord2:-76.615},
                {name:"chancay", coord1:-11.5597222, coord2:-77.27111109999998},
                {name:"chancayllo hacienda", coord1:-11.4883333, coord2:-77.305},
                {name:"chaquisa", coord1:-12.0666667, coord2:-76.25},
                {name:"chatacanchahuaique", coord1:-12.3, coord2:-76.35},
                {name:"chaucas", coord1:-12.6625, coord2:-75.7769444},
                {name:"chauco", coord1:-11.4155556, coord2:-76.5397222},
                {name:"chau pirarca", coord1:-11.1547222, coord2:-76.97916670000002},
                {name:"chicche", coord1:-10.563333300000002, coord2:-76.8861111},
                {name:"chico", coord1:-13.016666699999998, coord2:-76.41666670000002},
                {name:"chillipahuasi", coord1:-12.6655556, coord2:-75.5866667},
                {name:"chimba", coord1:-10.8, coord2:-76.91666670000002},
                {name:"chira", coord1:-12.35, coord2:-76.83333329999998},
                {name:"chirec", coord1:-10.6308333, coord2:-76.7308333},
                {name:"chiricurral", coord1:-11.018333300000002, coord2:-76.84},
                {name:"chocalla", coord1:-12.9347222, coord2:-75.8416667},
                {name:"chocapata", coord1:-12.9666667, coord2:-75.8833333},
                {name:"chocasa", coord1:-12.5094444, coord2:-75.93166670000002},
                {name:"chulmamachay", coord1:-10.7172222, coord2:-76.7388889},
                {name:"chunga", coord1:-11.1247222, coord2:-76.53944440000002},
                {name:"chupa cigarro grande", coord1:-10.9, coord2:-77.5333333},
                {name:"cochatama", coord1:-10.851388900000002, coord2:-76.68722220000002},
                {name:"cochca", coord1:-11.2741667, coord2:-76.74722220000002},
                {name:"cochec", coord1:-11.2072222, coord2:-76.91111109999999},
                {name:"colca", coord1:-12.7636111, coord2:-75.83888890000001},
                {name:"collaray", coord1:-11.016666699999998, coord2:-76.99861109999998},
                {name:"collpapuquio", coord1:-11.6, coord2:-76.6},
                {name:"colpa", coord1:-10.6, coord2:-76.95},
                {name:"comas hacienda", coord1:-11.95, coord2:-77.0666667},
                {name:"conchasica", coord1:-12.05, coord2:-76.4},
                {name:"concubay", coord1:-12.6527778, coord2:-75.9777778},
                {name:"contadero", coord1:-10.5280556, coord2:-76.9772222},
                {name:"copacabana", coord1:-11.85, coord2:-77.1},
                {name:"copacabana hacienda", coord1:-11.85, coord2:-77.1},
                {name:"corralon", coord1:-12.266666699999998, coord2:-76.3166667},
                {name:"curicancha", coord1:-11.5833333, coord2:-76.5333333},
                {name:"cusi", coord1:-12.5630556, coord2:-75.9080556},
                {name:"cutacancha", coord1:-10.6355556, coord2:-76.84388890000002},
                {name:"cutamajada", coord1:-10.4666667, coord2:-76.91666670000002},
                {name:"cuyahuasi", coord1:-12.4, coord2:-76.4},
                {name:"cuyrupcancha", coord1:-12.9216667, coord2:-75.6969444},
                {name:"desagravio", coord1:-11.0666667, coord2:-77.5666667},
                {name:"el arenal", coord1:-11.5666667, coord2:-77.1833333},
                {name:"el molino hacienda", coord1:-10.733333300000002, coord2:-77.75},
                {name:"encalada", coord1:-12.05, coord2:-76.9666667},
                {name:"erhuaca", coord1:-12.6697222, coord2:-75.9575},
                {name:"espuy", coord1:-12.7616667, coord2:-75.9483333},
                {name:"establo punchauca", coord1:-11.85, coord2:-77.0},
                {name:"florida", coord1:-12.9444444, coord2:-75.7508333},
                {name:"fopas", coord1:-12.75, coord2:-76.4833333},
                {name:"fundo copacabana", coord1:-12.733333300000002, coord2:-76.6166667},
                {name:"fundo santa fe", coord1:-11.4166667, coord2:-77.2166667},
                {name:"fundo santa juana", coord1:-10.9, coord2:-77.6333333},
                {name:"garbanzo", coord1:-10.6477778, coord2:-76.9858333},
                {name:"garita dona maria", coord1:-11.4, coord2:-77.4},
                {name:"gasgas", coord1:-11.4705556, coord2:-76.56},
                {name:"gorgor", coord1:-10.5833333, coord2:-77.0333333},
                {name:"granados", coord1:-12.0666667, coord2:-76.95},
                {name:"guacayan", coord1:-11.846666699999998, coord2:-76.1533333},
                {name:"hacienda chambara", coord1:-11.1, coord2:-77.33333329999998},
                {name:"hacienda el olivar", coord1:-11.733333300000002, coord2:-76.9833333},
                {name:"hacienda herbay bajo", coord1:-13.133333300000002, coord2:-76.4},
                {name:"hacienda huampani", coord1:-11.9666667, coord2:-76.7833333},
                {name:"hacienda humaya", coord1:-11.1, coord2:-77.41666670000002},
                {name:"hacienda janquil", coord1:-10.9275, coord2:-76.6466667},
                {name:"hacienda jesus del valle", coord1:-11.516666699999998, coord2:-77.2},
                {name:"hacienda marquez", coord1:-11.95, coord2:-77.1333333},
                {name:"hacienda miraflores", coord1:-11.5333333, coord2:-77.16666670000002},
                {name:"hacienda salitre", coord1:-12.6833333, coord2:-76.65},
                {name:"hacienda santa isabel", coord1:-10.983333300000002, coord2:-77.65},
                {name:"hacienda unanue", coord1:-13.116666699999998, coord2:-76.4},
                {name:"huacaypaca", coord1:-11.9158333, coord2:-76.14138890000002},
                {name:"huachinga", coord1:-11.198333300000002, coord2:-76.8972222},
                {name:"huacrocorral", coord1:-10.5169444, coord2:-76.9519444},
                {name:"huaguina", coord1:-11.9888889, coord2:-76.4091667},
                {name:"huaichautana", coord1:-11.010833300000002, coord2:-76.70138890000001},
                {name:"huallao", coord1:-10.9655556, coord2:-76.9572222},
                {name:"huallape", coord1:-10.366666699999998, coord2:-77.0},
                {name:"huambay chico", coord1:-10.9, coord2:-77.0666667},
                {name:"huampan", coord1:-11.1, coord2:-77.0},
                {name:"huanacallpi", coord1:-12.8288889, coord2:-75.6558333},
                {name:"huanacopunahuain", coord1:-10.8941667, coord2:-76.7483333},
                {name:"huancani", coord1:-12.483333300000002, coord2:-76.4333333},
                {name:"huanchay", coord1:-11.1144444, coord2:-76.5594444},
                {name:"huando hacienda", coord1:-11.5, coord2:-77.1833333},
                {name:"huarabi bajo hacienda", coord1:-11.6833333, coord2:-76.9},
                {name:"huarangal", coord1:-11.266666699999998, coord2:-76.9833333},
                {name:"huarangayo", coord1:-11.835, coord2:-76.16111109999999},
                {name:"huascata", coord1:-12.0, coord2:-76.83333329999998},
                {name:"huatara", coord1:-12.8130556, coord2:-75.77444440000002},
                {name:"huaura", coord1:-11.0647222, coord2:-77.6},
                {name:"huayan", coord1:-11.45, coord2:-77.1333333},
                {name:"huaylinco", coord1:-11.1530556, coord2:-76.9819444},
                {name:"huayto", coord1:-10.65, coord2:-77.66666670000002},
                {name:"huirpina", coord1:-13.0333333, coord2:-75.9666667},
                {name:"humaya hacienda", coord1:-11.1, coord2:-77.41666670000002},
                {name:"independencia", coord1:-11.983333300000002, coord2:-77.0333333},
                {name:"inya", coord1:-12.9838889, coord2:-75.86583329999998},
                {name:"iscaycocha", coord1:-12.9080556, coord2:-75.65388890000001},
                {name:"isco", coord1:-12.6297222, coord2:-75.5980556},
                {name:"jaiba", coord1:-10.883333300000002, coord2:-77.3833333},
                {name:"janca", coord1:-11.0566667, coord2:-76.6188889},
                {name:"japur", coord1:-10.9536111, coord2:-76.7016667},
                {name:"jicamarca", coord1:-11.65, coord2:-76.6166667},
                {name:"lacsa", coord1:-11.2627778, coord2:-76.7425},
                {name:"lagsaura", coord1:-10.8644444, coord2:-76.8688889},
                {name:"la hoyada", coord1:-10.75, coord2:-77.7333333},
                {name:"la milla", coord1:-12.016666699999998, coord2:-77.0666667},
                {name:"lampas", coord1:-10.5658333, coord2:-76.9486111},
                {name:"lancal", coord1:-10.6233333, coord2:-76.7508333},
                {name:"lantudan", coord1:-11.285833300000002, coord2:-76.52722220000003},
                {name:"la planicie", coord1:-12.0666667, coord2:-76.9},
                {name:"las huertas hacienda", coord1:-10.6833333, coord2:-77.65},
                {name:"las monjas", coord1:-10.6833333, coord2:-77.7833333},
                {name:"la toma", coord1:-10.55, coord2:-77.2333333},
                {name:"la virgen", coord1:-12.633333300000002, coord2:-76.66666670000002},
                {name:"layampata", coord1:-12.788888900000002, coord2:-75.7469444},
                {name:"leurac", coord1:-10.7288889, coord2:-76.7047222},
                {name:"lichigan", coord1:-11.3886111, coord2:-76.61583329999998},
                {name:"lihuanco", coord1:-13.016666699999998, coord2:-76.4666667},
                {name:"linday", coord1:-11.87, coord2:-76.46638890000001},
                {name:"llama huaca hacienda", coord1:-10.866666699999998, coord2:-77.55},
                {name:"llamapisillo", coord1:-11.8930556, coord2:-76.1383333},
                {name:"lliru", coord1:-11.6666667, coord2:-76.4369444},
                {name:"locicasos", coord1:-12.383333300000002, coord2:-76.7},
                {name:"lucumo hacienda", coord1:-13.0333333, coord2:-76.2},
                {name:"lucumo", coord1:-13.0333333, coord2:-76.2},
                {name:"lumbreras hacienda", coord1:-12.6833333, coord2:-76.6333333},
                {name:"lurimarca", coord1:-12.9302778, coord2:-75.9380556},
                {name:"lutacocha", coord1:-10.9616667, coord2:-76.60027779999999},
                {name:"machuranga", coord1:-12.8333333, coord2:-76.0166667},
                {name:"macotca", coord1:-11.4477778, coord2:-76.8086111},
                {name:"magdalena", coord1:-12.0833333, coord2:-77.0666667},
                {name:"magdalena vieja", coord1:-12.0833333, coord2:-77.0666667},
                {name:"manchay", coord1:-11.7558333, coord2:-76.2505556},
                {name:"maray", coord1:-10.9355556, coord2:-76.8338889},
                {name:"marcalla", coord1:-12.866666699999998, coord2:-76.2},
                {name:"matiraqui", coord1:-10.4, coord2:-76.8666667},
                {name:"millo", coord1:-11.5705556, coord2:-76.3497222},
                {name:"minapata", coord1:-10.5655556, coord2:-76.7261111},
                {name:"mira mar hacienda", coord1:-10.7, coord2:-77.8166667},
                {name:"mishuya", coord1:-10.7136111, coord2:-76.71861109999998},
                {name:"montepata", coord1:-11.9227778, coord2:-76.3291667},
                {name:"monterrico", coord1:-11.8522222, coord2:-76.39972220000001},
                {name:"naranjal", coord1:-10.5333333, coord2:-77.75},
                {name:"nauyana", coord1:-11.8502778, coord2:-76.1327778},
                {name:"nicolas de pierola", coord1:-11.95, coord2:-76.7},
                {name:"nieveria", coord1:-11.983333300000002, coord2:-76.91666670000002},
                {name:"ollancaca", coord1:-11.3125, coord2:-76.9397222},
                {name:"ongos", coord1:-12.8102778, coord2:-75.7658333},
                {name:"orcocoto", coord1:-12.1, coord2:-76.4666667},
                {name:"orrantia", coord1:-12.1, coord2:-77.05},
                {name:"otec", coord1:-11.1763889, coord2:-76.90638890000002},
                {name:"pacaybamba", coord1:-11.4605556, coord2:-76.89972220000001},
                {name:"pacchipampa", coord1:-11.0719444, coord2:-76.6936111},
                {name:"pachangara", coord1:-10.7830556, coord2:-76.8147222},
                {name:"pahuaray", coord1:-11.516666699999998, coord2:-76.7666667},
                {name:"pallicache", coord1:-11.97, coord2:-76.33972220000003},
                {name:"pampacancha", coord1:-11.9388889, coord2:-76.19555559999998},
                {name:"pampa libre", coord1:-10.8663889, coord2:-76.9683333},
                {name:"paqui", coord1:-12.915, coord2:-75.81833329999998},
                {name:"paria pampa", coord1:-12.696666699999998, coord2:-75.5877778},
                {name:"pasaca", coord1:-12.516666699999998, coord2:-76.5},
                {name:"pasapashimin", coord1:-10.6172222, coord2:-76.9705556},
                {name:"pati", coord1:-12.9022222, coord2:-75.8883333},
                {name:"picapiedra", coord1:-12.1833333, coord2:-76.8666667},
                {name:"piquillo hacienda", coord1:-11.4666667, coord2:-77.1166667},
                {name:"pirca huasi", coord1:-11.2555556, coord2:-76.8219444},
                {name:"piscuracgra", coord1:-11.0119444, coord2:-76.76861109999999},
                {name:"pitago", coord1:-10.916111099999998, coord2:-76.7130556},
                {name:"playa de santa maria", coord1:-12.4166667, coord2:-76.7833333},
                {name:"pomamayo", coord1:-10.6375, coord2:-76.7725},
                {name:"pongo", coord1:-12.35, coord2:-76.3166667},
                {name:"poquio", coord1:-12.85, coord2:-76.0166667},
                {name:"porococha", coord1:-12.5666667, coord2:-76.16666670000002},
                {name:"puca gallo", coord1:-12.45, coord2:-75.55},
                {name:"pueacorral", coord1:-11.8766667, coord2:-76.2316667},
                {name:"puente piedra hacienda", coord1:-11.8680556, coord2:-77.0775},
                {name:"puente piedra", coord1:-11.866666699999998, coord2:-77.08333329999998},
                {name:"puerto supe", coord1:-10.8166667, coord2:-77.75},
                {name:"puquian", coord1:-10.4333333, coord2:-77.1333333},
                {name:"purmacana", coord1:-10.75, coord2:-77.6333333},
                {name:"puruguay", coord1:-11.8177778, coord2:-76.17277779999998},
                {name:"quebrada seca", coord1:-12.4, coord2:-76.7833333},
                {name:"queroy", coord1:-12.5677778, coord2:-75.70527779999998},
                {name:"quillcata", coord1:-12.5427778, coord2:-75.7508333},
                {name:"quilmana", coord1:-12.95, coord2:-76.3833333},
                {name:"quimpata", coord1:-12.3333333, coord2:-75.75},
                {name:"quiscay", coord1:-12.5044444, coord2:-75.91861109999998},
                {name:"quives", coord1:-11.6672222, coord2:-76.7883333},
                {name:"racracancha", coord1:-10.7222222, coord2:-76.71888890000002},
                {name:"raucuta", coord1:-11.0466667, coord2:-76.8733333},
                {name:"raure", coord1:-11.3005556, coord2:-76.85611109999998},
                {name:"reparticion", coord1:-11.15, coord2:-77.0666667},
                {name:"ricardo palma", coord1:-11.9180556, coord2:-76.66638890000002},
                {name:"rinconada", coord1:-10.4166667, coord2:-77.7333333},
                {name:"rirco", coord1:-10.6263889, coord2:-76.81361109999997},
                {name:"rucma", coord1:-10.5977778, coord2:-76.9002778},
                {name:"rumo", coord1:-11.2677778, coord2:-76.84388890000002},
                {name:"runaquilca", coord1:-11.2797222, coord2:-76.5838889},
                {name:"rupay", coord1:-10.6947222, coord2:-76.8211111},
                {name:"sacallana", coord1:-11.9761111, coord2:-76.33972220000003},
                {name:"sacrampe", coord1:-11.8761111, coord2:-76.4247222},
                {name:"sacsacoto", coord1:-12.116666699999998, coord2:-76.45},
                {name:"san bartolo", coord1:-12.383333300000002, coord2:-76.7833333},
                {name:"sangallaya", coord1:-12.1666667, coord2:-76.2666667},
                {name:"san graciano", coord1:-11.5666667, coord2:-77.16666670000002},
                {name:"san juan de huagar", coord1:-10.9566667, coord2:-76.9541667},
                {name:"san juan", coord1:-11.1588889, coord2:-76.9183333},
                {name:"san mateo", coord1:-10.75, coord2:-77.75},
                {name:"san miguel characuaycui", coord1:-11.9730556, coord2:-76.4105556},
                {name:"san miguel de characuayqui", coord1:-11.9730556, coord2:-76.4105556},
                {name:"san pablo de ayaranga", coord1:-10.933611099999998, coord2:-76.94},
                {name:"san pedro", coord1:-10.9505556, coord2:-76.6930556},
                {name:"santa ana", coord1:-11.0833333, coord2:-77.6},
                {name:"santa cruz de ucros", coord1:-11.866666699999998, coord2:-76.5166667},
                {name:"santa maria alta", coord1:-13.0833333, coord2:-76.3166667},
                {name:"santa rosa de quibe", coord1:-11.6672222, coord2:-76.7883333},
                {name:"santa rosa de quives", coord1:-11.6672222, coord2:-76.7883333},
                {name:"saramasana", coord1:-13.0333333, coord2:-75.9333333},
                {name:"shampuy", coord1:-10.7655556, coord2:-77.00111109999997},
                {name:"shaprupacancha", coord1:-10.6408333, coord2:-76.80888890000001},
                {name:"shonco", coord1:-12.5833333, coord2:-76.2},
                {name:"sicsihuasi", coord1:-12.704166699999998, coord2:-75.6472222},
                {name:"sicsi", coord1:-13.0333333, coord2:-75.95},
                {name:"singua chico", coord1:-12.133333300000002, coord2:-75.7333333},
                {name:"singua grande", coord1:-12.2, coord2:-75.6833333},
                {name:"sipicuta", coord1:-10.6058333, coord2:-76.97972220000003},
                {name:"sirhuayo", coord1:-11.4552778, coord2:-76.5972222},
                {name:"socsi", coord1:-13.0333333, coord2:-76.2166667},
                {name:"sullcumachay", coord1:-12.825, coord2:-75.66027779999997},
                {name:"sumbilca", coord1:-11.4075, coord2:-76.82},
                {name:"sunicancha", coord1:-12.05, coord2:-76.3666667},
                {name:"surquillo", coord1:-12.116666699999998, coord2:-77.0333333},
                {name:"tamboraque", coord1:-11.7822222, coord2:-76.3075},
                {name:"tambo viejo", coord1:-10.733333300000002, coord2:-77.7833333},
                {name:"tampocancha", coord1:-11.9727778, coord2:-76.3433333},
            ],
            /*Matriz de relaciones entre los nodos*/
            relationsPair:[
                [1, 74], [1, 84], [1, 250], [1, 255], [2, 45], [2, 91], [2, 169], [2, 274], [2, 298], [3, 61], [3, 67], [3, 94], [4, 169], [4, 274], [5, 59], [5, 144], [5, 155], [6, 90], [6, 188], [6, 242], [6, 300], [7, 69], [7, 141], [7, 207], [8, 76], [8, 250], [9, 35], [9, 191], [10, 60], [10, 95], [10, 172], [10, 173], [10, 223], [10, 270], [10, 288], [11, 62], [11, 201], [11, 226], [11, 286], [12, 240], [12, 263], [13, 136], [13, 153], [13, 154], [13, 295], [14, 44], [14, 86], [14, 113], [14, 118], [15, 35], [15, 222], [15, 263], [16, 29], [16, 142], [16, 145], [16, 171], [16, 226], [17, 66], [17, 105], [17, 224], [18, 24], [18, 130], [18, 231], [19, 52], [19, 89], [19, 148], [19, 297], [20, 21], [20, 42], [20, 51], [20, 182], [20, 248], [21, 42], [21, 176], [21, 182], [22, 99], [22, 100], [22, 101], [22, 110], [22, 247], [22, 248], [23, 102], [23, 103], [23, 119], [23, 131], [23, 147], [23, 183], [23, 283], [24, 25], [24, 231], [24, 238], [25, 139], [25, 158], [25, 260], [26, 183], [26, 215], [26, 280], [27, 143], [27, 155], [27, 165], [27, 230], [28, 37], [28, 38], [28, 179], [28, 261], [29, 228], [29, 256], [30, 79], [30, 128], [31, 105], [31, 165], [31, 262], [31, 278], [32, 74], [33, 126], [33, 170], [33, 186], [33, 275], [34, 114], [34, 115], [34, 159], [34, 254], [34, 294], [35, 52], [35, 191], [35, 222], [35, 240], [36, 156], [36, 198], [36, 272], [37, 83], [37, 220], [37, 261], [37, 264], [38, 146], [38, 220], [39, 241], [39, 297], [40, 143], [40, 257], [40, 262], [40, 278], [40, 299], [41, 64], [41, 105], [41, 257], [41, 278], [41, 299], [42, 125], [42, 176], [42, 180], [42, 284], [43, 264], [43, 267], [44, 113], [44, 178], [45, 164], [46, 139], [46, 151], [46, 246], [46, 289], [47, 70], [47, 72], [47, 81], [47, 89], [47, 200], [48, 252], [48, 258], [48, 280], [49, 202], [49, 237], [49, 273], [50, 70], [50, 81], [50, 89], [50, 106], [50, 239], [50, 241], [50, 292], [51, 90], [51, 182], [52, 81], [52, 214], [52, 281], [53, 70], [53, 249], [54, 130], [54, 140], [55, 63], [55, 78], [55, 185], [56, 87], [56, 97], [56, 174], [56, 196], [57, 78], [57, 124], [57, 157], [57, 178], [57, 253], [58, 71], [58, 167], [58, 192], [58, 249], [59, 144], [59, 155], [59, 204], [60, 205], [60, 271], [60, 288], [61, 202], [61, 227], [61, 286], [62, 177], [62, 201], [62, 276], [62, 286], [63, 87], [63, 97], [63, 124], [63, 185], [64, 88], [64, 257], [64, 299], [65, 73], [65, 197], [65, 229], [65, 268], [66, 68], [66, 104], [66, 105], [66, 154], [66, 224], [67, 94], [67, 293], [68, 136], [69, 141], [70, 200], [71, 152], [71, 167], [71, 200], [71, 249], [72, 192], [72, 200], [72, 281], [72, 285], [73, 229], [73, 287], [75, 140], [75, 232], [75, 259], [75, 260], [76, 243], [77, 96], [77, 133], [77, 156], [77, 194], [77, 198], [77, 203], [78, 157], [78, 178], [78, 185], [79, 120], [79, 121], [79, 128], [79, 161], [79, 213], [80, 98], [80, 120], [80, 121], [80, 128], [80, 211], [81, 148], [81, 214], [81, 241], [82, 111], [82, 190], [82, 206], [82, 210], [83, 177], [83, 267], [83, 273], [84, 133], [84, 203], [84, 250], [84, 255], [85, 106], [85, 297], [86, 253], [87, 196], [87, 199], [87, 279], [88, 123], [88, 135], [89, 241], [89, 292], [90, 197], [91, 160], [91, 244], [92, 108], [92, 109], [92, 132], [92, 149], [92, 236], [93, 189], [93, 225], [93, 269], [93, 277], [93, 300], [94, 137], [94, 138], [94, 181], [95, 172], [95, 173], [95, 270], [96, 107], [96, 133], [96, 203], [97, 174], [97, 282], [98, 120], [98, 121], [98, 211], [98, 213], [99, 101], [99, 182], [99, 296], [100, 110], [100, 233], [100, 247], [100, 248], [100, 296], [101, 110], [101, 233], [101, 296], [102, 174], [102, 183], [102, 215], [103, 174], [103, 199], [103, 283], [104, 105], [106, 239], [106, 249], [106, 292], [108, 109], [108, 132], [108, 149], [108, 175], [108, 184], [108, 266], [109, 175], [109, 184], [110, 296], [111, 127], [111, 163], [111, 206], [111, 210], [112, 184], [112, 217], [113, 195], [114, 123], [114, 159], [115, 135], [115, 159], [115, 254], [116, 129], [116, 170], [116, 221], [117, 168], [117, 170], [117, 187], [117, 217], [118, 142], [119, 131], [119, 174], [119, 183], [120, 121], [120, 213], [122, 131], [122, 147], [122, 216], [122, 218], [123, 135], [124, 157], [125, 180], [125, 212], [125, 248], [125, 284], [126, 170], [126, 275], [127, 210], [127, 244], [128, 161], [128, 162], [128, 193], [128, 213], [128, 265], [128, 290], [129, 168], [129, 217], [129, 221], [129, 245], [130, 140], [131, 216], [131, 282], [131, 283], [132, 149], [132, 236], [132, 266], [133, 203], [134, 208], [134, 251], [134, 271], [135, 159], [136, 154], [136, 155], [137, 138], [137, 181], [138, 171], [138, 293], [139, 151], [139, 246], [139, 260], [139, 289], [140, 191], [140, 259], [140, 260], [141, 207], [142, 145], [142, 195], [143, 262], [144, 204], [144, 209], [144, 295], [145, 226], [146, 150], [146, 179], [146, 220], [146, 261], [147, 216], [147, 218], [147, 283], [148, 297], [149, 175], [149, 266], [150, 177], [150, 220], [150, 276], [151, 158], [151, 289], [152, 192], [152, 285], [153, 154], [153, 155], [154, 155], [154, 256], [155, 165], [156, 194], [157, 178], [157, 185], [157, 253], [157, 282], [158, 260], [158, 289], [159, 254], [160, 164], [163, 206], [165, 230], [166, 172], [166, 205], [166, 271], [167, 192], [167, 285], [168, 170], [168, 217], [169, 274], [169, 298], [170, 186], [170, 217], [170, 221], [170, 245], [170, 275], [171, 228], [172, 270], [172, 288], [173, 223], [173, 270], [175, 266], [176, 180], [176, 234], [176, 284], [177, 276], [178, 282], [179, 261], [179, 264], [180, 234], [180, 235], [181, 293], [183, 215], [183, 252], [186, 275], [187, 275], [188, 207], [188, 242], [188, 300], [189, 225], [189, 242], [189,269], [189, 300], [190, 206], [190, 210], [191, 232], [191, 259], [193, 211], [193, 213], [193, 265], [195, 253], [196, 199], [196, 279], [197, 268], [197, 287], [201, 286], [202, 227], [202, 286], [204, 230], [205, 288], [206, 210], [207, 242], [208, 251], [208, 271], [209, 256], [209, 295], [212, 284], [213, 265], [213, 290], [214, 281], [215, 280], [216, 218], [217, 245], [219, 291], [221, 245], [223, 288], [223, 291], [225, 269], [225, 277], [227, 276], [227, 286], [228, 256], [231, 238], [232, 259], [232, 260], [233, 247], [233, 296], [234, 248], [235, 248], [236, 266], [237, 264], [237, 267], [237, 273], [239, 249], [239, 292], [240, 281], [241, 292], [242, 269], [242, 300], [247, 296], [250, 255], [256, 293], [257, 262], [257, 299], [258, 280], [261, 264], [262, 278], [262, 299], [264, 267], [265, 290], [267, 273], [269, 277], [269, 287], [272, 274], [274, 298], [276, 286], [277, 287], [288, 291], [294, 299]
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
                    latlngs: [[this.points[value[0]-1].coord1, this.points[value[0]-1].coord2], [this.points[value[1]-1].coord1, this.points[value[1]-1].coord2]],
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
            }/* Agrega 1 y 7 de nuevo al minpath*/
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