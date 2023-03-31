<template>
  <v-container>
    <v-row>
      <v-col md="12" >
        <v-avatar >
          <v-img src="https://cdn.mos.cms.futurecdn.net/Py7jzQuvEBcZDTbLW3rtTG.jpg" ></v-img>
        </v-avatar>
        <h2 class="my-4">Deandre Mylove</h2>
        <v-btn color="primary" class="mb-4" v-model="follow" @click="followClicked">{{ followText }}</v-btn>
        <v-card class="class-list mt-6">
          <v-card-text>
          <h1>Class</h1>
          
            <v-list >
              <v-list-item v-for="(interest, index) in classes" :key="index">
                <v-list-item-title>{{ interest }}</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-card-text>
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
  width: 40%;
  margin-left: 10%;
  text-align: center;
  border-color: #4a6fa5;
  border-style: solid;
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
  width: 70%;
  height: auto;
  margin-left: 15%;
  margin-top: 2%;
  margin-bottom: 2%;
}

</style>