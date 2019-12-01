$(document).ready(function(){
  $('select').formSelect();
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
