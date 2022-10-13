<script setup>
import SuccessTransaction from "../components/SuccessTransaction.vue";
</script>

<script>
export default {
    data() {
      return{
        date:"",
        mcc: "",
        currency: "",
        amount:"",
        cardtype:"",
        transactionDate: "",
        cardNum: "",
        showSuccess: false
      }
    },
    methods: {
      sendTransaction(){
        this.showSuccess=true;
      },
      close(value){
        console.log(value)
        if(value == 'close'){
          this.showSuccess = false;
        }
      }
    },
    components:{
      SuccessTransaction
    }
};
</script>

<template>
  <main class="main-content">
    <div class="row">
        <div class="col-12">
        <h1>Add Transaction</h1>
        <br>
      <div v-show="!showSuccess">
      <div class="row">
        <div class="col-md-6 form-group">
          <label for="transactionDate">Transaction date</label>
                <input type="date" v-model="transactionDate" class="form-control" 
                name="transactionDate" placeholder="Username">
          </div>
          <div class="col-md-6 form-group">
          <label for="mcc">MCC</label>
                <input type="number" v-model="mcc" class="form-control" 
                name="mcc" placeholder="Select MCC">
          </div>
      </div>  
      <div class="row">
        <div class="col-md-6 form-group">
          <label for="currency">Currency</label>
                <input type="text" v-model="currency" class="form-control" 
                name="currency" placeholder="Select Currency)">
          </div>
          <div class="col-md-6 form-group">
          <label for="amount">Transaction Amount</label>
                <input type="number" v-model="amount" class="form-control" 
                name="mcc" placeholder="Transaction Amount">
          </div>
      </div>  
      <div class="row">
        <div class="col-md-6 form-group">
          <label for="cardtype">Card Type</label>
                <input type="text" v-model="cardtype" class="form-control" 
                name="cardtype" placeholder="Select Card Type">
          </div>
          <div class="col-md-6 form-group">
          <label for="cardNum">Card Number</label>
                <input type="number" v-model="cardNum" class="form-control" 
                name="cardNum" placeholder="Enter Card Number">
          </div>
      </div> 
      <div class="row">
        <div class="col-12 form-group">
        <button class="float-right btn btn-primary" @click="sendTransaction">Add Transaction</button>
        </div>
      </div> 
    </div>

      <div v-show="showSuccess">
      <SuccessTransaction @close="close" title="transaction added"></SuccessTransaction>
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

 
 
</style>
 