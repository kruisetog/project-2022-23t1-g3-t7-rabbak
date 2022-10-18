<script setup>
// import { useRoute } from 'vue-router';
// const route = useRoute();  
// const logout = route.params.logout;  
defineProps({
    logoutText:{
            required:true,
            type:Boolean
        }
})
</script>

<script>


export default {
    data() {
        return {
            post:{
                role:""
            },
            username:"",
            password:"",
            logOutMessage: "",
            message: "",
            logout: false
        };
    }, 
    
    methods: {
        login() {
           if(this.role == "customer"){
            this.$router.push('activity') 
           }
           else if(this.role == "staff"){
            this.$router.push('uploadFile')
           }
        },
        logout(value){  
            console.log(value)
        }
    }
    // , 
    // computed:{
    //     getRole(){
    //         return this.role
    //     }
    // }
};
</script>

<template>
    <div class="col-centered login-form">
                <h2 class="text-center">
            <a class="logo">
                <img id="loginImg" src='./../assets/logo.png' />
            </a>
            </h2> 
            <br>
            <h6 class="text-center" v-show="logoutText">Successfully Logged Out</h6> 
            <br> 
            <h6>{{message}}</h6>
            <h5 class="text-center">Login</h5>
            <div class="form-group">
                <input type="text" v-model="username" class="form-control" name="username" placeholder="Username">
            </div>
            <div class="form-group">
                <input type="password" v-model="password" class="form-control" name="password" placeholder="Password">
            </div>    
			<div class="form-group">
				<div class="row ml-1">
				<div class="form-check col-6 mr-3">
                    <input v-model="role"   class="form-check-input" value="customer" type="radio" name="roleSelect" id="customer" >
					<label class="form-check-label" for="customer">
                    Customer
					</label>
				  </div>
				  <div class="form-check col-6">
					<input v-model="role" class="form-check-input" type="radio" value="staff" name="roleSelect" id="staff">
					<label class="form-check-label" for="staff">
					  Staff
					</label>
				  </div>
				  </div>
            </div>       
            <div class="form-group">
                <button type="submit" @click="login" class="btn btn-primary btn-lg btn-block" style="font-weight:normal;">Login</button>
            </div>
    </div>
</template>

<style scoped>
.main-content {
  padding-top:80px;
  padding-left: 20px;
  padding-right: 20px;
  display: flex;
} 
.form-control {
	min-height: 41px;
	background: #fff;
	box-shadow: none !important;
	border-color: #e3e3e3;
}
.form-control:focus {
	border-color: #587da1;
}
.form-control, .btn {        
	border-radius: 2px;
}
.login-form {
    float:none;	
    margin-top:70px;
}
@media only screen and (min-width: 1000px) {
    .login-form {
        margin-right:100px;
    }
    #loginImg{
        width:20%;
        height:20%;
    }
}


.login-form form {
	color: #7a7a7a;
	border-radius: 2px;
	margin-bottom: 15px;
	font-size: 13px;
	background: #ececec;
	box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.3);
	padding: 30px;	
    padding-top:5px;
	position: relative;	
    width:50%;
}
.login-form h2 {
	font-size: 22px;
	margin: 35px 0 25px;
}
.login-form input[type="checkbox"] {
	position: relative;
	top: 1px;
}
.login-form .btn, .login-form .btn:active {        
	font-size: 16px;
	font-weight: bold;
	background: #587da1 !important;
	border: none;
	margin-bottom: 20px;
}
.login-form .btn:hover, .login-form .btn:focus {
	background: #365069 !important;
}    
.login-form a {
	color: #fff;
	text-decoration: underline;
}
.login-form a:hover {
	text-decoration: none;
}
.login-form form a {
	color: #7a7a7a;
	text-decoration: none;
}
.login-form form a:hover {
	text-decoration: underline;
}
.login-form .bottom-action {
	font-size: 14px;
}

@media only screen and (max-width: 1000px) {
    .login-form form {
         width: 100% !important;
    }
    .login-form {
        margin-right: 300px !important;
        width:100%;
    }
    #loginImg{
        width:40%;
        height:40%;
    }
}


</style>



 