$(document).ready(function() {
  $("a#single_image").fancybox();
  
  $("a.fancybox_gallery").fancybox({
  	'transitionIn'	:	'elastic',
  	'transitionOut'	:	'elastic',
  	'speedIn'		:	600, 
  	'speedOut'		:	200, 
  	'overlayShow'	:	false
  });
});
