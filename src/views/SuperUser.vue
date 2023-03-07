<template>
    <nav-bar></nav-bar>
      <v-container class="ml-16" style="background-color:transparent; display: flex; justify-content: center; height:100px;" >
        <v-btn class="banner-button" style="color:black; background-color: transparent; font-size: 30px;" elevation="0">
          Add Class
        </v-btn>
  
        <v-btn class="banner-button" style="color:black; background-color: transparent; font-size: 30px;" elevation="0">
          Manage Classes
        </v-btn>
  
        <v-btn class="banner-button" style="color:black; background-color: transparent; font-size: 30px;" elevation="0">
          Manage Moderators
        </v-btn>
      </v-container>
    
  
    <v-container fluid>
      <v-card>
        <v-card-title class="justify-center">Reported Posts</v-card-title>
        <v-card-text>
          <v-simple-table>
            <thead>
              <tr>
                <th class="text-left">ID</th>
                <th class="text-left">Author</th>
                <th class="text-left">Date</th>
                <th class="text-left">Content</th>
                <th class="text-center">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="post in posts" :key="post.post_id">
                <td>{{ post.post_id }}</td>
                <td>{{ post.name }}</td>
                <td>{{ post.post_date }}</td>
                <td>{{ post.post_text }}</td>
                <td class="text-right">
                  <v-btn color="red" class="mr-3">Delete</v-btn>
                  <!-- <v-btn color="primary">Repeal</v-btn> -->
                </td>
              </tr>
              <tr>
                <td colspan="5" class="border-top py-3"></td>
              </tr>
            </tbody>
          </v-simple-table>
        </v-card-text>
      </v-card>
    </v-container>
  </template>
  
  <script>
  import axios from "axios";
  import { ref } from "vue";
  
  export default {
    name: "SuperUserDash",
    setup() {
      const posts = ref([]);
      const error = ref(null);
      axios
        .get("http://localhost:5000/api/post")
        .then((response) => {
          posts.value = response.data;
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
      return { posts, error };
    },
  };
  </script>
  
  <style scoped>
  .v-card {
    max-width: 80%;
    margin: 50px auto;
  }
  
  td {
    padding: 10px;
  }
  
  .v-btn {
    margin: 0 10px;
  }
  
  .text-right {
    text-align: right;
  }
  
  tbody tr {
    border-top: 1px solid lightgray;
  }
  
  .black {
    background-color: #000000;
  }
  </style>