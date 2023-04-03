<template>
  <v-row>
    <v-col class="profile-page">
      <ProfilePage />
      <MyClassesProfile />
    </v-col>
    <v-col  >
      <WolfFeedProfile class="wolf-feed" />
    </v-col>
  </v-row>
  <nav-bar></nav-bar>
</template>

<script>
// import ProfileAvatar from "@/components/Dashboard/ProfileAvatar.vue";
import ProfilePage from "@/components/Profile/ProfilePage.vue";
import MyClassesProfile from "@/components/Profile/MyClassesProfile.vue";
import WolfFeedProfile from "@/components/Profile/WolfFeedProfile.vue";

export default {
  name: "ProfileView",
  components: {
    WolfFeedProfile,
    ProfilePage,
    MyClassesProfile,
  },
};
</script>

<style scoped>
.wolf-feed {
  position: absolute;
  top: 5%;
  /* margin-right: 5%; */
  right: -10%;
  height: 90%;
  width: 80%;
  font-size: 15px;
}

.profile-page {
  position: absolute;
 
}


</style>
