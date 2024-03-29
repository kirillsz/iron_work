<template>
<section class="b-specialists__wrapper g-wrapper" id="specialists">
    <div class="container">
        <div class="row just-sb align-ic">
            <div class="order-lg-1 order-sm-2 col-lg-5 col-sm-12">
                <div data-slider="OwlSpecialists" class="owl-carousel owl-loaded owl-drag">
                
                    <div class="owl-stage-outer">
                        <div class="owl-stage">

                            <div class="owl-item active">
                        
                                <div v-for="(slide, index) in slides" :key="slide.id" :class="['b-specialists__slider__item', { active: index === currentSlide }]">
                                    <img :src="require(`@/assets/img/specialists/${slide.img}`)" alt="" @contextmenu.prevent="event.preventDefault()">
                                </div>
                         
                            </div>

                        </div>
                    </div>
                    
                    <div class="owl-nav">

                        <button @click="prevSlide" type="button" role="presentation" class="owl-prev disabled">
                            <svg xmlns="http://www.w3.org/2000/svg" width="56" height="49" viewBox="0 0 56 49" fill="none">
                                <path d="M30.4854 16L22.0001 24.4853L30.4854 32.9706" stroke="black" stroke-width="2"></path>
                                <path d="M14.5773 1L41.4226 1L54.8453 24.2487L41.4226 47.4974H14.5773L1.1547 24.2487L14.5773 1Z" stroke="black" stroke-width="2"></path>
                            </svg>
                        </button>

                        <button @click="nextSlide" type="button" role="presentation" class="owl-next">
                            <svg xmlns="http://www.w3.org/2000/svg" width="56" height="49" viewBox="0 0 56 49" fill="none">
                                <path d="M26.4854 16.2485L34.9706 24.7338L26.4854 33.2191" stroke="black" stroke-width="2"></path>
                                <path d="M14.5773 1L41.4226 1L54.8453 24.2487L41.4226 47.4974H14.5773L1.1547 24.2487L14.5773 1Z" stroke="black" stroke-width="2"></path>
                            </svg>
                        </button>

                    </div>

                    <div class="owl-dots">
                        <button
                        v-for="(_, index) in slides"
                        :key="index"
                        @click="setCurrentSlide(index)"
                        :class="{ 'owl-dot': true, active: index === currentSlide }"
                        role="button"
                        >
                        <span></span>
                        </button>
                    </div>

                </div>
            </div>
            
            <div class="order-sm-1 col-lg-6 col-sm-12">
                <h2 class="b-specialists__title">Наши специалисты</h2>
                <div class="b-specialists__description">
                <p>Наши агрегатчики прошли профессиональную подготовку на Кировском заводе ещё в 1970–1980 гг. в Ленинграде.
                </p>
                <p>С тех пор ими были отремонтированы тысячи агрегатов и успешно переданы все знания и навыки нынешнему
                    действующему звену агрегатчиков «Железное дело»</p>
                <p>Вот почему агрегаты отремонтированные у нас «ходят» многие годы и тысячи моточасов без нареканий.</p>
                </div>
            </div>

        </div>
    </div>
</section>
</template>

<script setup>

import { ref } from 'vue';

const slides = [
    {
        "img": "НС_1.jpg"
    },
    {
        "img": "НС_2.jpg"
    },
    {
        "img": "НС_3.jpg"
    },
    {
        "img": "НС_4.jpg"
    },
    {
        "img": "НС_5.jpg"
    },
    {
        "img": "НС_6.jpg"
    },
    {
        "img": "НС_7.jpg"
    },
    {
        "img": "НС_8.jpg"
    },
    {
        "img": "НС_9.jpg"
    },
    {
        "img": "НС_10.jpg"
    },];

const currentSlide = ref(0);

const nextSlide = () => {
  currentSlide.value = (currentSlide.value + 1) % slides.length;
};

const prevSlide = () => {
  currentSlide.value = (currentSlide.value - 1 + slides.length) % slides.length;
};

const setCurrentSlide = (index) => {
  currentSlide.value = index;
};


</script>

<style>
.b-specialists__slider__item {
    display: none;
}

.b-specialists__slider__item.active {
    display: block;
}
</style>