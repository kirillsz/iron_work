<template>
    <section class="b-quiz__wrapper g-wrapper">
        <div class="container">

            <div class="row just-sb align-ic">
                <div class="col-lg-6 col-sm-12">
                    <div class="b-quiz__title">Укажите параметры вашей КПП и получите цену ремонта</div>
                    <div class="b-quiz__img">
                        <img src="@/assets/img/shem_White_1.png" alt="">
                    </div>
                </div>


                <div class="col-lg-5 col-sm-12">
                    <div class="b-quiz__quiz" data-quiz>
                        <div class="b-quiz__quiz__progress">
                            <ul data-quiz-progress="true">
                                <li :class="{ active: currentStage >= 1 }"></li>
                                <li :class="{ active: currentStage >= 2 }"></li>
                                <li :class="{ active: currentStage >= 3 }"></li>
                                <li :class="{ active: currentStage >= 4 }"></li>
                            </ul>
                            <span>
                                <span>Шаг <i>{{ currentStage }}</i> из <i>4</i></span>
                            </span>
                        </div>

                        <div class="b-quiz__quiz__items" data-quiz-steps>

                            <Stage1 v-if="currentStage === 1" 
                                :selectedTractor="selectedTractor" 
                                :updateTractor="updateTractor"
                                :tractors="tractors"></Stage1>

                            <Stage2 v-if="currentStage === 2"
                                :selectedService="selectedService" 
                                :updateService="updateService"
                                :services="services"></Stage2>

                            <Stage3 v-if="currentStage === 3"
                                :selectedTime="selectedTime" 
                                :updateTime="updateTime"
                                :times="times"></Stage3>

                            <Stage4 v-if="currentStage === 4"
                                :phone="phone" 
                                :updatePhone="updatePhone"></Stage4>

                            
                            <Stage5 v-if="currentStage === 5"></Stage5>

                        </div>

                        <div class="b-quiz__quiz__control">
                            <button :class="['btn_white', currentStage === 1 ? 'd-none' : '']" @click="goToPrevStage" v-if="currentStage > 1"><span>Назад</span></button>
                            <button :class="['btn_primary', currentStage === 1 ? 'w-100' : '']" @click="goToNextStage" v-if="currentStage < 5">Далее</button>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </section>
</template>


<script setup>
    
    import { computed, ref } from 'vue'
    import { useStore } from 'vuex'

    import Stage1 from "@/components/home/quiz/Stage1.vue";
    import Stage2 from "@/components/home/quiz/Stage2.vue";
    import Stage3 from "@/components/home/quiz/Stage3.vue";
    import Stage4 from "@/components/home/quiz/Stage4.vue";
    import Stage5 from "@/components/home/quiz/Stage5.vue";



    const store         = useStore()
    const domain        = computed(() => store.getters.domain)
    const currentStage  = ref(1);

    const goToNextStage = async () => {

        if (currentStage.value < 5) currentStage.value++;

        if (currentStage.value == 5){
            await order()
        }

    };

    const goToPrevStage = () => {
        if (currentStage.value > 1) currentStage.value--;
    };


    //выбор трактора
    const tractors = [
        'К—700(А)', 'К—701', 'К—702 УДМ', 'К—703', 'К—744', 
        'ХТЗ Т—150(К)', 'ГМП «Амкодор»', 'L—34, L—35', 'Т—130/170', 'Свой вариант'
    ]
    const selectedTractor = ref('')
    function updateTractor(value){
        selectedTractor.value = value
    }


    //выбор услуги
    const services = [
    'Обмен', 'Покупка', 'Ремонт',
    ]
    const selectedService = ref('')
    function updateService(value){
        selectedService.value = value
    }

    //выбор времени
    const times = [
        'Очень срочно', '3-7 дней', '7-14 дней', 'В течение месяца', 'Интересуюсь на будущее',
    ]
    const selectedTime = ref('')
    function updateTime(value){
        selectedTime.value = value
    }

    const phone = ref('')
    function updatePhone(value){
        phone.value = value
    }



    function pop_up_close(){
        store.dispatch('update_pop_up', false)
    }

    async function order() {

        await fetch(`${domain.value}/api/order/create`, {
            method: 'POST',
            headers: { 
                'Content-Type':'application/json',
            },
            body: JSON.stringify({
                phone: phone.value,
                desc: `${selectedTractor.value},  ${selectedService.value}, ${selectedTime.value}`,
            })
        })

        pop_up_close()

    }



</script>