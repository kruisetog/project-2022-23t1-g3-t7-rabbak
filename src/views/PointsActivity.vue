<script setup>
import TransactionTableRow from "../components/TransactionTableRow.vue";
import CampaignBlock from "../components/CampaignBlock.vue";
import TotalCard from "../components/TotalCard.vue";
import axios from "axios";
</script>

<template>
  <main class="main-content">
    <div class="row">
      <div class="col-7">
        <h1>My points activity</h1>
        <br>
        <div class="row">
          <TotalCard v-bind:cashbacks="cashback" v-bind:loyaltyPoints="points" v-bind:miles="miles" />
        </div>
      </div>
      <div class="col-4 myCards overflow-auto"> 
        <h3>My Cards <i class="icon-credit-card primary font-large-2"></i></h3>
        <label><input type="radio" :value='all' name="mycards" v-model="mycardsModel" v-on:change="cardSelected" selected/> Show All </label> 
        <br>
        <template v-for="card in myCards">
          <label><input type="radio" v-bind:value="card.Card_ID" name="mycards" v-model="mycardsModel" v-on:change="cardSelected"/> {{card.Card_Pan}} ({{card.Name}}) </label> 
          <br>
        </template>
      </div>
       
      <div class="col-lg-7 my-transactions">
        <br><br>
        <h5>My Transactions</h5>
        <table class="table">
          <thead>
            <tr>
              <th scope="col">Date</th>
              <th scope="col">Description</th>
              <th scope="col">Card Type</th>
              <th scope="col">Amount</th>
              <th scope="col">Benefit</th>
            </tr>
          </thead>
          <TransactionTableRow v-for="transaction in transactions">
            <template #date>{{transaction['Transaction Date']}}</template>
            <template #description>Flight ticket to MLA</template>
            <template #cardType>Freedom</template>
            <template #amount>{{transaction['Currency']}} {{transaction['Amount']}}</template>
            <template #benefit>3,041,730 miles</template>
          </TransactionTableRow>
        </table>
      </div>
    
      <div class="col-lg-5">
        <br><br>
        <h5>Ongoing Campaigns</h5>
        <CampaignBlock campaignName="Buy everything at shopee" campaignDesc="Earn 5% more cashback" expiryText="5 days" progress="50"/>
        <CampaignBlock campaignName="Salmon cafe opening" campaignDesc="Earn 5% more cashback with minimum $100 spent" expiryText="2 weeks" progress="60"/>
      </div>

    </div>

  </main>
</template>

<style scoped>
@media only screen and (min-width: 1000px) {
  .myCards{
  max-height:250px;
}
}
.main-content {
  padding-top:80px;
  padding-left: 20px;
  padding-right: 20px;
  display: flex;
} 
</style>



<script>
export default {
  data() {
  //   var myCards = [
  //     {
  //     "cardNumber": "****1234",
  //     "cardType": "Freedom"
  //   }, {
  //     "cardNumber": "****5678",
  //     "cardType": "SCIS Miles"
  //   }, {
  //     "cardNumber": "****1578",
  //     "cardType": "Freedom"
  //   }, {
  //     "cardNumber": "****1578",
  //     "cardType": "Freedom"
  //   }, 
  //   {
  //     "cardNumber": "****1578",
  //     "cardType": "Freedom"
  //   }, 
  //   {
  //     "cardNumber": "****1578",
  //     "cardType": "Freedom"
  //   },  {
  //     "cardNumber": "****1578",
  //     "cardType": "Freedom"
  //   },  {
  //     "cardNumber": "****1578",
  //     "cardType": "Freedom"
  //   },  {
  //     "cardNumber": "****1578",
  //     "cardType": "Freedom"
  //   },  {
  //     "cardNumber": "****1578",
  //     "cardType": "Freedom"
  //   }, 
    
  // ]
    return {
      myCards: {},
      transactions: {},
      points: 0,
      miles: 0,
      cashback: 0,
    }
  },
  methods: {
    cardSelected: function(e) {
            const selectedIndex = e.target.value;
            console.log(selectedIndex)
            if(parseInt(selectedIndex) == selectedIndex)
            this.getCardTransactions(selectedIndex)
            
        },
    async getCardTransactions(index){
      const transactionsResponse = await axios.get("https://wn67is82a0.execute-api.us-east-1.amazonaws.com/1/users/AA8EDA5B03B3422B819FE303E5CA0C18/card/" + index + "/transactions")
      this.transactions = transactionsResponse['data']
    },
    async getCards(){
      const usercardsResponse = await axios.get("https://wn67is82a0.execute-api.us-east-1.amazonaws.com/1/users/AA8EDA5B03B3422B819FE303E5CA0C18")
      this.points = usercardsResponse['data']['Points_Total']
      this.miles = usercardsResponse['data']['Miles_Total']
      this.cashback = usercardsResponse['data']['Cashback_Total']
      this.myCards = usercardsResponse['data']['Cards']
    }
    },
    async mounted(){
      await this.getCardTransactions()
      await this.getCards()
    }
}

</script>