"use strict";


function submitOrder()
{
    //initialisation
    let totalCost = 0;
    let nameRef = document.getElementById("nameCustomer");
    let mobileRef = document.getElementById("mobileCustomer")
    
    // name
    let nameCustomer = nameRef.value;
    if(nameCustomer == ""|| isNaN(Number(nameCustomer)) == false)
    {
        alert("Name is invalid")
    }

    //mobile number
    let mobileCustomer = mobileRef.value

    if (mobileCustomer == "" || isNaN(Number(mobileCustomer)) == true)
    {
        alert("Number is invalid")
    }

    //order no randomizer 
    let orderNo = Math.floor((Math.random() * 100) + 1);


    //burger meat
    let meatSelection = document.getElementsByName('meat');
    let meatChecked = false
    let selectedMeat="";
    for(let i=0; i<meatSelection.length; i++)
    {
        if(meatSelection[i].type=="radio" && meatSelection[i].checked==true)
        {
            meatChecked = true
            selectedMeat+=meatSelection[i].value;
            if(selectedMeat == "Chicken")
            {
                totalCost += 2
            }
            else if(selectedMeat == "Beef" || selectedMeat == "Pork")
            {
                totalCost += 3
            }
        }
    }


    if (meatChecked == false)
    {
        alert("Please select meat")
    }

    
    // cheese (all cheese $1)
    let cheeseSelection = document.getElementsByName("cheese");
    let selectedCheese="";
    for(let i=0; i<cheeseSelection.length; i++)
    {
        if(cheeseSelection[i].type=="checkbox" && cheeseSelection[i].checked==true)
        {
            
            selectedCheese+=cheeseSelection[i].value + ', ';
            totalCost += 1
        }
    }

    // sauce (all sauce $0.5)
    let sauceSelection = document.getElementsByName("sauce");
    let selectedSauce="";
    for(let i=0; i<sauceSelection.length; i++)
    {
        if(sauceSelection[i].type=="checkbox" && sauceSelection[i].checked==true)
        {
            
            selectedSauce+=sauceSelection[i].value + ', ';
            totalCost += 0.5
        }
    }

    //vegetables (all vege $1)
    let vegetablesSelection = document.getElementsByName("vegetables");
    let selectedVegetables="";
    for(let i=0; i<vegetablesSelection.length; i++)
    {
        if(vegetablesSelection[i].type=="checkbox" && vegetablesSelection[i].checked==true)
        {
            
            selectedVegetables+=vegetablesSelection[i].value + ', ';
            totalCost += 1
        }
    }
    
    //slice the last 2 strings (which is ', ')
    selectedVegetables = selectedVegetables.slice(0, -2);

    // spicy (according to price)
    let spicyRef = document.getElementById("spicy");
    let selectedSpicy = spicyRef.value;

    if(selectedSpicy == "Mild")
    {
        totalCost += 0.5;
    }
    else if(selectedSpicy == "Medium")
    {
        totalCost += 0.75;
    }
    else if(selectedSpicy == "Extra")
    {
        totalCost += 1;
    }
 
    // beverage (all $2)
    let beverageRef = document.getElementById("beverage");
    let selectedBeverage = beverageRef.value;
    if(selectedBeverage == "Coke" || selectedBeverage == "Sprite" || selectedBeverage == "Mountain Dew" || selectedBeverage == "Bunderberg")
    {
        totalCost += 2;
    }
    else
    {
        selectedBeverage = "not available"
    }


    //output (resultArea)
    let output = "";
    output = `${nameCustomer}, your order number is ${orderNo} and the total cost is $${totalCost}. <br><br>`;
    if(meatSelection == "")
    {
        output += `Your ${selectedMeat} burger meat is not selected`; 
    }
    else
    {
        output += `Your ${selectedMeat} burger`; 
    }

    if(selectedCheese == "")
    {
        output += `${selectedCheese} does not have cheese,`; 
    }
    else
    {
        output += ` includes ${selectedCheese}`;
    }

    if(selectedSauce == "")
    {
        output += ` ${selectedSauce} does not have sauce,`;
    }
    else
    {
        output += `${selectedSauce}`
    }

    if(selectedVegetables == "")
    {
        output += ` ${selectedVegetables} does not have vegetables,`;
    }
    else
    {
        output += `${selectedVegetables}`
    }

    
    output += ` and is ${selectedSpicy} spicy. Your drink is ${selectedBeverage}. <br><br> Enjoy!`;
    
    if(nameCustomer == "" || mobileCustomer == ""|| isNaN(Number(nameCustomer)) == false || isNaN(Number(mobileCustomer)) == true || meatChecked == false)
    {
        output =""
    }
    
    let resultAreaRef = document.getElementById("resultArea");
    resultAreaRef.innerHTML = output;
}   
