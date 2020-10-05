"use strict";
/*

Write some code to do the following:

Write a function findPrimes that takes two parameters, min and max.

You need to calculate all prime numbers between the given min and max, then return them as an array of values.

You can use the following to test the function
console.log(findPrimes(20,150));

Psuedocode:
1. define function
2. initialise a prime array
3. create a for loop with min max as boundaries
4. create another for loop to execute calculations whether it is a prime number
            - if any number in between the min max is divisible by any other number that is not itself, it is not a prime number
5. push into the array if its a prime number
6. return array
*/


function findPrimes(min,max)
{
    
    let prime = []
    for(min; min <= max; min++)
    {   
        let end = false
        for(let x = 2; x < min; x++)
        {
            if(min % x === 0) // if it's 0 means that it is divisible by any other number that is not itself
            {
                end = true
            }
            
        }

        if (end == false)
            {
                prime.push(min);
            }
          
    }
    return prime
}

console.log(findPrimes(20,150));





