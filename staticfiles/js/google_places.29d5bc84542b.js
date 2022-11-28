
// functions to add or remove classes and show and hide validation errrors
// inspired by my project portfolio 2 Change Fuel
// https://github.com/JoGorska/Keto-diet/blob/master/assets/js/calculator.js
// and adjusted to the needs of the current project

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

  function setAttribute(attributeName, attributeValue, targetNode) {
    targetNode.setAttribute(attributeName, attributeValue);
  }

  /**
   * Function to display Error after validation has been failed
   * makes div with help message visible and in red,
   * input's border is red and red icon
   * with exclamation mark is displayed in input field
   * @param {*} targetNodeInput
   * @param {*} targetNodeHelp
   */
  function displayErrorValidation(targetNodeInput, targetNodeHelp) {

    addClass("is-invalid",targetNodeInput);
    removeClass("is-valid",targetNodeInput);
    setAttribute("aria-describedby", "name-help", targetNodeInput);
    removeClass("my-invisible", targetNodeHelp);
    addClass("invalid-feedback", targetNodeHelp);
    removeClass("valid-feedback", targetNodeHelp);
  }

  /**
   * Function to display Error after validation has been failed
   * makes div with help message visible and in red, input's border is red
   * and red icon with exclamation mark is displayed in input field
   * @param {*} targetNodeInput
   * @param {*} targetNodeHelp
   */
   function displayPassedValidation(targetNodeInput, targetNodeHelp) {
    addClass("is-valid", targetNodeInput);
    removeClass("is-invalid", targetNodeInput);
    setAttribute("aria-describedby", "name-help", targetNodeInput);
    removeClass("my-invisible", targetNodeHelp);
    addClass("valid-feedback", targetNodeHelp);
    removeClass("invalid-feedback", targetNodeHelp);
  }

const journeyForm = document.getElementsByTagName("FORM")[0];
const inputAddressStart = document.getElementById("id-google-address-a");
const inputAddressDestination =  document.getElementById("id-google-address-b");
const helpDivStart = document.getElementById("google-address-a-help");
const helpDivDestination = document.getElementById("google-address-b-help");
const inputLatitudeStart = document.getElementById("id-lat-a");
const inputLongitudeStart = document.getElementById("id-long-a");
const inputLatitudeDestination = document.getElementById("id-lat-b");
const inputLongitudeDestination = document.getElementById("id-long-b");

/**
 * validates start
 * function to validate if the user has input all data needed
 * for the data model: address, latitude, longitude,
 * detects if all or one of the fields is empty
 * @returns true or false
 */
function validateGeolocationFoundStart() {

    if (inputAddressStart.value === "") {
        helpDivStart.innerHTML = "This field is required";
        displayErrorValidation(inputAddressStart, helpDivStart);
        return(false);
    } else if ((inputLatitudeStart.value === "") && (inputAddressStart.value !== "")) {
        helpDivStart.innerHTML = "Please click into the drop down field to choose the correct address";
        displayErrorValidation(inputAddressStart, helpDivStart);
        return(false);
    } else if ((inputLongitudeStart.value === "") && (inputAddressStart.value !== "")) {
        helpDivStart.innerHTML = "Please click into the drop down field to choose the correct address";
        displayErrorValidation(inputAddressStart, helpDivStart);
        return(false);
    } else {
        return(true);
    }
}

/**
 * validates destination
 * function to validate if the user has input all data needed
 * for the data model:
 * address, latitude, longitude, detects if all or one of the fields is empty
 * @returns true or false
 */
function validateGeolocationFoundDestination() {

    if (inputAddressDestination.value === "") {
        helpDivDestination.innerHTML = "This field is required";
        displayErrorValidation(inputAddressDestination, helpDivDestination);
        return(false);
    } else if ((inputLatitudeDestination.value === "") && (inputAddressDestination.value !== "")) {
        helpDivDestination.innerHTML = ("Please click into the drop down field to choose the correct address");
        displayErrorValidation(inputAddressDestination, helpDivDestination);
        return(false);
    } else if ((inputLongitudeDestination.value === "") && (inputAddressDestination.value !== "")) {
        helpDivDestination.innerHTML = ("Please click into the drop down field to choose the correct address");
        displayErrorValidation(inputAddressDestination, helpDivDestination);
        return(false);
    } else {
        return(true);
    }
}

// debounce and instant feedback on input copied from the below link
//https://www.javascripttutorial.net/javascript-dom/javascript-form-validation/

/**
 * Function to delay response
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
journeyForm.addEventListener ("input", debounce(function (e) {
    switch (e.target.id) {
        case "id-google-address-a":
            validateGeolocationFoundStart();
            break;

        case "id-google-address-b":
            validateGeolocationFoundDestination();
            break;

    }
}));

// functions created based on developers.google documentation
// https://developers.google.com/maps/documentation/places/web-service/supported_types
// and following tutorial Bobby did coding
// https://www.youtube.com/watch?v=wCn8WND-JpU&t=8s
// and refactored to the needs of the project

$.getScript( "https://maps.googleapis.com/maps/api/js?key=" + google_api_key + "&libraries=places") 
.done(function( script, textStatus ) {
    google.maps.event.addDomListener(window, "load", initAutocomplete());
});


let autocomplete_a;
let autocomplete_b;
/**
 * function that initializes autocomplete from google maps places API
 * user can search by postcode or full address
 * once API has been fetched successfully the div displays to the user that
 * the field passed validation successfully
 */
function initAutocomplete() {

  autocomplete_a = new google.maps.places.Autocomplete(
   document.getElementById("id-google-address-a"),
   {
       regions: ["postal_code"],
       componentRestrictions: {"country": ["uk"]}
   });

  autocomplete_a.addListener("place_changed", function(){
    onPlaceChanged("a");
    helpDivStart.innerHTML = "We have found geocoordinates";
    displayPassedValidation(inputAddressStart, helpDivStart);
  });


  autocomplete_b = new google.maps.places.Autocomplete(
   document.getElementById("id-google-address-b"),
   {
        regions: ["postal_code"],
       componentRestrictions: {"country": ["uk"]}
   });
  
  autocomplete_b.addListener("place_changed", function(){
    onPlaceChanged("b");
    helpDivDestination.innerHTML = "We have found geocoordinates";
    displayPassedValidation(inputAddressDestination, helpDivDestination);
  });

}

/**
 * function that listens for input / place changed in the start and destination fields and
 * autocompletes the address and latutude and longditude fields
 */
function onPlaceChanged (addy){

    let auto;
    let el_id;
    let lat_id;
    let long_id;

    if ( addy === "a"){
        auto = autocomplete_a;
        el_id = "id-google-address-a";
        lat_id = "id-lat-a";
        long_id = "id-long-a";
    }
    else{
        auto = autocomplete_b;
        el_id = "id-google-address-b";
        lat_id = "id-lat-b";
        long_id = "id-long-b";
    }

    var geocoder = new google.maps.Geocoder();
    var address_start = document.getElementById("id-google-address-a").value;
    var address_destination = document.getElementById("id-google-address-b").value;
    var address_list = [address_start, address_destination];

    for (var address in address_list) {
        address = document.getElementById(el_id).value;
        

        geocoder.geocode( { "address": address}, function(results, status) {

            if (status == google.maps.GeocoderStatus.OK) {
                var latitude = results[0].geometry.location.lat();
                var longitude = results[0].geometry.location.lng();

                $("#" + lat_id).val(latitude);
                $("#" + long_id).val(longitude);
                

            } else {

                alert("Directions request failed due to " + status);
                window.location.assign("/visits/");
            
            } 
        
        }); 
    }
}
