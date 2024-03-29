<template>
    <div data-quiz-step class="b-quiz__quiz__item active">
        <div class="b-quiz__quiz__item__title">Позвоним вам и сообщим цену по вашим параметрам</div>
        <label class="b-form__input__text">
            <span>Ваш номер</span>
            <input
              name="main_phone"
              v-model="phone"
              v-mask="['+7(###) ###-##-##']"
              type="tel"
              placeholder="+7 123 456 78 90"
            />
        </label>

        <label data-hidden-input="main_variant" class="b-form__input__text">
            <input name="main_variant"  placeholder="Введите свой вариант">
        </label>

    </div>
</template>


<script setup>
    import { defineProps, ref, watch } from 'vue';

    const props = defineProps({
        updatePhone: Function,
    });


    const phone = ref('+7');
    watch(phone, () => {
        props.updatePhone(phone.value)
    })

</script>
