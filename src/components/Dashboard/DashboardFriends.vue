<template>
  <VCard :border="true" class="friendslist" variant="outlined">
    <a href="friends">
      <VCardTitle class="cardtitle"> <h2>Following</h2></VCardTitle></a
    >
    <VDivider color="#003049" thickness="2"></VDivider>
    <v-row no-gutters>
      <v-col
        v-for="friend in friends"
        :key="friend"
        cols="4"
        align-self="stretch"
      >
        <VCard class="friendcard" color="white">
          <a href="/profile">
            <v-img
              :src="friend.image"
              aspect-ratio="1"
              cover
              class="bg-grey-lighten-2"
            >
              <template v-slot:placeholder>
                <v-row class="fill-height ma-0" align="center" justify="center">
                  <v-progress-circular
                    indeterminate
                    color="grey-lighten-5"
                  ></v-progress-circular>
                </v-row>
              </template> </v-img
          ></a>
          <VDivider thickness="2"></VDivider>

          <p>{{ friend.name }}</p>
        </VCard>
      </v-col>
    </v-row>
    <a href="friends" class="view-all-link">
      <p>View All</p>
    </a>
  </VCard>
</template>

<script>
import { ref } from "vue";

export default {
  name: "DashFriends",

  setup() {
    const friends = ref([
      {
        name: "Johnhy Davis",
        image: "https://randomuser.me/api/portraits/men/86.jpg",
      },
      {
        name: "Patricia Moore",
        image: "https://randomuser.me/api/portraits/women/24.jpg",
      },
      {
        name: "Jazzi Johnson",
        image: "https://randomuser.me/api/portraits/women/69.jpg",
      },
      {
        name: "Tyler Evans",
        image: "https://randomuser.me/api/portraits/men/52.jpg",
      },
      {
        name: "Alice Johnson",
        image: "https://randomuser.me/api/portraits/women/39.jpg",
      },
      {
        name: "Richard Harris",
        image: "https://randomuser.me/api/portraits/men/59.jpg",
      },
    ]);

    return { friends };
  },
};
</script>

<style scoped>
.cardtitle {
  text-align: center;
  background-color: #4a6fa5;
}
p {
  text-align: center;
  background-color: #4a6fa5;
  color: #dbe9ee;
}

h2 {
  color: #dbe9ee;
}
.friendslist {
  position: absolute;
  left: 6%;
  top: 50%;
  width: 25%;
  border: none;
  border-radius: 25px;
}
a {
  color: #dbe9ee;
}

.friendcard:hover {
  scale: 1.1;
}
</style>
