import LoginPage from "@/components/content/LoginPage.vue";
import RegistryPage from "@/components/content/RegistryPage.vue";
import { createRouter, createWebHashHistory } from "vue-router";

const router= createRouter({
    history:createWebHashHistory(),
    routes:[
        
        {
            name:"main",
            path:"/",
            redirect:"/login"
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

    ]
})

export default router