<template>
    <v-row>
      <v-col v-for="book in books" :key="book" class="d-flex" cols="3">
        <VCard class="bookcards">
          <a href="profile">
            <v-img :src="book.bookimage" cover class="bimage">
              <template v-slot:placeholder>
                <v-row class="fill-height ma-0" align="center" justify="center">
                  <v-progress-circular
                    indeterminate
                    color="grey-lighten-5"
                  ></v-progress-circular>
                </v-row>
              </template> </v-img
          ></a>
          <VDivider thickness="2"></VDivider>
          <p>{{ book.bookname }}</p>
          <VDivider class="dividers"></VDivider>
          <p>{{ book.bookclass }}</p>
          <VDivider class="dividers"></VDivider>
          <p>{{ book.postedby }}</p>
          <VDivider class="dividers"></VDivider>
          <p>{{ book.date }}</p>
        </VCard>
      </v-col>
    </v-row>
  </template>
  
  <script>
  
  
  export default {
      name: "NotesLists",
      data() {
          return {
              books: [
                  {
                      id: 1,
                      bookname: "The American Women’s Movement ",
                      bookclass: "PSC 255",
                      bookimage: "https://th.bing.com/th/id/OIF.XLtOXQg5N7Er3UpWosbrFQ?pid=ImgDet&rs=1",
                      postedby: "Avery Thompson",
                      date: "2023-04-05",
                  },
                  {
                      id: 2,
                      bookname: "Identity Politics in the United States",
                      bookclass: "PSC 353",
                      bookimage: "https://th.bing.com/th/id/OIP.LWa-1vW872I_fQNLd3_4DQAAAA?pid=ImgDet&rs=1",
                      postedby: "Marcus Nguyen",
                      date: "2023-04-05",
                  },
                  {
                      id: 3,
                      bookname: "Campbell Biology 12th Edition",
                      bookclass: "BIOL 191",
                      bookimage: "https://i.pinimg.com/736x/82/64/2c/82642c9a6b459e695221e4fb0fec6fa2.jpg",
                      postedby: "Caleb Green",
                      date: "2023-04-03",
                  },
                  {
                      id: 4,
                      bookname: "Mega 2560 Complete Starter Kit",
                      bookclass: "MATH 101",
                      bookimage: "https://i.pinimg.com/originals/0e/bb/08/0ebb081c12ad3cadcfd2b27b61e13e1e.jpg",
                      postedby: "Avery Thompson",
                      edition: "NA",
                      date: "2023-04-01",
                  },
                  {
                      id: 5,
                      bookname: "History of the World Map by Map",
                      bookclass: "HIST 310",
                      bookimage: "https://i.pinimg.com/originals/20/04/30/20043065f5d99dc1880db243572f1894.jpg",
                      postedby: "Olivia Davis",
                      edition: "NA",
                      date: "2023-04-01",
                  },
                  {
                      id: 6,
                      bookname: "History of the World Map by Map",
                      bookclass: "HIST 310",
                      bookimage: "https://66.media.tumblr.com/3e92781b581971f7540dd00fba2abe0e/tumblr_okvgdy6Zej1w0nmn2o2_640.jpg",
                      postedby: "Isabella Lee",
                      date: "2023-03-22",
                  },
                  {
                      id: 7,
                      bookname: "History of the World Map by Map",
                      bookclass: "HIST 310",
                      bookimage: "https://66.media.tumblr.com/43f2944dffe8b65ce7c5091be66ae5f1/tumblr_pfnha0uX9S1ufgbqj_1280.jpg",
                      postedby: "Caleb Green",
                      date: "2023-03-19",
                  },
                  {
                      id: 8,
                      bookname: "History of the World Map by Map",
                      bookclass: "HIST 310",
                      bookimage: "https://heyitscamillegrey.com/wp-content/uploads/2018/08/IMG_5063-1.jpg",
                      postedby: "Isabella Lee",
                      date: "2023-03-17",
                  },
                  {
                      id: 9,
                      bookname: "History of the World Map by Map",
                      bookclass: "HIST 310",
                      bookimage: "https://community.devexpress.com/blogs/office/v20.2/pdf-sticky-notes-20-2-blog.png",
                      postedby: "Olivia Davis",
                      date: "2023-03-13",
                  },
                  {
                      id: 10,
                      bookname: "History of the World Map by Map",
                      bookclass: "HIST 310",
                      bookimage: "https://new-fullview-html.oneclass.com/xZ42pBrOjD9jpA3BmAkkM2XW6e03JNgd/low/bg1.png",
                      postedby: "Avery Thompson",
                      date: "2023-03-12",
                  },
                  {
                      id: 10,
                      bookname: "History of the World Map by Map",
                      bookclass: "HIST 310",
                      bookimage: "https://pm1.narvii.com/6451/30bf2feeb50e019d0c01c0c371ea1f163d36509e_hq.jpg",
                      postedby: "Olivia Davis",
                      date: "2023-03-02",
                  },
                  {
                      id: 11,
                      bookname: "History of the World Map by Map",
                      bookclass: "HIST 310",
                      bookimage: "https://i.pinimg.com/564x/0b/a1/0b/0ba10bf5deac858d4952900282ea3623--calculus-notes-math-notes.jpg",
                      postedby: "Marcus Nguyen",
                      date: "2023-03-01",
                  },
              ],
          };
      },
  
  };
  </script>
  
  <style scoped>
  .bimage {
    height: 65%;
    width: 100%;
  }
  
  .bookcards {
    background-color: whitesmoke;
    /* margin: 10%; */
    margin-top: 3%;
    margin-right: 2%;
    margin-left: 25%;
    border-color: #4a6fa5;
    border-width: 3px;
    padding: 0.5rem;
    line-height: 1.5;
    width: 100%;
    height: 100%;
  }
  
  .bookcards:hover {
    box-shadow: 0 16px 56px rgba(0, 0, 0, 0.1), 0 16px 56px rgba(0, 0, 0, 0.1),
    0 16px 56px rgba(0, 0, 0, 0.1);


  box-sizing: border-box;
  }
  
  p {
    text-align: center;
    color: black;
  }
  
  .dividers {
    border-color: #05668d;
    border-width: 1px;
  }
  </style>
  