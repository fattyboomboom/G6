<template>
  <v-form>
    <v-card>
      <v-card-title class="text-h5">Add Class</v-card-title>
      <v-card-text class="">
        <v-col cols="12" md="12">
          <v-text-field
            label="Class Prefix"
            v-model="ClassPrefix"
            type="text"
            outlined
          ></v-text-field>
        </v-col>
        <v-col cols="12" md="12">
          <v-text-field
            label="Class Number"
            v-model="ClassNumber"
            type="number"
            outlined
          ></v-text-field>
        </v-col>
        <v-col cols="12" md="12">
          <v-text-field
            label="Class Sectioin"
            v-model="ClassSection"
            outlined
          ></v-text-field>
        </v-col>
      </v-card-text>

      <v-row>
        <v-col cols="12" md="10">
          <v-btn block @click="saveSettings">Save</v-btn>
        </v-col>
      </v-row>
    </v-card>
  </v-form>
</template>

<script>
export default {
  name: "AddClass",
};
</script>

<style scoped>
.v-form {
  background-color: rgba(
    255,
    255,
    255,
    0.5
  ); /* set a semi-transparent white background */
  backdrop-filter: blur(10px); /* apply a blur effect */
  opacity: 1; /* set the overall opacity */
}
.v-card {
  border: solid;
  border-color: #4a6fa5;
  border-width: 5px;
  /* margin-inline: 5%; */
  margin: 5%;
  height: 80%;
  box-shadow: 0 16px 56px rgba(0, 0, 0, 0.1), 0 16px 56px rgba(0, 0, 0, 0.1),
    0 16px 56px rgba(0, 0, 0, 0.1);
  width: 35%;
}

.v-card-title {
  color: black;
  text-align: center;
}

.v-avatar {
  height: 100%;
  width: 100%;
  margin: 5px;
}

.v-btn {
  border-color: #4a6fa5;
  border: solid;
  border-width: 2px;
  margin-left: 11%;
}
.v-text-field {
  border-color: #4a6fa5;
  border: solid;
  border-width: 2px;
  margin-left: 2%;
}
</style>
