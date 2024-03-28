
<template>
    <div data-quiz-step class="b-quiz__quiz__item active">
        <div class="b-quiz__quiz__item__title">Какой у вас трактор (тракторы)?</div>
        <div class="b-form__select__group">
            <label v-for="(tractor, index) in tractors" :key="index" @click="props.updateTractor(tractor)">
                <input type="radio" name="step2">
                <span>{{ tractor }}</span>
            </label>
        </div>
        <label class="b-form__input__text active">
            <input name="main_variant" v-model="customTractor" placeholder="Введите свой вариант">
        </label>
    </div>
</template>

<script setup>
    import { defineProps, ref, watch } from 'vue';

    const props = defineProps({
        selectedTractor: String,
        tractors: Array,
        updateTractor: Function,
    });

    const customTractor = ref('');
    watch(customTractor, () => {
        props.updateTractor(customTractor.value)
    })

</script>