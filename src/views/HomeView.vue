<template>
  <div>
    <DashboardFriends />
    <AddClass v-if="showModal" v-click-outside="closeModal"></AddClass>
    <MyClasses @add-class="openModal"></MyClasses>
    <ProfileAvatar />
    <WallPost />
    <nav-bar></nav-bar>
    <WolfFeed />
  </div>
</template>

<script>
import DashboardFriends from "@/components/Dashboard/DashboardFriends.vue";
import MyClasses from "@/components/Dashboard/MyClasses.vue";
import ProfileAvatar from "@/components/Dashboard/ProfileAvatar.vue";
import WallPost from "@/components/Dashboard/WallPost.vue";
import WolfFeed from "@/components/Dashboard/WolfFeed.vue";
import AddClass from "@/components/Dashboard/AddClass.vue";

export default {
  name: "HomeView",
  components: {
    DashboardFriends,
    MyClasses,
    ProfileAvatar,
    WallPost,
    WolfFeed,
    AddClass
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
body {
  background-color: #fdf0d5;
}
</style>
