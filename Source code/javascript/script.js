let menuIcon = document.querySelector('#menu-icon') ;
let navbar = document.querySelector('.navbar');
menuIcon.onclick = () => {
    menuIcon.classList.toggle('bx-x');
    navbar.classList.toggle('active');
};

let sections = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header nav a');
window.onscroll = () => {
    sections.forEach(sec =>  {
        let top = window.scrollY;
        let offset = sec.offsetTop - 150;
        let height = sec.offsetHeight;
        let id = sec.getAttribute('id');

        if(top >= offset && top < offset+height) {
            navLinks.forEach(links => {
                links.classList.remove('active');
                document.querySelector('header nav a[href*=' + id + ']').classList.add('active');
            });
        };
    });
    

    // Remove toggle icon and navbar when click navbar link

    menuIcon.classList.remove('bx-x');
    navbar.classList.remove('active');
};

ScrollReveal({ 
    reset: false,
    distance: '40px',
    duration: 2000,
    delay: 100
});


ScrollReveal().reveal('.home-content, .heading', { origin: 'top' });
ScrollReveal().reveal('.home-img, .services-container, .project-box, .contact form', { origin: 'bottom' });

// Swiper JS
var swiper = new Swiper('.slide-content', {
    slidesPerView: 3,   
    spaceBetween: 30,
    slidesPerGroup: 3,
    centerSlide: true,
    fade: true,
    loop: false,
    loopFillGroupWithBlank: true,
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
      dynamicBullets: true,
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },

    breakpoints: {
        0 : {
            slidesPerView: 1,
        },
        540 : {
            slidesPerView: 2,
        },
        950 : {
            slidesPerView: 3,
        },
    }

});