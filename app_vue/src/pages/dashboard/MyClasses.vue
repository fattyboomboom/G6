<template>
  <v-card class="classcard" variant="outlined">
    <v-list bg-color="black">
      <VListItemTitle class="itemtitle">
        <!-- <VBtn color="indigo" rounded="" >
              <v-icon>mdi-plus</v-icon>
            </VBtn> -->
        <h2>My Classes</h2>
      </VListItemTitle>

      <VDivider color="white" thickness="2"></VDivider>

      <VListItem class="listitem" v-for="classes in schedule" :key="classes.id" draggable="true">
        <li >
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
    <VBtn class="deleteclass" color="red" width="50%" rounded="0">Delete</VBtn>
  </v-card>
</template>

<script>

export default {
  name: "MyClasses",
  props: {
    className: {
      type: String,
      required: false,
    },
  },
 
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
          id: "CS: 326",
        },
        {
          id: "PHYS: 181",
        },
      ],
    };
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
  color: #000000;
  border: none;
  border-radius: 25px;
}

h2 {
  text-align: center;
}

.addclass {
  left: 0%;
}
.deleteclass {
  right: 0%;
}

h2 {
  background-color: #000000;
  color: white;
}

.listitem {
  background-color: snow;
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
  background-color: #000000;
}
.itemtitle {
  background-color: #000000;
}

.listitem:hover {
  scale: 1.2;
}
</style>
