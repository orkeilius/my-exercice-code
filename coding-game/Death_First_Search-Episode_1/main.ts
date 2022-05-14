interface Point{
    links: number[];
    exit?: boolean;
}
interface PointSearch{
    id: number;
    origin: number;
}


var inputs: number[] = readline().split(' ').map(x => parseInt(x));
const N: number = inputs[0]; // the total number of nodes in the level, including the gateways
const L: number = inputs[1]; // the number of links
const E: number = inputs[2]; // the number of exit gateways

var graph:Point[] = [] 
for (let i = 0; i < N; i++) {
    graph.push({links:[]})
}
for (let i = 0; i < L; i++) {
    var inputs: number[] = readline().split(' ').map(x => parseInt(x));
    graph[inputs[0]].links.push(inputs[1])
    graph[inputs[1]].links.push(inputs[0])
}
for (let i = 0; i < E; i++) {
    var eee = parseInt(readline())
    graph[eee].exit = true; // the index of a gateway node
}

// game loop
while (true) {
    const SI: number = parseInt(readline()); // The index of the node on which the Bobnet agent is positioned this turn

    var queue: PointSearch[] = [{id:SI,origin: 0}]
    var visited: number[]  = []
    while (graph[queue[0].id].exit == undefined) {
        graph[queue[0].id].links.forEach(element => {
            if (!(visited.includes(element))) {
                queue.push({id: element, origin: queue[0].id})
                visited.push(element)
            }
        });
        queue.shift()
    }
    console.log(queue[0].id + " " + queue[0].origin)
}