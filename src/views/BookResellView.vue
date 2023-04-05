<template>
  <v-app>
    <ListingsFilterResell @add-book="openModal"></ListingsFilterResell>
    <BookListings></BookListings>
    <BookPost v-if="showModal" v-click-outside="closeModal" @add-book="openModal"></BookPost>
    <nav-bar></nav-bar>
  </v-app>
</template>

<script>
import BookListings from "@/components/Resell/BookListings.vue";
import BookPost from "@/components/Resell/BookPost.vue";
import ListingsFilterResell from "@/components/Resell/ListingsFilter.vue";

export default {
  name: "BookResellView",
  components: {
    BookListings,
    BookPost,
    ListingsFilterResell,
  },
  data() {
    return {
      showModal: false,
    };
  },
  directives: {
    clickOutside: {
      bind(el, binding, vnode) {
        el.clickOutsideEvent = function(event) {
          if (!(el == event.target || el.contains(event.target))) {
            vnode.context[binding.expression](event);
          }
        };
        document.body.addEventListener("click", el.clickOutsideEvent);
      },
      unbind(el) {
        document.body.removeEventListener("click", el.clickOutsideEvent);
      },
    },
  },
  methods: {
    openModal() {
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
    },
  },

};
</script>

<style scoped>
</style>
