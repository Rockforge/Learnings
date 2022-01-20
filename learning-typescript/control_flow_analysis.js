function example() {
    let x;
    x = Math.random() < 0.5;
    console.log(x);
    if (Math.random() < 0.5) {
        x = 'string';
        console.log(x);
    }
    else {
        x = 100;
        console.log(x);
    }
    console.log(x);
}
example();
