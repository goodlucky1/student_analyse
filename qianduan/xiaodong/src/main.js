import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import { ElMessage } from 'element-plus';
import 'element-plus/dist/index.css';


createApp(App).use(store).use(router).use(ElMessage).mount('#app')
