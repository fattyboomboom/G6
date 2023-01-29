<template>
  <v-app>
    <v-sheet style="max-width: 3000px; position: relative;" class="flex">
      <v-menu v-model="menu" offset-y>
        <template v-slot:activator="{ on }">
          <v-btn block v-on="on" color="primary" elevation="2">
            Select Course
          </v-btn>
        </template>

        <v-list>
          <v-list-item
            v-for="course in courses"
            :key="course"
            @click="selectCourse(course)"
          >
            <v-list-item-title>{{ course }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-sheet>
    <v-content>
      <v-container fill-height grid-list-md class="ml-5">
        <v-layout row>
          <v-row>
            <v-col
              align="center"
              sm="3"
              col="3"
              v-for="note in notes"
              :key="note.id"
            >
              <v-card :class="{ 'elevation-12': hover }" class="mt-16">
                <v-img
                  :src="require('@/assets/' + note.image)"
                  :aspect-ratio="1"
                ></v-img>
              </v-card>
            </v-col>
          </v-row>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  components: {
  },

  data() {
    return {
      notes: [
        {
          id: 0,
          lecture: "1",
          professor: "Monica Nicolescu",
          image: "note.jpg",
        },
        {
          id: 1,
          lecture: "2",
          professor: "Monica Nicolescu",
          image: "note2.jpg",
        },
        {
          id: 2,
          lecture: "3",
          professor: "Monica Nicolescu",
          image: "note3.jpg",
        },
        {
          id: 3,
          lecture: "4",
          professor: "Monica Nicolescu",
          image: "note4.jpg",
        },
        {
          id: 4,
          lecture: "4",
          professor: "Monica Nicolescu",
          image: "note5.jpg",
        },
        {
          id: 5,
          lecture: "4",
          professor: "Monica Nicolescu",
          image: "note5.jpg",
        },
        {
          id: 6,
          lecture: "4",
          professor: "Monica Nicolescu",
          image: "note5.jpg",
        },
        {
          id: 7,
          lecture: "4",
          professor: "Monica Nicolescu",
          image: "note5.jpg",
        },
        {
          id: 8,
          lecture: "4",
          professor: "Monica Nicolescu",
          image: "note5.jpg",
        },
      ],
    };
  },
  methods: {},
};
</script>

<style>
#rounded-card {
  border-radius: 50%;
  min-height: 500px;
  min-width: 500px;
}

.v-card.v-hover {
  background-color: blue;
}
</style>
