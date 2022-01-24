// type Person = {
//     age: number,
//     name: string,
//     alive: boolean
// };

// Get the data type of the age property in type Person
type Age = Person['age'];

const myArray = [
    {name: 'Alice', age: 15},
    {name: 'Bob', age: 23},
    {name: 'Eve', age: 38}
];

type Person = typeof myArray[number];


function showAge(n: Age) {
    console.log(n);
}

let chansters: Person = {
    age: 23,
    name: 'Christian'
    //alive: true
};

console.log(typeof myArray[0]['name'])
showAge(chansters.age);
