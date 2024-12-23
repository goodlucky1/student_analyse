import DataEharts from "@/components/content/dataEharts.vue";
import FileUpload from "@/components/content/FileUpload.vue";
import LoginPage from "@/components/content/LoginPage.vue";
import RegistryPage from "@/components/content/RegistryPage.vue";
import { createMemoryHistory, createRouter, createWebHashHistory } from "vue-router";

const router= createRouter({
    history:createMemoryHistory(),
    routes:[
        
        {
            name:"main",
            path:"/",
            component:FileUpload
        },
        {
            name:"login",
            path:"/login",
            component:LoginPage
        },
        {
            name:"registry",
            path:"/registry",
            component:RegistryPage
        },
        {
            name:"fileUpload",
            path:"/fileUpload",
            component:FileUpload
        },
        {
            name:"dataEharts",
            path:"/dataEharts",
            component:DataEharts
        }

    ],
    linkExactActiveClass:"active_router"
})

export default router