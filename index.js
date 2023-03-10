const express = require('express');
const body_parser = require('body-parser');
const app = express();

app.use(express.json());
app.use(express.urlencoded({extended: false}));

const PORT = 3001;
let cors = require("cors");
const { request } = require('express');
app.use(cors());

const study = [
    {
        id: "1", studentName: "Carlos", className: "CS 365", classDate: "03-10-2023", classTime: "02:30 PM", classLocation: "WPEB 105",
    }
]

const book = [
    {
        id: "2", bookName: "The Clean Coder: A Code of Conduct for Professional Programmers", bookEdition: "1st Edition", bookAuthor: "Robert Martin", bookPrice: "$34.76",
        id: "3", bookName: "Clean Architecture: A Craftsman's Guide to Software Structure and Design", bookEdition: "1st Edition", bookAuthor: "Robert Martin", bookPrice: "28.35",

    }
]

const deviceStatus = [
    {
    "devices": [
    { id: 1, name: 'Device 1', status: 'online' },
    { id: 2, name: 'Device 2', status: 'offline' },
    { id: 3, name: 'Device 3', status: 'online' },
  ],
  "logs": [
    { id: 1, time: '10:00 AM', message: 'Device 1 turned on' },
    { id: 2, time: '10:15 AM', message: 'Device 2 turned off' },
    { id: 3, time: '11:00 AM', message: 'Device 3 turned on' },
  ],
}
]

app.listen(PORT, () => console.log(`Running Express Server on Port ${PORT}!`));

//form submission
app.post('/studyForm', (req,res) => {
    //res.send('studyForm');
    console.log(req.body)
    });

app.post('/devicesForm', (req,res) => {
    console.log(req.body)
});

app.get('/notifs', (req, res) => {
    res.status(200).send(study)
});

app.get('/devices', (req, res) => {
    res.status(200).send(deviceStatus)
});