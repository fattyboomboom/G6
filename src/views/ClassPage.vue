<template>
  <nav-bar></nav-bar>
  <ClassInfo></ClassInfo>
  <!-- <ClassAnnouncements></ClassAnnouncements> -->
  <ClassSessions></ClassSessions>
  <ClassPost></ClassPost>
  <ClassFeed></ClassFeed>
  <ClassNotes></ClassNotes>
</template>

<script>
// @ is an alias to /src
import ClassInfo from "@/components/Classes/ClassInfo.vue";
import ClassPost from "@/components/Classes/ClassPost.vue";
import ClassFeed from "@/components/Classes/ClassFeed.vue";
// import ClassAnnouncements from "@/components/Classes/ClassAnnouncements.vue";
import ClassNotes from "@/components/Classes/ClassNotes.vue";
import ClassSessions from "@/components/Classes/ClassSessions.vue";
export default {
  name: "ClassPage",
  components: {
    ClassInfo,
    ClassPost,
    ClassFeed,
    ClassNotes,
    ClassSessions,
    // ClassAnnouncements
  },
};
</script>

<style scoped>
body {
  background-color: #fdf0d5;
}
</style>
