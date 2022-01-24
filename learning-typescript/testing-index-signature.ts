interface StringArray {
    [index: number]: string;
}

const myArray: StringArray = ['hello', 'world'];
const secondItem = myArray[1];
console.log(secondItem);
