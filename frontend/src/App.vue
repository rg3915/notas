<template>
  <div id="app">
    <Navbar/>
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <Grades/>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import Navbar from './components/Navbar.vue'
import Grades from './components/Grades.vue'

export default {
  name: 'app',
  components: {
    // HelloWorld,
    Navbar,
    Grades
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
