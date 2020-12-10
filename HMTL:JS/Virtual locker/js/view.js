/** 
 * view.js 
 * Purpose: This file contains code that runs on load for view.html
 * Author: Germaine Pok
 * Last Modified: 10 October 2020
 */


"use strict";
// TODO: Write the function displayLockerInfo
function displayLockerInfo(locker)
/*This function displayes the information contained in the Locker 
eg. Locker ID, Label of Locker, Color of Locker and the Locker Content
*/
{
    let idRef = document.getElementById("lockerId");
    let labelRef = document.getElementById("lockerLabel");
    let colorRef = document.getElementById("lockerColor")
    let contentRef = document.getElementById("lockerContents");

    // display ID
    idRef.innerHTML = locker.id;

    // display contents
    if (locker.contents != "") 
    {
        contentRef.value = locker.contents;
    }
    // display Label
    if (locker.label != "") 
    {
        labelRef.value = locker.label;
    }
    // display Color
    if (locker.color == "FFFFFF")
    {
        colorRef.value = "3399ff";
    }
    else {
        colorRef.value = locker.color;
    }

    document.getElementById("deleteLocker").addEventListener("click", deleteThisLocker);
}


// TODO: Write the function unlock
function unlock(locker)
// This function allows the user to enter a pin and unlock the locker
{
    // Enter pin
    let pin = prompt("ENTER PIN");

    // Unlock locker if pin matches, else redirect back to index.html
	if ( pin == locker.pin )
	{
		locker.locked = false;
		locker.pin = "";
		displayLockerInfo(locker);
	}
	else
	{
        alert("Wrong pin, please enter pin again")
		window.location = "index.html";
	}
}

// TODO: Write the function deleteThisLocker
function deleteThisLocker()
// This function allows the user delete the locker 
{
    
    // Confirm with the user
    if (confirm("Are you very sure?"))
    {
    // Call lockerList to remove locker
    lockers.removeLocker(locker.id);
    // Updating Local Storage
    updateLocalStorage(lockers);
    // Inform user that selected locker is deleted
    alert("Deleted Locker");
    // redirecting to main page
    window.location = "index.html";
    }

}

// TODO: Write the function lockLocker
function lockLocker()
// This function allows the user to delete the locker
{
    // Confirm with the user
    if (confirm("Lock Locker?"))
    {       
        let pin1 = prompt("PLEASE ENTER PIN");
        let pin2 = prompt("PLEASE ENTER PIN AGAIN");
    
    // Validating Pin
        if ( pin1 == pin2 )
        {
            // Update locker data
            let label = document.getElementById("lockerLabel").value;
            let color = document.getElementById("lockerColor").value;
            let contents = document.getElementById("lockerContents").value;
            lockers.lockers[index].pin = pin1;
            lockers.lockers[index].locked = true;
            lockers.lockers[index].label = label;
            lockers.lockers[index].color = color;
            lockers.lockers[index].contents = contents;
            // Updating Local Storage
            updateLocalStorage(lockers);
            // Inform user that locker is now locked
            alert("Locked Locker");
            // redirecting back to main page
            window.location = "index.html";
        }
        else
        {
        // Error if pin doesn't match
        alert("ERROR! PIN DOESN'T MATCH");
        }
    }
}

// TODO: Write the function closeLocker
function closeLocker()
// This function allows user to close the locker without locking 
{
    // Confirm with the user
    if (confirm("Close Locker without locking?"))
    {       
        // Update locker data
        let label = document.getElementById("lockerLabel").value;
        let color = document.getElementById("lockerColor").value;
        let contents = document.getElementById("lockerContents").value;
        lockers.lockers[index].locked = false;
        lockers.lockers[index].label = label;
        lockers.lockers[index].color = color;
        lockers.lockers[index].contents = contents;
        // Updating Local Storage
        updateLocalStorage(lockers);
        // Inform user that locker is now locked
        alert("Closing locker without locking");
        // redirecting back to main page
        window.location = "index.html";
    }
}


// Retrieve the stored index from local storage
let index = localStorage.getItem(LOCKER_INDEX_KEY);
// using the getLocker method, retrieve the current Locker instance
let locker = lockers.getLocker(index);

// TODO: Write the code that will run on page load here
if (locker.locked == true )
{
	unlock(locker);
}
else
{
	displayLockerInfo(locker);
}
