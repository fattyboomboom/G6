<template>
    <div>
  
      <v-sheet
              :class="[computedMargin]"
              elevation="4"
              rounded
            >
      <v-card
        class="mx-auto"
        color="grey-lighten-3"
        max-width="400"
      >
        <v-card-text>
          <v-text-field
  v-model="searchInput"
  :loading="loading"
  density="default"
  variant="solo"
  label="Search users by name or email"
  append-inner-icon="mdi-magnify"
  single-line
  hide-details
  @click:append-inner="onClick"
></v-text-field>
        </v-card-text>
      </v-card>
      </v-sheet>
    </div>
      <v-table style="margin-left: 3.5rem;">
      <thead>
        <tr>
          <th class="text-left">
            Author
          </th>
          <th class="text-left">
            Date
          </th>
          <th class="text-left">
            Content
            </th>  
            <th class="text-center">
            Actions
            </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="post in filteredPosts" :key="post.uid">
          <td class="border-black">{{ `${post.FirstName} ${post.LastName}`}}</td>
          <td class="border-black">{{ formatDate (post.PostDate) }}</td>
          <td class="border-black">{{ post.content }}</td>
          <td class="border-black">
              <v-btn color="indigo" @click="deletePost(post)">
                Repeal
              </v-btn>
            </td>
            <td class="border-black">
              <v-btn color="error" @click="deletePost(post)">
                Delete
              </v-btn>
            </td>
        </tr>
      </tbody>
    </v-table>
  
  </template>

<script>

import { ref, onMounted } from "vue";
import { collection, query, where,  doc, updateDoc, onSnapshot } from "firebase/firestore";
import { db } from "@/firebase";
import { formatDistanceToNow } from "date-fns";

export default {
name: "SuperUserDash",
data: () => ({
    searchInput:'',
    loaded: false,
    loading: false,
}),
setup() {
    const posts = ref([]);
    const error = ref(null);

    const fetchPosts = async () => {
      try {
        const postRef = collection(db, "posts");
        const q = query(postRef, where("isDeleted", "==", false));
        onSnapshot(q, (docSnap) => {
                    posts.value = docSnap.docs.map((doc) => {
                        const data = doc.data();
                        data.id = doc.id;
                        return data;
                    });
      });
        
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

    async deletePost(post) {
    try {        
    const postRef = doc(db, "posts", post.id)
    await updateDoc(postRef, {
    isDeleted: true,
    });
    post.isDeleted = true;
     } catch (error) {
    console.error("Error adding report: ", error); }
    
  },
  onClick() {
    this.loading = true;
    setTimeout(() => {
      this.loading = false;
      this.$refs.searchInput.focus();
    }, 2000);
  },

  onButtonClicked(user) {
    console.log("Row clicked:", user);
  },
  computed: {
    displayedPosts() {
      return this.posts.slice(0, this.maxPosts);
    },
    filteredPosts() {
    const searchText = this.searchInput.toLowerCase();
  return this.users.filter(
    (user) =>
      user.AcctEmail.toLowerCase().includes(searchText) ||
      user.LastLogin.toString().toLowerCase().includes(searchText)
  );
  },
  },

}
}



</script>



<!-- <style scoped>
.v-card {
max-width: 80%;
margin: 5px auto;
}
td {
padding: 10px;
}
.v-btn {
margin: 0 10px;
}
.text-right {
text-align: right;
}
tbody tr {
border-top: 1px solid lightgray;
}
.black {
background-color: #000000;
}
</style> -->
