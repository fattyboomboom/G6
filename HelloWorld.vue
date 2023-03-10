<template>
<v-app :theme="theme">
    <v-app-bar>
      <v-spacer></v-spacer>

      <v-btn :prepend-icon="theme === 'light' ? 'mdi-weather-sunny' : 'mdi-weather-night'" @click="onClick">
        Toggle Theme
      </v-btn>
    </v-app-bar>

    <v-main>
      <v-app id="inspire">

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
<div class="container-style">
<div class="card1">
    <div class="card-header">
      <h1>Classes</h1>
    </div>
    <div class="card-body">
      <div class="button-group">
        <button class="button"><b><h3>CS 365</h3></b></button>
        <button class="button"><b><h3>MATH 486</h3></b></button>
        <button class="button"><b><h3>CS 326</h3></b></button>
        <button class="button"><b><h3>MATH 488</h3></b></button>
        <button class="button"><b><h3>CS 425</h3></b></button>
      </div>
    </div>
  </div>

    <div class="form-container">
      <div style="text-align: center;">
       <legend><h1><b>Create a Study Session</b></h1></legend>
       </div>
         <form>
            <fieldset>
                <div class="form-row">
                  <label for="name"><b><u>Select Class:</u></b></label>
                  <input type="text" id="name" v-model="form.name" />
                </div>
      <div class="form-row">
        <label for="date"><b><u>Date:</u></b></label>
        <input type="date" id="date" v-model="form.date" />
      </div>
      <div class="form-row">
        <label for="time"><b><u>Time:</u></b></label>
          <v-time-picker v-model="picker"></v-time-picker>
        <input type="time" id="time" v-model="form.time" />
      </div>
      <div class="form-row">
        <label for="message"><b><u>Study Session Title:</u></b></label>
        <textarea id="message" v-model="form.message"></textarea>
      </div>
      <div class="form-row">
        <label for="location"><b><u>Study Session Location:</u></b></label>
        <textarea id="location" v-model="form.location"></textarea>
      </div>
      <div style="text-align: left"><h3><center><b><i>Note: This location must be on campus.</i></b></center></h3></div>
      <div class="form-row">
        <label for="comments"><b><u>Additional Comments:</u></b></label>
        <textarea id="comments" v-model="form.comments"></textarea>
      </div>
        <button class="button" @click="submitForm" type="submit">Submit</button>
       <!-- <button type="submit">Submit</button>
        <div class="d-flex justify-space-between">
       </div>
    <v-btn>
      <button type="submit">Cancel</button>
        <div class="d-flex justify-space-between">
       </div>
    </v-btn>-->  
    </fieldset>
    </form>
    </div>

 <div class="control-card">
    <div class="control-header">
      <h1>Control Center</h1>
    </div>
    <div class="control-body">
      <h2><u>Devices</u></h2>
      <!--<ul>
        <li v-for="device in devices" :key="device.id">
          {{ device.name }} - {{ device.status }}
          <button @click="toggleStatus(device)">
            {{ device.status === 'online' ? 'Offline' : 'Online' }}
          </button>
        </li>
      </ul>
      <label for="device-name">Device Name</label>
        <input type="text" class="form-control" v-model="newDeviceName" id="device-name" placeholder="Enter device name">
      </div>
      <div>-->
    <form>
      <div style="text-align: center;">
        <label for="input-field">Device Name:</label>
      </div>
      <input type="text" id="deviceName" v-model="form.inputText" />
      <button class="button" @click="devicesForm">Submit</button>
    </form>
    <div v-if="outputText">
      <p>Output: {{ outputText }}</p>
    </div>
  </div>
</div>

      <!--<button class="btn btn-primary" @click="addDevice">Add Device</button>
    <div class="control-footer">
      <button @click="onClick">Click Me!</button>
      <h2>Logs</h2>
      <ul>
        <li v-for="log in logs" :key="log.id">
          {{ log.time }} - {{ log.message }}
        </li>
      </ul>
    </div>-->
  </div>


</v-main>
  </v-app>
   </v-main>
</v-app>

</template>

<script>
import { ref } from 'vue';
import axios from "axios";
//import { useTheme } from 'vuetify'

//const theme = ref('light')
//function onClick () {
  //theme.value = theme.value === 'light' ? 'dark' : 'light'
//}

export default {
  setup() {
    const notification = ref([]);
    const bookItem = ref([]);
    const deviceStatus = ref([]);
    const error = ref(null);
    const theme = ref(null)
    // const theme = useTheme();
    axios
      .get("http://localhost:3001/notifs")
      .then((response) => {
        console.log(response);
        notification.value = response.data;
        console.log(response.data);
      })
      .catch((error) => {
        console.log(error);
      });

      axios
      .get("http://localhost:3001/devices")
      .then((response) => {
        console.log(response);
        deviceStatus.value = response.data;
        console.log(response.data);
      })
      .catch((error) => {
        console.log(error);
      });

      return(notification, error, bookItem, deviceStatus, theme);
  },
  
    /*return {
      form,
      submitForm,
      picker: 'null',
      theme: 'light'
      };*/
   

   data:() => {
    return {
      form: {
      name: '',
      date: null,
      time: '',
      message: '',
      location: '',
      comments: '',
      deviceStatus: '',
      inputText:'',
      outputText: '',
      /*links: [
        'Dashboard',
        'Messages',
        'Profile',
        'Updates',
      ]*/
    }
   };
  },

  methods: {
    onClick () {
  this.theme = this.theme === 'light' ? 'dark' : 'light'
},
  /*toggleTheme() {
    this.theme = this.theme === 'light' ? 'dark' : 'light';
  }
  };
  toggleStatus(device) {
      device.status = device.status === 'online' ? 'offline' : 'online';
      const message = `${device.name} turned ${device.status}`;
      this.logs.push({ id: Date.now(), time: new Date().toLocaleTimeString(), message });
    },
    addDevice() {
      if (!this.newDeviceName) {
        return;
      }
      const newDevice = {
        id: Date.now(),
        name: this.newDeviceName,
        status: 'offline',
      };
      this.devices.push(newDevice);
      this.newDeviceName = '';
    },
    displayText() {
      this.outputText = this.inputText;
  },*/


  submitForm() {
    var data = {
      name: this.form.name,
      date: this.form.date,
      time: this.form.time,
      message: this.form.message,
      location: this.form.location,
      comments: this.form.comments,
    };
      
    axios
        .post("http://localhost:3001/studyForm", data)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });    
    },

  devicesForm(){
    var data = {
      deviceName: this.form.inputText,
    };

    axios
        .post("http://localhost:3001/devicesForm", data)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });    
    },
  },
};

</script>

<style>
/*.form-container {
  background-color: #9ac4ed;
  padding: 20px;
  max-width: 400px;
  margin: 0 auto;
  margin-top: 20%;
}

.form-row {
  display: grid;
  grid-template-columns: 5fr 5fr;
  margin-bottom: 20px;
  max-width: 400px;
  margin: 0 auto;
  margin-top: 20%;
}

label {
  text-align: left;
  padding-left: 20px;
}

.container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin-top: 20%;
}


.card-container {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
}
*/

.container-style {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 75px;
}

.card2 {
  width: 30%;
  height: 50%;
  margin-top: 15%;
  margin-right: 5%;
  background-color: white;
  border: 1px solid gray;
  border-radius: 5px;
  padding: 10px;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
}

.control-center {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.devices {
  margin-top: 20px;
}

.devices h2 {
  font-size: 18px;
}

.devices ul {
  list-style: none;
  padding: 0;
}

.devices li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  border-bottom: 1px solid #ccc;
}

.logs {
  margin-top: 20px;
}

.logs h2 {
  font-size: 18px;
}

.logs ul {
  list-style: none;
  padding: 0;
}

.logs li {
  padding: 10px;
  border-bottom: 1px solid #ccc;
}

.card1 {
  background-color: #fff;
  border: 1px solid #e0e0e0;
  border-radius: 5px;
  box-shadow: 0 12px 12px rgba(0, 0, 0, 0.1);
  width: 300px;
  padding: 20px;
  margin: 5px;
  border: 5px solid #3f7eeb
}

.card-header {
  background-color: #f5f5f5;
  border-bottom: 1px solid #ccc;
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
  font-size: 16px;
  font-weight: bold;
  padding: 10px;
  text-align: center;
  border: 5px solid #3f7eeb
}

.card-body {
  padding: 20px;
}

.button-group {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.button {
  background-color: #8fc2f8;
  border: none;
  border-radius: 5px;
  color: rgb(0, 0, 0);
  cursor: pointer;
  font-size: 14px;
  font-weight: bold;
  padding: 10px;
  text-align: center;
  text-decoration: none;
  transition: all 0.2s ease-in-out;
}

.button:hover {
  transform: scale(1.1);
}

/* form styling below */
.form-container {
  background-color: #f9fafb;
  border-radius: 20px;
  box-shadow: 0 12px 12px rgba(0, 0, 0, 0.1);
  width: 600px;
  padding: 20px;
  margin-left: 20px;
  border: 5px solid #3f7eeb;
}

.form-row {
  margin-bottom: 20px;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
}

input[type="text"],
input[type="date"],
input[type="message"],
input[type="location"],
input[type="comments"],
textarea {
  width: 100%;
  padding: 10px;
  border-radius: 5px;
  border: 2px solid #3f7eeb;
  background-color: #ffffff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

input[type="text"]:focus,
input[type="date"]:focus,
input[type="message"]:focus,
input[type="location"]:focus,
input[type="comments"]:focus,
textarea:focus {
  outline: none;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.btn {
  border-radius: 5px;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}

.btn-primary {
  background-color: #3f7eeb;
  color: rgb(0, 0, 0);
}

.control-card {
  background-color: #fff;
  border: 1px solid #e0e0e0;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  max-width: 600px;
  overflow: hidden;
  padding: 20px;
  margin: 5px;
  border: 5px solid #3f7eeb;
}

.control-header {
  border: 5px solid #3f7eeb;
  background-color: #f5f5f5;
  padding: 10px;
}

.control-header h2 {
  margin: 0;
}

.control-body {
  padding: 20px;
}

.control-footer {
  background-color: #f5f5f5;
  padding: 10px;
  text-align: right;
}

.control-footer button {
  background-color: #3f7eeb;
  border: none;
  border-radius: 5px;
  color: #fff;
  cursor: pointer;
  padding: 10px 20px;
  transition: background-color 0.2s ease-in-out;
}

.control-footer button:hover {
  background-color: #3f7eeb;
}

.form-container:hover {
  transform: scale(1.05);
  box-shadow: 0 12px 12px rgba(0, 0, 0, 0.2);
}

.card1:hover {
  transform: scale(1.05);
  box-shadow: 0 12px 12px rgba(0, 0, 0, 0.2);
}

.control-card:hover {
  transform: scale(1.05);
  box-shadow: 0 12px 12px rgba(0, 0, 0, 0.2);
}

</style>
