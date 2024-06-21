import Vue from "vue";
import VueRouter from "vue-router";


import HelloWorld from "@/components/HelloWorld.vue";
import LoginView from "@/view/auth/LoginView.vue";
import RegisterView from "@/view/auth/RegisterView"



Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'HelloWorld',
        component: HelloWorld,
    },
    {
        path: "/login",
        name:'LoginView',
        component: LoginView
    },
    {
        path: "/register",
        name:'RegisterView',
        component: RegisterView
    },
    {
        path: '*',
        redirect: '/',
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
})

export default router;
