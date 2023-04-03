## ***WolfCampus***

Built using Vue 3 and Firebase 9

## Project setup
Within Project Directory
```
npm install
```

## Run Project
```
npm run serve
```

## To use this project, make sure to add your Firebase configuration file to the following location: 
```
/src/firebase/index.js
```
**Warning:** Always ensure that the 'firebase' directory is git ignored.

## To use Firebase services and the Emulator UI:
```
1. Enter root directory
2. Run 'firebase init'
3. Enter 'Y'
4. Select Firestore & Functions
5. Retrieve firebase project ID and paste into project selection
6. To start emulators run: 'firebase emulators:start'
```

## What to do for out of date JDK
```
1. Install latest JDK here: https://www.oracle.com/java/technologies/downloads/#jdk20-windows
2. Enter Environment Variables
3. Create new system variable called: 'JAVA_HOME'
4. Find your 'Java' folder and copy path (i.e "C:\Program Files\Java\jdk-20")
5. Press OK
6. Edit 'Path' variable in system variables
7. Create new path called: '%JAVA_HOME%\bin'
8. Close all VSCode instances and reopen
9. To check you have a JDK version > 18, type in terminal 'java -version' You should have version 20.
```
