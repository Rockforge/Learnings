var Point = /** @class */ (function () {
    function Point() {
    }
    return Point;
}());
var Greeter = /** @class */ (function () {
    function Greeter(otherName) {
        this.name = 'hello';
        if (otherName !== undefined) {
            this.name = otherName;
        }
    }
    Greeter.prototype.err = function () {
        this.name = 'not ok';
    };
    return Greeter;
}());
