app = {}

// AOS.init();

app.hamburger = function() {
     // Hamburger open close toggle top nav
    $('.hamburger-toggle').on('click', function () {
        $(this).toggleClass('x-toggle');
        $('nav').toggleClass('res-menu');
    });
}

app.projectCarousel = function () {
    $('.carousel').flickity({
        cellAlign: 'left',
        wrapAround: true,
        cellSelector: '.carousel-cell',
        imagesLoaded: true
    });
}

// Init Function
app.init = function () {
    app.hamburger();
    app.projectCarousel();
};

// Document Ready
$(function () {
    app.init()
});



