// // В вашей директиве.js
// function isVisible(el) {
//     const rect = el.getBoundingClientRect();
//     return (rect.top <= window.innerHeight && rect.bottom >= 0);
// }

// export default {
//     mounted(el) {
//         const handleScroll = () => {
//         if (isVisible(el)) {
//             el.classList.add('visible');
//         }
//         };
//         window.addEventListener('scroll', handleScroll);
//         handleScroll();  // Для проверки при инициализации
//     },
//     unmounted(el) {
//         window.removeEventListener('scroll', el.__vueScrollHandler);
//     },
// };

export default {
    mounted(el, binding) {
      const options = {
        // Настройки IntersectionObserver, например:
        root: null,  // относительно вьюпорта
        threshold: 0.1  // элемент должен быть виден хотя бы на 10%
      };
  
      const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            binding.value();  // вызываем функцию, переданную в директиву
            observer.unobserve(el);  // перестаем наблюдать за элементом
          }
        });
      }, options);
  
      observer.observe(el);
    }
  };