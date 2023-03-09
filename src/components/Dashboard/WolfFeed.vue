<template>
  <div class="wolf-feed">
    <h1>Wolf Feed</h1>

    <div class="post-container">
      <div v-for="post in posts" :key="post.id" class="post">
        <div class="post-header">
          <img :src="post.avatar" alt="Author avatar" class="avatar" />
          <div class="author-info">
            <div class="author-name">{{ post.name }}</div>
            <div class="post-date">{{ formatDate(post.date) }}</div>
          </div>
        </div>
        <div class="post-content">{{ post.content }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import axios from "axios";
export default {
  name: "WolfFeed",
  setup() {
    const posts = ref([]);
    const error = ref(null);
    axios
      .get("http://localhost:3000/posts")
      .then((response) => {
        posts.value = response.data;
        console.log(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
    return { posts, error };
  },
  methods: {
    formatDate(date) {
      return new Intl.DateTimeFormat("en-US", {
        year: "numeric",
        month: "long",
        day: "numeric",
        hour: "numeric",
        minute: "numeric",
        hour12: true,
      }).format(date);
    },
  },
  computed: {
    displayedPosts() {
      return this.posts.slice(0, this.maxPosts);
    },
  },
};
</script>

<style scoped>
h1 {
  width: 15%;
  margin-left: 50%;
  color: #4a6fa5;
}
.news-feed {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}
.post-container {
  height: 61%;
  overflow-y: scroll;
  margin-top: 20px;
  background-color: #4a6fa5;
  border-top-right-radius: 25px;
  border-top-left-radius: 25px;
  width: 40%;
  position: absolute;
  margin-left: 36%;
}
.post {
  border: 1px solid #e0e1dd;
  margin-bottom: 10px;
  padding: 10px;
}
.post-header {
  display: flex;
  
}
::-webkit-scrollbar {
  display: none;
}
.avatar {
  width: 50px;
  height: 50px;
  margin-right: 10px;
  border-radius: 50%;
}
.author-info {
  display: flex;
  flex-direction: column;
  justify-content: center;
  color: #e0e1dd;
}
.author-name {
  font-weight: bold;
  color: #e0e1dd;
}
.post-date {
  color: #e0e1dd;
  font-size: 14px;
  font-style: italic;
}
.post-content {
  margin-top: 2%;  
  color: #e0e1dd;
}
</style>