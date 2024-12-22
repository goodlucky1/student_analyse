import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import  bs from 'bootstrap/dist/css/bootstrap.min.css';
/* global layer */
const app= createApp(App)
app.config.globalProperties.$layer = layer;
app.use(store).use(router).use(bs).mount('#app')
