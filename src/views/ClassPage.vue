<template>
 
    
    <nav-bar></nav-bar>
    <ClassInfo></ClassInfo>
    <ClassAnnouncements></ClassAnnouncements>
    <!-- <ClassPost></ClassPost> -->
    <ClassFeed></ClassFeed>
  
  </template>
  
  <script>
  // @ is an alias to /src
  import ClassInfo from "@/components/Classes/ClassInfo.vue"
  // import ClassPost from "@/components/Classes/ClassPost.vue"
  import ClassFeed from "@/components/Classes/ClassFeed.vue"
  import ClassAnnouncements from "@/components/Classes/ClassAnnouncements.vue";

  export default {
  name: "ClassPage",
  components: {
    ClassInfo,
    // ClassPost,
    ClassFeed,
    ClassAnnouncements
  },
  };
  </script>
  
  <style scoped>
  body {
  background-color: #fdf0d5;
  }
  </style>