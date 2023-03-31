<template>
  <v-container>
    <v-alert
      type="error"
      title="Error Submitting Post"
      closable
      close-label="Close"
      v-if="err"
      >{{ err }}</v-alert
    >
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
import axios from "axios";
import { auth, db } from "@/firebase/index";
import { getDoc, doc } from "firebase/firestore";
import ErrorService from "@/helperfuncts/errorHelper.js";
export default {
  name: "WallPost",
  data() {
    return {
      postContent: "",
      err: "",
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
      // const res = await addDoc(collection(db, "posts"), {
      //   content: this.postContent,
      //   PostDate: serverTimestamp(),
      //   uid: auth.currentUser.uid
      // });
      //  console.log(res)
      const userRef = doc(db, "users", auth.currentUser.uid);
      const userSnap = await getDoc(userRef);

      axios
        .post("http://localhost:5000/process", {
          content: this.postContent,
          uid: auth.currentUser.uid,
          lastname: userSnap.data().LastName,
        })
        .then((response) => {
          console.log("Post saved to database:", response.data);
        })
        .catch((err) => {
          let errorMessage = ErrorService.getErrorMessage(err.response.status);
          this.err = errorMessage;
          console.log(errorMessage);

          setTimeout(() => {
            this.err = "";
          }, 2000);
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
  margin-left: 35%;
}
</style>
