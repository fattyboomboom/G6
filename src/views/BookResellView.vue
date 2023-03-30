<template>
  <v-app>
    <listings-filter></listings-filter>
    <BookListings />
    <nav-bar></nav-bar>
  </v-app>
</template>

<script>
import BookListings from "@/components/Resell/BookListings.vue";

export default {
  name: "BookResellView",
  components: {
    BookListings,
 
  },
};
</script>

<style scoped>
</style>
