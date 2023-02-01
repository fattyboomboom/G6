<template>
<v-banner 
      :sticky="true"
      lines="three"
      height="60"
      class="no-border"
      
    >
  
        <v-btn class="banner-button ml-16" color="Black" elevation="0" >
          <h1>For You</h1>
        </v-btn>

        <v-btn class="banner-button ml-16" color="Black" elevation="0" >
          <h1>Explore</h1>
        </v-btn>
    </v-banner>
</template>

<style scoped>
.no-border{
    border:none;
}
</style>