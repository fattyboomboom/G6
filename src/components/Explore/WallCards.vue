<template>
    <v-container class="mt-12" color="grey-lighten-1" style="overflow-x: hidden; overflow-y: scroll; max-width: 100%; max-height: 580px;">
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
                icon 
                :color="category.follow ? '#C1121F' : 'white'"
                @click="followCategory(category.id)">
                <v-icon>{{ category.follow ? 'mdi-heart' : 'mdi-heart-outline' }}</v-icon>
              </v-btn>
            </v-card-actions>
          </div>
  
          <v-icon class="ma-3" size="75" color="white">{{category.icon}}</v-icon>
        </div>
      </v-card>
    </v-container>
  </template>
  
<script>
//Enabling axios
import axios from 'axios';
import { ref } from 'vue';

export default {
  name:"WallCards",
  setup() {

    //Reading Posts from JSON
    const categories = ref([]);
    axios.get('http://localhost:3000/categories').then(response => {
      categories.value = response.data;
    });

    const followCategory = categoryId => {
      const category = categories.value.find(p => p.id === categoryId);
      const url = `http://localhost:3000/categories/${categoryId}/follow`;
      const payload = { follow: !category.follow};
  
     
      axios.post(url, payload).then(response => {
        // update the frontend after likes are changed
        category.follow = response.data.follow;
      }).catch(error => {
        console.error(error);
      });
    };
    
    return {categories, followCategory};
  }
}
</script>
  
  <style scoped>
  .bottom-border{
    border-bottom: 1px solid #000;
    
  }
  </style>