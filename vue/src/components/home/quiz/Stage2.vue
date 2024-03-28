<template>
    <div data-quiz-step class="b-quiz__quiz__item active">
        <div class="b-quiz__quiz__item__title">Какая услуга вас интересует?</div>
        <div class="b-form__select__group">
            
            <label v-for="(service, index) in services" :key="index" @click="props.updateService(service)">
                <input type="radio" name="step2" :value="service">
                <span>{{ service }}</span>
            </label>


        </div>
        <div class="b-quiz__quiz__description">В случае обмена, мы предоставляем готовую КПП после капитального ремонта, взамен вашей, вышедшей из строя.</div>

        <label data-hidden-input="main_variant" class="b-form__input__text">
            <input name="main_variant" value="" placeholder="Введите свой вариант">
        </label>
    </div>
</template>


<script setup>
    import { defineProps } from 'vue';

    const props = defineProps({
        selectedService: String,
        services: Array,
        updateService: Function,
    });

</script>

