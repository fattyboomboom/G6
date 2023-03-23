<template>
  <div class="wolf-feed">
    <h1>Wolf Feed</h1>
    <div class="post-container">
      <VCard
        v-for="post in posts"
        :key="post.uid"
        class="post"
        variant="outlined"
      >
        <VCardItem class="post-header">
          <img :src="post.avatar" alt="Author avatar" class="avatar" />

          <div class="author-name">{{ post.name }}</div>

          <div class="post-date">{{ post.PostDate }}</div>
        </VCardItem>
        <div class="post-content">{{ post.content }}</div>
      </VCard>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { collection, query, where, getDocs } from "firebase/firestore";
import { db } from "@/firebase";
export default {
  name: "WolfFeed",

  setup() {
    const posts = ref([]);
    const error = ref(null);

    const fetchPosts = async () => {
      try {
        const postRef = collection(db, "posts");
        const q = query(postRef, where("isDeleted", "==", false));
        const querySnapshot = await getDocs(q);
        const postsArray = querySnapshot.docs.map((doc) => ({
          id: doc.id,
          ...doc.data(),
        }));
        posts.value = postsArray;
        console.log(posts.value);
      } catch (err) {
        error.value = err.message;
      }
    };

    onMounted(() => {
      fetchPosts();
    });

   
    return { posts, error };
  },

  methods: {

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
  background-color: #e0e1dd;

  width: 40%;
  position: absolute;
  margin-left: 36%;
}

.post {
  border: solid;
  border-color: #4a6fa5;
  border-width: 5px;
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 25px;
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
  color: black;
}

.author-name {
  font-weight: bold;
  color: black;
}

.post-date {
  color: black;
  font-size: 14px;
  font-style: italic;
}

.post-content {
  margin-top: 2%;
  color: black;
  text-align: center;
}
</style>
