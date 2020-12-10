/** 
 * shared.js 
 * Purpose: This file contains shared code that runs on both view.html and index.html
 * Author: Germaine Pok
 * Last Modified: 10 October 2020
 */

"use strict";
// Constants used as KEYS for LocalStorage
const LOCKER_INDEX_KEY = "selectedLockerIndex";
const LOCKER_DATA_KEY = "lockerLocalData";
// TODO: Write code to implement the Locker class
class Locker{

    constructor(id)
    {
        this._id = id;
        this._label = "";
        this._locked = false;
        this._pin = "";
        this._color = this.randomColor()
        this._contents = "";
        this._locnum = "";
    }

    get id()
    {
        return this._id;
    }

    get label()
    {
        return this._label;
    }

    get locked()
    {

        return this._locked;
    }

    get pin()
    {
        return this._pin;
    }

    get color()
    {
        return this._color;
    }

    get contents()
    {
        return this._contents;
    }

    set label(text)
    {
        this._label = text;
    }

    set locked(state)
    {
        this._locked = state;
    }

    set pin(pin)
    {
        this._pin = pin;
    }

    set color(color)
    {
        this._color = color;
    }

    set contents(text)
    {
        this._contents = text;
    }

    randomColor()
    //generate random colour for the locker
    {
        let hex = Math.floor(Math.random() * 0xFFFFFF);
        return ("000000" + hex.toString(16)).substr(-6);
    }

    fromData(data)
    {
        this._id = data._id;
        this._label = data._label;
        this._locked = data._locked;
        this._pin = data._pin;
        this._color = data._color;
        this._contents = data._contents;
        this._locnum = data._locnum;
    }
}
 
// TODO: Write code to implement the LockerList class

class LockerList{

    constructor()
    {
        this._lockers = []
    }

    get lockers()
    {
        return this._lockers;
    }

    get count()
    {
        return length.this._lockers;
    }

    addLocker(id)
    // add new locker
    {
        this._lockers.push(new Locker(id))
    }

    getLocker(index)
    // return the details of the locker according to index
    {
        return this._lockers[index]
    }

    removeLocker(id)
    // remove the locker
    {
        for (let i=0; i<=this.lockers.length-1;i++)
        {
            if (this._lockers[i].id == id)
            {
                this.lockers.splice(i,1)
            }
        } 
    }

    fromData(data)
    {
		for(let i = 0; i < data._lockers.length; i++)
		{
			let locker = new Locker();
			// the data for this locker is data[i]
			locker.fromData(data._lockers[i]);
			// using array push method to add to array
			this._lockers.push(locker);
		}
    }
    
}



// TODO: Write the function checkIfDataExistsLocalStorage
function checkIfDataExistsLocalStorage()
// check if local storage exists
{
    if (typeof(Storage) !== "undefined") // check if local storage exists 
    {
        let jsonString = localStorage.getItem(LOCKER_DATA_KEY);
        if (typeof(jsonString) ==! "undefined" || jsonString ==! "" || jsonString ==! null )
        {    
            return false
        }
        else
        {
            return true
        }
    }
}


// TODO: Write the function updateLocalStorage
function updateLocalStorage(data)
// update value in local storage
{
    localStorage.setItem(LOCKER_DATA_KEY, JSON.stringify(data)) ;

}

// TODO: Write the function getDataLocalStorage
function getDataLocalStorage()
// return the value stored in the local storage
{
    let update = JSON.parse(localStorage.getItem(LOCKER_DATA_KEY))
    return update 
}

// Global LockerList instance variable
let lockers = new LockerList();

// TODO: Write the code that will run on page load here
let data = checkIfDataExistsLocalStorage();
if (data == true)
{
    let restore = getDataLocalStorage();
    lockers.fromData(restore);
}
else
{
    lockers.addLocker("A001");
    updateLocalStorage(lockers)

}
