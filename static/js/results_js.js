function hamburger() {
  var x = document.getElementById("details");
  x.classList.toggle("input_animated");
}
function burger_bite(){
  var x = document.getElementById('cont');
  x.classList.toggle("change");
}

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    //x.innerHTML = "Geolocation is not supported by this browser.";
  }
}
function clear_cart(){
    var carts = document.getElementsByClassName('like_box');
    var subs = document.getElementsByClassName('cart_item');
    for(var i = 0; i < subs.length; i++){
       var a = subs[i];
        if (a.style.display === "block"){
           a.style.display = 'none';
       }
    }
    for(var k = 0; k < carts.length; k++){
       var t = carts[k];
        if (t.checked){
           t.checked = false;
       }
    }
}
function showPosition(position) {
  var CurrentLocation = "Latitude: " + position.coords.latitude + 
  "Longitude: " + position.coords.longitude;
  
   var xCoord =  position.coords.latitude;
   var yCoord = position.coords.longitude;
}