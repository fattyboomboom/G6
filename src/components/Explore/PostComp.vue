<template>
  <div id="app">
    <v-card
      v-for="post in posts"
      :key="post.id"
      class="ml-16 mt-8 text-white"
      color="#4A6FA5"
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
              <v-btn 
                class="me-1" 
                icon 
                :color="post.liked ? '#C1121F' : ''"
                @click="likePost(post.id)">
                <v-icon>{{ post.liked ? 'mdi-heart' : 'mdi-heart-outline' }}</v-icon>
              </v-btn>
              <span class="subheading me-2">{{ post.likes }}</span>
            </div>
          </template>
        </v-list-item>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
//Enabling axios
import axios from 'axios';
import { ref } from 'vue';

export default {
  name:"PostComp",
  setup() {

    //Reading Posts from JSON
    const posts = ref([]);
    axios.get('http://localhost:3000/posts').then(response => {
      posts.value = response.data;
    });

    const likePost = postId => {
      const post = posts.value.find(p => p.id === postId);
      const url = `http://localhost:3000/posts/${postId}/like`;
      const payload = { liked: !post.liked};
  
     
      axios.post(url, payload).then(response => {
        // update the frontend after likes are changed
        post.likes = response.data.likes;
        post.liked = response.data.liked;
      }).catch(error => {
        console.error(error);
      });
    };

    return { posts, likePost };
  }
}
</script>

<style scoped></style>
