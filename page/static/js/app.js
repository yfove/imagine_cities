$(document).ready(function () {

    // Hamburger open close toggle top nav
    $('.hamburger-toggle').on('click', function () {
        $(this).toggleClass('x-toggle');
        $('nav').toggleClass('res-menu');
    });
    
});

