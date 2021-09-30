<template>
    <v-app>   
        <v-main>
        <v-content >
            <v-container fill-height fluid class="my-15 ">
              <v-row>
                   <v-col >
                      
                      <carousel-3d  :height="600" :width="500" :border="1"  @load="slideHeight()">
                        <slide :index="0" >
                          <img src="@/assets/images/img-slide1.jpg" alt="">
                          <hr/>
                          <h5  class="txt-slide-titre" >Matériel d’énergie pneumatique (groupes électrogènes, onduleurs, pompes)</h5>
                          <hr/>
                          <p class="txt-slide-description"> - Entreprise innovante qui offre des services dans le domaine des solutions industrielles d’alimentation (onduleurs, régulateurs,
                            énergies renouvelables, batteries).</p>
                        </slide>
                        <slide :index="1">

                          <img src="@/assets/images/img-slide2.jpg" alt="">
                          <hr/>
                          <h4 class="txt-slide-titre"> Matériel technique</h4>
                          <hr/>
                          <p class="txt-slide-description">Cleanvac est spécialisée dans la production de machines à laver les tapis, de balais de type industriel, de nettoyeurs haute pression,
de nettoyeurs de sols durs</p>
                         
                        </slide>

                         <slide :index="2">
                           <img src="@/assets/images/img-slide3.jpg" alt="">
                          <hr/>
                          <h5 class="txt-slide-titre"> Conditionnement de produits en sac (Pesage, couture, soudure)</h5>
                          <hr/>
                          <p class="txt-slide-description">Société active dans le secteur de l’emballage et du
conditionnement,le domaines du pesage, de l’ensachage
et la couture</p>
                        </slide>

                        <slide :index="3">
                          <img src="@/assets/images/img-slide4.jpg" alt="">
                          <hr/>
                          <h5 class="txt-slide-titre">Matériel didactique et scientifique</h5>
                          <hr/>
                          <p class="txt-slide-description ">Fabriquant et concepteur des equipement didactiques dédiés à l’enseignemen supérieur et des outils
technologiques modernes pour une formation rapide, facile et efficace</p>
                        </slide>
                          <slide :index="4">
                          <img src="@/assets/images/img-slide5.jpg" alt="">
                          <hr/>
                          <h5 class="txt-slide-titre">Matériel de sûreté et de défense</h5>
                          <hr/>
                          <p class="txt-slide-description">Socièté spécialisée dans la fabrication, la conception,et le développment de produits suivants: Equipement
Anti-Riot, Engrenages militaires, Gilet pare-balles, Solution d’armures transparente, Décontamination, Détection
explosive,</p>
                        </slide>
                      </carousel-3d>

                    </v-col>
              </v-row>
                <v-row align-content="center" justify="center">
                     <v-col  lg="10">
                  <div class="container py-5">
                    <div class="row py-md-5 aos-init aos-animate" data-aos="fade-up">
                        <div class="col text-center">
                            <h3 class="txt-bleu text-uppercase">Livrer la performance attendue</h3>
                            <p>La mauvaise conception du système est souvent la première cause d’un problème lié au pneumatique. Nous nous faisons un point d’honneur de livrer des solutions dotées d’une ingéniosité solide et qui satisfont vos attentes de performance et permettent de maximiser votre retour sur investissement. </p>
                        </div>
                    </div>
                </div>
                    </v-col> 
                 
                </v-row>
                <v-row>
                  <v-col>
                    <div class="container py-5">
            <div class="row pt-md-5 aos-init aos-animate" data-aos="fade-up">
                <div class="col text-center mb-4">
                    <h4 class="txt-bleu text-uppercase">L’extension parfaite de votre R&amp;D pour :</h4>
                </div>
            </div>
            <div class="row mt-4 pb-md-5 aos-init aos-animate" data-aos="fade-up">
                <div class="col-md-4 separateur-v-bf">
                    <h3 class="txt-bleu font-weight-bold">CONCEVOIR</h3>
                    <p class="small">Nouveau système avec fonctions simples ou sophistiquées</p>
                </div>
                <div class="col-md-4 separateur-v-bf">
                    <h3 class="txt-bleu font-weight-bold">OPTIMISER</h3>
                    <p class="small">Contrôle précis de la vitesse du système pneumatique et productivité optimale</p>
                </div>
                <div class="col-md-4 m-0">
                    <h3 class="txt-bleu font-weight-bold">RÉPARER</h3>
                    <p class="small">Analyse des performances et amélioration de la durabilité</p>
                </div>
            </div>
        </div>
                  </v-col>
                </v-row>
                <v-row>
                  <div class="row-gris-fonce  bloc-gris">
        <div class="container py-5">
            <div class="row pt-md-5 aos-init aos-animate" data-aos="fade-up">

                <div class="col-12 col-sm-6 col-md-4 px-4 mb-5">
                    <img class="mb-3 mb-sm-5 img-fluid" src="@/assets/images/img-pneumatique1.jpg">
                    <h4 class="txt-bleu-ciel separateur-left">INGÉNIERIE PERFORMANTE</h4>
                    <p class="txt-blanc">La qualité et la rigueur dans la conception de nos systèmes vous assurent une combinaison parfaite sollicitant les capacités maximales de chaque composante </p>
                </div>
                <div class="col-12 col-sm-6 col-md-4 px-4 mb-5">
                    <img class="mb-3 mb-sm-5 img-fluid" src="@/assets/images/img-pneumatique2.jpg">
                    <h4 class="txt-bleu-ciel separateur-left">ASSEMBLAGE FIABLE ET PRÉCIS</h4>
                    <p class="txt-blanc">Bien assemblé. Parfaitement calibré. Nos systèmes pneumatiques sont fabriqués avec un souci du détail qui vous procure des gains d’efficacité.</p>

                </div>
                <div class="col-12 col-sm-6 col-md-4 px-4 mb-5">
                    <img class="mb-3 mb-sm-5 img-fluid" src="@/assets/images/img-pneumatique3.jpg">
                    <h4 class="txt-bleu-ciel separateur-left">INSTALLATION IRRÉPROCHABLE</h4>
                    <p class="txt-blanc">La mise en route de vos systèmes pneumatiques est profitable. Nos experts sont sur place et collaborent avec vous jusqu’à la toute fin, et même après.</p>

                </div>
                <div class="col-12 col-sm-6 col-md-4 px-4 mb-5">
                    <img class="mb-3 mb-sm-5 img-fluid" src="@/assets/images/img-pneumatique4.jpg">
                    <h4 class="txt-bleu-ciel separateur-left">SERVICE TECHNIQUE EFFICACE</h4>
                    <p class="txt-blanc">Rapidité. Fiabilité. Disponibilité. Notre service de haut calibre offre tout ce que vous êtes en droit de vous attendre d’un service efficace.</p>

                </div>
                <div class="col-12 col-sm-6 col-md-4 mr-auto-sm px-4 mb-5">
                    <img class="mb-3 mb-sm-5 img-fluid" src="@/assets/images/img-pneumatique5.jpg">
                    <h4 class="txt-bleu-ciel separateur-left">PIÈCES LIVRÉES RAPIDEMENT</h4>
                    <p class="txt-blanc">Le plus grand inventaire de pièces pneumatiques dans l’est du Canada, prêtes à être livrées rapidement.</p>

                </div>

            </div>
        </div>
    </div>
     <p/> <p/> <p/>
                </v-row>
               
            </v-container>
             
        </v-content>
       
        </v-main>
    </v-app>
</template>

<script>
import { Carousel3d, Slide } from 'vue-carousel-3d';

export default{
     name: "HeroComponent",
     Carousel3d,
     Slide ,

     data () {
       
      return {
       
       
      }
    },
computed:{
  slideHeight () {
    const sw = parseInt(this.width, 10) + (parseInt(this.border, 10) * 2)
    const sh = parseInt(parseInt(this.height) + (this.border * 2), 10)
    const ar = this.calculateAspectRatio(sw, sh)
    return this.slideWidth / ar
}


},

}
</script>

<style src="@/assets/style.css">

</style>
