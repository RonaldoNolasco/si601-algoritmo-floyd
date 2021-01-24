var MX = 300;
var INF = 1e10;

var d = [];
var parent = [];

for(let i = 0; i < MX; i++) {
    d.push([]);
    parent.push([]);
    for (let j = 0; j < MX; j++) {
        d[i].push(null);
        parent[i].push(null);
    }
}


function initialize(n){
    for (let i = 0; i < n; i++){
        for (let j = 0; j < n; j++){
            d[i][j] = INF
            parent[i][j] = -1
        }
        d[i][i] = 0
    }
}

function addEdge(u, v, w){
    u = u - 1
    v = v - 1
    
    if(d[u][v] > w) d[u][v] = w;
    if(d[v][u] > w) d[v][u] = w;
    parent[u][v] = u
    parent[v][u] = v
}

function floydWarshall(n){
    for (let k = 0; k < n; k++){
        for (let u = 0; u < n; u++){
            for (let v = 0; v < n; v++){
                if(d[u][k] == INF) continue;
                if(d[k][v] == INF) continue;
                if(d[u][k] + d[k][v] < d[u][v]){
                    d[u][v] = d[u][k] + d[k][v]
                    parent[u][v] = parent[k][v]
                }
            }
        }
    }
}

function getPath(u,v){
    u = u - 1
    v = v - 1

    path = []

    while(v != -1){
        path.push(v + 1)
        v = parent[u][v]
    }
    path.reverse()
    
    return path
}

initialize(4)

addEdge(1, 2, 5)
addEdge(2, 4, 8)
addEdge(1, 3, 3)
addEdge(3, 4, 6)

floydWarshall(4)

console.log(getPath(1,4))
