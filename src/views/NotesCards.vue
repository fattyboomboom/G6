<template>
<ListingsFilterNotes ></ListingsFilterNotes>
<nav-bar></nav-bar>
<NotesLists></NotesLists>
</template>

<script>
 import ListingsFilterNotes from "@/components/Notes/ListingsFilter.vue";
 import NotesLists from "@/components/Notes/NotesLists.vue";

 export default {
  name: "NotesView",
  components: {
    ListingsFilterNotes,
    NotesLists,
  },
 }
</script>

<style scoped>

</style>
