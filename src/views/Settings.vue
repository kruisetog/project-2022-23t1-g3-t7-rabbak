<script setup>
import LogOut from "../components/LogOut.vue";
</script>

<script>
export default {
    data() {
        return {
          post:{
            otp: "",
            otpMessage: ''
          },
            showDialog: false,
            showDeleted:false,
            otpEmpty:false,
            phoneNumber: "xxxx1234",
            timerEnabled: true,
            timerCount: 5,
            timerShow: true
        };
    },
    methods: {
      deleteAccount(){
            if(this.otp == undefined){
               this.otpMessage = "OTP not entered"
               this.otpEmpty = true
            }
            else{
                this.showDialog = false
                this.showDeleted = true
            }  
        },
        toggleModal() {
            this.showDialog = true
        },
        close(){
            this.showDialog = false
        },
        logout(value){
          console.log(value)
          this.$router.push({ name: 'logOut', params: { logout: value } })
        },
        resend(){
          console.log('resend')
          this.timerCount = 5
          this.timerEnabled(5)
        }
    },
    watch: {
      timerEnabled(value) {
          if (value) {
              setTimeout(() => {
                  this.timerCount--;
              }, 1000);
          }
      },
      timerCount: {
          handler(value) {
              if (value > 0 && this.timerEnabled) {
                  this.otpMessage = ""
                  this.otpEmpty = false
                  this.timerShow = true
                  setTimeout(() => {
                      this.timerCount--;
                  }, 1000);
              }
              if(value <= 0){
                this.otpMessage = "OTP Expired"
                this.otpEmpty = true
                this.timerShow = false
              }

          },
          immediate: true // This ensures the watcher is triggered upon creation
      },
      }
};
</script>

<template>
  <main class="main-content">
    <div class="row">
        <div class="col-7">
        <h1>Settings</h1>
        <br>
        </div>  
    </div> 
    <div class="row">
    <div class="col-md-10">
        <h5>I want to delete my account</h5>
    </div>
    <div class="col-md-2">
        <a href="#"><button class="btn btn-danger" @click="toggleModal" type="button">DELETE MY ACCOUNT</button></a>
    </div>
    </div>
   
   <div v-show="showDialog">
    <div class="modal show" style="display:block;">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h3 class="modal-title">Are You Sure You Want to Delete Your Account?</h3>
        </div>
        <div class="modal-body">
          <img class="img-fluid mx-auto d-block" src="../assets/exclamation-mark.png"/><br>
          <p>This action cannot be undone. We have sent an OTP to <strong>{{phoneNumber}}</strong> 
          Enter OTP in the box below to delete your account.</p>
          <p v-show="timerShow">OTP expiring in {{timerCount}}</p>
          <input type="number" v-model="otp" name ='otp'  class="form-control" id="otp" placeholder="Enter OTP">
          <a id="resend" class="float-right" @click="resend">Resend OTP</a>
          <p class="otpEmpty float-left" v-if="otpEmpty" href="#">{{ otpMessage }}</p>
          
        </div>
        <div class="modal-footer">
        <button class="btn btn-secondary" type="button"
            @click="close">
            CANCEL
          </button>
          <button class="btn btn-danger" type="submit"
            @click="deleteAccount">
            DELETE MY ACCOUNT
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
          <h3 class="modal-title">Account Deleted</h3>
        </div>
        <div class="modal-body">
          <h5>We have now permanently deleted your user account.</h5>
        </div>
        <div class="modal-footer">
          <LogOut @logout="logout"></LogOut>
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

a:hover{
  cursor: pointer;
}
 
</style>
 