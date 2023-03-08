<template>
  <v-card class="avatar" border="true">
   
      <v-avatar
        image="https://pbs.twimg.com/profile_images/1237550450/mstom_400x400.jpg"
      >
      </v-avatar>
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
      default: "Tom",
    },
    major: {
      type: String,
  
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
  position: absolute;
  margin-left: 6%;
  margin-top: 1%;
  background-color: #003049;
  width: 25%;
  border: none;
  border-radius: 25px;
  box-sizing: border-box;
}
.v-avatar {
  width: 70%;
  height: auto;
  margin-left: 15%;
  margin-top: 2%;
  margin-bottom: 2%;
  
  
}
body {
  background-color: #003049;
}
.v-divider {
  color: #fdf0d5;
}
h2 {
  color: #fdf0d5;
  font-size: 1.5rem;
  margin-inline: 5%;
  text-align: left;
  line-height: 2;
}
</style>