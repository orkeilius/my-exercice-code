interface Point{
    links: number[];
    exit?: boolean;
    origin?: number;
}
                     

var inputs: number[] = readline().split(' ').map(x => parseInt(x));
const N: number = inputs[0]; // the total number of nodes in the level, including the gateways
const L: number = inputs[1]; // the number of links
const E: number = inputs[2]; // the number of exit gateways

//get point
var graph:Point[] = [] 
for (let i = 0; i < N; i++) {
    graph.push({links:[]})
}

//get link
for (let i = 0; i < L; i++) {
    var inputs: number[] = readline().split(' ').map(x => parseInt(x));
    graph[inputs[0]].links.push(inputs[1])
    graph[inputs[1]].links.push(inputs[0])
}

//Add gateways
for (let i = 0; i < E; i++) {
    var eee = parseInt(readline())
    graph[eee].exit = true; // the index of a gateway node
}

// game loop
while (true) {
    const SI: number = parseInt(readline()); // The index of the node on which the Bobnet agent is positioned this turn

    var queue: number[] = [SI]
    var visited: number[]  = []
    while (graph[queue[0]].exit == undefined) {
             graph[queue[0]].links.forEach(element => {
            if (!(visited.includes(element))) {
                graph[element].origin = queue[0]
                queue.push(element)
                visited.push(element)
            }
        });
        queue.shift()
    }
    console.log(queue[0] + " " + graph[queue[0]].origin)
    console.error(graph)

    //delete cuted nodes
    graph[queue[0]].links.splice(graph[queue[0]].links.indexOf(graph[queue[0]].origin),1)
    graph[graph[queue[0]].origin].links.slice(graph[graph[queue[0]].origin].links.indexOf(queue[0]),1)
}

function readline() {
    throw new Error("Function not implemented.");
}
