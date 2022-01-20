function greeter(fn: (s: string) => void) {
    fn('Hello world')
}

function printToConsole(s: string) {
    console.log(s)
}

greeter(printToConsole)
