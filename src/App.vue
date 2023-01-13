<template>
  <v-app class="app">
    <!-- <v-app-bar color="black"></v-app-bar> -->
    <Navbar></Navbar>
    <v-main>
      <!-- <ProfileAvatarVue name="Tom Anderson" major="Computer Science" />
      <WallPostVue />
      <MyClassesVue />
      <DashboardFriendsVue /> -->
    </v-main>
  </v-app>
</template>

<script>
// import HelloWorld from "./components/HelloWorld.vue";
import Navbar from "./components/NavBar.vue";
// import ProfileAvatarVue from "./components/ProfileAvatar.vue";
// import MyClassesVue from "./components/MyClasses.vue";
// import DashboardFriendsVue from "./components/DashboardFriends.vue";
// import WallPostVue from "./components/WallPost.vue";

export default {
  name: "App",

  components: {
    // WallPostVue,
    Navbar,
    // ProfileAvatarVue,
    // MyClassesVue,
    // DashboardFriendsVue,
  },
};
</script>

<style>
.app {
  background-color: whitesmoke;
}
</style>
