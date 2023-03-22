<template>
  <div>
    <super-nav-bar></super-nav-bar>
    <!-- Your other Vue components go here --> 
    <v-sheet
            :class="[computedMargin]"
            elevation="4"
            rounded
          >
    <v-card
      class="mx-auto"
      color="grey-lighten-3"
      max-width="400"
    >
      <v-card-text>
        <v-text-field
          :loading="loading"
          density="default"
          variant="solo"
          label="Search users by name or email"
          append-inner-icon="mdi-magnify"
          single-line
          hide-details
          @click:append-inner="onClick"
        ></v-text-field>
      </v-card-text>
    </v-card>
    </v-sheet>
  </div>
</template>

<script>
import SuperNavBar from '@/components/SuperNavBar.vue'
export default {
    data: () => ({
    loaded: false,
    loading: false,
  }),

  methods: {
    onClick () {
      this.loading = true

      setTimeout(() => {
        this.loading = false
        this.loaded = true
      }, 2000)
    },
  },
  components: {
    SuperNavBar
  }
}
</script>
