<template>
  <v-banner :sticky="true" lines="three" height="65px" class="no-border">

    <v-btn :class="{ 'active': activeButton === 'forYou' }"
      class="banner-button ml-16"
      color="Black"
      elevation="0"
      @click="activateButton('forYou'); $emit('forYouFeed')">
      <h1>For You</h1>
    </v-btn>

    <v-btn :class="{ 'active': activeButton === 'explore' }"
      class="banner-button ml-16"
      color="Black"
      elevation="0"
      @click="activateButton('explore'); $emit('exploreFeed')">
            <h1>Explore</h1>
    </v-btn>

    <v-btn class="newPost" color="secondary" @click="$emit('new-post')">
      <p>New Post</p>  
    </v-btn>
  </v-banner>
</template>
    
<script>
export default {
  data() {
    return {
      activeButton: null,
    }
  },
  methods: {
    activateButton(button) {
      this.activeButton = button;
    },
  },
 
};
</script>
<style scoped>
.no-border {
  border: none;
}

.v-btn {
  color: #166088;
}
.active {
  background-color: rgba(22, 96, 136, 0.2); /* Opaque version of the blue */
}

.newPost{
  margin-left: 18%;
  margin-top: 2px;
}
</style>