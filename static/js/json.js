var i = [];  // var --> variable
var str = "string";

console.log(str, i);  // print()


var lst = [
    {
        "name": "John",
        "age": "20",
        "height": "50",
    },
    {
        "name": "Bob",
        "age": "20",
        "height": "80",
    },
    {
        "name": "Smith",
        "age": "25",
        "height": "50",
    }
];

console.log(lst);

function tellName(name){  // def tellName(name)
    console.log(name);
};

tellName("John");

var printName = (name) => {
    console.log(name)
};

printName("smith");
