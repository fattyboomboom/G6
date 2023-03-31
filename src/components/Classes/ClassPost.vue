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
        classNumber
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
          uid: auth.currentUser.uid,
          classPrefix: this.classPrefix,
          classNumber: this.classNumber
        });
         console.log(res)

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