<template>
  <div id="app">
    <v-container fill-height fluid class="my-15 grey lighten-5">
      <v-row no-gutters>
        <v-col cols="3"> </v-col>
        <v-col cols="6">
          <!-- ***** *** chargement des categories **********-->
          <v-select
            v-if="categories"
            v-bind:items="categories"
            v-model="SelectCategory"
            label="Sélectionner une Catégorie"
            single-line
            item-text="CategorieName"
            item-value="CategorieId"
            return-object
            bottom
            @click="getDataCategorie"
            @input="getFilterProducts(`${SelectCategory.CategorieName}`)"
            :hint="`${SelectCategory.CategorieName}`"
          >
          </v-select>
          <!--  ******* --------------------------------***** -->
        </v-col>
      </v-row>
      <v-row no-gutters>
        <v-col cols="3">
          <span class="input-group-text">Entrer le nom de Produit</span>
        </v-col>
        <v-col cols="6">
          <input
            type="text"
            class="form-control"
            v-model="ProductName"
            style="width: 95%"
          />
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="3">
          <span class="input-group-text">Déscription de Produit</span>
        </v-col>
        <v-col cols="6">
          <input
            type="text"
            class="form-control"
            v-model="ProductDescription"
            style="width: 95%"
          />
        </v-col>
      </v-row>
      <v-row>
        <v-col clos="6">
          <span> Choisir l'image </span>
        </v-col>
        <!--  ******* appel de la fonction imageUpload ***** -->
        <v-col cols="6">
          <img width="250px" height="250px" :src="PhotoPath + PhotoFileName" />
          <input
            :v-bind="value"
            type="file"
            name="uploadFile"
            @change="imageUpload"
          />
          <!--  ******* --------------------------------***** -->
        </v-col>
      </v-row>
      <v-row>
        <!--  ******* appel de la fonction Ajouter / Mettre à jour l'enregistrement ***** -->
        <v-col cols="3" align="right">
          <button
            type="button"
            @click="create_Function()"
            v-if="ProductId == 0"
            class="btn btn-primary"
          >
            Ajouter
          </button>
          <button
            type="button"
            @click="update_Function()"
            v-if="ProductId != 0"
            class="btn btn-primary"
          >
            Mettre à jour
          </button>
          <!--  ******* __________________________###############______________________ **** -->
        </v-col>
      </v-row>

      <v-row>
        <!--  ************** affichage des enregistrements sur la table  ****************   -->
        <table class="table is-fullwidth">
          <thead>
            <tr>
              <th>N° Produit</th>
              <th>Catégorie</th>
              <th>Name de Produit</th>
              <th>Description</th>
              <th>Opérations</th>
            </tr>
          </thead>

          <tbody>
            <!-- **** boucle recuperer des enregistrements Produits depuis la db **** -->
            <tr v-for="item in products" v-bind:key="item.ProductId">
              <td>{{ item.ProductId }}</td>
              <td>{{ item.RefCategorie }}</td>
              <td>{{ item.ProductName }}</td>
              <td>{{ item.ProductDecrip }}</td>
              <td>
                <!-- **** fonction Edite **** -->
                <button
                  type="button"
                  class="btn btn-light mr-1"
                  @click="edit_Function(item)"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    fill="currentColor"
                    class="bi bi-pencil-square"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"
                    />
                    <path
                      fill-rule="evenodd"
                      d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"
                    />
                  </svg>
                </button>

                <!-- **** fonction delete **** -->
                <button
                  type="button"
                  @click="delete_Function(item.ProductId)"
                  class="btn btn-light mr-1"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    fill="currentColor"
                    class="bi bi-trash-fill"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"
                    />
                  </svg>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
        <!--  ************** ___________fin de la table______________  ****************   -->
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000/";
const PHOTO_URL = "http://127.0.0.1:8000/Photos/";

export default {
  name: "ProductApp",

  data() {
    return {
      categories: [],
      SelectCategory: "",
      products: [],
      ProductId: 0,
      ProductName: "",
      ProductDescription: "",
      PhotoFileName: "logo.png",
      PhotoPath: PHOTO_URL,
    };
  },

  methods: {
    // **** Recuperer la liste des categories

    getDataCategorie() {
      axios.get(API_URL + "categorie").then((response) => {
        this.categories = response.data;
      });
    },

    // ****  filtrer les produits par catégorie

    getFilterProducts(getSelectCatory) {
      axios.get(API_URL + `producte/${getSelectCatory}`).then((response) => {
        this.products = response.data;
        console.log("************ :", getSelectCatory);
      });
    },

    // **** Edition des enregistrements

    edit_Function(item) {
      this.ProductId = item.ProductId;
      this.SelectCategory = item.RefCategorie;
      this.ProductName = item.ProductName;
      this.ProductDescription = item.ProductDecrip;
      this.PhotoFileName = item.PhotoFileName;
    },

    // **** Ajouter les enregistrements
    create_Function() {
      axios
        .post(API_URL + "producte", {
          RefCategorie: this.SelectCategory.CategorieName,
          ProductName: this.ProductName,
          ProductDecrip: this.ProductDescription,
          PhotoFileName: this.PhotoFileName,
        })
        .then((response) => {
          alert(response.data);
        });
    },

    // **** Modification des enregistrements

    update_Function() {
      axios
        .put(API_URL + "producte", {
          ProductId: this.ProductId,
          ProductName: this.ProductName,
          RefCategorie: this.SelectCategory,
          ProductDecrip: this.ProductDescription,
          PhotoFileName: this.PhotoFileName,
        })
        .then((response) => {
          alert(response.data);
        });
    },
    // **** Suppression des enregistrements

    delete_Function(id) {
      if (!confirm("Êtes-vous sûr de vouloir supprimer ce fichier ?")) {
        return;
      }
      axios.delete(API_URL + "producte/" + id).then((response) => {
        alert(response.data);
      });
    },

    // ****  Télechargement de l'images

    imageUpload(event) {
      let formData = new FormData();
      formData.append("uploadFile", event.target.files[0]);
      axios
        .post(API_URL + "producte/saveImage", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
            //'enctype': 'multipart/form-data'
          },
        })
        .then((response) => {
          this.PhotoFileName = response.data;
          //console.log(this.PhotoFileName);
        });
    },
  },
  mounted: function () {
    this.getDataCategorie();
    this.getFilterProducts();
    this.imageUpload();
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