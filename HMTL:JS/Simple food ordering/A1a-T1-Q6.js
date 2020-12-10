
"use strict";
/*
Write some code to do the following:

Write a function searchInternationalStudents that takes a parameter, dataArray.

You can expect dataArray to contain an array of objects (such as the one below). The function should search the provided array for international students using the nationality property of the object and count the number of students that meet the criteria, then return the total count of international students.

You can use the students array below, and call your function then print the result to the console. You can assume that any nationality that isn't "Australian" is an international student.

Psuedocode:
1. define function
2. initialise a count variable to count the number of international student
3. create a for loop to loop thorugh the array of objects
        - if the nationality is not "Australian", then increment count by 1
4. return count
*/

function searchInternationalStudents(dataArray)
{
    let count = 0

    for (let i = 0; i <= (dataArray.length -1) ; i++)
    {
        if (dataArray[i].nationality != "Australian")
        {
            count++
        }
    }
    return count
}


let students=[
	{
		id:28976577,
		unit:["ENG1003"],
		nationality:"Australian"
	},
	{
		id:28958234,
		unit:["ENG1003"],
		nationality:"Australian"
	},
	{
		id:36788927,
		unit:["ENG1003"],
		nationality:"Australian"
	},
	{
		id:23978904,
		unit:["ENG1003"],
		nationality:"Australian"
	},
	{
		id:28976589,
		unit:["ENG1003"],
		nationality:"American"
	},
	{
		id:28951284,
		unit:["ENG1003"],
		nationality:"Indian"
	},
	{
		id:36789027,
		unit:["ENG1003"],
		nationality:"Australian"
	},
	{
		id:22345604,
		unit:["ENG1003"],
		nationality:"Sri Lankan"
	}
];

console.log(searchInternationalStudents(students))