<template>
    <section class="b-repair__wrapper g-wrapper">
        <div class="container">
            <div class="row align-ic">
                <div class="order-lg-1 order-sm-1 col-lg-12 col-sm-12">
                    <div class="b-repair__title">Капитальный ремонт КПП</div>
                </div>
            <div class="order-lg-1 order-sm-3 col-lg col-sm-12">
            <div class="h2">Специалисты стажировались на Петербургском тракторном заводе им. Кирова и имеют стаж ремонта десятки лет!</div>
        </div>
        <div class="order-lg-1 col-lg-auto">
          <div class="b-documents__title__nav">
            <svg @click="click_left" xmlns="http://www.w3.org/2000/svg" width="56" height="49" viewBox="0 0 56 49" fill="none"
              class="customRepairPrevBtn disabled">
              <path d="M30.4854 16L22.0001 24.4853L30.4854 32.9706" stroke="black" stroke-width="2" />
              <path d="M14.5773 1L41.4226 1L54.8453 24.2487L41.4226 47.4974H14.5773L1.1547 24.2487L14.5773 1Z"
                stroke="black" stroke-width="2" />
            </svg>
            <svg @click="click_right" xmlns="http://www.w3.org/2000/svg" width="56" height="49" viewBox="0 0 56 49" fill="none"
              class="customRepairNextBtn">
              <path d="M26.4854 16.2485L34.9706 24.7338L26.4854 33.2191" stroke="black" stroke-width="2" />
              <path d="M14.5773 1L41.4226 1L54.8453 24.2487L41.4226 47.4974H14.5773L1.1547 24.2487L14.5773 1Z"
                stroke="black" stroke-width="2" />
            </svg>

          </div>
        </div>

        <div class="order-lg-1 order-sm-2 col-lg-12 col-sm-12">
            <div data-slider="OwlRepair">
                <div class="wrap-hardware">

                    <div class="hardware">

                        <div class="wrap">
  
                            <div @click="click_left" class="arrow-left">
                                <svg width="35" height="70" viewBox="0 0 35 70" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <g style="mix-blend-mode:hard-light">
                                        <path d="M35 35C35 54.33 19.33 70 0 70V0C19.33 0 35 15.67 35 35Z" fill="#1A2030"/>
                                    </g>
                                    <path d="M17.7683 25.3073L8.34525 34.7304L17.7683 44.1535L15.8837 47.9227L2.69141 34.7304L15.8837 21.5381L17.7683 25.3073Z" fill="#FFDD2D"/>
                                </svg>
                            </div>

                            <div v-if="sliders.length" class="wrap">
                                <div class="sliders" :style="{'left': '-' + offset_left + 'px'}">

                                    <div v-for="(slider, i) in sliders" :key="i" v-touch:swipe.left="click_right" v-touch:swipe.right="click_left" :class="['slider', slider.class]">
                                        <img :src="require(`@/assets/img/repair-kpp/${slider.img}`)" @contextmenu.prevent="event.preventDefault()"/>
                                    </div>

                                </div>
                            </div>

                            <div @click="click_right" class="arrow-right">
                                <svg width="35" height="70" viewBox="0 0 35 70" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <g style="mix-blend-mode:hard-light">
                                        <path d="M0 35C0 54.33 15.67 70 35 70V0C15.67 0 0 15.67 0 35Z" fill="#1A2030"/>
                                    </g>
                                    <path d="M17.2317 25.3073L26.6547 34.7304L17.2317 44.1535L19.1163 47.9227L32.3086 34.7304L19.1163 21.5381L17.2317 25.3073Z" fill="#FFDD2D"/>
                                </svg>
                            </div>

                        </div>

                        </div>

                        <!-- <box v-if="box.is" :close="box.close" :object="box.object" :sliders="sliders"></box> -->

                    </div>
            
                    </div>
                </div>
            </div>
        </div>



    </section>

</template>


<script>

import { useStore } from 'vuex'
import { computed, ref, onMounted, onUnmounted } from 'vue'

//import Box from '@/components/home/Box.vue'

export default {

	// components: {
	// 	'box': Box,
	// },


    setup(){

		const store = useStore()
		const domain = computed(() => store.getters.domain)


		// onBeforeMount(() => {
		// 	for(let i = 1; i < 75; i++){
		// 		sliders.value.push({
		// 			img: `КПП_${i}.jpg`,
		// 		})
		// 	}
		// 	console.log(sliders.value)
		// })

		onMounted(
			() => window.addEventListener("resize", () => offset_left.value = 0)
		)

		onUnmounted(() => window.removeEventListener("resize", () => offset_left.value = 0))


		const box = ref({is: false, object: null, close: null})
		function open_box(object) {

			box.value.is = true
			box.value.object = object
			box.value.close = () => box.value.is = false
		}

		const sliders = ref([
    {
        "img": "КПП_1.jpg"
    },
    {
        "img": "КПП_2.jpg"
    },
    {
        "img": "КПП_3.jpg"
    },
    {
        "img": "КПП_4.jpg"
    },
    {
        "img": "КПП_5.jpg"
    },
    {
        "img": "КПП_6.jpg"
    },
    {
        "img": "КПП_7.jpg"
    },
    {
        "img": "КПП_8.jpg"
    },
    {
        "img": "КПП_9.jpg"
    },
    {
        "img": "КПП_10.jpg"
    },
    {
        "img": "КПП_11.jpg"
    },
    {
        "img": "КПП_12.jpg"
    },
    {
        "img": "КПП_13.jpg"
    },
    {
        "img": "КПП_14.jpg"
    },
    {
        "img": "КПП_15.jpg"
    },
    {
        "img": "КПП_16.jpg"
    },
    {
        "img": "КПП_17.jpg"
    },
    {
        "img": "КПП_18.jpg"
    },
    {
        "img": "КПП_19.jpg"
    },
    {
        "img": "КПП_20.jpg"
    },
    {
        "img": "КПП_21.jpg"
    },
    {
        "img": "КПП_22.jpg"
    },
    {
        "img": "КПП_23.jpg"
    },
    {
        "img": "КПП_24.jpg"
    },
    {
        "img": "КПП_25.jpg"
    },
    {
        "img": "КПП_26.jpg"
    },
    {
        "img": "КПП_27.jpg"
    },
    {
        "img": "КПП_28.jpg"
    },
    {
        "img": "КПП_29.jpg"
    },
    {
        "img": "КПП_30.jpg"
    },
    {
        "img": "КПП_31.jpg"
    },
    {
        "img": "КПП_32.jpg"
    },
    {
        "img": "КПП_33.jpg"
    },
    {
        "img": "КПП_34.jpg"
    },
    {
        "img": "КПП_35.jpg"
    },
    {
        "img": "КПП_36.jpg"
    },
    {
        "img": "КПП_37.jpg"
    },
    {
        "img": "КПП_38.jpg"
    },
    {
        "img": "КПП_39.jpg"
    },
    {
        "img": "КПП_40.jpg"
    },
    {
        "img": "КПП_41.jpg"
    },
    {
        "img": "КПП_42.jpg"
    },
    {
        "img": "КПП_43.jpg"
    },
    {
        "img": "КПП_44.jpg"
    },
    {
        "img": "КПП_45.jpg"
    },
    {
        "img": "КПП_46.jpg"
    },
    {
        "img": "КПП_47.jpg"
    },
    {
        "img": "КПП_48.jpg"
    },
    {
        "img": "КПП_49.jpg"
    },
    {
        "img": "КПП_50.jpg"
    },
    {
        "img": "КПП_51.jpg"
    },
    {
        "img": "КПП_52.jpg"
    },
    {
        "img": "КПП_53.jpg"
    },
    {
        "img": "КПП_54.jpg"
    },
    {
        "img": "КПП_55.jpg"
    },
    {
        "img": "КПП_56.jpg"
    },
    {
        "img": "КПП_57.jpg"
    },
    {
        "img": "КПП_58.jpg"
    },
    {
        "img": "КПП_59.jpg"
    },
    {
        "img": "КПП_60.jpg"
    },
    {
        "img": "КПП_61.jpg"
    },
    {
        "img": "КПП_62.jpg"
    },
    {
        "img": "КПП_63.jpg"
    },
    {
        "img": "КПП_64.jpg"
    },
    {
        "img": "КПП_65.jpg"
    },
    {
        "img": "КПП_66.jpg"
    },
    {
        "img": "КПП_67.jpg"
    },
    {
        "img": "КПП_68.jpg"
    },
    {
        "img": "КПП_69.jpg"
    },
    {
        "img": "КПП_70.jpg"
    },
    {
        "img": "КПП_71.jpg"
    },
    {
        "img": "КПП_72.jpg"
    },
    {
        "img": "КПП_73.jpg"
    },
    {
        "img": "КПП_74.jpg"
    }
])

		const pagination = ref({
            start: 0,
			stop: 4,
        })

		const offset_left = ref(0)


		function click_left() {
            if(pagination.value.start > 0){

                pagination.value.start -= 1
				pagination.value.stop -= 1

				if(document.documentElement.clientWidth > 1240){
					offset_left.value -= 315
				}else{
					offset_left.value -= 235
				}

            }
        }

        function click_right() {
            if(pagination.value.stop < sliders.value.length){
				
                pagination.value.start += 1
				pagination.value.stop += 1

				if(document.documentElement.clientWidth > 1240){
					offset_left.value += 315
				}else{
					offset_left.value += 235
				}

            }
        }


        return {
			domain,
			sliders,
            //sliders_filter,
			offset_left,
            click_right,
            click_left,
			open_box,
			box,
        }
    
    }

}
</script>


<style>

/* block 9 */

.wrap-hardware {
	position: relative;
}

.wrap-hardware .hardware {
	position: relative;
}

@media (min-width: 1150px){
	.wrap-hardware .hardware {
		padding: 60px;
	}
}

@media (min-width: 1150px){
	.wrap-hardware .hardware {
		margin: 0 auto;
	}
}

@media (min-width: 1150px){
	.wrap-hardware .hardware {
		max-width: 1240px;
		padding: 0;
	}
}

.wrap-hardware .hardware > .wrap {
	position: relative;
	display: flex;
	align-items: center;
}

.wrap-hardware .hardware > .wrap > .wrap {
	position: relative;
	display: flex;
	overflow: hidden;
	width: 100%;
	height: 320px;
}

@media (min-width: 1150px){
	.wrap-hardware .hardware > .wrap > .wrap {
		height: 400px;
	}
}

.wrap-hardware .hardware > .wrap .sliders {
	display: flex;
    position: absolute;
	transition: left 500ms ease;
}

.wrap-hardware .hardware > .wrap .arrow-left {
    position: absolute;
	display: flex;
	align-items: center;
	z-index: 1;
	cursor: pointer;
}

.wrap-hardware .hardware > .wrap .arrow-right {
    position: absolute;
	display: flex;
	align-items: center;
	z-index: 1;
	right: 0;
	cursor: pointer;
}

.wrap-hardware .hardware > .wrap .sliders .slider {
	width: 225px;
	min-width: 225px;
    margin-right: 10px;
	display: flex;
    flex-direction: column;
	cursor: pointer;
}

@media (min-width: 1150px){
	.wrap-hardware .hardware > .wrap .sliders .slider {
		width: 295px;
		margin-right: 20px;
		min-width: 295px;
	}
}

.wrap-hardware .hardware > .wrap .sliders .slider > img {
    height: 320px;
    width: 100%;
    object-fit: cover;
    max-height: 320px;
	user-select: none;
}

@media (min-width: 1150px){
	.wrap-hardware .hardware > .wrap .sliders .slider > img {
		height: 400px;
		min-height: 400px;
		width: 100%;
	}
}

/* block 9 */
@media (min-width: 1150px){
	.block_9 {
		display: flex;
		justify-content: center;
	}
}

.block_9 > .wrap {
    padding: 70px 0;
}

@media (min-width: 1150px){
	.block_9 > .wrap {
		max-width: 1240px;
		padding: 0;
	}
}

.block_9 > .wrap > .top {
	padding: 0 20px 50px;
}

@media (min-width: 1150px){
	.block_9 > .wrap > .top {
		max-width: 740px;
		padding: 100px 80px 65px;
	}
}

.block_9 > .wrap > .top > .name {
	font-weight: 300;
	font-size: 25px;
	line-height: 120%;
	color: #1A2030;
	margin: 0;
}

@media (min-width: 1150px){
	.block_9 > .wrap > .top > .name {
		font-size: 40px;
		line-height: 135%;
		display: flex;
		flex-direction: column;
	}
}

.block_9 > .wrap > .top > .name > h2 {
    margin: 0;
	font-size: 25px;
	line-height: 120%;
	color: #1A2030;
}

@media (min-width: 1150px){
	.block_9 > .wrap > .top > .name > h2 {
		font-size: 40px;
		line-height: 135%;
		display: flex;
		flex-direction: column;
	}
}


.block_9 > .wrap > .top > .name > span {
	font-weight: 700;
}

@media (min-width: 1150px){}

.block_9 > .wrap > .top > .desc {
	font-weight: 300;
	font-size: 15px;
	line-height: 150%;
	color: #1A2030;
	margin-top: 40px;
}

@media (min-width: 1150px){
	.block_9 > .wrap > .top > .desc {
		font-size: 15px;
		line-height: 150%;
		margin-top: 5px;
	}
}

@media (min-width: 1150px){
	.block_9 > .wrap > .center {
		display: flex;
	}
}

.block_9 > .wrap > .center > .left {
    background: #1A2030;
	padding: 40px 40px 40px 20px;
}

@media (min-width: 1150px){
	.block_9 > .wrap > .center > .left {
		padding: 40px 125px 40px 100px
	}
}

.block_9 > .wrap > .center > .left > .wrap {
    display: flex;
	margin-top: 15px;
}

@media (min-width: 1150px){}

.block_9 > .wrap > .center > .left > .wrap:first-of-type {
    margin-top: 0;
}

@media (min-width: 1150px){}

.block_9 > .wrap > .center > .left > .wrap > .icon {
    font-weight: 600;
    font-size: 30px;
    line-height: 36px;
    color: #FFDD2D;
}

@media (min-width: 1150px){}

.block_9 > .wrap > .center > .left > .wrap > .name {
    font-weight: 400;
    font-size: 15px;
    line-height: 150%;
    color: #FFFFFF;
	margin-left: 20px;
}

@media (min-width: 1150px){
	.block_9 > .wrap > .center > .left > .wrap > .name {
		font-weight: 300;
	}
}

.block_9 > .wrap > .center > .right {
    padding: 40px 20px 0;
}

@media (min-width: 1150px){
	.block_9 > .wrap > .center > .right {
		margin: 0 0 0 100px;
		padding: 0;
	}
}

.block_9 > .wrap > .center > .right > .name {
	margin-top: 15px;
	font-weight: 400;
	font-size: 15px;
	line-height: 150%;
	color: #1A2030;
}

@media (min-width: 1150px){
	.block_9 > .wrap > .center > .right > .name {
		font-size: 20px;
	}
}

.block_9 > .wrap > .center > .right > .wrap {
    margin-top: 35px;
}

.block_9 > .wrap > .center > .right > .wrap > .name {
	margin-top: 20px;
	font-weight: 300;
	font-size: 15px;
	line-height: 150%;
	color: #1A2030;
}

.block_9 > .wrap > .bottom {
    padding: 80px 20px 0;
}

@media (min-width: 1150px){
	.block_9 > .wrap > .bottom {
		display: flex;
		justify-content: flex-end;
		padding: 80px 0;
	}
}

.block_9 > .wrap > .bottom > .btn {
    background: #FFDD2D;
    border-radius: 5px;
    font-weight: 400;
    font-size: 20px;
    color: #1A2030;
    padding: 20px 25px;
    text-align: center;
	text-decoration: none;
}

@media (min-width: 1150px){
	.block_9 > .wrap > .bottom > .btn {
		padding: 20px 100px;
	}
}
</style>