type Predicate = (x: unknown) => boolean;
type K = ReturnType<Predicate>

function f() {
    return {x: 10, y: 3};
}

type fType = ReturnType<typeof f>;



function helloWorld(): fType {
    return {
        x: 23,
        y: 23
    }
}

console.log(helloWorld());
