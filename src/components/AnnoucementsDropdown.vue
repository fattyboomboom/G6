<template>
  <div class="announcements-dropdown">
    <button class="announcements-dropdown-button" @click="isOpen = !isOpen">
      Announcements <span class="arrow" :class="{ 'open': isOpen }"></span>
    </button>
    <ul class="announcements-dropdown-list" v-if="isOpen">
      <li v-for="(announcement, index) in announcements" :key="index">
        {{ announcement }}
      </li>
    </ul>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  name: 'AnnouncementsDropdown',
  setup() {
    const isOpen = ref(false);
    const announcements = ref([
      'Announcement 1',
      'Announcement 2',
      'Announcement 3'
    ]);

    return {
      isOpen,
      announcements
    };
  }
};
</script>

<style>
.announcements-dropdown {
  position: relative;
}

.announcements-dropdown-button {
  background-color: #fff;
  border: 1px solid #ccc;
  border-radius: 3px;
  cursor: pointer;
  display: block;
  font-size: 16px;
  padding: 10px 15px;
  text-align: left;
  width: 100%;
}

.announcements-dropdown-button .arrow {
  display: inline-block;
  margin-left: 10px;
  width: 0;
  height: 0;
  border: 5px solid transparent;
  border-top-color: #333;
  vertical-align: middle;
  transition: transform 0.3s ease-in-out;
}

.announcements-dropdown-button .arrow.open {
  transform: rotate(180deg);
}

.announcements-dropdown-list {
  background-color: #fff;
  border: 1px solid #ccc;
  border-top: none;
  border-radius: 0 0 3px 3px;
  list-style: none;
  margin: 0;
  padding: 0;
  position: absolute;
  top: 100%;
  width: 100%;
  z-index: 1;
}

.announcements-dropdown-list li {
  padding: 10px 15px;
  text-align: left;
}

</style>
