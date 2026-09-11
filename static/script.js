const swiper1 = new Swiper('.reviews__slider', {
    loop: true,
    slidesPerView: 1.61,
    initialSlide: 1,
    centeredSlides: true,
    autoplay: {
        delay: 5000,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
    },
    speed: 500
});

let left_button = document.querySelector(".left");
let right_button = document.querySelector(".right");

left_button.addEventListener("click", () => {swiper1.slidePrev()})
right_button.addEventListener("click", () => {swiper1.slideNext()})
