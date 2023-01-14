<template>
  <v-row>
    <v-col v-for="book in books" :key="book" class="d-flex child-flex" cols="3">
      <VCard color="white">
        <a href="profile">
          <v-img
            :src="book.bookimage"
            siz
            cover
            class="bimage bg-grey-lighten-2"
          >
            <template v-slot:placeholder>
              <v-row class="fill-height ma-0" align="center" justify="center">
                <v-progress-circular
                  indeterminate
                  color="grey-lighten-5"
                ></v-progress-circular>
              </v-row>
            </template> </v-img
        ></a>
        <VDivider color="white" thickness="2"></VDivider>
        <center>
          <p>{{ book.bookname }}</p>
        </center>
        <VDivider></VDivider>
        <center>
          <p>{{ book.bookclass }}</p>
        </center>
        <VDivider></VDivider>
        <center>
          <p>{{ book.price }}</p>
        </center>
      </VCard>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: "BookListings",
  data() {
    return {
      books: [
        {
          id: 0,
          bookname: "History of the World Map by Map",
          bookclass: "HIST 310",
          bookimage: "https://m.media-amazon.com/images/I/81VTod4MpkL.jpg",
          price: "Price",
        },
        {
          id: 1,
          bookname: "The C++ Programming Language, 4th Edition",
          bookclass: "CS 135",
          bookimage: "https://m.media-amazon.com/images/I/51iQMFmLFtL.jpg",
          price: "Price",
        },
        {
          id: 2,
          bookname: "Campbell Biology 12th Edition",
          bookclass: "BIOL 191",
          bookimage: "https://m.media-amazon.com/images/I/41mqPR4WuCL.jpg",
          price: "Price",
        },
        {
          id: 3,
          bookname: " Mega 2560 Complete Starter Kit",
          bookclass: "CPE 301",
          bookimage:
            "https://m.media-amazon.com/images/I/51K67ltZWdL._AC_SL1000_.jpg",
          price: "Price",
        },
        {
          id: 4,
          bookname: "History of the World Map by Map",
          bookclass: "HIST 310",
          bookimage: "https://m.media-amazon.com/images/I/51iQMFmLFtL.jpg",
          price: "Price",
        },
        {
          id: 5,
          bookname: "History of the World Map by Map",
          bookclass: "HIST 310",
          bookimage: "https://m.media-amazon.com/images/I/51iQMFmLFtL.jpg",
          price: "Price",
        },
        {
          id: 6,
          bookname: "History of the World Map by Map",
          bookclass: "HIST 310",
          bookimage: "https://m.media-amazon.com/images/I/51iQMFmLFtL.jpg",
          price: "Price",
        },
        {
          id: 7,
          bookname: "History of the World Map by Map",
          bookclass: "HIST 310",
          bookimage: "https://m.media-amazon.com/images/I/51iQMFmLFtL.jpg",
          price: "Price",
        },
        {
          id: 8,
          bookname: "History of the World Map by Map",
          bookclass: "HIST 310",
          bookimage: "https://m.media-amazon.com/images/I/51iQMFmLFtL.jpg",
          price: "Price",
        },
        {
          id: 9,
          bookname: "History of the World Map by Map",
          bookclass: "HIST 310",
          bookimage: "https://m.media-amazon.com/images/I/51iQMFmLFtL.jpg",
          price: "Price",
        },
        {
          id: 10,
          bookname: "History of the World Map by Map",
          bookclass: "HIST 310",
          bookimage: "https://m.media-amazon.com/images/I/51iQMFmLFtL.jpg",
          price: "Price",
        },
        {
          id: 11,
          bookname: "History of the World Map by Map",
          bookclass: "HIST 310",
          bookimage: "https://m.media-amazon.com/images/I/51iQMFmLFtL.jpg",
          price: "Price",
        },
      ],
    };
  },
};
</script>

<style>
.bimage {
  height: 300px;
  width: 250px;
  align-items: center;
}
</style>
