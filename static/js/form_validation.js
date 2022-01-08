// functions to add or remove classes and show and hyde validation errrors copied
// from my project portfolio 2 Change Fuel
// https://github.com/JoGorska/Keto-diet/blob/master/assets/js/calculator.js
/**
 * Function to add class
 * @param {*} className 
 * @param {*} targetNode 
 */
 function addClass(className, targetNode) {
    targetNode.classList.add(className);
  }
  
  /**
   * Function to remove class
   * @param {*} className 
   * @param {*} targetNode 
   */
  
  function removeClass(className, targetNode){
    targetNode.classList.remove(className);
  }
  
  /**
   * Function to set attribute
   * @param {*} className 
   * @param {*} targetNode 
   */
  
  function setAtribute(atributeName, atributeValue, targetNode) {
    targetNode.setAttribute(atributeName, atributeValue);
  }
  /**
   * Function to remove attribute
   * @param {*} atributeName 
   * @param {*} atributeValue 
   * @param {*} targetNode 
   */
  function removeAtribute(atributeName, atributeValue, targetNode) {
    targetNode.removeAttribute(atributeName, atributeValue);
  }
  
  /**
   * Function to display Error after validation has been failed
   * makes div with help message visible and in red, input's border is red and red icon with exclamation mark is displayed in input field
   * @param {*} targetNodeInput 
   * @param {*} targetNodeHelp 
   */
  
  function displayErrorValidation(targetNodeInput, targetNodeHelp) {
  
    addClass("is-invalid",targetNodeInput);
    removeClass("is-valid",targetNodeInput);
    setAtribute("aria-describedby", "name-help", targetNodeInput);
    removeClass("my-invisible", targetNodeHelp);
    addClass("invalid-feedback", targetNodeHelp);
    removeClass("valid-feedback", targetNodeHelp);
  
  }

  /**
   * Function to display Error after validation has been failed
   * makes div with help message visible and in red, input's border is red and red icon with exclamation mark is displayed in input field
   * @param {*} targetNodeInput 
   * @param {*} targetNodeHelp 
   */

   function displayPassedValidation(targetNodeInput, targetNodeHelp) {
  
    addClass("is-valid", targetNodeInput);
    removeClass("is-invalid", targetNodeInput);
    setAtribute("aria-describedby", "name-help", targetNodeInput);
    removeClass("my-invisible", targetNodeHelp);
    addClass("valid-feedback", targetNodeHelp);
    removeClass("invalid-feedback", targetNodeHelp);
  
  }
  
  /**
   * Function to remove display Error after validation has been passed
   * makes div with help message invisible, input border comes back to standard and icon with exclamation mark disapears
   * @param {*} targetNodeInput 
   * @param {*} targetNodeHelp 
   */
  
//   function removeErrorValidation(targetNodeInput, targetNodeHelp) {
  
//     removeClass("is-invalid",targetNodeInput);
//     removeAtribute("aria-describedby", "name-help", targetNodeInput);
//     addClass("my-invisible", targetNodeHelp);
//     removeClass("invalid-feedback", targetNodeHelp);
//   }
const journeyForm = document.getElementsByTagName("FORM")[0];
const inputAddressStart = document.getElementById("id-google-address-a");
const inputAddressDestination =  document.getElementById("id-google-address-b");
const helpDivStart = document.getElementById("google-address-a-help");
const helpDivDestination = document.getElementById("google-address-b-help");
const inputLatitudeStart = document.getElementById("id-lat-a");
const inputLongitudeStart = document.getElementById("id-long-a");
const inputLatitudeDestination = document.getElementById("id-lat-b");
const inputLongitudeDestination = document.getElementById("id-long-b");

function validateGeolocationFoundStart() {
    // need to check if all long and lat has been loaded
    // but display feedback in help node for address
    // because I don't want to show coordinates to the user, too much
    // information


//     if ((inputLatitudeStart === "") ) {
//         helpDivStart.innerHTML = "Please click into the drop down field to choose the correct address";
//         displayErrorValidation(inputAddressStart, helpDivStart);
//         return(false);
//     } else if ((inputLongitudeStart === "") ) {
//         helpDivStart.innerHTML = "Please click into the drop down field to choose the correct address";
//         displayErrorValidation(inputAddressStart, helpDivStart);
//         return(false);
//     } else {
//         helpDivStart.innerHTML = "We have found geocoordinates";
//         displayPassedValidation(inputAddressStart, helpDivStart);
//         return(true);
//     }

// }





    if (inputAddressStart.value === "") {
        helpDivStart.innerHTML = "This field is required";
        displayErrorValidation(inputAddressStart, helpDivStart);
        return(false);
    } else if ((inputLatitudeStart.value === "") && (inputAddressStart.value != "")) {
        helpDivStart.innerHTML = "Please click into the drop down field to choose the correct address";
        displayErrorValidation(inputAddressStart, helpDivStart);
        return(false);
    } else if ((inputLongitudeStart.value === "") && (inputAddressStart.value != "")) {
        helpDivStart.innerHTML = "Please click into the drop down field to choose the correct address";
        displayErrorValidation(inputAddressStart, helpDivStart);
        return(false);
    } else if ((inputLongitudeStart.value != "") && (inputAddressStart.value != "")) {
        helpDivStart.innerHTML = "We have found geocoordinates";
        displayPassedValidation(inputAddressStart, helpDivStart);

        return(true);
    }

}



// } else if ((inputLongitudeStart != "") && (inputAddressStart != "")) {
//     helpDivStart.innerHTML = "We have found geocoordinates";
//     displayPassedValidation(inputAddressStart, helpDivStart);
//     return(true);
// }
// function allValidationResults() {
//     if (validateGeolocationFoundStart() == false) {
//         console.log("START FAILED JS FORM VALIDATION")
//         return(false);
//     }
// }

// debounce and instant feedback on input copied from the below link
//https://www.javascripttutorial.net/javascript-dom/javascript-form-validation/

/**
 * Function to delay response
 * @param {*} fn 
 * @param {*} delay 500
 * @returns 
 */

 const debounce = (fn, delay = 500) => {
    let timeoutId;
    return (...args) => {
        // cancel the previous timer
        if (timeoutId) {
            clearTimeout(timeoutId);
        }
        // setup a new timer
        timeoutId = setTimeout(() => {
            fn.apply(null, args);
        }, delay);
    };
  };

/**
* Gives instant feedback on input with the delay set above
*/

journeyForm.addEventListener ('input', debounce(function (e) {
    switch (e.target.id) {
        case 'id-google-address-a':
            validateGeolocationFoundStart();
            break;

        case 'id-lat-a':
            validateGeolocationFoundStart();
            break;

    }
}));