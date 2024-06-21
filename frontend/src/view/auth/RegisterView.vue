<template>
    <div>
        <AuthHeader current_page="register"></AuthHeader>
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
                            <b-form-input id="input-2" v-model="form.password" type="password" placeholder="Enter name"
                                required></b-form-input>
                        </b-form-group>
                        <b-form-group id="input-group-2" label="Re-Password:" label-for="input-2">
                            <b-form-input id="input-2" v-model="form.re_password" type="text"
                                placeholder="Re-Enter Password" required></b-form-input>
                        </b-form-group>
                        <b-form-group id="input-group-2" label="Select Role:" label-for="input-2">
                            <b-form-radio-group id="radio-group-1" v-model="form.role_selected" :options="options"
                                :aria-describedby="ariaDescribedby" name="radio-options"></b-form-radio-group>
                        </b-form-group>
                        <b-button type="submit" variant="primary">Register</b-button>&nbsp; &nbsp; 
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
import axios from 'axios'

export default {
    name: "LoginPage",
    components:{
        AuthHeader
    },
    data() {
        return {
            form: {
                email: '',
                password: '',
                re_password:'',
                role_selected: '',
            },
            options: [
                { text: 'Admin', value: 'watcher' },
                { text: 'Normal User', value: 'admin' },
                
            ]
        }
    },
    methods: {
        onSubmit(event) {
            event.preventDefault()
            console.log(this.form.email, this.form.password, this.form.re_password)
            if (!this.form.email || !this.form.password || !this.form.re_password){
                alert("Please enter all the fields");
                return;
            }
            if (!this.form.role_selected){
                alert("Please select role");
                return;
            }
            if (this.form.password != this.form.re_password){
                alert("Passwords don't match!!")
            }

            axios.post("http://127.0.0.1:8081/api/register", {
                user_mail: this.form.email,
                password: this.form.password,
                role: this.form.role_selected
            }).then((response) => {
                console.log(response)
                if (response.data.status == "success"){
                    alert("Successfully Registered!!");
                    this.$router.push("/login");
                }
                if (response.data.status == "failed"){
                    alert(response.data.message);
                    this.onReset();
                }
            }).catch((error) => {
                console.error(error);
                alert("An error occurred while registering the user")
            })


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

<style></style>