<template>
  <v-container>
    <v-textarea
      clearable
      clear-icon="mdi-close-circle"
      label="Post to your wall"
      variant="outlined"
      no-resize=""
    ></v-textarea>
  </v-container>
</template>

<script>
export default {
  name: "WallPost",
};
</script>

<style>
.v-container {
  width: 550px;
  color: black;
  position: absolute;
  left: 32%;
}
</style>
