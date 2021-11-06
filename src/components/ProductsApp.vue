<template>

 <v-content>
  
   <v-container fill-height fluid class="my-15">
     <div ></div>
    <v-row class="row text-center pt-md-5 aos-init aos-animate ">
      <v-col lg="12" class="col-12 align-self-center py-md-5 ">
        <v-subheader class="text-h4 justify-center"> LES PLUS GRANDES MARQUES DE L’INDUSTRIE SOUS UN MÊME TOIT</v-subheader>
      </v-col>
    </v-row>   

    <!--  ************* Debut Bloc Menu  de Domaines*******************   -->

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

       <!--  ************* Fin Bloc Menu *******************   -->


       <v-row justify="center">

      <!--  ******** Slot domaine MT *********  -->

      <slot v-if="activeDomaine === 'domaine_MT'">
        <v-col
          lg="4"
          v-for="(mt, index_mt) in MT"
          :key="index_mt"
        >
          <v-card class="mx-auto my-12" max-width="374" style="height: 500px">

            <v-img
              height="250"
              :src="mt.images"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
            >
            </v-img>

            <v-card-title>{{ mt.title }}</v-card-title>

            <v-card-text>
              
                <span 
                  class="d-inline-block text-truncate"
                  style="max-width: 300px;"
                >
                   {{ mt.description }}
                </span>
              
             </v-card-text>

            <v-divider></v-divider>
            <v-card-actions class="my-2">
              <v-btn 
                color="success" 
                rounded 
                @click="$refs.pageDetailProduit.showDetails(mt.title, mt.description) "
              >plus
              </v-btn>
                           
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

  
         <!--  ******** Slot domaine MEP *********  -->

      <slot v-if="activeDomaine === 'domaine_MEP'">
        <v-col
          lg="4"
          v-for="(mep, index_mep) in MEP"
          :key="index_mep"
        >
     <v-card class="mx-auto my-12" max-width="374" style="height: 500px">

            <v-img
              height="250"
              :src="mep.images"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
            >
            </v-img>

            <v-card-title>{{ mep.title }}</v-card-title>

            <v-card-text><p
            class="d-inline-block text-truncate"
            style="max-width: 300px"
             >{{ mep.description }}
             </p></v-card-text>

            <v-divider></v-divider>
            <v-card-actions class="my-2">
              <v-btn 
                color="success" 
                rounded 
                @click="$refs.pageDetailProduit.showDetails(mep.title, mep.description) "
              >plus
              </v-btn>
                           
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


   
         <!--  ******** Slot domaine  CPS *********  -->

      <slot v-if="activeDomaine === 'domaine_CPS'">
        <v-col
          lg="4"
          v-for="(cps, index_cps) in CPS"
          :key="index_cps"
        >
  <v-card class="mx-auto my-12" max-width="374" style="height: 500px">

            <v-img
              height="250"
              :src="cps.images"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
            >
            </v-img>

            <v-card-title>{{ cps.title }}</v-card-title>

            <v-card-text><p 
            class="d-inline-block text-turncate"
            style="max-width: 300px"
            >{{ cps.description }}
            </p></v-card-text>

            <v-divider></v-divider>
            <v-card-actions class="my-2">
              <v-btn 
                color="success" 
                rounded 
                @click="$refs.pageDetailProduit.showDetails(cps.title, cps.description) "
              >plus
              </v-btn>
                           
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


   
     <!--  ******** Slot domaine  MDS *********  -->

 <slot v-if="activeDomaine === 'domaine_MDS'">
        <v-col
          lg="4"
          v-for="(mds, index_mds) in MDS"
          :key="index_mds"
        >
 <v-card class="mx-auto my-12" max-width="374" style="height: 500px">

            <v-img
              height="250"
              :src="mds.images"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
            >
            </v-img>

            <v-card-title>{{ mds.title }}</v-card-title>

            <v-card-text><p 
            class="d-inline-block text-truncate"
            style="max-width: 300px"
            >{{ mds.description }}
            </p></v-card-text>

            <v-divider></v-divider>
            <v-card-actions class="my-2">
              <v-btn 
                color="success" 
                rounded 
                @click="$refs.pageDetailProduit.showDetails(mds.title, mds.description) "
              >plus
              </v-btn>
                           
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

  

           <!--  ******** Slot domaine  MSDEF *********  -->

      <slot v-if="activeDomaine === 'domaine_MSDEF'">
        <v-col
          lg="4"
          v-for="(msdef, index_msdef) in MSDEF"
          :key="index_msdef"
        >
          <v-card class="mx-auto my-12" max-width="374" style="height: 500px">

            <v-img
              height="250"
              :src="msdef.images"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
            >
            </v-img>

            <v-card-title>{{ msdef.title }}</v-card-title>

            <v-card-text><p 
            class="d-inline-block text-truncate"
            style="max-width: 300px;"
            >{{ msdef.description }}
            </p></v-card-text>

            <v-divider></v-divider>
            <v-card-actions class="my-2">
              <v-btn 
                color="success" 
                rounded 
                @click="$refs.pageDetailProduit.showDetails(msdef.title, msdef.description) "
              >plus
              </v-btn>
                           
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

<!--referencé notre fenetre Modal( "page detail produits" ) -->
    <modal ref="pageDetailProduit" >
   </modal>
<!-- *---------------------------------------------------* -->
   </v-container>
 </v-content>
</template>

<script>
import Modal from '@/components/Modal.vue';

export default {

  name: "ProductsApp",

  components: {

    Modal

  },

  methods : {
 
  },
 
  data() {
       
    return {
     
    // afficher le contenu de chaque produits selon le domaine

     //* ---MT Matériel technique ---- */

     activeDomaine: "domaine_MT",

     MT: [
        {
          title: "Tapis & Nettoyeur vapeur ameublement",
          description:
            "VAPEUR TAPIS & Meubles rembourrés ISV 2800 S: Notre modèle de ISV 2800 S nettoyage de tapis à vapeur produit jusqu'à 150-170 degrés de la vapeur grâce à son générateur de vapeur. La vapeur d'eau aide à dissoudre les salissures dans une courte période de temps et ne laisse aucune humidité sur les surfaces. L'humidité créée par la vapeur disparait aussi rapidement. Avec […]",
          images: require("@/assets/images/img_produits/img_MT/1.png"),
        },
        {
          title: "RL 1400 Une centrifugeuse pieds Tapis essorage",
          description:
            "Centrifugeuses de tapis et de tapis essoreuse viennent dans différentes longueurs de batterie interne entre 2,7 m (8,85 ft) et 4,2 m ( 13,8 ft) en standard et même jusqu'à 5 mètres (16,4 ft) versions peuvent être effectués sur demande du client. Avec prise de raccordement sur le couvercle des centrifugeuses tapis / tapis essorage rincer les tapis et les moquettes efficacement",
          images: require("@/assets/images/img_produits/img_MT/2.png"),
        },
        {
          title: "RL 1200 Couverture & Mat tordant Centrifugeuse",
          description:
            "RL 1400 TAPIS centrifugeuse est notre modèle le plus abordable adapté pour le rinçage et le séchage petits tapis et moquettes. Grande petite centrifugeuse surtout demandée par les magasins d'automobiles détaillant pour sécher les tapis de voiture et de nettoyage de tapis dans les versions de plus grande taille. Disponible en différentes tailles jusqu'à 2,7 mètres de longueur.  ",
          images: require("@/assets/images/img_produits/img_MT/3.png"),
        },
                {
          title: "RL 1400 T roues Tapis essorage Centrifugeuse",
          description:
            "Pour Easy Move intérieur des plantes de nettoyage de tapis / tapis roues séchoirs à centrifuger tapis d'essorage sont les bonnes machines surtout quand la zone de l'usine est petite. Centrifugeuses de tapis et de tapis essoreuse viennent dans différentes longueurs de batterie interne entre 2,7 m (8,85 ft) et 4,2 m ( 13,8 ft) en standard et même jusqu'à 5 mètres (16,4 ...",
          images: require("@/assets/images/img_produits/img_MT/4.png"),
        },
             
        {
          title: "Manuel Monobrosse Tapis Machine à laver",
          description:"MANUEL MACHINE À LAVER CARPET Cleanvac manuel Machines à laver tapis sont utilisés à des fins de nettoyage et de polissage des sols (marbre,pvc,mosaïques etc) également le brossage, lavage et nettoyage de tapis. Fournit un modèle de fonctionnement facile et silencieux avec entraînement par courroie et boîte de vitesses Ce sont récurage professionnels. […]",
          images: require("@/assets/images/img_produits/img_MT/5.jpg"),
        },
        {
          title : "Floor Cleaning Machines",
          description:"Europower offers the broadest portfolio of high-quality, Deep-Cycle Flooded, Gel and AGM batteries for floor machine applications. Durability, reliability and performance mean less unplanned downtime and increased return on your battery investment!",
          images: require("@/assets/images/img_produits/img_MT/6.jpg"),
        },
           {
          title : "Balayeuse de voirie Diesel",
          description:"- Piste de nettoyage min : 1500 mm  - Piste de nettoyage max : 1850 mm - Capacité du conteneur : 0.8 m3  Rendement horaire : 22000 m2/h Alimentation Diesel",
          images: require("@/assets/images/img_produits/img_MT/7.jpg"),
        },
           {
          title : "Balayeuse électrique 5 brosses",
          description:"Cette balayeuse est l'équipement idéal pour le nettoyage des avenues, rues, places piétonnes et parcs de stationnement.Elle est dotée de 4 brosses latérales et d'une brosse principale s'adaptant à tous types de revêtements (enrobés, pavés, dalles, béton désactivé, résine, etc.). Avec une batterie d'une autonomie de 13 h",
          images: require("@/assets/images/img_produits/img_MT/8.jpg"),
        },
           {
          title : "Machine de nettoyage vapeur",
          description:"Machine de nettoyage électrique dédiée au lavage et entretien intérieur et extérieur automobile. L'association vapeur et produits de nettoyage usuels (dégraissant,cire ou shampooing) permet le nettoyage complet du véhicule. Le nettoyeur vapeur SP35 A, modèle le plus puissant de la gamme 220V, est équipé d'un aspirateur 1200 Watts et d'une larg",
          images: require("@/assets/images/img_produits/img_MT/9.jpg"),
        },
        {
          title: "Tapis déshumidificateur",
          description:"Cleanvac DRY60 déshumidificateurs tapis fait tapis & tapis séchage plus rapide. Après le lavage et l'essorage tapis en tapis centrifugeuses essoreuse, tapis et carpettes sortent sur 5% humide, et exige la pendaison et les garder environ 24-48 heures en fonction des conditions météorologiques pour les obtenir 100% sec. Cependant, à l'aide de tapis déshumidificateurs raccourcissent cette […]",
          images: require("@/assets/images/img_produits/img_MT/10.jpg"),
        },
           {
          title : "Modèle Combi Tapis Machine à laver et séchage",
          description:"Cleanvac Modèle combiné lavage automatique Tapis & Séchage en machine est très compacte conçue pour les petites et étroites installations de lavage de tapis. rondelles de tapis qui est dans la lessive et des affaires de nettoyage à sec n'ont pas grand espace pour l'installation des machines séparement. Notre machine à laver et le séchage automatique tapis fournit les sauver de […]",
          images: require("@/assets/images/img_produits/img_MT/11.jpg"),
        },
           {
          title : "Tapis & Tapis Machine de nettoyage Starter Pack",
          description:"Nous avons tapis complets et des solutions de nettoyage de tapis pour toutes les tailles de nettoyage. De base à la plus grande capacité et des offres entièrement automatiques, Nous fabriquons des machines pour toutes les entreprises de nettoyage de taille à votre budget.",
          images: require("@/assets/images/img_produits/img_MT/12.jpg"),
        },
           {
          title : "",
          description:"",
          images: require("@/assets/images/img_produits/img_MT/13.jpg"),
        },
        
      ],
        //**-----MEP -Matériel d’énergie pneumatique */
      MEP: [
        {
           title: "MOTOBOMBAS DIESEL",
          description:
            "Acelerador manual.Electroválvula de corte.Con cargador de baterías.Sensor presión de aceite (señal).Cuadro de arranque y paro con llave contacto.Incluye piloto señalizador de presión y temperatura de aceite.",
          images: require('@/assets/images/img_produits/img_MEP/1.jpg'),
         
        },
        {
         title: "Groupe electrogene insonoriser | Alfa Generators",
          description:
            "Tout d’abord, nous pouvons voir que c’est un générateur / générateur de la société Alfa Generators.Par conséquent, ceci est une image représentative de nos produits. Cette photo de générateur est représentative de 800 kva de puissance à 1250 kva. Les moteurs pourraient être Volvo ou Perkins. Ce générateur, également appelé une centrale électrique, pourrait être classé comme silencieux, insonorisé ou de musculation",
          images: require("@/assets/images/img_produits/img_MEP/2.jpg"),
        },
        {
          title: "MOTEURS ÉLECTRIQUES DE TYPE EXPLOITATION",
          description:
            "Les moteurs Exproof de la famille des D6 qui dote d’entre d’une structure 71-132, elles accompagnent des plusieurs innovations hors concours! Elles ont les certificats selon les standards EN 60079 et EN61241 qui a réactualisé a la place des standards comme EN50014, EN50018, EN 50019, EN50021, EN50081 et EN50281 qui est en vigueur.",
          images: require("@/assets/images/img_produits/img_MEP/3.jpg"),
        },
        {
          title: "MOTEURS INDUSTRIELS ELECTRIQUES",
          description:
            "Le Group Marelli Motori est le leader dans la production des moteurs électriques moyenne courante et sous-tension, par sa compétence  depuis du siécle, Le group Marelli Motori compte parmi les groupes grands du monde avec ses employés 14.000 dans l’espace sur la production d’énergie, de la distribution et du déplacement.",
          images: require("@/assets/images/img_produits/img_MEP/4.jpg"),
        },
        {
          title: "MOTEURS INDUSTRIELS ELECTRIQUES",
          description:
            "Les moteurs Exproof de la famille des D6 qui dote d’entre d’une structure 71-132, elles accompagnent des plusieurs innovations hors concours! Elles ont les certificats selon les standards EN 60079 et EN61241 qui a réactualisé a la place des standards comme EN50014, EN50018, EN 50019, EN50021, EN50081 et EN50281 qui est en vigueur.",
          images: require("@/assets/images/img_produits/img_MEP/5.jpg"),
        },
        {
          title: "Moteur électrique triphasé IE1 B3 1,5KW 230/400V, 3000 Tr/min",
          description:
            "Moteur électrique triphasé 1,5kW / 2CV alimenté exclusivement en 230/400V avec une vitesse de rotation de 3000 tr/min.Ce moteur électrique a une hauteur d’axe de 80 mm et un diamètre d'arbre de 19 mm Il se fixe par deux pieds : montage B3 (pattes de fixation amovibles et démontables). La classe d’isolation F des moteurs triphasés CEMER leur permettent de supporter une température maximale du bobinage de 155°C et une température ambiante de 40°C",
          images: require("@/assets/images/img_produits/img_MEP/6.jpg"),
        },
        {
         title: "GENERADOR LOMBARDINI INDUSTRIAL DE 8 KVA / 8 KW | LDW1404L",
          description:
            "El Grupo electrógeno LOMBARDINI de 8 kVA / 8 kW, de la gama industrial se caracteriza por su versatilidad, alto rendimiento y fácil mantenimiento. Su uso habitual es suministrar electricidad como fuente principal a lugares aislados sin red eléctrica o con cortes frecuentes. Se usan principalmente en: -Industria -Construcciones -Hoteles",
          images: require("@/assets/images/img_produits/img_MEP/7.jpg"),
        },
        {
          title:"SSP-H Extra Heavy Duty Slurry Pumps",
          description :
          "La qualité et la fiabilité de ce moteur lui permettent de s’adapter à tous les environnements industriels et agricoles. Exemples d’applications : pompes, machines-outils, convoyeurs, ventilateurs, compresseurs… Moteur IP55 de classe S1 pour utilisation continue. Grâce à ces deux condensateurs ce moteur offre un couple de démarrage important.",
          images: require("@/assets/images/img_produits/img_MEP/8.jpg"),
        },
        {
          title: "TH GRV-VD / VB Boosters",
          description:
          "High pressure, quiet running, compact and low power consumption. GRV-VD / VB pumps are suitable for pumping non-abrasive, clean or slightly contaminated, low viscosity without solid & ﬁbrous particles liquids. Vertical structure saves space.",
          images: require("@/assets/images/img_produits/img_MEP/9.png"),
        },
        {
          title:"TH CDLF-Stainless Boosters",
          description :"High pressure, quiet running, compact and low power consumption. All surfaces that contact with the liquid are stainless steel, ln-line (straight pipe attachable) type pumps. CDLF pumps are suitable for pumping non-abrasive, clean or slightly contaminated, low-viscosity liquids without solid & ﬁbrous particles. Bearing is provided by tungsten carbide sliding bearings. Vertical structure saves space.",
          images: require("@/assets/images/img_produits/img_MEP/10.png")
        },
                {
          title: "Drainage Submersible Pumps",
          description: "Les pompes submersibles sont utilisées dans les trous de drainage, les excavations de construction, l'évacuation de quelques eaux sales, les fosses septiques, l'évacuation de particules fibreuses et non solides dans l'eau, les inondations d'eau, l'évacuation des eaux usées du bas niveau, le transfert de liquides hygiéniques, les industries alimentaires, système de traitement, piscines ornementales, aquariums de type industriel, fourniture d'eau propre, petits systèmes de surpression, transfert de certains liquides par mélange, évacuation d'eau de boue et plus encore.",
          images: require("@/assets/images/img_produits/img_MEP/11.png"),
        },
        {
          title: "Dirty Water Submersible Pumps",
          description: "Les pompes submersibles sont utilisées dans les trous de drainage, les excavations de construction, l'évacuation de quelques eaux sales, les fosses septiques, l'évacuation de particules fibreuses et non solides dans l'eau, les inondations d'eau, l'évacuation des eaux usées du bas niveau, le transfert de liquides hygiéniques, les industries alimentaires, système de traitement, piscines ornementales, aquariums de type industriel, fourniture d'eau propre, petits systèmes de surpression, transfert de certains liquides par mélange, évacuation d'eau de boue et plus encore.",
          images: require("@/assets/images/img_produits/img_MEP/12.png"),
        },
        {
          title: "Blade Septic Submersible Pumps",
          description: "Les pompes submersibles sont utilisées dans les trous de drainage, les excavations de construction, l'évacuation de quelques eaux sales, les fosses septiques, l'évacuation de particules fibreuses et non solides dans l'eau, les inondations d'eau, l'évacuation des eaux usées du bas niveau, le transfert de liquides hygiéniques, les industries alimentaires, système de traitement, piscines ornementales, aquariums de type industriel, fourniture d'eau propre, petits systèmes de surpression, transfert de certains liquides par mélange, évacuation d'eau de boue et plus encore.",
          images: require("@/assets/images/img_produits/img_MEP/13.png"),
        },
        {
          title: "",
          description: "",
          images: require("@/assets/images/img_produits/img_MEP/14.jpg"),

        },
        {
          title: "SCP ISO 2858 Norm Pumps",
          description: "Clean or normal contaminated low or medium viscosity liquids without solid & fibrous particles.",
          images: require("@/assets/images/img_produits/img_MEP/15.png"),

        },
        {
          title: "SSP-V Extra Heavy Duty Slurry Pumps",
          description: "Slurry, highly contaminated, viscous, corrosive and abrasive liquids with solid or fibrous particles. SSP-V pump series are carefully designed by taking into consideration years of production experience of STANDART POMPA and field experiences of our customers using process and slurry pumps. Hydraulic efficiency and hardwearing are considerate and optimised while hard solid particles were pumping.",
          images: require("@/assets/images/img_produits/img_MEP/16.jpg"),

        },
        {
         title: "NMT(D) MAX F Wet Rotor Cırculatıon Pumps",
         description: "In use for pumping clean water or clean water & anti-freeze mixture liquids in heating systems. Water should be according to current quality standarts (such as VDI 2035). Liquid should not be contained with abrasive or explosive mixtures, mineral oil, solid or ﬁbrous particles.",
         images: require("@/assets/images/img_produits/img_MEP/17.png"),      
        },
        {
          title:"C Submersible Sewage Pumps",
          description: "Domestic and industrial waste water, raw sewage, liquids with fibrous and solid substances.",
          images: require("@/assets/images/img_produits/img_MEP/18.jpg")
        },
      ],

       //**--------CPS Conditionnement de produits en sac--- */

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

 //**---- MDS -Matériel didactique et scientifique */

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

      //**----- MSDEF Matériel de sûreté et de défense- */
      
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
