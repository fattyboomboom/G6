<template>
  <v-col cols="3">
    <v-card color="black" position="absolute" border="true"
      ><center>
        <v-avatar
          image="https://pbs.twimg.com/profile_images/1237550450/mstom_400x400.jpg"
          size="200"
        >
        </v-avatar>
      </center>
      <v-divider color="white" thickness="2"></v-divider>
      <h2>Name: {{ name }}</h2>

      <v-divider color="white" thickness="2"></v-divider>
      <h2>Major: {{ major }}</h2>
    </v-card>
  </v-col>
</template>

<script>
export default {
  name: "ProfileAvatar",
  props: ["name", "major"],
  data() {
    return {};
  },
};
</script>
