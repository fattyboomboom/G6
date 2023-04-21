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
import { db, auth } from "@/firebase";
import {
  collection,
  addDoc,
  serverTimestamp,
  doc,
  getDoc,
} from "firebase/firestore";

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
      if (this.postContent.trim() === "") {
        // Alert the user that the post content cannot be empty
        alert("Post content cannot be empty");
        return;
      }
      // Get a reference to the current user's document
      const userRef = doc(db, "users", auth.currentUser.uid);

      // Get the user's profile picture URL, first name, and last name from their document
      const userDoc = await getDoc(userRef);
      const data = userDoc.data();
      const profilePicture = data.profilePicture;
      const firstName = data.FirstName;
      const lastName = data.LastName;

      // Add the post to the "posts" collection with the profile picture URL, first name, and last name included
      const res = await addDoc(collection(db, "posts"), {
        content: this.postContent.replace(
          /fuck|shit|bitch|asshole|ass/gi,
          " **** "
        ),
        PostDate: serverTimestamp(),
        uid: auth.currentUser.uid,
        isDeleted: false,
        profilePicture: profilePicture,
        FirstName: firstName,
        LastName: lastName,
      });
      console.log(res);

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
