<template>
 <v-content>
   <v-container fill-height fluid class="my-15">
     <div ></div>
    <v-row class="row text-center pt-md-5 aos-init aos-animate ">
      <v-col lg="12" class="col-12 align-self-center py-md-5 ">
        <v-subheader class="text-h4 justify-center">PRODUITS DISTRIBUÉS</v-subheader>
        <p>
              LES PLUS GRANDES MARQUES DE L’INDUSTRIE SOUS UN MÊME TOIT
        </p>
      </v-col>
    </v-row>
     <v-row>
       <div class="container py-5">
            <div class="row pt-md-5 aos-init aos-animate" data-aos="fade-up">

                <div class="col-12 col-sm-6 col-md-4 px-4 mb-5">
                    <img class="mb-3 mb-sm-5 img-fluid" src="@/assets/logo/fournisseurs/idea.png">                  
                </div>
                 <div class="col-12 col-sm-6 col-md-4 px-4 mb-5">
                    <img class="mb-3 mb-sm-5 img-fluid" src="@/assets/logo/fournisseurs/Edibon.jpg">                  
                </div>
                 <div class="col-12 col-sm-6 col-md-4 px-4 mb-5">
                    <img class="mb-3 mb-sm-5 img-fluid" src="@/assets/logo/fournisseurs/Lega.png">                  
                </div>
                 <div class="col-12 col-sm-6 col-md-4 px-4 mb-5">
                    <img class="mb-3 mb-sm-5 img-fluid" src="@/assets/logo/fournisseurs/semic.png">                  
                </div>
                 <div class="col-12 col-sm-6 col-md-4 px-4 mb-5">
                    <img class="mb-3 mb-sm-5 img-fluid" src="@/assets/logo/fournisseurs/alfa.png">                  
                </div>
                 <div class="col-12 col-sm-6 col-md-4 px-4 mb-5">
                    <img class="mb-3 mb-sm-5 img-fluid" src="@/assets/logo/fournisseurs/sumakpump.png">                  
                </div>
                 <div class="col-12 col-sm-6 col-md-4 px-4 mb-5">
                    <img class="mb-3 mb-sm-5 img-fluid" src="@/assets/logo/fournisseurs/standart.png">                  
                </div>
                 <div class="col-12 col-sm-6 col-md-4 px-4 mb-5">
                    <img class="mb-3 mb-sm-5 img-fluid" src="@/assets/logo/fournisseurs/lotus.png">                  
                </div>
                <div class="col-12 col-sm-6 col-md-4 px-4 mb-5">
                    <img class="mb-3 mb-sm-5 img-fluid" src="@/assets/logo/fournisseurs/alpha.png">                  
                </div>

            </div>
        </div>
     </v-row>
  
     
      <v-row class="row text-center pt-md-5 aos-init aos-animate" >
         
        <div class="justify-center">
          <v-chip
            @click="activeDomaine = 'domaine_MT'"
            :color="activeDomaine === 'domaine_MT' ? 'success' : ''"
            class="mx-5"
            >Matériel technique</v-chip
          >
          <v-chip
            @click="activeDomaine = 'domaine_MEP'"
            :color="activeDomaine === 'domaine_MEP' ? 'success' : ''"
            class="mx-5"
            >Matériel d’énergie pneumatique</v-chip
          >
          <v-chip
            @click="activeDomaine = 'domaine_CPS'"
            :color="activeDomaine === 'domaine_CPS' ? 'success' : ''"
            class="mx-5"
            >Conditionnement de produits en sac</v-chip
          >
               <v-chip
            @click="activeDomaine = 'domaine_MDS'"
            :color="activeDomaine === 'domaine_MDS' ? 'success' : ''"
            class="mx-5"
            >Matériel didactique et scientifique</v-chip
          >
          </div>
          </v-row>
          <v-row  class="justify-content-center">
            <div>
      
            <v-chip
            @click="activeDomaine = 'domaine_MSDEF'"
            :color="activeDomaine === 'domaine_MSDEF' ? 'success' : ''"
            class="mx-5"
            >Matériel de sûreté et de défense</v-chip
          >

        </div>
      
       </v-row>
       <v-row justify="center">
      <!-- slot d MT-->
      <slot v-if="activeDomaine === 'domaine_MT'">
        <v-col
          lg="4"
          v-for="(mt, index_mt) in MT"
          :key="index_mt"
        >
          <v-card class="mx-auto my-12" max-width="374">
            <v-img
              height="250"
              :src="mt.images"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
            >
            </v-img>

            <v-card-title>{{ mt.title }}</v-card-title>

            <v-card-text>
              <div>{{ mt.description }}</div>
            </v-card-text>

            <v-divider class="mx-4"></v-divider>
            <v-card-actions>
              <v-btn color="success" rounded>details</v-btn>
              <v-spacer />
              <v-rating
                :value="4.5"
                color="amber"
                dense
                half-increments
                readonly
                size="14"
              >
              </v-rating>
            </v-card-actions>
          </v-card>
        </v-col>
      </slot>

      <!-- slote MEP-->

      <slot v-if="activeDomaine === 'domaine_MEP'">
        <v-col
          lg="4"
          v-for="(mep, index_mep) in MEP"
          :key="index_mep"
        >
          <v-card class="mx-auto my-12" max-width="374">
            <v-img
              height="250"
              :src="mep.images"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
            >
            </v-img>

            <v-card-title>{{ mep.title }}</v-card-title>

            <v-card-text>
              <div>{{ mep.description }}</div>
            </v-card-text>

            <v-divider class="mx-4"></v-divider>
            <v-card-actions>
              <v-btn color="success" rounded>details</v-btn>
              <v-spacer />
              <v-rating
                :value="4.5"
                color="amber"
                dense
                half-increments
                readonly
                size="14"
              >
              </v-rating>
            </v-card-actions>
          </v-card>
        </v-col>
      </slot>


      <!-- slot d image CPS-->
      <slot v-if="activeDomaine === 'domaine_CPS'">
        <v-col
          lg="4"
          v-for="(cps, index_cps) in CPS"
          :key="index_cps"
        >
          <v-card class="mx-auto my-12" max-width="374">
            <v-img
              height="250"
              :src="cps.images"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
            >
            </v-img>

            <v-card-title>{{ cps.title }}</v-card-title>

            <v-card-text>
              <div>{{ cps.description }}</div>
            </v-card-text>

            <v-divider class="mx-4"></v-divider>
            <v-card-actions>
              <v-btn color="success" rounded>details</v-btn>
              <v-spacer />
              <v-rating
                :value="4.5"
                color="amber"
                dense
                half-increments
                readonly
                size="14"
              >
              </v-rating>
            </v-card-actions>
          </v-card>
        </v-col>
      </slot>

 <!-- slot d image -->
 <slot v-if="activeDomaine === 'domaine_MDS'">
        <v-col
          lg="4"
          v-for="(mds, index_mds) in MDS"
          :key="index_mds"
        >
          <v-card class="mx-auto my-12" max-width="374">
            <v-img
              height="250"
              :src="mds.images"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
            >
            </v-img>

            <v-card-title>{{ mds.title }}</v-card-title>

            <v-card-text>
              <div>{{ mds.description }}</div>
            </v-card-text>

            <v-divider class="mx-4"></v-divider>
            <v-card-actions>
              <v-btn color="success" rounded>details</v-btn>
              <v-spacer />
              <v-rating
                :value="4.5"
                color="amber"
                dense
                half-increments
                readonly
                size="14"
              >
              </v-rating>
            </v-card-actions>
          </v-card>
        </v-col>
      </slot>

      <!-- slot d MT-->
      <slot v-if="activeDomaine === 'domaine_MSDEF'">
        <v-col
          lg="4"
          v-for="(msdef, index_msdef) in MSDEF"
          :key="index_msdef"
        >
          <v-card class="mx-auto my-12" max-width="374">
            <v-img
              height="250"
              :src="msdef.images"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
            >
            </v-img>

            <v-card-title>{{ msdef.title }}</v-card-title>

            <v-card-text>
              <div>{{ msdef.description }}</div>
            </v-card-text>

            <v-divider class="mx-4"></v-divider>
            <v-card-actions>
              <v-btn color="success" rounded>details</v-btn>
              <v-spacer />
              <v-rating
                :value="4.5"
                color="amber"
                dense
                half-increments
                readonly
                size="14"
              >
              </v-rating>
            </v-card-actions>
          </v-card>
        </v-col>
      </slot>

    </v-row>
  </v-container>
 </v-content>
</template>

<script>
export default {
  name: "Products",

  data() {
    return {
     activeDomaine: "domaine_MT",
    


      MT: [
        {
          title: "Nettoyeur haute pression PW-C45",
          description:
            "Pression 110-190 bar Débit 500-900 l/h Puissance 2,9-4,9 kW",
          images: require("@/assets/images/img_produits/img_MT/1.jpg"),
        },
        {
          title: "Aspirateur GP 2/62",
          description:
            "Puissance : 2600 w Dépression : 2380 Débit d’air : 400 m3/h Capacité du réservoir : 62 l",
          images: require("@/assets/images/img_produits/img_MT/2.jpg"),
        },
        {
          title: "Balayeuse de voirie",
          description:
            "Cette mini Balayeuse de voirie reconditionnée permet d’améliorer la propreté et à moindre coût ",
          images: require("@/assets/images/img_produits/img_MT/3.jpg"),
        },
        {
          title: "Mini Balayeuse de voirie",
          description:
            "Cette mini Balayeuse de voirie reconditionnée permet d’améliorer la propreté et à moindre coût ",
          images: require("@/assets/images/img_produits/img_MT/4.jpg"),
        },
        {
          title: "Machine Nettoyage vapeur",
          description:"Lavage automobile intérieur / extérieur - Nettoyeur vapeur pour automobile ",
          images: require("@/assets/images/img_produits/img_MT/5.jpg"),
        },
        
        {
          title: "Nettoyage des sols",
          description:"type des machines autonomes de nettoyage des sols ",
          images: require("@/assets/images/img_produits/img_MT/6.jpg"),
        },
        
      ],

      MEP: [
        {
           title: "INGÉNIERIE PERFORMANTE",
          description:
            "La qualité et la rigueur dans la conception de nos systèmes vous assurent une combinaison parfaite sollicitant les capacités maximales de chaque composante",
          images: require('@/assets/images/img_produits/img_MEP/1.jpg'),
         
        },
        {
         title: "ASSEMBLAGE FIABLE ET PRÉCIS",
          description:
            "Bien assemblé. Parfaitement calibré. Nos systèmes pneumatiques sont fabriqués avec un souci du détail qui vous procure des gains d’efficacité.",
          images: require("@/assets/images/img_produits/img_MEP/2.png"),
        },
        {
          title: "INSTALLATION IRRÉPROCHABLE",
          description:
            "La mise en route de vos systèmes pneumatiques est profitable. Nos experts sont sur place et collaborent avec vous jusqu’à la toute fin, et même après.",
          images: require("@/assets/images/img_produits/img_MEP/3.jpg"),
        },
        {
          title: "SERVICE TECHNIQUE EFFICACE",
          description:
            "Rapidité. Fiabilité. Disponibilité. Notre service de haut calibre offre tout ce que vous êtes en droit de vous attendre d’un service efficace.",
          images: require("@/assets/images/img_produits/img_MEP/4.png"),
        },
        {
          title: "PIÈCES LIVRÉES RAPIDEMENT",
          description:
            "Le plus grand inventaire de pièces pneumatiques dans l’est du Canada, prêtes à être livrées rapidement.",
          images: require("@/assets/images/img_produits/img_MEP/5.jpg"),
        },
        {
          title: "Matériel d’énergie pneumatique",
          description:
            "Small plates, salads & sandwiches - an intimate setting with 12 indoor seats plus patio seating",
          images: require("@/assets/images/img_produits/img_MEP/6.jpg"),
        },
        {
         title: "Matériel d’énergie pneumatique",
          description:
            "Small plates, salads & sandwiches - an intimate setting with 12 indoor seats plus patio seating",
          images: require("@/assets/images/img_produits/img_MEP/7.png"),
        },
      ],



      CPS: [
        {
          title: "Soudure",
          description:
            "Société active dans le secteur de l’emballage et du conditionnement,le domaines du pesage, de l’ensachage et la couture",
          images: require("@/assets/images/img_produits/img_CPS/1.jpg"),
        },
        {
          title: "Pesage, couture, soudure",
          description:
            "Societe professionnelle dans la fabrication des pièces de rechange pour les marques de machines à coudre.",
          images: require("@/assets/images/img_produits/img_CPS/2.jpg"),
        },
        {
          title: "Machine de pesage automatique",
          description:
            "Machine de pesage automatique, à peser automatique",
          images: require("@/assets/images/img_produits/img_CPS/3.jpg"),
        },
      ],

MDS: [
        {
          title: "Microscope scientifique",
          description:
            "Microscope pour enfants 1200 fois mis expérience scientifique matériel didactique jouets scientifiques Microscope d'enseignement de biologie pour enfants",
          images: require("@/assets/images/img_produits/img_MDS/1.jpg"),
        },
        {
          title: "Gyroscope U52006 3B Scientific",
          description:
            "- Gyroscope de qualité premium qui repose sur le principe de précession - Appareil proposant différentes expériences possibles (moments d'inertie, de rotations etc.)",
          images: require("@/assets/images/img_produits/img_MDS/2.jpg"),
        },
        {
          title: "Pirani-Vakuummeter U145051-230 3B",
          description:
            "Vakuumanschluss DN 16 KF Messbereich: 120 hPa bis 0,001 hPa Messunsicherheit: < 20% vom Anzeigewert Anzeige: digitale LED-Anzeige in hPa/Torr Ziffernhöhe: 10 mm Auslesung: 5 pro sec Schreiberausgang: 0 bis 10 V Schwellwertschalter: 2 x 230 V, 2 A, unabhängig einstellbar Schaltgenauigkeit/Hysterese: ± 1 Digit Zulässige Überlast: 2 bar absolut Leistungsaufnahme: max. 15 W Abmessungen: ca. 98x98x152 mm³ Masse: ca. 1,2 kg",
          images: require("@/assets/images/img_produits/img_MDS/3.jpg"),
        },
      ],
MSDEF: [
        {
          title: "Instruments Tactiques De Sécurité",
          description:
            "Instruments Tactiques De Sécurité,Équipement Swat,Agent De Sécurité , Find Complete Details about Instruments Tactiques De Sécurité,Équipement ..",
          images: require("@/assets/images/img_produits/img_MSDEF/1.jpg"),
        },
        {
          title: "Protège-genou unisexe",
          description:
            "Protège-genou unisexe, accessoires pour policier et infirmières, protection des genoux",
          images: require("@/assets/images/img_produits/img_MSDEF/2.png"),
        },
        {
          title: "AliExpress Zestawy potężny Zoomable XML ",
          description:
            "AliExpress Zestawy potężny Zoomable XML Q5 Led latarka teleskopowa samoobrona Stick Tactical Baton latarka na",
          images: require("@/assets/images/img_produits/img_MSDEF/3.jpg"),
        },
      ],




    };
  },
};
</script>

<style src="@/assets/css/style.css">

</style>
