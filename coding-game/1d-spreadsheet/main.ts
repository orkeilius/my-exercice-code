
interface Cell{
    operation: string;
    value: any[];
    result?: number;
}

function calc(cell : Cell) {
    if (cell.result != undefined) {
        return cell.result      
    }

    /* transform string and ref into number value */
    for (let i = 0; i < 2; i++) {
        if (cell.value[i].startsWith("$")) {
            cell.value[i] = calc(grid[cell.value[i].substring(1)]);
        }
        else if (cell.value[i] != '_'){
            cell.value[i] = parseInt(cell.value[i])
        }
    }
    
    switch (cell.operation) {
        case "VALUE":
            cell.result = cell.value[0];
            break;
        case "ADD":
            cell.result = cell.value[0] + cell.value[1];
            break;
        case "SUB":
            cell.result = cell.value[0] - cell.value[1];
            break;
        case "MULT":
            cell.result = cell.value[0] * cell.value[1];
            break;

    }
    return(cell.result);
}

const N: number = parseInt(readline());
var grid: Cell[] = [];

for (let i = 0; i < N; i++) {
    var x: string[] = readline().split(' ')
    grid.push({operation: x[0],value: [x[1],x[2]]});
}

grid.forEach(element => {
    calc(element)
    console.log(element.result + 0 ); /* remove -0 value */
});
