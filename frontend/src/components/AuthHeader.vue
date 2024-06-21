<template>
    <b-navbar toggleable="lg" type="dark" variant="info">
        <b-navbar-brand href="#">NavBar</b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
            <b-navbar-nav>
                <router-link to="/login" class="link" v-if="current_page== 'register'">Login</router-link>
                <router-link to="/register" class="link" v-if="current_page== 'login'">Register</router-link>
            </b-navbar-nav>

        </b-collapse>


    </b-navbar>
</template>



<script>
export default {
    name: 'AuthHeader',
    props: {
        current_page: String,
    }
}
</script>



<style scoped>
.link {
    text-decoration: none;
    margin-left: 20px;
    color: white;
}
</style>