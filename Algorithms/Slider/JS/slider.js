let pos = 0;
let sliderWidth = 1900;
let sliderHeight = 300;
let slideCount = 3;

let slides = document.querySelector('.slides');
let slider = document.querySelector('.slider');
let allSlides = document.querySelectorAll('.slide'); // .slide classina aid olan butun elementleri sec
// set slider width and height

slider.style.width = `${sliderWidth}px`;
slider.style.height = `${sliderHeight}px`;

// butun slide elementlerinin genisliyini javascript vasitesi ile teyin edirem
for (let slide of allSlides) {
    slide.style.width = `${sliderWidth/2}px`
}

// slides divinin genisliyi dinamik olaraq teyin edirem

slides.style.width = `${sliderWidth/2*allSlides.length}px`

// slider dots

let dots = document.querySelector('.slider-dots');

for (let i = 0; i < allSlides.length; i++) {
    dots.innerHTML += `<div class="dot" onclick="slideSelectedItem(${i})">${i}</div>`
}


function left() {
    if (pos >= 0) {
        pos = 0
    } else {
        pos += sliderWidth / 2;
        slides.style.left = `${pos}px`;
    }

}

function right() {
    if (pos <= -((sliderWidth / 2) * (allSlides.length - 2))) {
        pos = -((sliderWidth / 2) * (allSlides.length - 2))
    } else {
        pos -= sliderWidth / 2;
        slides.style.left = `${pos}px`;
    }

}

function slideSelectedItem(i) {
    slides.style.left = `${-i*sliderWidth / 2}px`
}