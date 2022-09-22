//dummy fonction for vscode do not copy
function readline() {
    return ""
}


interface Point {
    links: number[];
    exit: boolean;
    origin: number;
    heat: number;
}

var inputs: number[] = readline().split(' ').map(x => parseInt(x));
const nbNode: number = inputs[0]; // the total number of nodes in the level, including the gateways
const nbLink: number = inputs[1]; // the number of links
const nbExit: number = inputs[2]; // the number of exit gateways

//get point
var graph: Point[] = []
for (let i = 0; i < nbNode; i++) {
    graph.push({
        links: [],
        exit: false,
        origin: 0,
        heat: 0
    })
}

//get link
for (let i = 0; i < nbLink; i++) {
    var inputs: number[] = readline().split(' ').map(x => parseInt(x));
    graph[inputs[0]].links.push(inputs[1])
    graph[inputs[1]].links.push(inputs[0])
}

//Add gateways
for (let i = 0; i < nbExit; i++) {
    var e = parseInt(readline())
    graph[e].exit = true; // the index of a gateway node
}

// game loop
while (true) {
    const SI: number = parseInt(readline()); // The index of the node on which the Bobnet agent is positioned this turn
    var bestLink: number[] = [-1000, 0, 0];
    var queue: number[] = [SI]
    var visited: number[] = []
    while (queue.length != 0) {
        graph[queue[0]].heat = graph[graph[queue[0]].origin].heat - 1;
        graph[queue[0]].links.forEach(element => {
            if (!(visited.includes(element))) {
                if (graph[element].exit) {
                    graph[queue[0]].heat++;

                    if (bestLink[0] < graph[queue[0]].heat) {
                        bestLink = [graph[queue[0]].heat, queue[0], element]
                    }
                }
                else {
                    graph[element].origin = queue[0];
                    queue.push(element);
                    visited.push(element);
                }
            }
            
        });


        queue.shift()
    }
    console.log(bestLink[1] + " " + bestLink[2])
    console.error(graph)

    //delete cut nodes
    graph[bestLink[1]].links.splice(graph[bestLink[1]].links.indexOf(bestLink[2]), 1)
    graph[bestLink[2]].links.splice(graph[bestLink[1]].links.indexOf(bestLink[1]), 1)
}
