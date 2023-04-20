<template>
  <div>

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
              <span class="">·</span>
              <v-btn class="me-1" @click="isLiked(post) ? unlikePost(post) : likePost(post)"
                :style="{ 'color': isLiked(post) ? '#C1121F' : 'black' }" icon>
                <v-icon v-if="!isLiked(post)">mdi-heart-outline</v-icon>
                <v-icon v-else>mdi-heart</v-icon>
              </v-btn>

              <span class="subheading me-2">{{ post.likes.length }}</span>
            </div>
          </template>
        </v-list-item>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { collection, onSnapshot, query, where, updateDoc, doc, arrayUnion, arrayRemove } from "firebase/firestore";
import { db, auth } from "@/firebase";
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
    const q = query(postRef, where("category", "!=", ""));
    onSnapshot(q, (docSnap) => {
  posts.value = docSnap.docs.map((doc) => {
    const data = doc.data();
    data.id = doc.id;
    return data;
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
  methods: {
    formatTime(timestamp) {
  if (!timestamp) {
    return '';
  }
  const date = timestamp.toDate();
  const hours = date.getHours();
  const minutes = date.getMinutes().toString().padStart(2, '0');
  const ampm = hours >= 12 ? 'PM' : 'AM';
  const twelveHours = hours % 12 || 12;
  return `${twelveHours}:${minutes} ${ampm}`;
},

    formatDate(timestamp) {
  if (!timestamp) {
    return ''; 
  }
  const date = timestamp.toDate();
  const options = { month: 'numeric', day: 'numeric', year: '2-digit' };
  return new Intl.DateTimeFormat('en-US', options).format(date);
},

    isLiked(post) {
      return post.likes.includes(auth.currentUser.uid);
    },
    async likePost(post) {
      try {
        const uid = auth.currentUser.uid;

        const postRef = doc(db, "posts", post.id);

        // Like the post by adding the user's UID to the likes array
        await updateDoc(postRef, {
          likes: arrayUnion(uid),
        });

        post.likes.push(uid);
      } catch (error) {
        console.error("Error updating likes: ", error);
      }
    },

    async unlikePost(post) {
      try {
        const uid = auth.currentUser.uid;

        const postRef = doc(db, "posts", post.id);

        // Unlike the post by removing the user's UID from the likes array
        await updateDoc(postRef, {
          likes: arrayRemove(uid),
        });

        const index = post.likes.indexOf(uid);
        if (index > -1) {
          post.likes.splice(index, 1);
        }
      } catch (error) {
        console.error("Error updating likes: ", error);
      }
    }


  }
};
</script>

<style scoped>
.no-border {
  border: none;
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
  transform: scale(1.1);
}

.v-btn .mdi-heart:hover {

margin-top: -3px;
transform: scale(1.1);
}
/*.v-btn :hover .v-btn__content::before {
    background-color: pink;
  } */
</style>
