$(document).ready(function() {
	$(window).scroll(function(){
		if ( $(this).scrollTop() > 40) {
			$('.navbar').addClass("navbar-scrolled");
			$('.top-social').addClass("social-scrolled");
		} else {
			$('.navbar').removeClass("navbar-scrolled");
			$('.top-social').removeClass("social-scrolled");
		}
	});
    $(".player .toggle").click(function() {
        if ( $(this).parent().hasClass("auto_height") ) {
            $(this).html("<i class=\"fa fa-chevron-up\" aria-hidden=\"true\"></i>");
        }
        else {
            $(this).html("<i class=\"fa fa-chevron-down\" aria-hidden=\"true\"></i>");
        }
        $(this).parent().toggleClass("auto_height");
    });
});