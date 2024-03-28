import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import vueTouchEvents from './api/touch'
import VueSmoothScroll from 'v-smooth-scroll'


import "@/assets/scss/index.scss"
import "@/assets/fonts/fonts.css"
import "@/assets/css/owl.carousel.css"

//import vScrollDirective from './directive.js';

import VueTheMask from 'vue-the-mask'


const app = createApp(App)
app.use(store)
app.use(router)

app.use(vueTouchEvents)
app.use(VueSmoothScroll)
app.use(VueTheMask)
//app.directive('scroll-directive', vScrollDirective);

app.mount('#app')
