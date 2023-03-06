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
            <v-col class="wall-col" xs="12" md="4" style="padding-right: 2rem;">
            <WallCards />
          </v-col>
        
      </v-row>
      </v-main>
    </v-app>
  </template>
  
  <script>
    import NavBar from "@/globalcomponents/NavBar.vue"
    import WallCards from "../components/Explore/WallCards.vue"
    import PostComp from "../components/Explore/PostComp.vue"
    import ExploreBanner from "../components/Explore/ExploreBanner.vue"
  export default {
    name: "App",
    
    components: {
      PostComp,
      ExploreBanner,
      WallCards,
      NavBar
    },
  
    data: () => ({
      //
    }),
  }
  </script>