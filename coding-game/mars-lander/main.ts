//! dummy fonction for vscode do not copy
function readline() {
  return ''
}

const CURVE_PRECISION = 10000 // presision of the curve hitbox
interface Curve {
  start: number[]
  end: number[]
  point1: number[]
}

const N: number = parseInt(readline()) // the number of points used to draw the surface of Mars.
var land: number[] = []
for (let i = 0; i < N; i++) {
  land.push(parseInt(readline().split(' ')[1]))
}

function lerp(start: number[], end: number[], interpolate: number) {
  // return a interpolate value between to point
  return [
    start[0] + (start[0] - end[0]) * interpolate,
    start[1] + (start[1] - end[1]) * interpolate,
  ]
}
function getCurvePoint(curve: Curve, interpolate: number): number[]{
  // return a point of a curve
  return lerp(
    lerp(curve.start, curve.point1, interpolate),
    lerp(curve.point1, curve.end, interpolate),
    interpolate,
  )
}
function hitboxCurve(curve: Curve) {
  // find where the curve will collide with the terrain

  for (let index = 0; index < CURVE_PRECISION; index++) {
    var pos: number[] = getCurvePoint(curve, index / CURVE_PRECISION)
    if (pos[1] <= land[pos[0]] && pos[0] != curve.end[0]) {
      return [pos[0], land[pos[0]]]
    }
  }
  return curve.end
}
function getDistance(point1:number[], point2:number[]) {
  return Math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1]))
}
function distanceFromCurve(curve: Curve, point: number[]) {
  //return the distance from a curve
  var best: number[] = [ 9999, 0];
  var i = 0;
  while (i != CURVE_PRECISION) {
    distance = getDistance(point, getCurvePoint(curve, i / CURVE_PRECISION);
    if (distance <= best[0]){
      best = [distance, i]
    }
    i += 1;
  }

  return best
}

function findTarget(land, xPos): number[] {
  // find place to land
  var flat: boolean = false
  for (let i = 1; i < N; i++) {
    if (land[i] == land[i - 1] && !flat) {
      if (i >= xPos) {
        return [i, land[i]]
      }
      flat = true
    } else if (land[i] != land[i - 1] && flat) {
      if (i <= xPos) {
        return [i, land[i]]
      } else {
        return [xPos, land[xPos]]
      }
    }
  }
  return [0, 0]
}

var inputs: string[] = readline().split(' ')
const X: number = parseInt(inputs[0])
const Y: number = parseInt(inputs[1])
const target: number[] = findTarget(land, X)
var start = true

var targetCurve: Curve = {
  start: [X, Y],
  end: target,
  point1: lerp([X, Y], target, 0.5),
}
while (hitboxCurve(targetCurve) != target) {
  targetCurve.point1[1]++
}
console.error(targetCurve, hitboxCurve(targetCurve), target)

// game loop
while (true) {
  if (!start) {
    var inputs: string[] = readline().split(' ')
    const X: number = parseInt(inputs[0])
    const Y: number = parseInt(inputs[1])
  } else {
    start = false
  }
  const HS: number = parseInt(inputs[2]) // the horizontal speed (in m/s), can be negative.
  const VS: number = parseInt(inputs[3]) // the vertical speed (in m/s), can be negative.
  const F: number = parseInt(inputs[4]) // the quantity of remaining fuel in liters.
  const R: number = parseInt(inputs[5]) // the rotation angle in degrees (-90 to 90).
  const P: number = parseInt(inputs[6]) // the thrust power (0 to 4).

  // Write an action using console.log()

  var bestDistance: number = 999999999;
  // power
  for (let power = 0; power <= 4; power++) {
    // angle
    for (let angle = -15; angle <= 15; angle ++) {
      var newX: number = power / Math.sin(angle + R)
      var newY: number = power / Math.sin(angle + R)
      var distance = getDistance()
      if bestDistance < distance:
    }
  }
}
