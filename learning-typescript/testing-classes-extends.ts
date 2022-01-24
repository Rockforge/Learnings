class Animal {
    move() {
        console.log('Moving along');
    }
}

class Dog extends Animal {
    woof(times: number) {
        for (let x = 0; x < times; x++) {
            console.log('woof');
        }
    }
}

let d = new Dog()
d.move();
d.woof(3);

// Overriding methods
class Base {
    greet() {
        console.log('Hello World');
    }
}

class Derived extends Base {
    greet(name?: string) {
        if(name) {
            console.log(`Hello, ${name.toUpperCase()}`);
        } else {
            super.greet();
        }
    }
}

let derived = new Derived();
derived.greet();
derived.greet('Chansters')

