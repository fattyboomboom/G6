<template>

<v-row>
<v-col cols="4">
<v-autocomplete
  clearable
  chips
  label="Classes"
  :items="['CS425', 'CS426', 'ENG101', 'PHYS180']"
  multiple
  variant="solo"
></v-autocomplete>

<v-btn>
Add Classes
</v-btn>
</v-col>
</v-row>

</template>

<script>

</script>