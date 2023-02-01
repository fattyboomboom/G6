<template>

  <DashboardFriends />
  <MyClasses />
  <ProfileAvatar />
  <WallPost />
  <NavBar />
  
</template>

<script>
// @ is an alias to /src
import DashboardFriends from "./DashboardFriends.vue";
import MyClasses from "./MyClasses.vue";
import ProfileAvatar from "./ProfileAvatar.vue";
import WallPost from "./WallPost.vue";
import NavBar from "@/globalcomponents/NavBar.vue";

export default {
  name: "HomeView",
  components: {
    DashboardFriends,
    MyClasses,
    ProfileAvatar,
    WallPost,
    NavBar,
  },
};
</script>

<style scoped>
body {
  background-color: #fdf0d5;
}
</style>
