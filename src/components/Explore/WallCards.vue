<template>
  <v-container class="mt-12" color="grey-lighten-1" style="overflow-x: hidden; overflow-y: scroll; max-width: 100%; max-height: 750px;">
    <v-card-title class="text-h4 bottom-border" style="text-align:center;">Community Walls</v-card-title>
    <v-card v-for="category in categories" :key="category.id" class="mt-2" color="#4A6FA5">
      <div class="d-flex flex-wrap justify-space-between">
        <div>
          <v-card-title class="text-h4 mt-3" style="color: white;">
            {{category.title}}
          </v-card-title>
          <v-card-actions>
            <v-btn 
              class="ml-2" 
              icon>
              <v-icon color="white">{{ category.follow ? 'mdi-heart' : 'mdi-heart-outline' }}</v-icon>
            </v-btn>
          </v-card-actions>
        </div>
        <v-icon class="ma-3" size="75" color="white">{{category.icon}}</v-icon>
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
</style>