var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var Base = /** @class */ (function () {
    function Base() {
        this.k = 4;
    }
    return Base;
}());
var Derived = /** @class */ (function (_super) {
    __extends(Derived, _super);
    function Derived() {
        var _this = 
        // super() must be called before accessing parent variables
        _super.call(this) || this;
        console.log(_this.k);
        return _this;
    }
    return Derived;
}(Base));
var derived = new Derived();
