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
  import {  db, auth } from '@/firebase/index'
  import { collection, addDoc, serverTimestamp } from "firebase/firestore"
  import { ref } from 'vue'
  import { useRoute } from "vue-router";
  export default {
    name: "ClassPost",
    setup(){
   
    },
    data() {
    const route = useRoute();
    const classPrefix= ref(route.params.classPrefix);
    const classNumber= ref(route.params.classNumber);
      return {
        postContent: "",
        classPrefix,
        classNumber,
        
      };
    },
    methods: {
      async submitPost() {
  try {
    if (this.postContent.trim() !== "") {
      const res = await addDoc(collection(db, "posts"), {
        content: this.postContent,
        PostDate: serverTimestamp(),
        uid: auth.currentUser.uid,
        classPrefix: this.classPrefix,
        classNumber: this.classNumber,
        FirstName: auth.currentUser.displayName.split(' ')[0],
        LastName: auth.currentUser.displayName.split(' ')[1],
        postType: "post",
        likes: []
      });
      console.log(res);

      this.postContent = "";
    } else {
      console.log("Post content is empty.");
    }
  } catch (error) {
    console.error("Error submitting post:", error);
  }
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