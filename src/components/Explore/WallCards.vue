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
        icon>
        <v-icon :class="{'red-heart': category.isLiked}">{{ category.isLiked ? 'mdi-heart' : 'mdi-heart-outline' }}</v-icon>
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
import { db } from '@/firebase'
import { collection, onSnapshot } from 'firebase/firestore';
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
        newCategories.push({ id: doc.id, ...doc.data() });
      });
      categories.value = newCategories;
    });

    return { categories };
  },
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
</style>