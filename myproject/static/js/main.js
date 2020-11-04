
//This handles the drop down menu on mobile
$('.navbar-item').each(function(e) {
    $(this).on('click', function(){
      if($('#navbar-burger-id').hasClass('is-active')){
        $('#navbar-burger-id').removeClass('is-active');
        $('#navbar-menu-id').removeClass('is-active');
      }
    });
});

// Open or Close mobile & tablet menu
$('#navbar-burger-id').on('click', function () {
  if($('#navbar-burger-id').hasClass('is-active')){
    $('#navbar-burger-id').removeClass('is-active');
    $('#navbar-menu-id').removeClass('is-active');
  }else {
    $('#navbar-burger-id').addClass('is-active');
    $('#navbar-menu-id').addClass('is-active');
  }
});

  //Dismiss notifications
$(document).on('click', '.notification > button.delete', function() {
  $(this).parent().addClass('is-hidden');
  return false;
});

setTimeout(function() {$('#message').fadeOut('slow')}, 3000);