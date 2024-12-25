import CourseCpn from "@/components/CourseCpn.vue";
import HomeCpnr from "@/components/dzy/views/HomeCpnr.vue";
import IndexCpn from "@/components/IndexCpn.vue";
import InfoCpn from "@/components/InfoCpn.vue";
import MyContent from "@/components/MyContent.vue";
import MyMenu from "@/components/MyMenu.vue";
import ScoreCpn from "@/components/ScoreCpn.vue";
import LoginEdge from "@/components/wjx/views/LoginEdge.vue";
import RegisteCpnr from "@/components/wjx/views/RegisteCpnr.vue";

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
                component:HomeCpnr
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
        redirect:"/login",
       
    },
    {
        path:"/info",
        name:"info",
        component:InfoCpn
    },
    {
        path:"/login",
        component:LoginEdge,
        
    },
    {
        path:"/register",
        component:RegisteCpnr
    }

]



const router=createRouter({
    history:createWebHashHistory(),
    routes,
})



export default router