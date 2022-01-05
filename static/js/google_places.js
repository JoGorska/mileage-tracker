// functions created based on developers. google documentation
// and following tutorial
// https://www.youtube.com/watch?v=wCn8WND-JpU&t=8s

$.getScript( "https://maps.googleapis.com/maps/api/js?key=" + google_api_key + "&libraries=places") 
.done(function( script, textStatus ) {
    google.maps.event.addDomListener(window, "load", initAutocomplete()),
    google.maps.event.addDomListener(document.getElementById('btn'),'click', calcDistance)

})


let autocomplete_a;
let autocomplete_b;
/**
 * function that initializes autocomplete from google maps places
 */

function initAutocomplete() {

  autocomplete_a = new google.maps.places.Autocomplete(
   document.getElementById('id-google-address-a'),
   {
       types: ['address'],
       componentRestrictions: {'country': ['uk']},
   })
  
  autocomplete_a.addListener('place_changed', function(){
    onPlaceChanged('a')
  });


  autocomplete_b = new google.maps.places.Autocomplete(
   document.getElementById('id-google-address-b'),
   {
       types: ['address'],
       componentRestrictions: {'country': ['uk']},
   })
  
  autocomplete_b.addListener('place_changed', function(){
    onPlaceChanged('b')
  });

}

/**
 * function that listens for input / place changed in the start and destination fields and
 * autocompletes the address and latutude and longditude fields
 */

function onPlaceChanged (addy){

    let auto
    let el_id
    let lat_id
    let long_id

    if ( addy === 'a'){
        auto = autocomplete_a
        el_id = 'id-google-address-a'
        lat_id = 'id-lat-a'
        long_id = 'id-long-a'
    }
    else{
        auto = autocomplete_b
        el_id = 'id-google-address-b'
        lat_id = 'id-lat-b'
        long_id = 'id-long-b'
    }

    var geocoder = new google.maps.Geocoder()
    var address_start = document.getElementById('id-google-address-a').value
    var address_destination = document.getElementById('id-google-address-b').value
    var address_list = [address_start, address_destination]
    console.log(address_list)

    for (address in address_list) {
        var address = document.getElementById(el_id).value
        

        geocoder.geocode( { 'address': address}, function(results, status) {

            if (status == google.maps.GeocoderStatus.OK) {
                var latitude = results[0].geometry.location.lat();
                var longitude = results[0].geometry.location.lng();

                $('#' + lat_id).val(latitude) 
                $('#' + long_id).val(longitude) 

                $('#calculate-route').click(get_long_lat);
            } 
        
        }); 
    }
}


// functions created based on developers. google documentation
// and following tutorial
// https://www.youtube.com/watch?v=wCn8WND-JpU&t=8s

// loading map 
// https://developers.google.com/maps/documentation/javascript/overview



function get_long_lat() {
   
    lat_a = $('#id-lat-a').val()
    long_a = $('#id-long-a').val()
    lat_b = $('#id-lat-b').val()
    long_b = $('#id-long-b').val()
    var directionsService = new google.maps.DirectionsService;
    var directionsDisplay = new google.maps.DirectionsRenderer;
    var map = new google.maps.Map(document.getElementById('map-route'), {
        zoom: 7,
        // center: {lat: lat_a, lng: long_a}

    });
    directionsDisplay.setMap(map);
    calculateAndDisplayRoute(directionsService, directionsDisplay);

}

// google directions api documentation
// https://developers.google.com/maps/documentation/directions/overview

// https://developers.google.com/maps/documentation/javascript/directions

function calculateAndDisplayRoute(directionsService, directionsDisplay) {
    var origin = $('#id-google-address-a').val()
    var destination = $('#id-google-address-b').val()
    
    directionsService.route({
        origin: origin,
        destination: destination,
        travelMode: 'DRIVING'
    }, function(response, status) {
      if (status === 'OK') {
        directionsDisplay.setDirections(response);


      } else {

        alert('Directions request failed due to ' + status);
        window.location.assign("/visits/")
      }
    });
}

// pre-fill the date field with today's date
// https://css-tricks.com/prefilling-date-input/


// let today = new Date().toISOString().substr(0, 10);
// document.querySelector("#id_date_of_journey").value = today;

