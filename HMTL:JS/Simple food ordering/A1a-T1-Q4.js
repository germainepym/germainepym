"use strict";
/*

Write some code to do the following:

Write a function daySuffix that takes one parameter, day. This function takes a single number (day) and returns a string with the correct suffix attached to the day (i.e. 1st, 2nd, 3rd, 5th) appended.

Note that if the day is invalid, your function should return null (as a string).

You can use the code below to test if your function works correctly.

Psuedocode:
1. define function 
2. create an if else statement 
        - if the number ends in 1 except 11 = st
        - if the number ends in 2  except 12 = nd
        - if the number ends in 3 except 13 = rd
        - else all end in th 
        - else if its not a number within the boundary or not a number = null


*/

function daySuffix(day)
{
    if(day == 1 || day == 21 || day == 31)
    {
        return day + " : " + day + "st"

    }
    else if(day == 2 || day == 22)
    {
        return day + " : " + day + "nd"
    }
    else if(day == 3 || day == 23)
    {
        return day + " : " + day + "rd"
    }
    else if (day < 32 && day > 0)
    {
        return day + " : " + day + "th"
    }
    else
    {
        return day + " : " + null
    }

}


let output = "";
for (let i = 1; i <= 31; i++)
{
    output += daySuffix(i) + "\n";
}
output += daySuffix("dog") + "\n";
output += daySuffix(-1) + "\n";
output += daySuffix(100) + "\n";
output += daySuffix("d0g") + "\n";
console.log(output);