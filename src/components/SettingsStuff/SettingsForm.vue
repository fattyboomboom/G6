<template>
  <v-form>
    <v-card>
      <v-row no-gutters>
        <v-col cols="4">
          <v-avatar :image=profilePictureUrl> </v-avatar>
        </v-col>
        <v-col cols="8">
          <v-card-title> Change Profile Picture </v-card-title>
          <v-card-text>
            <v-file-input
              v-model="file"
              label="Upload Profile Picture"
              accept="image/*"
              @change="uploadPicture"
            ></v-file-input>
            <v-btn class="savebtn">Save</v-btn>
          </v-card-text>
        </v-col>
      </v-row>
    </v-card>

    <v-card>
      <v-card-title class="text-h5">About You</v-card-title>
      <v-card-text class="">
        <v-row>
          <v-col cols="12" md="6">
            <v-text-field
              label="First Name"
              v-model="FirstName"
              outlined
            ></v-text-field>
          </v-col>
          <v-col cols="12" md="6">
            <v-text-field
              label="Last Name"
              v-model="LastName"
              outlined
            ></v-text-field>
          </v-col>
          <v-col cols="12" md="6">
            <v-text-field
              label="Date of Birth"
              v-model="DOB"
              outlined
            ></v-text-field>
          </v-col>
          <v-col cols="12" md="6">
            <v-text-field label="Major" v-model="Major" outlined></v-text-field>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>

    <v-row class="mt-8">
      <v-col cols="12" md="6" offset-md="3">
        <v-btn color="primary" block @click="saveSettings">Save Settings</v-btn>
      </v-col>
    </v-row>
  </v-form>
</template>

<script>
// import { ref } from 'vue'
import { getStorage, ref, uploadBytesResumable, getDownloadURL, } from "firebase/storage";
import { auth } from "@/firebase";

export default {
  name: "SettingsForm",
  data() {
    return {
      file: null,
      profilePictureUrl: "",
    };
  },
  methods: {
    async uploadPicture(e) {
      const storage = getStorage();
      const storageRef = ref(storage, auth.currentUser.uid + "/profilePicture/" + e.target.files[0].name);

      // 'file' comes from the Blob or File API
      const uploadTask = uploadBytesResumable(storageRef, e.target.files[0]);

      uploadTask.on(
        "state_changed",
        (snapshot) => {
          // Observe state change events such as progress, pause, and resume
          // Get task progress, including the number of bytes uploaded and the total number of bytes to be uploaded
          const progress =
            (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
          console.log("Upload is " + progress + "% done");
          switch (snapshot.state) {
            case "paused":
              console.log("Upload is paused");
              break;
            case "running":
              console.log("Upload is running");
              break;
          }
        },
        (error) => {
          // Handle unsuccessful uploads\
          console.log(error);
        },
        () => {
          // Handle successful uploads on complete
          // For instance, get the download URL: https://firebasestorage.googleapis.com/...
          getDownloadURL(uploadTask.snapshot.ref).then((downloadURL) => {
            console.log("File available at", downloadURL);
            this.profilePictureUrl = downloadURL;
            console.log(this.profilePictureUrl);
            console.log(this.file);
          });
        }
      );
    },
  },
};
</script>

<style scoped>
.v-form {
  border: solid;
  border-color: #4a6fa5;
  border-width: 5px;
  width: 50%;
  margin-left: 25%;
  height: 90%;
  box-shadow: 0 16px 56px rgba(0, 0, 0, 0.1), 0 16px 56px rgba(0, 0, 0, 0.1),
    0 16px 56px rgba(0, 0, 0, 0.1);
}
.v-card {
  border: solid;
  border-color: #4a6fa5;
  border-width: 5px;
  /* margin-inline: 5%; */
  margin: 5%;
  height: 35%;
}

.savebtn {
  margin-left: 40%;
  margin-top: 5%;
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
  align-content: center;
  border-color: #4a6fa5;
  border: solid;
  border-width: 2px;
}
.v-text-field,
.v-select,
.v-checkbox {
  margin-bottom: 16px;
}
</style>
