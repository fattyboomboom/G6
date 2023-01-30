<template>
    <v-form
      ref="form"
      v-model="valid"
      lazy-validation
    >
    <v-row> 
    <v-col cols="4">
      <v-text-field
        v-model="Title"
        :counter="10"
        :rules="bookRules"
        label="Book Title"
        required
      ></v-text-field>
  
      <v-text-field
        v-model="Class"
        :rules="classRules"
        label="Class"
        required
      ></v-text-field>
  
      <v-select
        v-model="select"
        :items="conditions"
        :rules="[v => !!v || 'Condition is required']"
        label="Condition"
        required
      ></v-select>
      
      <v-text-field 
      label="Additional Info (Optional)"
      >
        

      </v-text-field>

      <v-btn
        
        class="mr-4"
        @click="validate"
      >
        List
      </v-btn>
  
      <v-btn
        color="error"
        class="mr-4"
        @click="reset"
      >
        Reset Form
      </v-btn>
    </v-col>
    </v-row>

    </v-form>
  </template>
  <script>
    export default {
      data: () => ({
        valid: true,
        bookTitle: '',
        bookRules: [
          v => !!v || 'Book Title is required',
        ],
        classTitle: '',
        classRules: [
          v => !!v || 'Class is required',
        ],
        select: null,
        conditions: [
          'Like New',
          'Very Good',
          'Good',
          'Poor',
        ],
        checkbox: false,
      }),
  
      methods: {
        async validate() {
          const { valid } = await this.$refs.form.validate()
  
          if (valid) alert('[List Success]')
        },
        reset () {
          this.$refs.form.reset()
        }
      },
    }
  </script>