<template>
<v-app>
  <v-row class="row text-center pt-md-5 aos-init aos-animate ">
      <v-col lg="12" class="col-12 align-self-center py-md-5 ">
        <v-subheader class="text-h4 justify-center">NOS FOURNISSEURS</v-subheader>
        <p>
          NOS PRODUITS SONT DISTRIBUÉS PAR LES PLUS GRANDES MARQUES DE L’INDUSTRIE
        </p>
      </v-col>
    </v-row >
                <!--- --- --- --- Animation --- --- --- --->  
                
             <div class="container py-5" >
                              
                    <div id="app" v-if ="logo === 'logo_Fournisseurs'">                     
                        
                        <sequential-entrance >
                       
                          <v-img class="box"
                                src="@/assets/logo/fournisseurs/alfa.png"
                            >
                          </v-img>    
                             <v-img class="box"
                                src="@/assets/logo/fournisseurs/alpha.png"
                            >
                          </v-img>                     
                              <v-img class="box"
                                src="@/assets/logo/fournisseurs/Edibon.jpg"
                            >
                          </v-img> 
                            <v-img class="box"
                                src="@/assets/logo/fournisseurs/idea.png"
                            >
                          </v-img> 
                          <v-img class="box"
                                src="@/assets/logo/fournisseurs/semic.png"
                          >
                          </v-img>
                          <v-img class="box"
                                src="@/assets/logo/fournisseurs/standart.png"
                          >
                          </v-img>
                          <v-img class="box"
                                src="@/assets/logo/fournisseurs/sumakpump.png"
                          >
                          </v-img>
                           <v-img class="box"
                            src="@/assets/logo/fournisseurs/cleananvac.png"
                          >
                          </v-img>
                          <v-img class="box"
                            src="@/assets/logo/fournisseurs/Lega.png"
                          >
                          </v-img>
                        </sequential-entrance>
                    </div>
              
              </div>  
             <!--- --- --- --- ------- --- --- --- ---> 
    
  <v-footer padless fluid >
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
          <strong>Designed and Developed by Ait Oufkir</strong>
        </v-subheader>
      </div>
    </v-col>
  </v-footer>
  
  </v-app>
</template>

<script>
export default {
  name: "Footer",

  data() {
    return {
      icons: ["mdi-facebook", "mdi-twitter", "mdi-linkedin", "mdi-instagram"],

        logo : "logo_Fournisseurs",
        logo_Fournisseurs : [
            { 
                images: require("@/assets/logo/fournisseurs/alfa.png") ,
                
            }
        ],

    };
  },

        

};
</script>

<style src="@/assets/css/style.css">

</style>>

