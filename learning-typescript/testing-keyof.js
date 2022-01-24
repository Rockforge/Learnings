const users = [
    {
        name: "Chad",
        age: 31,
        location: "Japan"
    },
    {
        name: "Bob",
        age: 29,
        location: "USA"
    },
    {
        name: "Jane",
        age: 30,
        location: "France"
    }
];
function getData(dataList, dataType) {
    return dataList.map((data) => data[dataType]);
}
// Now, getData can fetch the specific properties of a dataList
// Making it generic
console.log(getData(users, 'name'));
console.log(getData(users, 'age'));
console.log(getData(users, 'location'));
