import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex)

export default new Vuex.Store({
    state:{
        user:{
            user_id: "",
            role: "",
            user_mail: "",
        },
        access_token: "",
        refresh_token: "",
        logger_status: false
    },
    getters:{
        get_user: function(state){
            return state.user
        },
        get_user_email: function(state){
            return state.user.user_mail
        },
        get_user_role: function(state){
            return state.user.role
        },
        get_user_id: function(state){
            return state.user.user_id
        },
        get_access_token: function(state){
            return state.access_token
        },
        get_refresh_token: function(state){
            return state.refresh_token
        },
        get_logged_status: function(state){
            return state.logger_status
        }
    },
    mutations:{
        intialiseStore(state){
            if (localStorage.getItem('store')){
                console.log('App creating. Store available in loacl storage.');
                this.replaceState(
                    Object.assign(state, JSON.parse(localStorage.getItem('store')))
                )
            }
        },
        SET_STATE_AFTER_LOGIN(state, payload){
            state.user.user_id = payload.user_id;
            state.user.user_mail = payload.user_mail;
            state.user.role = payload.role;
            state.access_token = payload.access_token;
            state.refresh_token = payload.refresh_token;
            state.logger_status = true;
        },
        SET_STATE_AFTER_LOGOUT(state){
            state.user.user_id = "";
            state.user.user_mail = "";
            state.user.role = "";
            state.access_token = "";
            state.refresh_token = "";
            state.logger_status = false
        },
        SET_STATE_AFTER_PROFILE_UPDATE(state, payload){
            state.user.user_mail = payload.user_mail;
        },

    },
    actions:{
        set_state_after_login(context, payload){
            context.commit('SET_STATE_AFTER_LOGIN', payload)
        },
        set_state_after_logout(context, payload){
            context.commit('SET_STATE_AFTER_LOGOUT', payload)
        },
        set_state_after_profile_update(context, payload){
            context.commit('SET_STATE_AFTER_PROFILE_UPDATE', payload)
        }
    },
    modules:{

    }
})
