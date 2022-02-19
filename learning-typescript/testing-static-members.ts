class MyClass {
    static x = 0;
    static print() {
        console.log(MyClass.x);
    }
}


MyClass.print();


class Base {
    static getGreeting() {
        return 'Hello, world';
    }
}

class Derived extends Base {
    myGreeting = Derived.getGreeting();
}

let d = new Derived();
console.log(d.myGreeting);

