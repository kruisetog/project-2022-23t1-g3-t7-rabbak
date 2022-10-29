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
          <TotalCard cashbacks="-" loyaltyPoints="500" miles="3,041,730" />
        </div>
      </div>
      <div class="col-4 myCards overflow-auto"> 
        <h3>My Cards <i class="icon-credit-card primary font-large-2"></i></h3>
        <label><input type="radio" :value='all' name="mycards" v-model="mycardsModel" v-on:change="cardSelected" selected/> Show All </label> 
        <br>
        <template v-for="(card, index) in myCards">
          <label><input type="radio" :value="index" name="mycards" v-model="mycardsModel" v-on:change="cardSelected"/> {{card.cardNumber}} ({{card.cardType}}) </label> 
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
          <TransactionTableRow date="6th Sep 2022" desc="Flight ticket to MLA" 
          cardType="Freedom" amount="$2,000" benefit="3,041,730 miles">
          </TransactionTableRow>
         
          <TransactionTableRow excludeProcessing=true date="7th Sep 2022" desc="Ezlink Top up" 
          cardType="Platinum Miles" amount="$10" benefit="-">
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
    var myCards = [
      {
      "cardNumber": "****1234",
      "cardType": "Freedom"
    }, {
      "cardNumber": "****5678",
      "cardType": "SCIS Miles"
    }, {
      "cardNumber": "****1578",
      "cardType": "Freedom"
    }, {
      "cardNumber": "****1578",
      "cardType": "Freedom"
    }, 
    {
      "cardNumber": "****1578",
      "cardType": "Freedom"
    }, 
    {
      "cardNumber": "****1578",
      "cardType": "Freedom"
    },  {
      "cardNumber": "****1578",
      "cardType": "Freedom"
    },  {
      "cardNumber": "****1578",
      "cardType": "Freedom"
    },  {
      "cardNumber": "****1578",
      "cardType": "Freedom"
    },  {
      "cardNumber": "****1578",
      "cardType": "Freedom"
    }, 
    
  ]
    return {
      myCards: myCards 
    }
  },
  methods: {
    cardSelected: function(e) {
            const selectedIndex = e.target.value;
            console.log(selectedIndex)
            
        },
    async getTransactions(){
      const transactionsResponse = await axios.get("https://wn67is82a0.execute-api.us-east-1.amazonaws.com/1/users/AA8EDA5B03B3422B819FE303E5CA0C18/card/1/transactions")
      console.log(transactionsResponse)
    }
    },
    async mounted(){
      await this.getTransactions()
    }
}

</script>