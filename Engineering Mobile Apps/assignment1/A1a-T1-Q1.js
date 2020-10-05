"use strict";
/*
Write some code to do the following:

1. Write a function fahrenheitToCelsius that will take a parameter, fahrenheit and return the converted value in celsius.

2. You should ensure that you round the returned value to three decimal places

Pseudocode:
    1. Define function
    2. convert fahrenheit to celsius using formula
    3. round celsius to 3 decimal point
    4. return celsius
*/


function fahrenheitToCelsius(fahrenheit)
{
    let celsius = (fahrenheit - 32) * 5/9

    celsius = celsius.toFixed(3);

    return celsius
}

console.log(fahrenheitToCelsius(32))