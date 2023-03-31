<template>
  <ProfileAvatar />
  <nav-bar></nav-bar>
</template>

<script>
import ProfileAvatar from "@/components/Dashboard/ProfileAvatar.vue";

export default {
  name: "ProfileView",
  components: {
    ProfileAvatar,
  },
};
</script>
