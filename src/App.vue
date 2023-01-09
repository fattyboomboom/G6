<template>
  <v-app>
    <!-- <v-app-bar color="black"></v-app-bar> -->
    <Navbar></Navbar>
    <v-main>
      <ProfileAvatarVue name="Tom Anderson" major="Computer Science" />
    </v-main>
  </v-app>
</template>

<script>
// import HelloWorld from "./components/HelloWorld.vue";
import Navbar from "./components/NavBar.vue";
import ProfileAvatarVue from "./components/ProfileAvatar.vue";

export default {
  name: "App",

  components: {
    // HelloWorld,
    Navbar,
    ProfileAvatarVue,
  },

  data: () => ({
    //
  }),
};
</script>
