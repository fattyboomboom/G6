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
// import { ref } from "vue";
import axios from 'axios';
export default {
  name: "WolfFeed",
  data() {
    return {
      posts:[],
    }
  },

  setup() {
    // const posts = ref([]);
    // const error = ref(null);

    // const load = async () => {
    //   try {
    //     let data = await fetch("http://127.0.0.1:5000/posts");
    //     if (!data.ok) {
    //       throw Error("no data available");
    //     }
    //     posts.value = await data.json();
    //   } catch (err) {
    //     error.value = err.message;
    //     console.log(error.value);
    //   }
    // };
    // load();
    // return { posts, error };
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

    getPosts() {
      const path = 'http://localhost:5000/api/post';
      axios.get(path)
      .then((res) => {
        this.posts = res.data.posts
      })
      .catch((error) => {
        console.error(error)
      })
    }
  },
  computed: {
    displayedPosts() {
      return this.posts.slice(0, this.maxPosts);
    },
  },
  created() {
    this.getPosts();
  }
};
</script>

<style scoped>
h1 {
  width: 15%;
  margin-left: 45%;
  color: rgb(0, 0, 0);
}
.news-feed {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

.post-container {
  height: 60%;
  overflow-y: scroll;
  margin-top: 20px;
  background-color: rgb(0, 0, 0);
  width: 40%;
  position: absolute;
  margin-left: 36%;
}

.post {
  border: 1px solid rgb(255, 255, 255);
  margin-bottom: 10px;
  padding: 10px;
}

.post-header {
  display: flex;
  align-items: center;
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
  color: white;
}

.author-name {
  font-weight: bold;
  color: white;
}

.post-date {
  color: rgb(255, 255, 255);
  font-size: 14px;
  font-style: italic;
}

.post-content {
  margin-top: 10px;
  white-space: pre-line;
  color: white;
}
</style>
