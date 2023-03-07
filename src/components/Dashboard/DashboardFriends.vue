<template>
  <VCard :border="true" class="friendslist" variant="outlined">
    <a href="friends">
      <VCardTitle class="cardtitle"> <h2>Friends</h2></VCardTitle></a
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
  </VCard>
</template>

<script>
import { ref } from "vue";
import axios from "axios";
export default {
  name: "DashFriends",

  setup() {
    const friends = ref([]);
    const error = ref(null);

    axios.get("http://localhost:3000/friends").then(response => {
      friends.value = response.data;
      console.log(response.data);
  })
  .catch(error => {
    console.log(error);
  });

    return { friends, error };
  },
};
</script>

<style scoped>
.cardtitle {
  text-align: center;
  background-color: #003049;
}
p {
  text-align: center;
  background-color: #003049;
  color: #fdf0d5;
}

h2 {
  color: #fdf0d5;
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
  color: #fdf0d5;
}

.friendcard:hover {
  scale: 1.1;
}
</style>
