$(document).ready(function () {

    // Initiate animate on scroll
	AOS.init();

    // Hamburger open close toggle top nav
    $('.hamburger-toggle').on('click', function () {
        $(this).toggleClass('x-toggle');
        $('nav').toggleClass('res-menu');
    });

    // Initiate smooth scroll
    $('a').smoothScroll({
		speed: 1000
	});
    
});

