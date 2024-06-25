import Vue from "vue";
import VueRouter from "vue-router";
import store from "../store";
import * as common from "../assets/common.js"

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



router.beforeEach((to,from,next)=>{
    // redirect to login page if not logged in and if someone is trying to access a restricted page
    const publicPages = ['/login','/register'];
    const authRequired = !publicPages.includes(to.path);
    if (!store.getters.get_logged_status){
        store.commit('intialiseStore')
    }
    console.log(from)
    const logged_status = store.getters.get_logged_status
    if (authRequired && !logged_status){
        // this.flashMessage.error({
        //     message: "You are not allowed to access these routes please login"
        // })
        alert("You are not allowed to access these routes please login")
        return next(`/login`)
    }
    if (authRequired && logged_status){
        const role = store.getters.get_user_role

        if ((( role === 'watcher') && (common.WATCHER_ROUTES.includes(to.path)))  ||  (( role === 'admin') && (common.ADMIN_ROUTES.includes(to.path)))){
                return next()
            }
        else{
            alert("You are not allowed to access these routes please login")

                return next(`/${role}-home`)
        }

    }
    next();

})


export default router;
