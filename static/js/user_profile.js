// functions created based on developers.google documentation
// https://developers.google.com/maps/documentation/places/web-service/supported_types
// and following tutorial Bobby did coding
// https://www.youtube.com/watch?v=wCn8WND-JpU&t=8s
// and refactored to the needs of the project

$.getScript( "https://maps.googleapis.com/maps/api/js?key=" + google_api_key + "&libraries=places") 
.done(function( script, textStatus ) {
    google.maps.event.addDomListener(window, "load", initAutocomplete());
});


let autocomplete_user;
let autocomplete_employer;
/**
 * function that initializes autocomplete from google maps places API
 * user can search by postcode or full address
 * once API has been fetched successfully the div displays to the user that
 * the field passed validation successfully
 */
function initAutocomplete() {

  autocomplete_a = new google.maps.places.Autocomplete(
   document.getElementById("id_your_address"),
   {
       regions: ["postal_code"],
       componentRestrictions: {"country": ["uk"]}
   });

  autocomplete_a.addListener("place_changed", function(){
    onPlaceChanged("user");
    helpDivStart.innerHTML = "We have found geocoordinates";
    displayPassedValidation(inputAddressStart, helpDivStart);
  });


  autocomplete_b = new google.maps.places.Autocomplete(
   document.getElementById("id_employer_address"),
   {
        regions: ["postal_code"],
       componentRestrictions: {"country": ["uk"]}
   });
  
  autocomplete_b.addListener("place_changed", function(){
    onPlaceChanged("employer");
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

    if ( addy === "user"){
        auto = autocomplete_user;
        el_id = "id_your_address";
        lat_id = "id_latitude";
        long_id = "id_longitude";
    }
    else{
        auto = autocomplete_employer;
        el_id = "id_employer_address";
        lat_id = "id_employer_latitude";
        long_id = "id_employer_longitude";
    }

    var geocoder = new google.maps.Geocoder();
    var address_user = document.getElementById("id_your_address").value;
    var address_employer = document.getElementById("id_employer_address").value;
    var address_list = [address_user, address_employer];

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
                window.location.assign("/users/");
            
            } 
        
        }); 
    }
}
