$(document).ready(function(){
  $('select').formSelect();
  $('.carousel').carousel();
  $('.modal').modal();
  $('.datepicker').datepicker({
    selectMonths: true,
    minDate: new Date(2019,11,01)
  });
  $('.dropdown-trigger').dropdown({
    hover: true,
    belowOrigin: true,
    alignment: 'right',
    coverTrigger: false,
    closeOnClick: false
  });
  $('input.autocomplete').autocomplete2({
    data: [
      {id:1,text:'Apple',img:'http://placehold.it/250x250'},
      {id:2,text:'Microsoft',img:'http://placehold.it/250x250'},
      {id:3,text:'Google',img:'http://placehold.it/250x250'},
    ]
  });
});

function getId() {
  alert($('#autocomplete').data('id'));
}

function getHotels() {
  loc = $('#autocomplete').val();
  if (loc == '') {
    alert('You have to select location!');
  }
  else {
    date_from = $('#start').val();
    date_to = $('#end').val();
    path = '/gethotels?location='+loc+'&date_from='+date_from+'&date_to='+date_to;
    window.location = path;
  }
}

function getFilterHotels() {
  body = {
    amenities: $('#amenities').val(),
    features: $('#features').val(),
    price_min: $('#price_min').val(),
    price_max: $('#price_max').val(),
    city: $('#autocomplete').val()
  }
  nodes = document.querySelectorAll('input[name=rating]:checked');
  rating = []
  nodes.forEach(function(item){
    rating.push(item.value);
  });
  body.rating = rating;
  if (body.amenities.length == 0) {
    body.amenities.push('');
  }
  if (body.features.length == 0) {
    body.features.push('');
  }
  if (body.price_min == null) {
    body.price_min = -1;
  }
  if (body.price_max == null) {
    body.price_max = 100000;
  }
  console.log(body);
  $.ajax({
    url: "getfilterhotels",
    type: 'POST',
    data: JSON.stringify(body),
    contentType: 'application/json',
    dataType: 'html',
    success: function(result) {
      $('#hotellist').empty();
      // console.log(result);
      $('#hotellist').html(result);
    }
  });
}

function getHotelDetails(elem) {
  console.log(elem.value);
  loc = $('#autocomplete').val();
  date_from = $('#start').val();
  date_to = $('#end').val();
  path = '/gethoteldetails?hotel_id='+elem.value+'&location='+loc+'&date_from='+date_from+'&date_to='+date_to;
  window.location = path;
}

function checkoutPage() {
  if ($('#start').val() == '' || $('#end').val() == ''|| $('#adults').val() == '' || $('#children').val() == '' || $('#autocomplete').val() == '') {
    alert('You must Enter Location, Start Date, End Date and Number of Adults and Children!');
  }
  else {
    loc = $('#autocomplete').val();
    date_from = $('#start').val();
    date_to = $('#end').val();
    adults = $('#adults').val();
    child = $('#children').val();
    hotel_id = $('#checkout_btn').val();
    path = '/checkout?hotel_id='+hotel_id+'&location='+loc+'&date_from='+date_from+'&date_to='+date_to+'&adults='+adults+'&child='+child;
    window.location = path;
  }
}

function calcCost() {
  rooms = $('#rooms').val();
  if (rooms == '') {
    cost = '';
  }
  else {
    cost = $('#price').data('price') * $('#days').data('days') * parseInt(rooms);
  }
  $('#totalcost').html('<b>Total Price - '+cost+'</b>')
}

$("form").submit(function(e){
  e.preventDefault();
  $('#checkoutmod').modal('open'); 
});
