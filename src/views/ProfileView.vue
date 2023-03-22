<template>
 
  <DashboardFriends />
  <OtherProfileAvatar />
  <nav-bar></nav-bar>
  <WolfFeed />

</template>

<script>
// @ is an alias to /src
import DashboardFriends from "@/components/Dashboard/DashboardFriends.vue";
import OtherProfileAvatar from "@/components/Dashboard/OtherProfileAvatar.vue";
import WolfFeed from "@/components/Dashboard/WolfFeed.vue";

export default {
name: "ProfileView",
components: {
  DashboardFriends,
  OtherProfileAvatar,
  WolfFeed,
},
};
</script>

<style scoped>
body {
background-color: #fdf0d5;
}
</style>
