<script setup>
import SuccessTransaction from "../components/SuccessTransaction.vue";
import currencies from 'currencies.json';

defineProps({
      transactionDate: String,
      mcc: String,
      merchant: String,
      currency: String,
      amount: String, 
      cardtype: String,
      transactionDate: String,
      cardNum: String,
})
</script>

<script>
export default{
    data() {
      return{
        post:{
          showSuccess: true,
        },
        showSuccess: false,
        showError: false,
        errormsge: '',
        // transaction: {},
        currencyCode: []
      }
    },
    methods: {
      sendTransaction(){
      // this.transaction = {
      //   'transaction_date': this.transactionDate,
      //   'merchant': this.merchant,
      //   'mcc': this.mcc,
      //   'currency': this.currency,
      //   'amount': this.amount,
      //   'card_pan': this.cardNum,
      //   'card_type': this.cardtype,
      // }
      console.log(JSON.parse(JSON.stringify({
        'transaction_date': this.transactionDate,
        'merchant': this.merchant,
        'mcc': this.mcc,
        'currency': this.currency,
        'amount': this.amount,
        'card_pan': this.cardNum,
        'card_type': this.cardtype,
      })))
      // if(this.transactionDate.length == 0){
      //   this.showSuccess = true;
      //   this.errormsge = "Transaction Date is empty";
      //   this.showError = true;
      // }
      this.showSuccess = true;
      },
      close(value){
        if(value == 'close'){
          this.showSuccess = false;
          this.showError = false;
          this.errormsge = '';
          // this.transaction = {}
          // console.log(this.transaction)
          // this.transactionDate = '';
          // this.merchant = '',
          // this.mcc = '',
          // this.currency = 'SGD',
          // this.cardNum = '',
          // this.cardType = 'scis_platinummiles'
        }
      },
      closeError(value){
        if(value == 'close'){
          this.showSuccess = false;
          this.showError = false;
          this.errormsge = '';
        }
      }
    },
    computed: {
      getCurrencyCode(){        
      this.currencyCode = []
      for (let i = 0; i < currencies.currencies.length; i++) {
          this.currencyCode.push(currencies.currencies[i]['code']);
        }
       return this.currencyCode
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
      <div v-if="!showSuccess">
      <div class="row">
        <div class="col-md-12 form-group">
          <label for="transactionDate">Transaction date</label>
                <input type="date" v-model="transactionDate" class="form-control" 
                name="transactionDate" placeholder="Username">
          </div>
          <div class="col-md-6 form-group">
          <label for="merchant">Merchant</label>
                <input type="text" v-model="merchant" class="form-control" 
                name="merchant" placeholder="Enter Merchant">
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
                <option v-for="code in getCurrencyCode" :value="code">{{code}}</option>
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
                <option value="scis_platinummiles">scis_platinummiles</option>
                <option value="scis_shopping">scis_shopping</option>
                <option value="scis_freedom">scis_freedom</option>
                <option value="scis_premiummiles">scis_premiummiles</option>
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

    <div v-if="showError">
      <SuccessTransaction @close="closeError" :fail="showError" :error=errormsge ></SuccessTransaction>
    </div>
    <div v-else>
    <SuccessTransaction @close="close" :success=showSuccess title="transaction added"></SuccessTransaction>
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
 