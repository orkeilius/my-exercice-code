interface Point {
    links: number[];
    exit: boolean;
    origin: number;
    heat: number;
};

interface link {
    //used only for bestLink
    heat: number;
    start: number;
    end: number;
};

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
    });
};

//get link
for (let i = 0; i < nbLink; i++) {
    var inputs: number[] = readline().split(' ').map(x => parseInt(x));
    graph[inputs[0]].links.push(inputs[1]);
    graph[inputs[1]].links.push(inputs[0]);
};

//Add gateways
for (let i = 0; i < nbExit; i++) {
    var e = parseInt(readline());
    graph[e].exit = true; // the index of a gateway node
};

// heat = heat of the previous node - 1 (because further) + exit node link to it
//the the node with the most heat will have a link cut

// game loop
while (true) {
    const SI: number = parseInt(readline()); // The index of the node on which the Botnet agent is positioned this turn
    var bestLink: link = { heat: -9999, start: 0, end: 0 };
    var queue: number[] = [SI];
    var visited: number[] = [];
    while (queue.length != 0) {
        var actualNode: number = queue.shift()!;
        graph[actualNode].heat = graph[graph[actualNode].origin].heat - 1;
        
        graph[actualNode].links.forEach(element => {
            if (!(visited.includes(element))) {
                // exit node
                if (graph[element].exit) {
                    graph[actualNode].heat++;

                    if (bestLink.heat < graph[actualNode].heat) {
                        bestLink = { heat: graph[actualNode].heat, start: actualNode, end: element };
                    }
                }
                //normal node
                else {
                    graph[element].origin = actualNode;
                    queue.push(element);
                    visited.push(element);
                };
            };
        });
    };
    console.log(bestLink.start + " " + bestLink.end)

    //delete cut nodes
    graph[bestLink.start].links.splice(graph[bestLink.start].links.indexOf(bestLink.end), 1);
    graph[bestLink.end].links.splice(graph[bestLink.end].links.indexOf(bestLink.start), 1);
}


//! dummy fonction for vscode do not copy
function readline() {return ""};