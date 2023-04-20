<template>
  <v-container class="wall-container" color="grey-lighten-1" style="overflow-x: hidden;  max-width: 100%;">
    <v-card-title class="text-h4 bottom-border" style="text-align:center;">Community Pages</v-card-title>
    <v-card v-for="category in categories" :key="category.id" class="categories mt-2" >
      <div class="d-flex flex-wrap justify-space-between">
        <div>
          <v-card-title class="text-h4 mt-3">
            {{category.title}}
          </v-card-title>
          <v-card-actions>
            <v-btn
  class="ml-2"
  @click="isLiked(category) ? unlikeCategory(category) : likeCategory(category)"
  :style="{ 'color': isLiked(category) ? '#C1121F' : 'black' }"
  icon
>
  <v-icon v-if="!isLiked(category)">mdi-heart-outline</v-icon>
  <v-icon v-else>mdi-heart</v-icon>
</v-btn>

          </v-card-actions>
        </div>
        <v-icon class="ma-3" size="75">{{category.icon}}</v-icon>
      </div>
    </v-card>
  </v-container>
</template>

<script>
import { ref } from 'vue';
import { db, auth } from '@/firebase'
import { collection, onSnapshot, doc, updateDoc, arrayUnion, arrayRemove } from 'firebase/firestore';

export default {
  name: "WallCards",
  setup() {
    // Reading categories from Firebase
    const categories = ref([]);

    // Create a reference to the categories collection in Firebase Firestore
    const categoriesRef = collection(db, 'categories');

    // Listen for changes to the categories collection
    onSnapshot(categoriesRef, (querySnapshot) => {
  const newCategories = [];
  querySnapshot.forEach((doc) => {
    const data = doc.data();
    const categoryData = {
      id: doc.id,
      title: data.title,
      icon: data.icon,
      likes: data.likes && Array.isArray(data.likes) ? data.likes : []
    };
    newCategories.push(categoryData);
  });
  categories.value = newCategories;
});

    return { categories };
  },
  methods: {
    isLiked(category) {
      return category.likes.includes(auth.currentUser.uid);
    },
    async likeCategory(category) {
      try {
        const uid = auth.currentUser.uid;

        const categoryRef = doc(db, "categories", category.id);

        // Like the category by adding the user's UID to the likes array
        await updateDoc(categoryRef, {
          likes: arrayUnion(uid),
        });

        category.likes.push(uid);
      } catch (error) {
        console.error("Error updating likes: ", error);
      }
    },

    async unlikeCategory(category) {
      try {
        const uid = auth.currentUser.uid;

        const categoryRef = doc(db, "categories", category.id);

        // Unlike the category by removing the user's UID from the likes array
        await updateDoc(categoryRef, {
          likes: arrayRemove(uid),
        });

        const index = category.likes.indexOf(uid);
        if (index > -1) {
          category.likes.splice(index, 1);
        }
      } catch (error) {
        console.error("Error updating likes: ", error);
      }
    }
  }
};
</script>

<style scoped>
.bottom-border{
  border-bottom: 1px solid #000;
}
.categories {
      border: solid;
      border-color: #4a6fa5;
      border-width: 5px;
      margin-bottom: 10px;
      padding: 10px;
      border-radius: 25px;
  }
  .red-heart {
    color: #C1121F;
  }
  .wall-container{
    margin-top:-5px
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
</style>