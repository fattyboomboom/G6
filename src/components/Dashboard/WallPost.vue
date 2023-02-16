<template>
  <v-container>
    <v-textarea
      clearable
      clear-icon="mdi-close-circle"
      label="Post to your wall"
      variant="outlined"
      no-resize=""
      v-model="postContent"
      @keyup.enter="submitPost"
    ></v-textarea>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "WallPost",
  data() {
    return {
      postContent: "",
    };
  },
  methods: {
    submitPost() {
     
      axios
        .post("/api/posts", { content: this.postContent })
        .then((response) => {
          console.log("Post saved to database:", response.data);
        })
        .catch((error) => {
          console.error("Error saving post to database:", error);
        });

      // Clear the textarea content
      this.postContent = "";
    },
  },
};
</script>

<style scoped>
.v-container {
  width: 40%;

  /* margin-right: 25%; */
  margin-left: 33%;
}
</style>
