<template>
  <BookListingsFilter />
  <BookListings />
  <NavBar /></template>

<script>
import BookListings from "@/components/Resell/BookListings.vue";
import BookListingsFilter from "@/globalcomponents/BookListingsFilter.vue";
import NavBar from "@/globalcomponents/NavBar.vue";

export default {
  name: "BookResellView",
  components: {
    BookListings,
    BookListingsFilter,
    NavBar
  },
};
</script>


