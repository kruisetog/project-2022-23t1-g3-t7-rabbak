<script setup>
import SuccessTransaction from "../components/SuccessTransaction.vue";
</script>

<script>
export default {
    data() {
      return{
        date:"",
        mcc: "",
        currency: "1",
        amount:"",
        cardtype:"1",
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
                name="mcc" placeholder="Enter MCC">
          </div>
      </div>  
      <div class="row">
        <div class="col-md-6 form-group">
          <label for="currency">Currency</label>
          <select class="form-control" v-model="currency" id="currency">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
          </select>
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
          <select class="form-control" v-model="cardtype" id="cardtype">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
          </select>
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
 