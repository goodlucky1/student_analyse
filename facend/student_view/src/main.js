import { createApp } from 'vue'
import App from './App.vue'
import router from '@/router'
import axios from 'axios';

// axios.defaults.withCredentials = true
import * as echarts from "echarts"

const app = createApp(App).use(router)
app.mount('#app')


