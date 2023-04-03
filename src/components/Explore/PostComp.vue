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

    <v-card v-for="post in posts" :key="post.id" class="ml-16 mt-8 text-white" color="#4A6FA5" max-width="800"
      :title="post.uid">
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
              <span class="subtitle me-2">{{ formatDate(post.PostDate) }}</span>
              <span class="me-2">·</span>
              <span class="subtitle me-2">{{ formatTime(post.PostDate) }}</span>
              <span class="me-2">·</span>
              <v-btn class="me-1" icon>
                <v-icon>mdi-heart-outline</v-icon>
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
import { ref } from 'vue';
import { db } from '@/firebase'
import { collection, onSnapshot } from 'firebase/firestore';
export default {
name: "PostComp",
setup() {
  // Reading categories from Firebase
  const posts = ref([]);

  // Create a reference to the categories collection in Firebase Firestore
  const postsRef = collection(db, 'posts');

  // Listen for changes to the categories collection
  onSnapshot(postsRef, (querySnapshot) => {
    const postsArray = [];
    querySnapshot.forEach((doc) => {
      postsArray.push({ id: doc.id, ...doc.data() });
      
    });
    posts.value = postsArray;
  });
  console.log(posts)
  return { posts };
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
    }</style>