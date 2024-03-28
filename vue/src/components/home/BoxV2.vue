<template>
    <div class="box">

        <div @click="close" class="back"></div>

        <div class="wrap">

            <div @click="close" class="close">
                <svg width="13" height="19" viewBox="0 0 13 19" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M7.807881 9.5L12.0453 5.69406L12.9045 4.9092C13.0313 4.79342 13.0313 4.60527 12.9045 4.48949L11.9852 3.64971C11.8584 3.53393 11.6525 3.53393 11.5257 3.64971L6.5 8.24051L1.47428 3.64934C1.34753 3.53355 1.14156 3.53355 1.01481 3.64934L0.0950625 4.48912C-0.0316875 4.6049 -0.0316875 4.79305 0.0950625 4.90883L5.12119 9.5L0.0950625 14.0908C-0.0316875 14.2066 -0.0316875 14.3947 0.0950625 14.5105L1.01441 15.3503C1.14116 15.4661 1.34712 15.4661 1.47387 15.3503L6.5 10.7595L10.6665 14.5654L11.5257 15.3503C11.6525 15.4661 11.8584 15.4661 11.9852 15.3503L12.9045 14.5105C13.0313 14.3947 13.0313 14.2066 12.9045 14.0908L7.87881 9.5Z" fill="white"/>
                </svg>
            </div>
            
            <img v-if="active" :src="require(`@/assets/img/box-docs/${active.img}`)" @click="next" class="image"/>

        </div>
    </div>
</template>

<script>

import { computed, onMounted, ref } from 'vue'
import { useStore } from 'vuex'


export default {

    props: {
        close: Function,
        object: Object,
        sliders: Array,
    },
  
    setup(props){

        const store = useStore()
        const domain = computed(() => store.getters.domain)

        const active = ref(null)

        onMounted(() => {
            active.value = props.object
        })

        function next() {
            // Find the index of the current active slide
            let currentIndex = props.sliders.findIndex(slider => slider.id === active.value.id);

            // Increment the index (go to the next slide)
            currentIndex++;

            // If we're at the end of the sliders array, go back to the beginning
            if (currentIndex >= props.sliders.length) {
                currentIndex = 0;
            }

            // Set the new active slide
            active.value = props.sliders[currentIndex];
        }

        return { domain, active, next, }

    },

}
</script>

<style scoped>

.box {
    position: fixed;
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
    z-index: 2;
    padding: 1em;
    display: flex;
    align-items: center;
    justify-content: center;
}

.box > .back {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.64);
}

.box > .wrap {
    z-index: 3;
    position: relative;
    height: 100%;
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;

}

.box > .wrap .close {
    display: flex;
    justify-content: flex-end;
    margin-top: 4em;
    align-self: flex-end;
}

.box > .wrap .close svg {
    cursor: pointer;
    width: 2em;
    height: 2em;
}

.box > .wrap > .image {
    height: 80%;
    object-fit: contain;
    margin-bottom: 1em;
    cursor: pointer;
}

</style>