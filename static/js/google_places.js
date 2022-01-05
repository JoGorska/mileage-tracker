// functions created based on developers. google documentation
// and following tutorial
// https://www.youtube.com/watch?v=wCn8WND-JpU&t=8s

$.getScript( "https://maps.googleapis.com/maps/api/js?key=" + google_api_key + "&libraries=places") 
.done(function( script, textStatus ) {
    google.maps.event.addDomListener(window, "load", initAutocomplete())

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
       types: ['regions'],
       types: ['address'],
       componentRestrictions: {'country': ['uk']},
   })
  
  autocomplete_a.addListener('place_changed', function(){
    onPlaceChanged('a')
  });


  autocomplete_b = new google.maps.places.Autocomplete(
   document.getElementById('id-google-address-b'),
   {
       types: ['regions'],
       componentRestrictions: {'country': ['uk']},
   })
  
  autocomplete_b.addListener('place_changed', function(){
    onPlaceChanged('b')
  });

}


/**
 * function to validate form for empty fields
 * 
 */

 function validateForm() {
    var valid = true;
    $('.geo').each(function () {
        if ($(this).val() === '') {
            valid = false;
            return false;
        }
    });
    return valid
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

            } else {

                alert('Directions request failed due to ' + status);
                window.location.assign("/visits/")
            

                // $('#calculate-route').click(get_long_lat);
            } 
        
        }); 
    }
}

