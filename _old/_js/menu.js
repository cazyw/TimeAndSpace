var main = function() {
  $('.icon-toggle').click(function() {
    $('.menu').toggle();
  });

  $(window).resize(function() {
        // This will fire each time the window is resized:
        if($(window).width() >= 768) {
            // if larger or equal
            $('.menu').hide();
        }
    });
  
};

$(document).ready(main);