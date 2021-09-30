<template>
  <v-footer padless fluid>
    <v-col lg="12">
      <v-row justify="center">
        <v-col lg="4" class="text-center">
           <v-toolbar-title
          ><span class="H_logo">HORIZON </span>
          <span class="E_logo"> EQUIPEMENT</span></v-toolbar-title
        >
          <v-card-text>
            <v-btn
              v-for="icon in icons"
              :key="icon"
              class="mx-4 black--text"
              icon
            >
              <v-icon size="24px">
                {{ icon }}
              </v-icon>
            </v-btn>
          </v-card-text>
          <v-subheader>
HORIZON EQUIPEMENT a noué des partenariats stratégiques avec des experts et des professionnels dans ses secteurs
d’intérêt au Maroc et à l’étranger afin de mieux répondre aux exigences du marché marocain.
          </v-subheader>
          <v-form class="mt-4">
            <v-text-field label="Email" outline dense />
            <v-btn rounded color="success">Demande Devis</v-btn>
          </v-form>
        </v-col>
      </v-row>
      <div class="mt-10">
        <v-divider></v-divider>
        <v-subheader>
          Copyright Horizon Equipements. All Rights Reserved
          {{ new Date().getFullYear() }} — <strong> </strong>
          <v-spacer />
          <strong>Designed by Ait Oufkir</strong>
        </v-subheader>
      </div>
    </v-col>
  </v-footer>
</template>


<script>
export default {
  name: "Footer",

  data() {
    return {
      icons: ["mdi-facebook", "mdi-twitter", "mdi-linkedin", "mdi-instagram"],
    };
  },
};
</script>

<style src="@/assets/style.css">

</style>>

