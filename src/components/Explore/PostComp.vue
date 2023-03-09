<template>
  <div id="app">
    <v-btn-group>
      <v-btn @click="updateFilteredPostsForYou()">All posts</v-btn>
      <v-btn @click="updateFilteredPosts()">For you</v-btn>
    </v-btn-group>

    <v-card v-for="post in filteredPosts" :key="post.id" class="ml-16 mt-8 text-white" color="#4A6FA5" max-width="800"
      :title="post.name">
      <template v-slot:prepend>
        <v-avatar color="grey-darken-3"
          image="https://static.vecteezy.com/system/resources/thumbnails/009/292/244/small/default-avatar-icon-of-social-media-user-vector.jpg"></v-avatar>
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
              <v-btn class="me-1" icon :color="post.liked ? '#C1121F' : ''" @click="likePost(post.id)">
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
import axios from 'axios';
import { ref, computed } from 'vue';

export default {
  name: 'PostComp',
  setup() {
    const posts = ref([]);
    axios.get('http://localhost:3000/posts').then((response) => {
      posts.value = response.data;
    });

    const followedCategories = ref([]);
    axios.get('http://localhost:3000/categories').then((response) => {
      followedCategories.value = response.data.filter((category) => category.follow);
    });

    const filteredPosts = computed(() => {
      if (followedCategories.value.length === 0) {
        return posts.value;
      } else {
        return posts.value.filter((post) => {
          return followedCategories.value.find((category) => category.title === post.category);
        });
      }
    });

    const likePost = (postId) => {
      const post = posts.value.find((p) => p.id === postId);
      const url = `http://localhost:3000/posts/${postId}/like`;
      const payload = { liked: !post.liked };

      axios
        .post(url, payload)
        .then((response) => {
          post.likes = response.data.likes;
          post.liked = response.data.liked;
        })
        .catch((error) => {
          console.error(error);
        });
    };

    const updateFilteredPosts = () => {
      followedCategories.value = followedCategories.value.filter((category) => category.follow);
    };

    const updateFilteredPostsForYou = () => {
      if (followedCategories.value.length === 0) {
        followedCategories.value = posts.value
          .map(post => post.category)
          .filter((category, index, self) => self.indexOf(category) === index)
          .map(category => ({ title: category, follow: true }));
      } else {
        const categories = posts.value
          .map(post => post.category)
          .filter((category, index, self) => self.indexOf(category) === index)
          .map(category => ({ title: category, follow: followedCategories.value.some(c => c.title === category) }));
        followedCategories.value = categories;
      }
    };

    return {
      posts,
      followedCategories,
      filteredPosts,
      likePost,
      updateFilteredPosts,
      updateFilteredPostsForYou
    };
  },
};
</script>

<style scoped></style>
