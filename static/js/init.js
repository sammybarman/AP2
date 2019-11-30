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
