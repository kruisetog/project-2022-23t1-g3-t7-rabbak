<script setup>
import MyCardBlock from "../components/MyCardBlock.vue";
import axios from "axios";
</script>

<script>
export default {
    data() {
        return {
          post:{
            otp: "",
            otpMessage: ''
          },
          deletecardNum: '',
          showDeleteModal: false,
          deletecardValue: '',
          otpEmpty:false,
          phoneNumber: "xxxx1234",
          showDeleted: false,
          deletedcardNum: '',
          myCards: {}
        };
    },
    methods: {
        showDeleteCard(value, value2){
            this.showDeleteModal = true;
            this.deletecardValue = value;
            this.deletedcardNum = value2
        },
      toggleModal() {
            this.showDeleteModal = true
        },
        close(){
            this.showDeleteModal = false
            this.showDeleted = false
        },
        deleteCard(){
            if(this.otp == undefined){
               this.otpMessage = "OTP not entered"
               this.otpEmpty = true
            }
            else{
                this.showDeleteModal = false
                this.showDeleted = true
            }  
        },
        async getCards(){
          const usercardsResponse = await axios.get("https://wn67is82a0.execute-api.us-east-1.amazonaws.com/1/users/AA8EDA5B03B3422B819FE303E5CA0C18")
          this.myCards = usercardsResponse['data']['Cards']
      }
    },
    async mounted(){
      await this.getCards()
    },
    components:{
      MyCardBlock
    }
};
</script>

<template>
  <main class="main-content">
    <div class="row">
      <div class="col-12">
        <h1>My Cards</h1>
        <br>
      </div>
      <div class="col-12">
        <table class="table">
          <thead>
            <tr>
              <th scope="col">Your Card</th>
              <th scope="col">Card Type</th>
              <th scope="col">Actions</th>
            </tr>
          </thead>
          <MyCardBlock v-for="card in myCards" v-bind:cardid="card['Card_ID']" v-bind:cardNum="card['Card_Pan']">
            <template #cardNum>{{card['Card_Pan']}}</template>
            <template #cardType>{{card['Name']}}</template>
          </MyCardBlock>
        </table>
      </div>
    </div>

    <div v-show="showDeleteModal">
    <div class="modal show" style="display:block;">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h3 class="modal-title">Are You Sure You Want to Delete Card {{deletedcardNum}}?</h3>
        </div>
        <div class="modal-body">
          <img class="img-fluid mx-auto d-block" src="../assets/exclamation-mark.png"/><br>
          <p>This action cannot be undone. We have sent an OTP to <strong>{{phoneNumber}}</strong> 
          Enter OTP in the box below to delete your account.</p>
          <input type="number" v-model="otp" name ='otp'  class="form-control" id="otp" placeholder="Enter OTP">
          <a id="resend" class="float-right" href="#">Resend OTP</a>
          <p class="otpEmpty float-left" v-if="otpEmpty" href="#">{{ otpMessage }}</p>
        </div>
        <div class="modal-footer">
        <button class="btn btn-secondary" type="button"
            @click="close">
            CANCEL
          </button>
          <button class="btn btn-danger" type="submit"
            @click="deleteCard">
            DELETE MY CARD
          </button>
        </div>
      </div>
    </div>
  </div>
  <div class="modal-backdrop show"></div> 
</div>

<div v-show="showDeleted">
    <div class="modal-backdrop show"></div> 
    <div class="modal show" style="display:block;">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h3 class="modal-title">Card Has Been Deleted</h3>
        </div>
        <div class="modal-body">
          <h5>We have now permanently deleted your card, {{deletedcardNum}}.</h5>
          <button class="btn btn-secondary float-right" type="button"
            @click="close">
            CLOSE
        </button>
        </div>
      </div>
    </div>
  </div>
</div>

  </main>
</template>

<style scoped>
 
.main-content {
  padding-top:80px;
  padding-left: 20px;
  padding-right: 20px;
} 

#resend{
    color: lightgrey !important;
    text-decoration: underline;
}

.otpEmpty{
    color:red;
}

img{
    width:30%;
    height:30%;
}

.modal-title{
    text-align:center;
}
 

</style>



 