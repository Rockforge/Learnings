class Base {
    k = 4;
}

class Derived extends Base {

    constructor() {
        // super() must be called before accessing parent variables
        super();
        console.log(this.k);
    }
}

let derived = new Derived();

