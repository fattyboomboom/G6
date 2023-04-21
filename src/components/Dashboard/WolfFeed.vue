<template>
  <div class="wolf-feed">
    <h1>Wolf Feed</h1>
    <div class="post-container">
      <VCard
        v-for="(post, index) in posts"
        :key="post.uid"
        class="post"
        variant="outlined"
      >
        <VCardItem class="post-header">
          <v-row no-gutters class="align-items-center justify-space-between">
            <v-avatar
              color="grey-darken-2"
              size="50"
              image="https://static.vecteezy.com/system/resources/thumbnails/009/292/244/small/default-avatar-icon-of-social-media-user-vector.jpg"
            ></v-avatar>

            <div class="author-name pt-3 mr-auto pl-4">
              {{ `${post.FirstName} ${post.LastName}` }}
              <div class="post-date d-flex">
                {{ formatDistanceToNow(post.PostDate) }} ago
              </div>
            </div>

            <div>
              <v-btn
                class="d-flex post-menu"
                icon="mdi-dots-vertical"
                variant="plain"
                color="#78909C"
                size="x-large"
                :ripple="false"
                @click="menu[index] = !menu[index]"
              ></v-btn>
            </div>

            <v-expand-transition>
              <v-card
                v-show="menu[index]"
                height="100"
                width="100"
                class="elip-menu bg-secondary"
              ></v-card>
            </v-expand-transition>

          </v-row>
        </VCardItem>
        <div class="post-content">{{ post.content }}</div>
        <!-- <v-row class="d-flex">
          <v-btn
            class="d-flex align-self-center mt-8"
            icon="mdi-trash-can-outline"
            variant="plain"
            size="large"
            color="#C62828"
            :ripple="false"
          ></v-btn>
          <v-btn
            class="d-flex mt-8"
            icon="mdi-pencil-outline"
            variant="plain"
            size="large"
            color="#78909C"
            :ripple="false"
          ></v-btn> -->
        <!-- </v-row> -->
      </VCard>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { collection, onSnapshot } from "firebase/firestore";
import { db } from "@/firebase";
import { formatDistanceToNow } from "date-fns";

export default {
  name: "WolfFeed",

  data() {
    return {
      menu: []
    }
  },

  setup() {
    const posts = ref([]);
    const error = ref(null);

    const fetchPosts = async () => {
      try {
        const postRef = collection(db, "posts");

        onSnapshot(postRef, (docSnap) => {
          docSnap.docChanges().forEach((change) => {
            posts.value.push(change.doc.data());
          });

          posts.value.sort((a, b) => b.PostDate - a.PostDate);
          console.log(posts);
        });
      } catch (err) {
        error.value = err.message;
        console.log(error);
      }
    };

    onMounted(() => {
      fetchPosts();
    });

    return { posts, error };
  },

  methods: {
    formatTime(timestamp) {
      const date = timestamp.toDate();
      const hours = date.getHours();
      const minutes = date.getMinutes().toString().padStart(2, "0");
      const ampm = hours >= 12 ? "PM" : "AM";
      const twelveHours = hours % 12 || 12;
      return `${twelveHours}:${minutes} ${ampm}`;
    },

    formatDate(timestamp) {
      const date = timestamp.toDate();
      const options = { month: "short", day: "numeric", year: "2-digit" };
      return new Intl.DateTimeFormat("en-US", options).format(date);
    },

    formatDistanceToNow(timestamp) {
      const date = timestamp.toDate();
      return formatDistanceToNow(date);
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

.elip-menu {
  margin-left: 25rem;
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
  margin-bottom: 8px;
  padding: 10px;
  border-radius: 25px;
}

.post-header {
  /* display: flex; */
  align-items: center;
}

::-webkit-scrollbar {
  width: 8px; /* 1px wider than Lion. */
  /* This is more usable for users trying to click it. */
  background-color: rgba(0,0,0,0);
  -webkit-border-radius: 100px;
}

::-webkit-scrollbar-track,::-webkit-scrollbar-thumb {
  border: 5px solid transparent;
  border-radius: 999px;
}

::-webkit-scrollbar-thumb:vertical {
  background: rgba(0,0,0,0.5);
  -webkit-border-radius: 100px;
}

::-webkit-scrollbar-thumb:vertical:active {
  background: rgba(0,0,0,0.61); /* Some darker color when you click it */
  -webkit-border-radius: 100px;
}

::-webkit-scrollbar:hover {
  background-color: rgba(0, 0, 0, 0.09);
}
/* .avatar {
  width: 50px;
  height: 50px;
  margin-right: 10px;
  border-radius: 50%;
} */

.author-info {
  display: flex;
  flex-direction: column;
  justify-content: center;
  color: black;
}

.author-name {
  font-weight: bold;
  color: black;
  font-weight: bold;
  margin-top: -0.6rem;
}

.post-date {
  color: black;
  font-size: 14px;
  margin-left: auto;
}

.post-content {
  margin-top: 2%;
  color: black;
  text-align: center;
}

.post-menu {
  margin-top: -.5rem;
  margin-left: 13rem;
}
</style>