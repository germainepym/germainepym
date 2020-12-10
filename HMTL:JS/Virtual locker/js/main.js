/** 
 * main.js 
 * Purpose: This file contains code that runs on load for index.html
 * Author: Germaine Pok
 * Last Modified: 10 October 2020
 */
"use strict";

// TODO: Write the function displayLockers
function displayLockers(data)
// This function displays the lockers in index.html
{
    let output = "";
    let textColor = "";
    //for each locker
    for(let i = 0; i<data._lockers.length; i++)
    {
        // obtain the colour of the lcoker
        let hexBack = data._lockers[i]._color
        
        let r = hexBack.substr(0, 2);
        let g = hexBack.substr(2, 2);
        let b = hexBack.substr(4);

        r = parseInt(r,16)
        g = parseInt(g,16)
        b = parseInt(b,16)

        let brightness  =  Math.sqrt(0.299*Math.pow(r,2)  + 0.587*Math.pow(g,2) + 0.114*Math.pow(b,2))

        //if the brighness of the colour is less than 128, then color of text is white, else black
        if (brightness <128)
        {
            textColor = "white"
        }
        else
        {
            textColor = "black"
        }

        //producing locker in html.code
        output += "<div class=\"mdl-cell mdl-cell--4-col\">";
        output += "<div class=\"mdl-card mdl-shadow--2dp locker\"";
        output += "style=\"background-color:#"+data._lockers[i]._color+"\">";
        output += "<div class =\"mdl-card__actions mdl-card--action\">"
        output += "<div class=\"mdl-layout-spacer\"></div>";
        output += "<button class=\"mdl-button mdl-js-button mdl-button--fab mdl-button--mini-fab mdl-color-text--"+textColor+"\" onmousedown=mouseDown("+i+") id=\"deleteLocker"+i+"\"><i class=\"material-icons\">delete_forever</i></button></div>" ;
        output += "<div class=\"mdl-card__title mdl-card--expand mdl-color-text--"+textColor+"\">";
		output += "<h2>"+data._lockers[i]._id+"</h2>";
		output += "<h4>&nbsp;"+data._lockers[i]._label+"</h4></div>";
		output +=  "<div class=\"mdl-card__actions mdl-card--border mdl-color-text--"+textColor+"\">";
        output += "<a class=\"mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect mdl-color-text--"+textColor+"\" onclick=\"view("+i+")\">Open Locker</a>";
		output += "<div class=\"mdl-layout-spacer\"></div>";
        output += "<i class=\"material-icons\">";

        if (data._lockers[i]._locked == true) 
        {
            output += "unlock";
        }
        else 
        {
            output += "lock_open";
        }
        
        output += "</i></div></div></div>";
    }

    //display locker
    let outputref = document.getElementById("lockerDisplay");
    outputref.innerHTML = output;
}

// TODO: Write the function addNewLocker
function addNewLocker()
// add a new locker 
{   
    // if length of locker is 0, then locker id is A001
    if (lockers._lockers.length == 0)
    {
        lockers.addLocker("A001")
    }
    // add locker according the previous ID added
    else
    { 
        let prev = lockers._lockers[lockers._lockers.length-1]._id.slice(-3)
        prev = Number(prev) + 1
        if(prev < 10)
        {
            lockers.addLocker(`A00${prev}`)
        }
        else if (prev < 100)
        {
            lockers.addLocker(`A0${prev}`)
        }
        else
        {
            lockers.addLocker(`A${prev}`)
        }
        
    }
    
    updateLocalStorage(lockers);
    displayLockers(lockers);
} 

function deleteThisLocker()
// delete a locker 
{
    
    // Confirm with the user
        if (confirm("Are you very sure?"))
        {
        // Call lockerList to remove locker
        lockers.removeLocker(lockers.lockers[index].id);
        // Updating Local Storage
        updateLocalStorage(lockers);
        // Inform user that selected locker is deleted
        alert("Deleted Locker");
        // redirecting to main page
        window.location = "index.html";
        }
    
}

// TODO: Write the function view
function view(index)
// bring users to view.html
{
	let stringedIndex = JSON.stringify(index);
	localStorage.setItem(LOCKER_INDEX_KEY, stringedIndex);

	// Directing page
	window.location = "view.html";
}

let index = localStorage.getItem(LOCKER_INDEX_KEY);

function mouseDown(i)
// on mousedown, call deleteThisLocker function and delete the lcoker
{
    let deletedIndex = JSON.stringify(i);
    localStorage.setItem(LOCKER_INDEX_KEY, deletedIndex);
    index = localStorage.getItem(LOCKER_INDEX_KEY);
    document.getElementById("deleteLocker"+index).addEventListener('click', deleteThisLocker);

}

// TODO: Write the code that will run on load here
displayLockers(lockers);

