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
      currentPage: 1,
      mycardsModel: 'all',
      selected: 'all',
      showPage: false
    }
  },
  methods: {
    cardSelected: function(e) {
            let selectedIndex = e.target.value;
            this.currentPage = 1
            if(selectedIndex != this.mycardsModel){
              selectedIndex = selectedIndex.split('.')
              this.selected =  selectedIndex[1]
              this.getCardTransactions(selectedIndex[1])
              this.getCardCampaigns(selectedIndex[1])
            }
            else{
              this.mycardsModel = selectedIndex
              this.getUserTransactions()
              this.getCampaigns()
            }
        },
    async getCards(){
      var config = {
        method: "get",
        url: "https://wn67is82a0.execute-api.us-east-1.amazonaws.com/1/users/" + this.userID,
        headers: {},
      };

      const response = await axios(config);
      if (response.status === 200) {
        console.log(response);
        this.points = response.data.total_points;
        this.miles = response.data.total_miles;
        this.cashback = response.data.total_cashback;
        this.myCards = response.data.Cards;
      }
    },
    getUserTransactions(){
      this.transactions = {}
      axios.post("https://wn67is82a0.execute-api.us-east-1.amazonaws.com/1/users/" + this.userID + "/transactions?page=" + this.currentPage).then(res=>{
        if(res['data'].length > 0){
          this.transactions = res['data']
          console.log(res['data'])
          for (let i = 0; i < this.transactions.length; i++) {
            console.log(String(this.transactions[i]['rewards']).length)
            if(this.transactions[i]['rewards'] == 0){
              this.transactions[i]['Excluded'] = true
            }
            else{
              this.transactions[i]['Excluded'] = false
            }
          }
          console.log(this.transactions)
        }
      })
    },
    async getCardTransactions(index){
      var config = {
        method: "get",
        url: "https://wn67is82a0.execute-api.us-east-1.amazonaws.com/1/users/" + this.userID + "/card/" + index + "/transactions?page=" + this.currentPage,
        headers: {},
      };

      const response = await axios(config);
      if (response.status === 200) {
        this.transactions = response.data;
        for (let i = 0; i < this.transactions.length; i++) {
            if(this.transactions[i]['rewards'] == 0){
              this.transactions[i]['Excluded'] = true
            }
            else{
              this.transactions[i]['Excluded'] = false
            }
          };
      }
      console.log(this.transactions)
    },
   async getCampaigns(){
    var config = {
        method: "get",
        url: "https://wn67is82a0.execute-api.us-east-1.amazonaws.com/1/campaigns",
        headers: {},
      };

      const response = await axios(config);
      if (response.status === 200) {
        this.campaigns = response.data;
        for (let i = 0; i < this.campaigns.length; i++) {
            let startDateSplit = this.campaigns[i]['start_date'].split(" ")
            let endDateSplit = this.campaigns[i]['end_date'].split(" ")
            this.campaigns[i]['start_date'] = startDateSplit[0]
            this.campaigns[i]['end_date'] = endDateSplit[0]
          }
      }
    },
    getCardCampaigns(index){
        axios.get("https://wn67is82a0.execute-api.us-east-1.amazonaws.com/1/cards/" + index + "/campaign").then(res=>{
          console.log(res); 
          if(res['data'].length > 0){
          this.campaigns = res['data']
          console.log(this.campaigns)
          for (let i = 0; i < this.campaigns.length; i++) {
            let startDateSplit = this.campaigns[i]['start_date'].split(" ")
            let endDateSplit = this.campaigns[i]['end_date'].split(" ")
            this.campaigns[i]['start_date'] = startDateSplit[0]
            this.campaigns[i]['end_date'] = endDateSplit[0]
            }
          }
          else{
            this.campaigns = {}
          }
        }).catch(err=>{
        console.log(err)
        })
    },
    onClickHandler(pageNumber) {
      if (pageNumber) {
        this.currentPage = pageNumber;
        console.log(this.selected)
        console.log(this.mycardsModel)
        console.log(this.currentPage)
        if(this.selected != this.mycardsModel){
          this.getCardTransactions(this.selected)
        }
        else{
          this.getUserTransactions()
        }
      }
    }
    },
    // computed:{
    //   recordsShown: function () {
    //   const startIndex = this.itemsPerPage * (this.currentPage - 1);
    //   const endIndex = this.itemsPerPage * this.currentPage;
    //   return this.records.slice(startIndex, endIndex);
    //   },
    // },
    async mounted(){
      await this.getCards();
      await this.getUserTransactions();
      await this.getCampaigns();
      this.showPage = true;
    }
}

</script>

<template>
  <main class="main-content">
    <div v-if="showPage">
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
        <label><input type="radio" value='all' name="mycards" v-model="mycardsModel" v-on:change="cardSelected"/> Show All </label> 
        <br>
        <template v-for="card in myCards">
          <label><input type="radio" v-bind:value="card.card_type" v-model="mycardsModel" name="mycards"  v-on:change="cardSelected"/> **** **** **** {{card.card_pan_last}} ({{card.card_type}}) </label> 
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
            <template #date>{{transaction['transaction_date']}}</template>
            <template #description>{{transaction['merchant']}}</template>
            <template #cardType>{{transaction['card_type']}}</template>
            <template #amount>{{transaction['amount']}}</template>
            <template #benefit>{{transaction['rewards']}}</template>
          </TransactionTableRow>
        </table>
       
        <vue-awesome-paginate 
              v-model="currentPage"
              :on-click="onClickHandler"/>
        
      
      </div>
    
      <div class="col-lg-4">
        <br><br>
        <h5>Active Campaigns</h5>
        <CampaignBlock v-for="campaign in campaigns">
          <template #campaignName>{{campaign['merchant']}}</template>
          <template #campaignDesc>{{campaign['description']}}</template>
          <template #startDate>{{campaign['start_date']}}</template>
          <template #endDate>{{campaign['end_date']}}</template>
        </CampaignBlock>
      </div>
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



