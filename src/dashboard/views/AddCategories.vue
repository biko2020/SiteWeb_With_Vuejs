<template>
 <v-app>
    <Header />
    <router-view />
   <v-conten>
        <CategorieApp />
   </v-conten>
 </v-app>
   
</template>
<script>
import Header from '@/dashboard/components/Admin/Header.vue';
import CategorieApp from '@/dashboard/components/CategorieApp.vue';
export default {
    name:'Categories',
    components: {
        Header,
        CategorieApp,
    }
    
}
</script>
