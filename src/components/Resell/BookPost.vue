<template>
    <v-card>
      <v-card-title class="headline">Search Books</v-card-title>
      <v-card-text>
        <v-text-field class="query" v-model="query" label="Search For Book"></v-text-field>
        <v-btn class="search" @click="searchBooks">Search</v-btn>
       
            <div class="bookcontainer">
              <v-list> 
          <v-list-item v-for="book in books" :key="book.id" @click="selectBook(book)">
          
              <v-img :src="getBookImage(book)" contain></v-img>
         
            
              <v-list-item-title>{{ book.volumeInfo.title }}</v-list-item-title>
              <v-list-item-subtitle>{{ book.volumeInfo.authors }}</v-list-item-subtitle>
           
          </v-list-item>
      </v-list>
       </div>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        
  
      </v-card-actions>
    </v-card>
 </template>
  
<script>
  import axios from 'axios';
  
  export default {
    name: 'BookPost',
    data() {
      return {
        dialog: false,
        query: '',
        books: [],
        selectedBook: null,
        price: 0,
      };
    },
    
    methods: {
      searchBooks() {
        axios
          .get('https://www.googleapis.com/books/v1/volumes', {
            params: {
              q: this.query,
            },
          })
          .then((response) => {
            this.books = response.data.items;
            this.currentPage = 1;
          })
          .catch((error) => {
            console.error(error);
          });
      },
      closeDialog() {
        this.dialog = false;
      },
      getBookImage(book) {
        if (book.volumeInfo.imageLinks && book.volumeInfo.imageLinks.thumbnail) {
          return book.volumeInfo.imageLinks.thumbnail;
        } else {
          // Return a default image if no image is available
          return 'https://via.placeholder.com/128x192?text=No%20Image';
        }
      },
      selectBook(book) {
        this.selectedBook = book;
      },
      createPost() {
      },
    },
  };
</script>
<style scoped>
.v-card {
    width: 55%;
    border: 3px solid #4a6fa5;
    border-style: solid;
    border-radius: 25px;
    margin-top: 5%;
    height: 51%;
    box-shadow: 0 16px 56px rgba(0, 0, 0, 0.1), 0 16px 56px rgba(0, 0, 0, 0.1),
      0 16px 56px rgba(0, 0, 0, 0.1);
    margin-inline: 25%;
    z-index: 1;
    position: absolute;
  }
  .search {
    left: 80%;
    margin-bottom: 3%;
    background-color: #4a6fa5;
    color: white;
    margin-top: 2%;
    border-width: 2px;
  }

  .headline {
    text-align: center;
  } 

  .query{
    margin-left: 5%;
    width: 90%;
    color:#4a6fa5;
    border: 2px solid #4a6fa5;
  }
  .v-img {
    width: 50%;
    height: 192px;
  }

  .bookcontainer {
    height: 70%;
  overflow-y: scroll;
  margin-top: 20px;
  background-color: #e0e1dd;
  width: 100%;
  position: absolute;

  }
  
</style>
  
  
  
  