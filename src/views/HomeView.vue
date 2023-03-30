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
import DashboardFriends from "@/components/Dashboard/DashboardFriends.vue";
import MyClasses from "@/components/Dashboard/MyClasses.vue";
import ProfileAvatar from "@/components/Dashboard/ProfileAvatar.vue";
import WallPost from "@/components/Dashboard/WallPost.vue";
import WolfFeed from "@/components/Dashboard/WolfFeed.vue";

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
