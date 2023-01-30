<template>
  <v-app class="app">
    <v-main>
      <NavBar />
      <ExploreBanner />

        <v-row>
          <v-col class="post-col" xs="12" md="8">
           <PostComp />
          </v-col>
          <v-spacer md="1"/> 
          <v-col class="wall-col" xs="12" md="3" style="padding-right: 2rem;">
          <WallCards />
        </v-col>
      
    </v-row>
      
     <!-- <HelloWorld />
    -->
    <!-- <CalendarComp /> -->
    <!-- <NewListingComp />-->
    <!--<AddClassComp />-->
    </v-main>
  </v-app>
</template>

<script>
//import HelloWorld from "./components/HelloWorld.vue";
 import WallCards from "./components/WallCards.vue"
 //import CalendarComp from "./components/CalendarComp.vue"
 //import NewListingComp from "./components/NewListingComp.vue"
 //import AddClassComp from "./components/AddClassComp.vue"
 import NavBar from "./components/NavBar.vue"
 import PostComp from "./components/PostComp.vue"
 import ExploreBanner from "./components/ExploreBanner.vue"
export default {
  name: "App",
  
  components: {
    NavBar,
    PostComp,
    ExploreBanner,
    WallCards
  // HelloWorld
  //CalendarComp
  // NewListingComp
  //AddClassComp
  },

  data: () => ({
    //
  }),
}
</script>

