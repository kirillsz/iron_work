<template>
  <div id="app">

    <Header></Header>

    <router-view></router-view>

    <Footer></Footer>

    <div v-if="pop_up" data-popup-bg class="active">
      <form data-popup class="active">

        <button data-close-popup class="close-popup" @click="pop_up_close">
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="17" viewBox="0 0 18 17" fill="none">
            <line x1="2.70711" y1="1.29289" x2="16.8492" y2="15.435" stroke="black" stroke-width="2" />
            <line y1="-1" x2="20" y2="-1" transform="matrix(-0.707107 0.707107 0.707107 0.707107 16.1421 2)"
              stroke="black" stroke-width="2" />
          </svg>
        </button>

        <div class="popup_content">
          <div class="popup_title">Звоните по телефону</div>
          <a href="tel:+79195150777" class="popup_phone">+7 919 515 07 77</a>
          <div class="popup_text">или укажите номер телефона и мы вам перезвоним</div>

          <label class="b-form__input__text">
            <span>Ваш номер</span>
            <input name="main_phone" v-model="phone" v-mask="['+7(###) ###-##-##',]" type="tel" placeholder="+7 123 456 78 90">
          </label>

          <button type="submit" class="btn_primary w-100" @click.prevent="order"><span>Отправить</span></button>

          <a href="#" class="popup_police">Политика конфиденциальности</a>
        </div>
      </form>
    </div>

  </div>
</template>

<script setup>

import { computed, ref } from 'vue'
import { useStore } from 'vuex'

import Header from "./components/Header.vue" 
import Footer from "./components/Footer.vue" 


const store       = useStore()
const pop_up      = computed(() => store.getters.pop_up)
const domain      = computed(() => store.getters.domain)

function pop_up_close(){
  store.dispatch('update_pop_up', false)
}

const phone = ref("+7")

async function order() {

  await fetch(`${domain.value}/api/order/create`, {
    method: 'POST',
    headers: { 
      'Content-Type':'application/json',
    },
    body: JSON.stringify({
      phone: phone.value,
      desc: "",
    })
  })

  pop_up_close()

}

</script>
