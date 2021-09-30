<template>
  <v-container fill-height  class="my-15">
    <v-row justify="center">
      <v-col lg="12" class="text-center">
        <v-subheader class="text-h4 justify-center">Contact Us</v-subheader>
        <p>
          Besoin de parler à un expert ?
          N’hésitez pas à communiquer avec nous.
        </p>
      </v-col>

      <v-col md="4">
        <iframe
          src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d13294.531127293294!2d-7.573442409359025!3d33.58888254175123!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xda7cce0e3802d55%3A0x458cd3047e24c709!2sHay%20Mohammadi%2C%20Casablanca!5e0!3m2!1sfr!2sma!4v1632409488725!5m2!1sfr!2sma"
          width="600"
          height="450"
          style="border: 0"
          allowfullscreen=""
          loading="lazy"
        ></iframe>
      </v-col>

      <v-col md="4" offset-md="4">

        <!---- **** form for e-mail ****----->
        <v-form action="https://formsubmit.co/90d8b5720842d59ffcdd6b38f8161c0e" method="POST" >
         
        
         <input type="hidden" name="_next" value="http://localhost:8080/thanks.html">
         <input type="hidden" name="_autoresponse" value="Bonjour, nous ne manquerons pas de vous faire un retour , incessamment cordialement">
          <v-text-field v-model="contactinfo.email" name="email" label="E-mail" required placeholder="monmail@gmail.com">
          </v-text-field>
          <v-text-field
            v-model="contactinfo.name"
            :counter="10"
            label="Sujet"
            name="subject"
            required
          >
          </v-text-field>
          <v-textarea label="Message" name="message" v-model="contactinfo.message">
          </v-textarea>
          <v-btn color="success" class="mr-4" type="submit">
            Envoyer
          </v-btn>

          <v-btn color="error" class="mr-4" @click="reset()"> Annuler </v-btn>
        </v-form>

        <!--End for form e-mail-->
      </v-col>
    </v-row>
  </v-container>
</template>


<script>
//import SendEmail from '@/components/email/sendEmail.js';
// import axios from 'axios';

export default {
  name: "Contactus",
  
  data() {
  //  SendEmail
    return {
      
      contactinfo: {
                  name:'',
                  email:'',
                  message:''

        },
    };
  },
methods:
{



  // async validate()
  // {
  //    let result = await axios.post(SendEmail, 
  //    {

  //      Host: "smtp.gmail.com",Username : "brhimlion38@gmail.com",Password : "openyoutube01",To : 'brhimlion38@gmail.com',From : "contactinfo.email",Subject : "contactinfo.message",Body : "contactinfo.message",

  //    }
  //    );
  //     console.log(result)

  //  },


}

};
</script>