<template>
    <v-container class="mt-12" color="grey-lighten-1" style="overflow-x: hidden; overflow-y: scroll; max-width: 100%; max-height: 580px;">
      <v-card-title class="text-h4 bottom-border" style="text-align:center;">Community Walls</v-card-title>
      <v-card v-for="category in categories" :key="category.title" class="mt-2" color="#4A6FA5">
        <div class="d-flex flex-wrap justify-space-between">
          <div>
            <v-card-title class="text-h4 mt-3" style="color: white;">
              {{category.title}}
            </v-card-title>
  
            <v-card-actions>
              <v-btn class="ml-2" :color="category.fill ? '#C1121F' : 'white'"  variant="text" @click="category.fill = !category.fill" icon>
               <v-icon>{{ !category.fill ? "mdi-heart-outline"  : "mdi-heart" }}</v-icon> 
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

    
    return {categories};
  }
}
</script>
  
  <style scoped>
  .bottom-border{
    border-bottom: 1px solid #000;
    
  }
  </style>