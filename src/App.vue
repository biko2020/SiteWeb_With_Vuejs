<template>
  <v-app>
    <Header />
    <v-content>
      <router-view></router-view>
    </v-content>
    <v-main>    
    <Footer />
    </v-main>

  </v-app>
</template>

<script>

import Header from './components/Header.vue';
import Footer from './components/Footer.vue';

export default {
  name: 'App',
  components: {
    Header,
    Footer
  },

 data() {
   return {

   }
  },
};
</script>
