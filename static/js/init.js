$('.carousel.carousel-slider').carousel({
    fullWidth: true,
    indicators: true
  });
  var autoplay = true;
  setInterval(function() { if(autoplay) $('.carousel.carousel-slider').carousel('next'); }, 2000);
  $('.carousel.carousel-slider').hover(function(){ autoplay = false; },function(){ autoplay = true; });

$(document).ready(function(){
  $('.sidenav').sidenav();
  $('.parallax').parallax();
  $('.scrollspy').scrollSpy();
  $('.materialboxed').materialbox();
  $('.fixed-action-btn').floatingActionButton();
  $('.tap-target').tapTarget();
  $('.tooltipped').tooltip();
  $('.datepicker').datepicker({
    selectMonths: true,
    minDate: new Date(2019,10,29)
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


// $(window).scroll(function(){
//
//   if($(window).scrollTop()>20){
//     $('nav').addClass('bg');
//     $('.brand-logo').addClass('black-text');
//     $('.forjq').addClass('bg2');
//   }else{
//     $('nav').removeClass('bg');
//     $('.brand-logo').removeClass('black-text');
//     $('.forjq').removeClass('bg2');
//   }
// });



$(document).ready(function(){
    $('.parallax').parallax();
  });

$(document).ready(function(){
      $('.fixed-action-btn').floatingActionButton();

  });
