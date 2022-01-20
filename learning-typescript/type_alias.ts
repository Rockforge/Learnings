type Point = {
    x: number,
    y: number
};

function printCoord(pt: Point) {
    console.log(pt.x);
    console.log(pt.y);
}

printCoord({x: 12, y: 23})
