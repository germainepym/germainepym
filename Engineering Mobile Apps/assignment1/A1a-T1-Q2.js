"use strict";
/*
Write some code to do the following:

Write a function checkMarkValid that will take a parameter, mark.

Your function should return a boolean depending on if the mark entered is valid.
The range of valid marks are 0 - 100 (inclusive, only whole numbers).

Write some code to implement your function using the following array to test your function:
let marks = [12,45,67,900,"dog",-1,true];

Psuedocode:
    1. create function
    2. create a loop to loop through the list
    3. create an if statement to check conditions
            - if date type - number
            - if the data type is in between 0 - 100
    4. print true or false according to the data
*/

let marks = [12,45,67,900,"dog",-1,true];

function checkMarkValid(marks)
{
    for(let i = 0; i<= (marks.length-1); i++)
    {
        if (typeof(marks[i]) == "number" && marks[i] >= 0 && marks[i] <= 100)
            {
                console.log(marks[i] + ": true ");
            }
        
        else
            {
                console.log(marks[i] + ": false" );
            }   
        
    }
}

checkMarkValid(marks)