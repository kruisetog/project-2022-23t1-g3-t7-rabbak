<script setup>
import TransactionTableRow from "../components/TransactionTableRow.vue";
import CampaignBlock from "../components/CampaignBlock.vue";
import TotalCard from "../components/TotalCard.vue";
import axios from "axios";
</script>

<script>
export default {
  data() {
    return {
      myCards: {},
      transactions: {},
      points: 0,
      miles: 0,
      cashback: 0,
      campaigns: {},
      userID: "",
      currentPage: 1,
      itemsPerPage: 10,
    }
  },
  methods: {
    cardSelected: function(e) {
            const selectedIndex = e.target.value;
            // console.log(selectedIndex)
            if(parseInt(selectedIndex) == selectedIndex){
              this.getCardTransactions(selectedIndex)
            }
            else{
              this.getUserTransactions()
            }
        },
    async getCards(){
      const usercardsResponse = await axios.get("https://wn67is82a0.execute-api.us-east-1.amazonaws.com/1/users/AA8EDA5B03B3422B819FE303E5CA0C18").then(res =>{
        this.points = res['data']['Points_Total']
        this.miles = res['data']['Miles_Total']
        this.cashback = res['data']['Cashback_Total']
        this.myCards = res['data']['Cards']
      })
    },
    async getUserTransactions(){
      const transactionsResponse = await axios.get("https://wn67is82a0.execute-api.us-east-1.amazonaws.com/1/users/AA8EDA5B03B3422B819FE303E5CA0C18/transactions").then(res=>{
        this.transactions = res['data']
        for (let i = 0; i < this.transactions.length; i++) {
          if(this.transactions[i]['Rewards'] == null){
            this.transactions[i]['Excluded'] = true
          }
          else{
            this.transactions[i]['Excluded'] = false
          }
          this.transactions[i]['Name'] = this.getCardName(this.transactions[i]['Card_ID'])
        }
        console.log(this.transactions)
        this.showPage = true
      })
    },
    async getCardTransactions(index){
      const transactionsResponse = await axios.get("https://wn67is82a0.execute-api.us-east-1.amazonaws.com/1/users/AA8EDA5B03B3422B819FE303E5CA0C18/card/" + index + "/transactions").then(res =>{
        this.transactions = res['data']
        for (let i = 0; i < this.transactions.length; i++) {
          if(this.transactions[i]['Rewards'] == null){
            this.transactions[i]['Excluded'] = true
          }
          else{
            this.transactions[i]['Excluded'] = false
          }
          this.transactions[i]['Name'] = this.getCardName(this.transactions[i]['Card_ID'])
        }
        console.log(this.transactions)
      })
    },
      // console.log(transactionsResponse)
      // this.transactions.forEach((key)=>{
      //   console.log("key: ", key)
      //   if(key['Rewards'] == null){
      //     key['excluded'] = true
      //   }
      //   else{
      //     key['excluded'] = false
      //   }
      //   key['Name'] = this.getCardName(transaction['Card_ID'])
      // })
      // for(transaction in this.transactions){
      //   if(transaction['Rewards'] == null){
      //     transaction['excluded'] = true
      //   }
      //   else{
      //     transaction['excluded'] = false
      //   }
      //   transaction['Name'] = this.getCardName(transaction['Card_ID'])
      // }
      // console.log('this.transactions' , this.transactions)
    async getCampaigns(){
      const campaignDetails = await axios.get("https://wn67is82a0.execute-api.us-east-1.amazonaws.com/1/campaigns").then(res =>{
        this.campaigns = res['data']
      })
    },
    getCardName(card_id){
      for (let i = 0; i < this.myCards.length; i++) {
        if(this.myCards[i]['Card_ID'] == card_id){
          return this.myCards[i]['Name']
        }
      }
    },
    onClickHandler(pageNumber) {
      if (pageNumber) {
        this.currentPage = pageNumber;
      }
      console.log(pageNumber);
    }
    },
    computed:{
      recordsShown: function () {
      const startIndex = this.itemsPerPage * (this.currentPage - 1);
      const endIndex = this.itemsPerPage * this.currentPage;
      return this.records.slice(startIndex, endIndex);
      },
    },
    async mounted(){
      await this.getCards()
      await this.getUserTransactions()
      await this.getCardTransactions()
      await this.getCampaigns() 
      this.showPage = true;
    }
}

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
          <br /><br />
          <h5>My Transactions</h5>
          <table class="table">
          <thead>
            <tr>
              <th scope="col">Date</th>
              <th scope="col">Merchant</th>
              <th scope="col">Card Type</th>
              <th scope="col">Amount</th>
              <th scope="col">Rewards</th>
            </tr>
          </thead>
          <TransactionTableRow v-for="transaction in transactions" excludeProcessing="{{transaction['Excluded']}}">
            <template #date>{{transaction['Transaction_Date']}}</template>
            <template #description></template>
            <template #cardType>{{transaction['Name']}}</template>
            <template #amount>{{transaction['Currency']}} {{transaction['Amount']}}</template>
            <template #benefit>{{transaction['Rewards']}}</template>
          </TransactionTableRow>
        </table>
       
        <vue-awesome-paginate 
              :items-per-page="itemsPerPage"
              v-model="currentPage"
              :on-click="onClickHandler"/>
        
      
      </div>
    
      <div class="col-lg-4">
        <br><br>
        <h5>Ongoing Campaigns</h5>
        <CampaignBlock v-for="campaign in campaigns">
          <template #campaignName>{{campaign['Name']}}</template>
          <template #campaignDesc>{{campaign['Description']}}</template>
          <template #endDate>{{campaign['End_Date']}}</template>
        </CampaignBlock>
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

<style>
/* table td {
  max-width: 0;
} */
tr td:first-child {
  width: 1%;
  white-space: nowrap;
} 
.pagination-container {
  display: flex;
  margin-top: 20px;
  list-style: none;
  column-gap: 10px;
  padding-left: 0;
}
.paginate-buttons {
  height: 40px;
  width: 40px;
  border-radius: 20px;
  cursor: pointer;
  background-color: rgb(242, 242, 242);
  border: 1px solid rgb(217, 217, 217);
  color: black;
}
.paginate-buttons:hover {
  background-color: #d8d8d8;
}
.active-page {
  background-color: #3498db;
  border: 1px solid #3498db;
  color: white;
}
.active-page:hover {
  background-color: #2988c8;
}
</style>



