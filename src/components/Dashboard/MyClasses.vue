<template>
  <v-card class="classcard" variant="outlined">
    <v-list bg-color="#003049">
      <VListItemTitle class="itemtitle">
        <!-- <VBtn color="indigo" rounded="" >
              <v-icon>mdi-plus</v-icon>
            </VBtn> -->
        <h2>My Classes</h2>
      </VListItemTitle>

      <VDivider thickness="2"></VDivider>

      <VListItem
        class="listitem"
        v-for="classes in schedule"
        :key="classes.id"
        draggable="true"
      >
        <li>
          <a href="class page">{{ classes.id }} </a>
        </li>
      </VListItem>
    </v-list>
    <VBtn
      class="addclass"
      color="success"
      width="50%"
      rounded="0"
      @click="addClass"
      >Add</VBtn
    >
    <VBtn class="deleteclass" width="50%" rounded="0">Delete</VBtn>
  </v-card>
</template>

<script>
import axios from "axios";
import { ref} from "vue";

export default {
  name: "MyClasses",

  setup() {

    const schedule = ref([]);
    const error = ref(null);

    axios
      .get("http://localhost:3000/schedule")
      .then((response) => {
        schedule.value = response.data;
        console.log(response.data);
      })
      .catch((error) => {
        console.log(error);
      });

      return { schedule, error };
  },

  props: {
    className: {
      type: String,
      required: false,
    },
  },

  data() {
    return {};
  },
  methods: {
    addClass() {
      this.schedule.push({ id: this.newClass });
      this.newClass = "";
      this.dialog = false;
    },
  },
};
</script>

<style scoped>
.classcard {
  position: absolute;
  right: 1%;
  width: 20%;
  top: 1%;
  color: #fdf0d5;
  border: none;
  border-radius: 25px;
}

h2 {
  text-align: center;
}

.addclass {
  left: 0%;
  background-color: #669bbc;
}
.deleteclass {
  right: 0%;
  background-color: #c1121f;
}

h2 {
  background-color: #003049;
  color: white;
}

.listitem {
  background-color: #fdf0d5;
  /* color: white; */
  width: 70%;
  margin: 0 15%;
  border: none;
  border-radius: 5px;
  list-style: none;
  margin-top: 3%;
}
a {
  color: rgb(0, 0, 0);
}
v-card {
  background-color: #003049;
}
.itemtitle {
  background-color: #003049;
}

.listitem:hover {
  scale: 1.2;
}
</style>
