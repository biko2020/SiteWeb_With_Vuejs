<template>
<v-app>
            
        <v-main>
<v-content>
    <v-container fill-height fluid class="my-15">
        <!--- debut Table --->
<table class="table table-striped">
  
    <thead>
        <tr>
            <th scope="col">Categorie Id</th>
            <th scope="col">Categorie Name</th>
            <th scope="col">options</th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="(catego, index) in categories" :key="index">
            <td>{{catego.CategorieId}}</td>
            <td>{{catego.CategorieName}}</td>
            <td>
                <button>ok</button>
            </td>
            
        </tr>
    </tbody>
</table>

  <v-row>
      <v-col v-for="(catego, index) in categories" :key="index">
             <v-card class="mx-auto my-12" max-width="374" style="height: 100px">
         <v-card-title>
             Titre
             {{catego.CategorieId}}
             {{catego.CategorieName}}
             </v-card-title>
             
     </v-card>   
      </v-col>
      </v-row>            
<!---- Fin Table ---->
    </v-container>
</v-content>
        </v-main>
 
</v-app>
   
  
</template>

<script>
//import Vue from 'vue'
import axios  from 'axios'
import parametre from "../js/ApiConnect.js";
//Vue.use(axios)

export default {
    name: 'CategorieApp',
    
     data() {
        return {
         categories:[],
         CategorieName:"",
         CategorieId:0,


        }
    },

    methods: {
        getData(){
            axios.get(parametre.API_URL+"/categorie")
            .then((response)=>{
                this.categories=response.data;
                
                
            })
        },
    mounted:function(){
        this.getData();
    }
    }
    
}
</script>

<style>
thead,
tfoot {
    background-color: #3f87a6;
    color: #fff;
}

tbody {
    background-color: #e4f0f5;
}

table {
    border-collapse: collapse;
    border: 2px solid rgb(200, 200, 200);
    letter-spacing: 1px;
    font-family: sans-serif;
    font-size: .8rem;
}

td,
th {
    border: 1px solid rgb(190, 190, 190);
    padding: 5px 10px;
}

td {
    text-align: center;
}

</style>