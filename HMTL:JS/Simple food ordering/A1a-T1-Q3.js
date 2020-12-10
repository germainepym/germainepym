"use strict";
/*

Write some code to do the following:

Write a function movingAverage that takes an array of numbers as its parameter, data. 
This function calculates the cumulative moving average (CMA), which is the average of all the data up to the last available data point. 
ßour function needs to return the cumulative moving average value.

You should use the following variables to test your function.
let dataArray = [515, 523, 512, 504, 564, 535, 526, 596, 577, 508, 530, 578];
let dataArray1 = [515, 523, 512, 504, 564, 535, 526, 596, 577, 508, 530, 578, 594, 538, 521, 599];
let dataArray2 = [515, 523, 512, 504, 564, 535, 526, 596, 577, 508, 530, 578, 594, 538, 521, 599, 561, 585, 584, 550, 567];

Pseudocode:
1. define function 
2. create a for loop to loop through the array
3. add each and every data in the array and then divide it by the size of the array 
4. return the average 


*/

function movingAverage(data)
{
    let average = 0;
    for(let i = 0; i <= (data.length-1); i++)
    {
        average = average + data[i];
    }

    average = average/data.length;

    return average;

}


let dataArray = [515, 523, 512, 504, 564, 535, 526, 596, 577, 508, 530, 578];
let dataArray1 = [515, 523, 512, 504, 564, 535, 526, 596, 577, 508, 530, 578, 594, 538, 521, 599];
let dataArray2 = [515, 523, 512, 504, 564, 535, 526, 596, 577, 508, 530, 578, 594, 538, 521, 599, 561, 585, 584, 550, 567];

console.log(movingAverage(dataArray2))