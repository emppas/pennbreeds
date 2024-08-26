document.addEventListener('DOMContentLoaded', function () {
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', function () {
        if (window.scrollY > 50) { // Adjust scroll threshold as needed
            navbar.classList.add('navbar-scrolled');
        } else {
            navbar.classList.remove('navbar-scrolled');
        }
    });
});

$(document).ready(function() {
    $('#heroCarousel').carousel({
        interval: 5000,
        pause: 'hover'
    });

    // Typing animation for hero section text
    var typed = new Typed('.typed-text', {
        strings: ["Welcome to Checkengineer", "Innovative Solutions", "Your Engineering Partner"],
        typeSpeed: 50,
        backSpeed: 25,
        loop: true
    });

    // Change background color dynamically based on active slide
    $('#heroCarousel').on('slide.bs.carousel', function (e) {
        var newBgColor = $(e.relatedTarget).data('bg-color');
        $('#hero').css('background-color', newBgColor);
    });

    // Initial background color
    var initialBgColor = $('.carousel-item.active').data('bg-color');
    $('#hero').css('background-color', initialBgColor);
});