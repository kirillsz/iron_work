<template>
  <header class="b-header__wrapper g-wrapper">
    <div class="container">
      <div class="row just-sb align-ic">
        <div class="order-lg-1 order-md-1 order-sm-1 col-lg-2 col-md-auto col-sm-auto">
          <a href="#" class="b-header__logo">
            <img src="@/assets/img/logo.png" alt="">
          </a>
        </div>
        <div class="order-lg-1 order-md-1 order-sm-1 col-lg-5 col-md-auto col-sm-auto">
          <div class="b-header__contacts">
            <a href="tel:+79195150777">+7 919 515 07 77</a>
            <span>Работаем в выходные<br>и праздники</span>
          </div>
        </div>
        <div class="order-lg-1 order-md-1 order-sm-4 col-lg-3 col-md-auto col-sm-12">
          <div class="b-header__action">
            <a href="#" class="btn_primary" data-open-popup @click="pop_up_open">Получить консультацию</a>
          </div>
        </div>

        <div class="order-lg-1 order-md-3 order-sm-2 col-lg-7 col-md-10 col-sm-12">
          <div class="b-header__center">
            <div class="b-header__center__accent">Работаем по {{ location }}</div>
            <h1 class="b-header__center__title">Ремонт КПП и<br>гидромеханических трансмиссий</h1>
            <div class="b-header__center__text">«Кировец», «ХТЗ», «Амкодор»</div>
          </div>
        </div>
        <div class="order-lg-1 order-md-2 order-sm-3 col-lg-5 col-md-12 col-sm-12 z0">
          <div class="b-header__center__img">
            <img src="@/assets/img/drigatel2.webp" alt="">
          </div>
        </div>

        <div class="order-lg-1 order-md-4 order-sm-5 col-lg-2 col-md-2 col-sm-12 b-header__year__wrapper">
          <div class="b-header__year">
            <div class="b-header__year__subtitle">Работаем с</div>
            <div class="b-header__year__title">1991 г.</div>
          </div>
        </div>
        <div class="order-lg-1 order-md-5 order-sm-6 col-lg-auto col-md-12 col-sm-12 b-header__pluses__wrapper">
          <div class="b-header__pluses__list">
            <div class="b-header__pluses__item__wrapper">
              <div class="b-header__pluses__item">
                <div class="b-header__pluses__item__title">Расширенная гарантия 1 год или 2500 м/ч</div>
              </div>
            </div>
            <div class="b-header__pluses__item__wrapper">
              <div class="b-header__pluses__item">
                <div class="b-header__pluses__item__title">Обмен КПП по Trade-in за 1 день</div>
              </div>
            </div>
            <a href="#tradein" class="b-header__pluses__item__wrapper" style="text-decoration: none;">
              <div class="b-header__pluses__item b-header__pluses__item_link">
                <div class="b-header__pluses__item__title">Всегда в наличии обменный фонд</div>
              </div>
            </a>
            <a href="#delivery" class="b-header__pluses__item__wrapper" style="text-decoration: none;">
              <div class="b-header__pluses__item b-header__pluses__item_link">
                <div class="b-header__pluses__item__title">Доставка до трактора за 1 день</div>
              </div>
            </a>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup>

import { useStore } from 'vuex'
import { ref, onMounted } from 'vue'

const store = useStore()

function pop_up_open(){
  store.dispatch('update_pop_up', true)
}

const location = ref('России')


onMounted(() => {

  // Получаем текущий URL из адресной строки браузера
  const currentUrl = window.location.href;

  // Создаем объект URL
  const parsedUrl = new URL(currentUrl)

  // Используем searchParams для получения значения параметра 'location'
  const raw_location = parsedUrl.searchParams.get("location")

  // Проверяем, есть ли параметр 'location' и выводим его значение
  if (raw_location) {
    location.value = raw_location
  }

})

</script>
