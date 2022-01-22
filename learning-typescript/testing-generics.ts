type Pointeru  = {x: number, y: number};
type P = keyof Pointeru

function testingru(test: P) {
    console.log(test);
}


function identity<T>(arg: T): T {
    return arg;
}

let output = identity<string>('Hello world');

