let isOp;
let current;
let sqrt_num = '';
let isSqrt = false;
let first = false;


const calculator = document.querySelector('#result')
const evaluate_screen = document.querySelector("#evaluate")

const screen = (input) => {
    if (!isOp) {
        if(input === "√"){
            isSqrt = true;
        }
        else if(isSqrt){
            sqrt_num += input
        }
        else{
            current += input
        }
        if (calculator.value === "0") {
            calculator.value = input
        } else {
            calculator.value += input
        }
    }
}

const numbers = document.querySelectorAll(".num");
numbers.forEach((number,) => {
    number.addEventListener("click", (event) => {
        isOp = false;
        screen(event.target.value)
        first = true;
    });
});

const operations = document.querySelectorAll(".opp");
operations.forEach((operation) => {
    operation.addEventListener("click", (event) => {
        if (first) {
            if (isSqrt){
                console.log(float(sqrt_num))
                current += Math.sqrt(float(sqrt_num))
                isSqrt = false
            }
            screen(event.target.value)
            isOp = true;
        }
    })
});

const square = document.querySelector(".sqrt");
square.addEventListener("click", (event) => {
    console.log(event)
    isOp=false
    if(!isSqrt){
        screen(event.target.value)}
});


const result = document.querySelector(".give-answer");
result.addEventListener("click", () => {
    console.log(calculator.value)
    if (isSqrt){
        console.log(float(sqrt_num))
        current += Math.sqrt(float(sqrt_num))
        isSqrt = false
    }
    $.ajax({
        url: '/process',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(current),
        success: function(response){
            evaluate_screen.value = calculator.value;
            calculator.value = response;
            current = response;
    }});

});

const delete_button = document.querySelector(".delete-button");
delete_button.addEventListener("click", () => {
    calculator.value = calculator.value.slice(0, -1);
    current = current.slice(0, -1);
    isOp = Array.from(operations).some(op => op.textContent === calculator.value.slice(-1));
})

function resetCalculator() {
    calculator.value = "0";
    evaluate_screen.value = "";
    current = "";
    isOp = false;
    first = false;
}

window.onload = resetCalculator;
