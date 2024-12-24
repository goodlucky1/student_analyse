import CourseCpn from "@/components/CourseCpn.vue";
import HomeCpn from "@/components/HomeCpn.vue";
import IndexCpn from "@/components/IndexCpn.vue";
import InfoCpn from "@/components/InfoCpn.vue";
import LoginCpn from "@/components/LoginCpn.vue";
import MyContent from "@/components/MyContent.vue";
import MyMenu from "@/components/MyMenu.vue";
import ScoreCpn from "@/components/ScoreCpn.vue";

import { createRouter,createWebHashHistory } from "vue-router";

const routes=[
    {
        name:"index",
        path:"/index",
        component:IndexCpn,
        children:[
            {
                path:"/home",
                name:"home",
                component:HomeCpn
            },
            {
                path:"/info",
                component:InfoCpn
            },
            {
                path:"/score",
                component:ScoreCpn
            },
            {
                path:"/course",
                component:CourseCpn
            },
            
        ]
    },
    {
        name:"menu",
        path:"/menu",
        component:MyMenu
    },
    {
        name:"content",
        path:"/content",
        component:MyContent
    },
    {
        path:"/",
        redirect:"/index",
       
    },
    {
        path:"/info",
        name:"info",
        component:InfoCpn
    },
    {
        path:"/login",
        component:LoginCpn
    }

]



const router=createRouter({
    history:createWebHashHistory(),
    routes,
})

export default router