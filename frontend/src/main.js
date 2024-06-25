import { IconsPlugin, BootstrapVue} from 'bootstrap-vue'

import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import FlashMessage from '@smartweb/vue-flash-message'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue'

Vue.config.productionTip = false

Vue.use(BootstrapVue);
Vue.use(IconsPlugin)


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

store.subscribe((mutation, state) => {
  localStorage.setItem('store', JSON.stringify(state))
})