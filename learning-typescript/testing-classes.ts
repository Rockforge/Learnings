class Point {
    // If --strictPropertyIntialization is set
    // Then you must assign these values to a constructor
    // or you can append ! after the variable name
    // x!: number;
    // y!: number;

    x: number;
    y?: number;
    s: string;
    xs: any;

    constructor(s: string);
    constructor(x: number, y: number);
    constructor(xs: any, y?: any) {
        // Notice that this third constructor overload
        // should cater to all available overloaded constructors
        this.xs = xs;
        //this.y = y;
    }

}


class Greeter {
    readonly name: string = 'hello';

    constructor(otherName?: string) {
        if (otherName !== undefined) {
            this.name = otherName;
        }
    }

    err() {
        this.name = 'not ok';
    }
}
