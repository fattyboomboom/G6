<template>
    <v-card class="ml-16" max-width="30%">
      <v-card-title class="headline">Class Information</v-card-title>
      <v-card-text>
        <p>Class Description: {{ classDescription }}</p>
        <p>Professor Name: {{ professorName }}</p>
        <p>Section Number: {{ sectionNumber }}</p>
      </v-card-text>
      <v-card-actions>
        <v-btn @click="showDialog = true">Edit Class</v-btn>
      </v-card-actions>
      <v-dialog v-model="showDialog" max-width="400px">
        <v-card>
          <v-card-title class="headline">Edit Class Information</v-card-title>
          <v-card-text>
            <v-form ref="form">
              <v-text-field v-model="classDescription" label="Class Description"></v-text-field>
              <v-text-field v-model="professorName" label="Professor Name"></v-text-field>
              <v-select v-model="sectionNumber" :items="sectionNumbers" label="Section Number"></v-select>
              <v-btn @click="openUploadPrompt">Upload Image</v-btn>
            <input type="file" ref="fileInput" @change="uploadImage" style="display: none"/>
            <v-btn @click="openUploadPrompt">Upload Syllabus</v-btn>
            <input type="file" ref="fileInput" @change="uploadImage" style="display: none"/>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-btn @click="cancelChanges">Cancel</v-btn>
            <v-btn color="primary" @click="saveChanges">Save</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-card>
  </template>
  
  <script>

  export default {
    name: "ModEdit",
    data() {
      return {
        showDialog: false,
        classDescription: "Class Description",
        professorName: "John Doe",
        sectionNumber: "1001",
        sectionNumbers: ["1001", "1002"],
      };
    },
    methods: {
      cancelChanges() {
        this.classDescription = "Class Description";
        this.professorName = "John Smith";
        this.sectionNumber = "1001";
        this.showDialog = false;
      },
      saveChanges() {
        this.$refs.form.validate();
        this.showDialog = false;
      },
      openUploadPrompt() {
      this.$refs.fileInput.click();
    },
    uploadImage() {

    }
    },
  };
  </script>