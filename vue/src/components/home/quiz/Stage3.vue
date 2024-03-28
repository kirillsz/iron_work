<template>
    <div data-quiz-step class="b-quiz__quiz__item active">
        <div class="b-quiz__quiz__item__title">Как срочно Вам нужна КПП?</div>
        <div class="b-form__select__group">

            <label v-for="(service, index) in times" :key="index" @click="props.updateTime(service)">
                <input type="radio" name="step2" :value="service">
                <span>{{ service }}</span>
            </label>

        </div>

        <label data-hidden-input="main_variant" class="b-form__input__text">
            <input name="main_variant" value="" placeholder="Введите свой вариант">
        </label>
    </div>
</template>


<script setup>
    import { defineProps } from 'vue';

    const props = defineProps({
        selectedTime: String,
        times: Array,
        updateTime: Function,
    });

</script>

