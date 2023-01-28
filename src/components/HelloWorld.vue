<template>
<v-app :theme="theme">
    <v-app-bar>
      <v-spacer></v-spacer>

      <v-btn
        :prepend-icon="theme === 'light' ? 'mdi-weather-sunny' : 'mdi-weather-night'"
        @click="onClick"
      >Toggle Theme</v-btn>
    </v-app-bar>

    <v-main>
      <v-app id="inspire">
    <v-app-bar flat>
      <v-container class="fill-height d-flex align-center">
        <v-avatar
          class="me-10 ms-4"
          color="grey-darken-1"
          size="32"
        ></v-avatar>

        <v-btn
          v-for="link in links"
          :key="link"
          variant="text"
        >
          {{ link }}
        </v-btn>

        <v-spacer></v-spacer>

        <v-responsive max-width="260">
          <v-text-field
            density="compact"
            hide-details
            variant="solo"
          ></v-text-field>
        </v-responsive>
      </v-container>
    </v-app-bar>

    <v-main class="bg-grey-lighten-3">
      <v-navigation-drawer expand-on-hover rail color="black" permanent="">
    <v-list>
      <v-list-item
        prepend-avatar="https://pbs.twimg.com/profile_images/1237550450/mstom_400x400.jpg"
        title="Tom Anderson"
        subtitle="TomA@gmail.com"
      ></v-list-item>
    </v-list>
    <v-divider color="white"></v-divider>
    <v-list density="compact" nav>
      <v-list-item
        prepend-icon="mdi-home"
        title="Home"
        value="home"
      ></v-list-item>
      <v-list-item
        prepend-icon="mdi-domain"
        title="Explore"
        value="explore"
      ></v-list-item>
      <v-list-item
        prepend-icon="mdi-tag"
        title="Book Resell"
        value="resell"
      ></v-list-item>
      <v-list-item
        prepend-icon="mdi-pen"
        title="Study"
        value="study"
      ></v-list-item>
      <v-list-item
        prepend-icon="mdi-note"
        title="Notes"
        value="notes"
      ></v-list-item>
    </v-list>
    <v-divider color="white"></v-divider>
    <v-list density="compact" nav>
      <v-list-item
        prepend-icon="mdi-logout"
        title="Sign Out"
        value="signout"
      ></v-list-item>
    </v-list>
  </v-navigation-drawer>
      <v-container>
        <v-row>
          <v-col cols="2">
            <v-sheet rounded="lg">
              <v-list rounded="lg">
                <v-list-item
                  v-for="n in 5"
                  :key="n"
                  link
                >
                  <v-list-item-title>
                    List Item {{ n }}
                  </v-list-item-title>
                </v-list-item>

                <v-divider class="my-2"></v-divider>

                <v-list-item
                  link
                  color="grey-lighten-4"
                >
                  <v-list-item-title>
                    Refresh
                  </v-list-item-title>
                </v-list-item>
              </v-list>
            </v-sheet>
          </v-col>

          <v-col>
            <v-sheet
              min-height="70vh"
              rounded="lg"
            >
            <center>
              <br>
              
            </center>
              <!--  -->
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>

    </v-main>
  </v-app>
</template>

<script>
  export default {
    data: () => ({
      links: [
        'Dashboard',
        'Messages',
        'Profile',
        'Updates',
      ],
    }),
  }
  
</script>

<script setup>
  import { ref } from 'vue'

const theme = ref('light')

function onClick () {
  theme.value = theme.value === 'light' ? 'dark' : 'light'
}

</script>