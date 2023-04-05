<template>
  <v-container>
    <v-row>
      <v-col md="12" >
        <v-avatar >
          <v-img src="https://cdn.mos.cms.futurecdn.net/Py7jzQuvEBcZDTbLW3rtTG.jpg" ></v-img>
        </v-avatar>
        <h2 class="my-4">Deandre Mylove</h2>
        <v-btn  class="mb-4" v-model="follow" @click="followClicked">{{ followText }}</v-btn>
        <v-card class="class-list mt-6">
         
        </v-card>
      </v-col>
     
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "ProfilePage",
  data: () => ({
    follow: false,
    classes: ['CS 420', 'MATH 381', 'PHYS 181', 'IS 301']
  }),
  computed: {
    followText() {
      return this.follow ? 'Following' : 'Follow'
    }
  },
  methods: {
    followClicked() {
      this.follow = !this.follow
    }
  }
}
</script>

<style scoped>
.v-container {
  width: 30%;
  margin-left: 10%;
  text-align: center;
  border: 3px solid #4a6fa5;
  border-style: solid;
  border-radius: 25px;

  margin-top: 5%;
  height: 80%;
  box-shadow: 0 16px 56px rgba(0, 0, 0, 0.1), 0 16px 56px rgba(0, 0, 0, 0.1),
    0 16px 56px rgba(0, 0, 0, 0.1);
}
.v-card-text {
  text-align: center;
  border-color: #4a6fa5;
  border-style: solid;
}
.v-avatar {
  width: 60%;
  height: auto;
  margin-inline: 20%;
}

.v-btn {
  background-color: #4a6fa5;
  color: white;
  border-radius: 25px;
  width: 50%;
  box-shadow: 0 16px 46px rgba(0, 0, 0, 0.1), 0 16px 56px rgba(0, 0, 0, 0.1),
    0 16px 56px rgba(0, 0, 0, 0.1);
  margin-inline: 25%;
}
</style>