console.log('hello world');

function greet(person: string, date: Date) {
    console.log(`Hello ${person}, today is ${date.toDateString()}`);
}

greet('Chan', new Date())

const names = ['Alice', 'Bob', 'Jeff']

names.forEach((s) => {
    console.log(s.toUpperCase())
});
