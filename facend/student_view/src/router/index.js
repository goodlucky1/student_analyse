import LoginPage from "@/components/content/LoginPage.vue";
import RegistryPage from "@/components/content/RegistryPage.vue";
import { createMemoryHistory, createRouter, createWebHashHistory } from "vue-router";

const router= createRouter({
    history:createMemoryHistory(),
    routes:[
        
        {
            name:"main",
            path:"/",
            component:LoginPage
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
        }

    ],
    linkExactActiveClass:"active_router"
})

export default router