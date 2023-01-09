<template>
  <v-col cols="3">
    <v-card variant="outlined">
      <v-list>
        <center>
          <VListItemTitle color="black"><h2>My Classes</h2></VListItemTitle>
          <VDivider color="black" thickness="2"></VDivider>
        </center>
        <VListItem v-for="classes in schedule" :key="classes.id">
          <li>
            <a href="class page">{{ classes.id }} </a>
          </li>
        </VListItem>
      </v-list>
    </v-card>
  </v-col>
</template>

<script>
import { VDivider } from "vuetify/lib/components";

export default {
  name: "MyClasses",
  props: {
    className: {
      type: String,
      required: false,
    },
  },
  components: { VDivider },
  data() {
    return {
      schedule: [
        {
          id: "CS:365",
        },
        {
          id: "MATH: 486",
        },
        {
          id: "CS: 425",
        },
        {
          id: "CS 326",
        },
        {
          id: "PHYS 181",
        },
      ],
    };
  },
};
</script>
