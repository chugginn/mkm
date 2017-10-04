$(document).ready(function() {
	$(window).scroll(function(){
		if ( $(this).scrollTop() > 0) {
			$('.navbar').addClass("navbar-scrolled");
		} else {
			$('.navbar').removeClass("navbar-scrolled");
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