//! dummy fonction for vscode do not copy
function readline() {
    return ""
};

//ia setting
const DISTANCEBOOST: number = 8000 // distance from next checkpoint to enable boost


function getDistance(x1:number, y1:number, x2:number, y2:number) {
    return Math.sqrt((x1-x2)**2 + (y1-y2))
}


var boost = true
while (true) {
    var inputs: string[] = readline().split(' ');
    const x: number = parseInt(inputs[0]);
    const y: number = parseInt(inputs[1]);
    const nextCheckpointX: number = parseInt(inputs[2]); // x position of the next check point
    const nextCheckpointY: number = parseInt(inputs[3]); // y position of the next check point
    const nextCheckpointDist: number = parseInt(inputs[4]); // distance to the next checkpoint
    const nextCheckpointAngle: number = parseInt(inputs[5]); // angle between your pod orientation and the direction of the next checkpoint
    var inputs: string[] = readline().split(' ');
    const opponentX: number = parseInt(inputs[0]);
    const opponentY: number = parseInt(inputs[1]);
    var thrust: any = 0

    if ((-90 < nextCheckpointAngle) && (nextCheckpointAngle < 90)){
        thrust = 100
        if (getDistance(x, y, nextCheckpointX, nextCheckpointY) <= DISTANCEBOOST) {
            thrust = "BOOST"
        }
    }
    console.log(nextCheckpointX + ' ' + nextCheckpointY + ' ' + thrust);
}