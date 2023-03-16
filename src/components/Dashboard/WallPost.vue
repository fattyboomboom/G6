<template>
  <v-container>
    <v-textarea
      clearable
      clear-icon="mdi-close-circle"
      label="Post to your wall"
      variant="outlined"
      no-resize=""
      v-model="postContent"
    ></v-textarea>
    <v-btn @click="submitPost" variant="outlined">Submit</v-btn>
  </v-container>
</template>

<script>
// import axios from "axios";
import {  db, auth } from '@/firebase'
import { collection, addDoc, serverTimestamp } from "firebase/firestore";

export default {
  name: "WallPost",
  data() {
    return {
      postContent: "",
    };
  },
  methods: {
    currentDate() {
      const current = new Date();
      const date =
        `${
          current.getMonth() + 1
        }/${current.getDate()}/${current.getFullYear()}` +
        " " +
        `${current.getHours()}:${current.getMinutes()}:${current.getSeconds()}`;
      return date;
    },

   async submitPost() {
      
      const res = await addDoc(collection(db, "posts"), {
        content: this.postContent,
        PostDate: serverTimestamp(),
        uid: auth.currentUser.uid
      });
       console.log(res)
      // axios
      //   .post("http://localhost:3000/posts", { content: this.postContent })
      //   .then((response) => {
      //     console.log("Post saved to database:", response.data);
      //   })
      //   .catch((error) => {
      //     console.error("Error saving post to database:", error);
      //   });

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
  margin-left: 35%;
}
</style>
