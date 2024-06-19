import { BootstrapVueIcons, BootstrapVue, FormFilePlugin, ImagePlugin } from 'bootstrap-vue'

import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import FlashMessage from '@smartweb/vue-flash-message'

Vue.config.productionTip = false

Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);
Vue.use(FormFilePlugin);
Vue.use(ImagePlugin);

Vue.use(FlashMessage,{
  name: "flashMessage",
  tag: "FlashMessage",
  time: 4000,
  strategy: "multiple"
});



new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')

// store.subscribe((mutation, state) => {
//   localStorage.setItem('store, JSON.stringify(state)')
// })