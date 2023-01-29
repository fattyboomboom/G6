<template>
  <v-app>
    <router-view></router-view>
    <NavBar></NavBar>
  </v-app>
</template>

<script>
import NavBar from "./globalcomponents/NavBar.vue";
export default {
  components: {
    NavBar,
  },
};
</script>

<style></style>
