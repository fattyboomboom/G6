<template>
 
    <DashboardFriends />
    <MyClasses />
    <ProfileAvatar />
    <WallPost />
    <nav-bar></nav-bar>
    <WolfFeed />
 
</template>

<script>
// @ is an alias to /src
import DashboardFriends from "@/pages/dashboard/DashboardFriends.vue";
import MyClasses from "@/pages/dashboard/MyClasses.vue";
import ProfileAvatar from "@/pages/dashboard/ProfileAvatar.vue";
import WallPost from "@/pages/dashboard/WallPost.vue";
import WolfFeed from "@/pages/dashboard/WolfFeed.vue";

export default {
  name: "HomeView",
  components: {
    DashboardFriends,
    MyClasses,
    ProfileAvatar,
    WallPost,
    WolfFeed,
  },
};
</script>

<style scoped>
body {
  background-color: #fdf0d5;
}
</style>