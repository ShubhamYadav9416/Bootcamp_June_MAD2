<template>
  <div id="app">
    <FlashMessage
    :position= "'left bottom'"
    style="font-size: 15px; position: relative; z-index: 10000;"
    />
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {},
  data() {
    return{};
  },
  methods:{},
  computed:{},
  beforeCreate(){
    console.log("Creating app.");
    this.$store.commit("intialiseStore")
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0;
}
</style>
