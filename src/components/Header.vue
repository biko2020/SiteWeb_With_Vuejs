<template>
  <nav>
    <v-card>
      <v-app-bar dark fixed dense>
        <v-app-bar-nav-icon></v-app-bar-nav-icon>
        
        <v-toolbar-title class="H_logo">
           <v-img src="@/assets/logo/app/logo.png"></v-img>
        </v-toolbar-title>
        <v-spacer></v-spacer>

        <v-btn icon>
          <v-icon>mdi-magnify</v-icon>
        </v-btn>

        <v-btn icon>
          <v-icon>mdi-dots-vertical</v-icon>
        </v-btn>

        <template v-slot:extension>
            <v-toolbar-side-icon slot="activator"></v-toolbar-side-icon>
          <v-tabs hidden-md-and-up
            centered
            slider-color="yellow"
            background-color="transparent"
           
          >
            <v-tab
              link
              v-for="(menu, index) in menus"
              :key="index"
              :href="`#tab-${index}`"
              :to="menu.route"
            >
              {{ menu.title }}
            </v-tab>
          </v-tabs>
        </template>
      </v-app-bar>
    </v-card>
  </nav>
</template>


<script>
export default {
  name: "Header",

  data() {
    return {
      menus: [
        { title: "Home", route: "/" },
        { title: "Produits", route: "products" },
        { title: "Services", route: "services" },
        { title: "About-Us", route: "about" },
        { title: "Contact", route: "contact" },
      ],
    };
  },
};
</script>

<style scoped>
.H_logo {
  position: relative;
  padding: 0;
  top:40%;
  /*color: #ffca28;
  font-weight: bold;
  background-image: url("@/assets/logo/fournisseurs/alfa.png");
  background-repeat:no-repeat;*/
}
span.E_logo {
  color: #bdbdbd;
  font-weight: bold;
}
</style>

