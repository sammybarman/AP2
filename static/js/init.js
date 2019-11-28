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
  $('.dropdown-trigger').dropdown({
    hover: true,
    belowOrigin: true,
    alignment: 'right',
    coverTrigger: false,
    closeOnClick: false
  });
});


$(window).scroll(function(){

  if($(window).scrollTop()>20){
    $('nav').addClass('bg');
    $('.brand-logo').addClass('black-text');
    $('.forjq').addClass('bg2');
  }else{
    $('nav').removeClass('bg');
    $('.brand-logo').removeClass('black-text');
    $('.forjq').removeClass('bg2');
  }
});



$(document).ready(function(){
    $('.parallax').parallax();
  });

$(document).ready(function(){
      $('.fixed-action-btn').floatingActionButton();

  });

$(document).ready(function(){

      $(window).scroll(function(){

       if($(window).scrollTop()>20){
         $('nav').addClass('bg');
       }else{
         $('nav').removeClass('bg');
       }
    });
  });
