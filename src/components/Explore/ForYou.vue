<template>
  <div id="app">

    <!-- <v-banner 
          :sticky="true"
          lines="three"
          height="60"
          class="no-border"
          
        >
      
            <v-btn @click="updateFilteredPosts()" class="banner-button ml-16" color="Black" elevation="0" >
              <h1>For You</h1>
            </v-btn>
    
            <v-btn  @click="updateFilteredPostsForYou()" class="banner-button ml-16" color="Black" elevation="0" >
              <h1>Explore</h1>
            </v-btn>
        </v-banner> -->

    <v-card v-for="post in posts" :key="post.id" class="post ml-16 mt-8" max-width="800">
      <template v-slot:prepend>
        <v-avatar color="grey-darken-3"
          image="https://static.vecteezy.com/system/resources/thumbnails/009/292/244/small/default-avatar-icon-of-social-media-user-vector.jpg"></v-avatar>
      </template>
      <v-card-title>
    {{ `${post.FirstName} ${post.LastName}` }}
  </v-card-title>
      <v-card-text class="text-h5 py-2">
        {{ post.content }}
      </v-card-text>

      <v-card-actions>
        <v-list-item class="w-100">
          <div class="justify-self-start">
            <span class="subtitle me-2">{{ post.category }}</span>
          </div>
          <template v-slot:append>
            <div class="justify-self-end">
              <span class="subtitle me-2">{{ formatDate(post.PostDate) }}</span>
              <span class="me-2">·</span>
              <span class="subtitle me-2">{{ formatTime(post.PostDate) }}</span>
              <!-- <span class="">·</span>
              <v-btn class="me-1"    :style="{ 'background-color': hover ? 'red' : 'transparent' }" icon>
                <v-icon>mdi-heart-outline</v-icon> 
              </v-btn>-->
              <span class="subheading me-2">{{ post.likes }}</span>
            </div>
          </template>
        </v-list-item>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { collection, onSnapshot, query, where } from "firebase/firestore";
import { db } from "@/firebase";
export default {
name: "PostComp",
setup() {
  // Reading categories from Firebase
  const posts = ref([]);
  const error = ref(null);
  // Create a reference to the categories collection in Firebase Firestore

  const fetchPosts = async () => {
  try {
    const postRef = collection(db, "posts");
    const q = query(postRef, where("category", "==", "Art"));

    onSnapshot(q, docSnap => {
      docSnap.docChanges().forEach(change => {
        posts.value.push(change.doc.data());
      });
      posts.value.sort((a, b) => b.PostDate - a.PostDate);
      console.log(posts);
    });
  } catch (err) {
    error.value = err.message;
  }
};
      onMounted(() => {
          fetchPosts();
      });

      return { posts, error };
  },
methods:{
  formatTime(timestamp) {
    const date = timestamp.toDate();
    const hours = date.getHours();
    const minutes = date.getMinutes().toString().padStart(2, '0');
    const ampm = hours >= 12 ? 'PM' : 'AM';
    const twelveHours = hours % 12 || 12;
    return `${twelveHours}:${minutes} ${ampm}`;
  },
  formatDate(timestamp) {
    const date = timestamp.toDate();
    const options = { month: 'numeric', day: 'numeric', year: '2-digit' };
    return new Intl.DateTimeFormat('en-US', options).format(date);
  }
}
};
</script>

<style scoped>
    .no-border{
        border:none;
    }
    .post {
      border: solid;
      border-color: #4a6fa5;
      border-width: 5px;
      margin-bottom: 10px;
      padding: 10px;
      border-radius: 25px;
  }
  .mdi-heart-outline {
   
    margin-top: -3px;
}
.v-btn .mdi-heart-outline:hover {
   
   margin-top: -3px;
  color: rgb(180, 25, 25);
}
/*.v-btn :hover .v-btn__content::before {
    background-color: pink;
  } */
  </style>
