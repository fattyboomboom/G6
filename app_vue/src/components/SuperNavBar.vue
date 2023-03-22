<template> 
    <v-row> 
    
      <v-col> 
        
        <v-card> 
          <v-card-title class="bg-black d-flex justify-space-between"> 
            <v-spacer></v-spacer> 
            <span class="text-center">Super User</span> 
   
            <v-spacer></v-spacer> 
   
            <v-menu> 
              <template v-slot:activator="{ props }"> 
                <v-btn variant= "text" v-bind="props">Class</v-btn> 
              </template> 
   
              <v-list> 
                <v-list-item 
                  v-for="(item, i) in items" 
                  :key="i" 
                > 
                  <v-list-item-title>{{ item.title }}</v-list-item-title> 
                </v-list-item> 
              </v-list> 
            </v-menu> 
             <v-menu> 
              <template v-slot:activator="{ props }"> 
                <v-btn variant= "text" v-bind="props">User</v-btn> 
              </template> 
              <v-list> 
                <v-list-item 
                  v-for="(item, i) in items2" 
                  :key="i" 
                > 
                  <v-list-item-title>{{ item.title }}</v-list-item-title> 
                </v-list-item> 
              </v-list> 
            </v-menu> 
            <v-btn variant= "text" >Review reports</v-btn>
          </v-card-title> 
        </v-card> 
      </v-col> 
    </v-row> 
  </template> 
     
  <script> 
    export default { 
      data: () => ({ 
        items: [ 
          { title: 'Add' }, 
          { title: 'Modify' }, 
          { title: 'Remove' }, 
       ], 
         items2: [ 
          { title: 'Add' }, 
          { title: 'Modify' }, 
          { title: 'Remove' }, 
        ], 
      }), 
    } 
  </script>