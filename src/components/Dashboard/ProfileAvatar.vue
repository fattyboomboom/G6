<template>
  <v-card class="avatar" border="true">
    <center>
      <v-avatar
        image="https://pbs.twimg.com/profile_images/1237550450/mstom_400x400.jpg"
      >
      </v-avatar>
    </center>
    <v-divider thickness="2"></v-divider>
    <h2>Name: {{ name }}</h2>

    <v-divider thickness="2"></v-divider>
    <h2>Major: {{ major }}</h2>
  </v-card>
</template>

<script>
export default {
  name: "ProfileAvatar",
  props: {
    name: {
      type: String,
      required: true,
      default: "Tom",
    },
    major: {
      type: String,
      required: false,
      default: "Undecided",
    },
  },
  data() {
    return {};
  },
};
</script>

<style scoped>
.avatar {
  position: fixed;
  margin-left: 6%;
  margin-top: 1%;
  background-color: #000000;
  width: 25%;
}
.v-avatar {
  width: 50%;
  height: auto;
  margin: 0 auto 1rem;
}

body {
  background-color: #003049;
}

.v-divider {
  background-color: white;
}

h2 {
  color: white;
  font-size: 1.5rem;
  margin: 0.5rem 0;
  text-align: left;
}
</style>
