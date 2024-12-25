import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import zhCn from 'element-plus/es/locale/lang/zh-cn'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import App from './App.vue'
import router from './router'
import layer from 'layui'
import store from './store'
import  bs from 'bootstrap/dist/css/bootstrap.min.css';

const app=createApp(App);
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
  }

app.config.globalProperties.$layer = layer;
app.use(router)
app.use(store)
 app.use(bs)
app.use(ElementPlus,{locale:zhCn})
app.mount("#app")
