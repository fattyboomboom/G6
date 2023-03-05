<template>
  <VCard :border="true" class="friendslist" variant="outlined">
    <a href="friends">
      <VCardTitle class="cardtitle"> <h2>Friends</h2></VCardTitle></a
    >
    <VDivider color="black" thickness="2"></VDivider>
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
  </VCard>
</template>

<script>
import { ref } from "vue";
// import axios from 'axios';
export default {
  name: "DashFriends",

  setup() {
    const friends = ref([]);
    const error = ref(null);

    const load = async () => {
      try {
        let data = await fetch("http://localhost:3000/friends");
        if (!data.ok) {
          throw Error("no data available");
        }
        friends.value = await data.json();
      } catch (err) {
        error.value = err.message;
        console.log(error.value);
      }
    };
    load();
    return { friends, error };
  },
};
</script>

<style scoped>
.cardtitle {
  text-align: center;
  background-color: #000000;
}
p {
  text-align: center;
  background-color: #000000;
  color: white;
}

h2 {
  color: white;
}
.friendslist {
  position: absolute;
  left: 6%;
  top: 55%;
  width: 25%;
  border: none;
  border-radius: 25px;
}
a {
  color: white;
}

.friendcard:hover {
  scale: 1.1;
}
</style>
