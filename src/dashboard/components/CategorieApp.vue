<template>

    <div id="app">
        
    <v-container fill-height fluid class="my-15 grey lighten-5">
    
     <v-row no-gutters>
         <v-col cols="3">
             <span class="input-group-text">Entrer le nom de Catégorie</span>
            
        </v-col>

         <v-col cols="6" >
              <input type="text" class="form-control" v-model="CategorieName" style="width:95%">
         </v-col>
         
         <v-col cols="3">    
            <button type="button" @click="createClick()"
                v-if="CategorieId==0" class="btn btn-primary">
                Ajouter
            </button>
            <button type="button" @click="updateClick()"
                v-if="CategorieId!=0" class="btn btn-primary">
                Mettre à jour
             </button>
        </v-col>
     </v-row>
    
       <v-row>
            <table class="table is-fullwidth" >
            <thead>
                <tr>
                    <th>N °</th>
                    <th>CatégoriesName</th>
                    <th>Opérations</th>
                </tr>

            </thead>

            <tbody :class="{ in: getData() }">
                <tr
                    v-for="item in categories"
                    v-bind:key="item.CategorieId"
                >
                    <td>{{ item.CategorieId }}</td>
                    <td>{{ item.CategorieName }}</td>
                    <td>
                    <button type="button"
                        class="btn btn-light mr-1"
                      @click="editClick(item)"
                        >
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
                        <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                        <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
                        </svg>
                    </button>
                    <button type="button" @click="deleteClick(item.CategorieId)"
                         class="btn btn-light mr-1">
                          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash-fill" viewBox="0 0 16 16">
                         <path d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"/>
                        </svg>
                    </button>
                    </td>

                </tr>
            </tbody>
        </table>
           
       </v-row>
       
            
    </v-container>
</div>
</template>

<script>
import axios from "axios";


//import parametres from './../js/ApiConnect.js'
const API_URL = "http://127.0.0.1:8000/";

export default {
  name: "CategorieApp",

  data() {
    return {
      categories: [],
      Title:"",
      CategorieId: 0,
      CategorieName: "",
     
    };
  },

  methods: {
    getData() {
      //const url = `${API_URL}categorie/`
      //return axios.get(url)
      axios.get(API_URL + "categorie").then((response) => {
        this.categories = response.data;
      });
    },
    mounted: function () {
      this.getData();
    },
  
    editClick(item) {
        this.CategorieId = item.CategorieId;
        this.CategorieName = item.CategorieName;

    },

    createClick() {
        axios.post(API_URL + "categorie",{
            CategorieName: this.CategorieName
        })
        .then((response)=>{
             this.getData();
            alert(response.data);
           
        })
    },
     updateClick() {
        axios.put(API_URL + "categorie",{
            CategorieId: this.CategorieId,
            CategorieName: this.CategorieName,
        })
        .then((response)=>{
             this.getData();
            alert(response.data);
           
        })
    },

     deleteClick(id){
        if(!confirm("Are you sure?")){
            return;
        }
        axios.delete(API_URL+"categorie/"+id)
        .then((response)=>{
            this.getData();
            alert(response.data);
        });

    },

  },
  
};
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
  font-size: 0.8rem;
}

td,
th {
  border: 1px solid rgb(190, 190, 190);
  padding: 5px 10px;
}

td {
  text-align: center;
}
input {
  width: 50%;
}
</style>