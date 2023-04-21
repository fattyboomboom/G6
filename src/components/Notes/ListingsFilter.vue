<template>
  <v-container class="dropdowncontainer pa-2" fluid>
    <VToolbar class="toolbar">
      <v-btn rounded="pill" prepend-icon="mdi-pencil-outline">Edit</v-btn>

      <VAutocomplete
        :items="['HIST 310', 'CS 135', 'BIOL 191', 'CPE 301']"
        label="Classes"
        class="dropdown"
      ></VAutocomplete>

      
      <v-btn rounded="pill" prepend-icon="mdi-plus" @click="$emit('add-book')"
        >Create</v-btn
      >
    </VToolbar>
  </v-container>
</template>

<script>
import { ref } from "vue";

export default {
  name: "ListingsFilterNotes",

  setup() {
    const isOpen = ref(false);

    return { isOpen };
  },
};
</script>

<style scoped>
.dropdowncontainer {
  background-color: #166088;
}

.dropdown {
  margin: 1%;
  background-color: #dbe9ee;
}

.toolbar {
  width: 50%;
  height: 80%;
  margin: auto;
  background-color: #166088;
}

.v-btn {
  background-color: #c0d6df;
  height: 60%;
}
</style>
