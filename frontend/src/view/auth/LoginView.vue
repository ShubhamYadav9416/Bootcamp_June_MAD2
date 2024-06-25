<template>
    <div>
        <auth-header current_page="login" ></auth-header>
        <b-container class="bv-example-row">
            <b-row>
                <b-col cols="2"></b-col>
                <b-col cols="8">
                    <b-form @submit="onSubmit" @reset="onReset">
                        <b-form-group id="input-group-1" label="Email address:" label-for="input-1"
                            description="We'll never share your email with anyone else.">
                            <b-form-input id="input-1" v-model="form.email" type="email" placeholder="Enter email"
                                required></b-form-input>
                        </b-form-group>

                        <b-form-group id="input-group-2" label="Password:" label-for="input-2">
                            <b-form-input id="input-2" v-model="form.password" type="password"
                                placeholder="Enter Password" required></b-form-input>
                        </b-form-group>
                        <b-button type="submit" variant="primary">Login</b-button>&nbsp; &nbsp;
                        <b-button type="reset" variant="warning">Reset</b-button>
                    </b-form>
                </b-col>
                <b-col cols="2"></b-col>


            </b-row>
        </b-container>
        <h1>Hello</h1>

    </div>
</template>

<script>

import AuthHeader from '../../components/AuthHeader.vue';
import axios from 'axios';
export default {
    name: "RegisterPage",
    components: {
       'auth-header' : AuthHeader,
    },
    data() {
        return {
            form: {
                email: '',
                password: '',
            },
            
        }
    },
    methods: {
        onSubmit(event) {
            event.preventDefault()
            if (!this.form.email || !this.form.password){
                alert("Please eneter email and password");
                return;
            }
            axios.post("http://127.0.0.1:8081/api/login",{
                user_mail: this.form.email,
                password: this.form.password
            })
            .then((response) => {
                if(response.data.status === "success"){
                    this.$store.dispatch("set_state_after_login", response.data);
                    this.flashMessage.success({
                        message: response.data.message
                    })

                    this.$router.push("/");
                }
                if(response.data.status === "failed"){
                    this.flashMessage.error({
                        message: response.data.message
                    })
                }
            }).catch((error) =>{
                console.error(error);
                // alert("An error occurred while login the user")
                this.flashMessage.error({
                    message: "Error occur will login the user"
                })
            }
            )
        },
        onReset(event) {
            event.preventDefault()
            // Reset our form values
            this.form.email = ''
            this.form.password = ''
        }
    }
}

</script>

<style scoped></style>