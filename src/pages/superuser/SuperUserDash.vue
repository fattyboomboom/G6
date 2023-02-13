<template>
  <v-banner 
        :sticky="true"
        lines="two"
        height="80"
        class="no-border"
        style=" background-color:black; display: flex; justify-content: center;"
      >
      <v-container class="ml-16">
          <v-btn class="banner-button" style="color:white; background-color: transparent; font-size: 30px;" elevation="0" >
            Add Class
          </v-btn>
  
          <v-btn class="banner-button" style="color:white; background-color: transparent; font-size: 30px;" elevation="0" >
            Manage Classes
          </v-btn>
  
          <v-btn class="banner-button" style="color:white; background-color: transparent; font-size: 30px;" elevation="0" >
            Manage Moderators
          </v-btn>
        </v-container>
      </v-banner>
  
  
  
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
              <tr v-for="post in reportedPosts" :key="post.id">
                <td>{{ post.id }}</td>
                <td>{{ post.author }}</td>
                <td>{{ post.date }}</td>
                <td>{{ post.content }}</td>
                <td class="text-right">
                  <v-btn color="red" class="mr-3">Delete</v-btn>
                  <v-btn color="primary">Repeal</v-btn>
                </td>
              </tr>
              <tr><td colspan="5" class="border-top py-3"></td></tr>
            </tbody>
          </v-simple-table>
        </v-card-text>
      </v-card>
    </v-container>
  </template>
  
  
  <script>
  export default {
    name: "SuperUserDash",
    data() {
      return {
        isBannerVisible: true,
        reportedPosts: [
          {
            id: 1,
            author: "Olivia M.",
            date: "2022-01-01",
            content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
          },
          {
            id: 2,
            author: "Marcus B.",
            date: "2022-02-01",
            content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
          },
          {
            id: 3,
            author: "John S.",
            date: "2022-03-01",
            content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
          },
          {
            id: 4,
            author: "Jared L.",
            date: "2022-03-01",
            content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
          },
          {
            id: 5,
            author: "Quincy J.",
            date: "2022-03-01",
            content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
          },
          {
            id: 6,
            author: "Arthur M.",
            date: "2022-03-01",
            content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
          },
          {
            id: 7,
            author: "Nick B.",
            date: "2022-03-01",
            content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
          },
          {
            id: 8,
            author: "Jerry S.",
            date: "2022-03-01",
            content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
          },
          {
            id: 9,
            author: "Gabriel I.",
            date: "2022-03-01",
            content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
          },
          {
            id: 10,
            author: "George L.",
            date: "2022-03-01",
            content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
          },
        ]
      };
    }
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