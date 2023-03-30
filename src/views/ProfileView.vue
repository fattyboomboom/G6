<template>
  <v-row>
    <v-col class="profile-page">
      <ProfilePage />
    </v-col>
    <v-col  >
      <WolfFeed class="wolf-feed" />
    </v-col>
  </v-row>
  <nav-bar></nav-bar>
</template>

<script>
// import ProfileAvatar from "@/components/Dashboard/ProfileAvatar.vue";
import ProfilePage from "@/components/Profile/ProfilePage.vue";
import WolfFeed from "@/components/Dashboard/WolfFeed.vue";

export default {
  name: "ProfileView",
  components: {
    WolfFeed,
    ProfilePage,
  },
};
</script>

<style scoped>
.wolf-feed {
  position: absolute;
  top: 5%;
  /* margin-right: 5%; */
  right: -10%;
  height: 140%;
  width: 80%;
  /* box-shadow: 0 16px 56px rgba(0, 0, 0, 0.1), 0 16px 56px rgba(0, 0, 0, 0.1),
    0 16px 56px rgba(0, 0, 0, 0.1); */
  font-size: 15px;
}

.profile-page {
  position: absolute;
  /* top: 5%; */
  /* margin-right: 5%; */
  /* left: 0%; */
  /* height: 120%; */
  /* width: 150%; */
  /* transform: translateY(-50%); */
  /* font-size: 15px; */
}
</style>
