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

export default {
  name: "WolfFeed",
  setup() {
    const posts = ref([]);
    const error = ref(null);

    const load = async () => {
      try {
        let data = await fetch("http://localhost:3000/post");
        if (!data.ok) {
          throw Error("no data available");
        }
        posts.value = await data.json();
      } catch (err) {
        error.value = err.message;
        console.log(error.value);
      }
    };
    load();
    return { posts, error };
  },
  // data() {
  //   return {
  //     posts: [
  //       {
  //         id: 1,
  //         author: {
  //           name: "John Doe",
  //           avatar: "https://randomuser.me/api/portraits/men/1.jpg",
  //         },
  //         // date: new Date(),
  //         content: "This is my first post on the news feed!",
  //       },
  //       {
  //         id: 2,
  //         author: {
  //           name: "Jane Smith",
  //           avatar: "https://randomuser.me/api/portraits/women/1.jpg",
  //         },
  //         // date: new Date(),
  //         content: "Just had a great time at the beach with my family!",
  //       },
  //       {
  //         id: 3,
  //         author: {
  //           name: "John Doe",
  //           avatar: "https://randomuser.me/api/portraits/men/1.jpg",
  //         },
  //         // date: new Date(),
  //         content: "This is my first post on the news feed!",
  //       },
  //       {
  //         id: 4,
  //         author: {
  //           name: "Jane Smith",
  //           avatar: "https://randomuser.me/api/portraits/women/1.jpg",
  //         },
  //         // date: new Date(),
  //         content: "Just had a great time at the beach with my family!",
  //       },
  //       {
  //         id: 5,
  //         author: {
  //           name: "John Doe",
  //           avatar: "https://randomuser.me/api/portraits/men/1.jpg",
  //         },
  //         // date: new Date(),
  //         content: "This is my first post on the news feed!",
  //       },
  //       {
  //         id: 6,
  //         author: {
  //           name: "Jane Smith",
  //           avatar: "https://randomuser.me/api/portraits/women/1.jpg",
  //         },
  //         // date: new Date(),
  //         content: "Just had a great time at the beach with my family!",
  //       },
  //       {
  //         id: 7,
  //         author: {
  //           name: "John Doe",
  //           avatar: "https://randomuser.me/api/portraits/men/1.jpg",
  //         },
  //         // date: new Date(),
  //         content: "This is my first post on the news feed!",
  //       },
  //       {
  //         id: 8,
  //         author: {
  //           name: "Jane Smith",
  //           avatar: "https://randomuser.me/api/portraits/women/1.jpg",
  //         },
  //         // date: new Date(),
  //         content: "Just had a great time at the beach with my family!",
  //       },
  //     ],
  //     maxPosts: 20,
  //   };
  // },
  // mounted() {

  // },
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
  height: 500px;
  overflow-y: scroll;
  margin-top: 20px;
  background-color: rgb(0, 0, 0);
  width: 40%;
  margin-left: 33%;
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
