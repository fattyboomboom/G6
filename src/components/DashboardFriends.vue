<template>
  <VRow>
    <VCol cols="3" >
      <VCard
        :border="true"
        
        class="friendslist"
        variant="outlined"
        width="300"
      >
        <VCardTitle> <h2>Friends</h2> </VCardTitle>
        <VDivider color="black" thickness="2"></VDivider>

        <v-row no-gutters="true">
          <v-col v-for="n in 6" :key="n" cols="4" align-self="stretch">
            <VCard color="white" density="">
              <a href="profile">
                <v-img
                  :src="`https://picsum.photos/500/300?image=${n * 5 + 10}`"
                  :lazy-src="`https://picsum.photos/10/6?image=${n * 5 + 10}`"
                  aspect-ratio="1"
                  cover
                  class="bg-grey-lighten-2"
                >
                  <template v-slot:placeholder>
                    <v-row
                      class="fill-height ma-0"
                      align="center"
                      justify="center"
                    >
                      <v-progress-circular
                        indeterminate
                        color="grey-lighten-5"
                      ></v-progress-circular>
                    </v-row>
                  </template> </v-img
              ></a>
              <VDivider color="white" thickness="2"></VDivider>
              <center><p>Name</p></center>
            </VCard>
          </v-col>
        </v-row>
      </VCard>
    </VCol>
  </VRow>
</template>

<script>
export default {
  name: "DashFriends",
};
</script>

<style scoped>
h2 {
  text-align: center;
}

.friendslist {
    position: absolute;
    left:6%;
    top: 55%;
}
</style>
