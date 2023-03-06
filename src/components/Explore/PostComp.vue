<template>

    <div id="app">
    <v-card
      v-for="post in posts"
      :key="post.name"
      class="ml-16 mt-8 text-white"
      color="#003049"
      max-width="800"
      :title="post.name"
    >
      <template v-slot:prepend>
        <v-avatar
          color="grey-darken-3"
          image="https://static.vecteezy.com/system/resources/thumbnails/009/292/244/small/default-avatar-icon-of-social-media-user-vector.jpg"
        ></v-avatar>
      </template>
  
      <v-card-text class="text-h5 py-2 text-white">
        {{ post.content }}
      </v-card-text>
  
      <v-card-actions>
        <v-list-item class="w-100 text-white">
          <div class="justify-self-start">
            <span class="subtitle me-2">{{ post.category }}</span>
          </div>
          <template v-slot:append>
            <div class="justify-self-end">
              <span class="subtitle me-2">{{ post.date }}</span>
              <span class="me-2">·</span>
              <span class="subtitle me-2">{{ post.time }}</span>
              <span class="me-2">·</span>
              <v-icon class="me-1" icon="mdi-heart"></v-icon>
              <span class="subheading me-2">{{ post.likes }}</span>
            </div>
          </template>
        </v-list-item>
      </v-card-actions>
    </v-card>
  </div>
  </template>
  
  <script>
import axios from 'axios';

export default {
  data() {
    return {
      posts:[],
    };
  },
  created() {
    axios.get('http://localhost:3000/posts')
  .then(response => {
    this.posts = response.data.posts;
  })
  .catch(error => {
    console.log(error);
  });

  },
};
</script>
  
  <style scoped></style>a