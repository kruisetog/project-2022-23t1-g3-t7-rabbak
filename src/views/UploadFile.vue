<script setup>
import SuccessTransaction from "../components/SuccessTransaction.vue";
import { Storage } from 'aws-amplify';
</script>


<script>
export default {
  data() {
    var filelist = [];
    return { 
      filetype: ['text/csv', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,', 'application/vnd.ms-excel'],
      filelist: [],
      showSuccess: false,
      showFile: true,
      showError: false,
      errormsge: ''
    } 
  },
  methods: {
    dragover(event) {
      event.preventDefault();
    },
    dragleave(event) {
      event.preventDefault();
    },
    drop(event) {
      event.preventDefault();
      this.$refs.file.files = event.dataTransfer.files;
      this.onChange();
    },
    onChange() {
      this.filelist = [...this.$refs.file.files]
    },
    browse(){
      const elem = this.$refs.file
      elem.click()
    },
    upload(){
      // console.log(this.filelist[0])
      if (this.filelist.length == 0){
        this.showError = true;
        this.errormsge = 'Please select a file to upload'
      }
      else if(this.filetype.includes(this.filelist[0].type) == false){
        this.showError = true;
        this.showFile = false;
        this.errormsge = 'Unsupported File Type'
      }
      else{
        console.log(this.filelist[0])
        Storage.put(this.filelist[0].name, this.filelist[0], {
        }).then((data)=>{
          this.showFile = false;
          this.showSuccess=true;
        }).catch((err)=>{
          this.showFile = false;
          this.showError=true;
          this.errormsge=err;
        })
    }
    } ,close(value){
        this.showSuccess = false;
        this.showError = false;
        this.showFile = true;
        this.errormsge = '';
        this.filelist = [];
      }
  },
    components:{
      SuccessTransaction
    }
}
</script>

<template>
  <main class="main-content">
    <div class="content">
      <h1>File Upload</h1>
      <br>
      <div v-if="showFile" class="row">
        <div class="col-md-2"></div>
        <div class="col-md-8">
        <div class="upload-box" @dragover="dragover" @dragleave="dragleave" @drop="drop">
          <input type="file" multiple name="fields[assetsFieldHandle][]" id="assetsFieldHandle"
            @change="onChange" ref="file" accept=".csv, .xlsx" />
          <span class="upload-icon">
            <i class="icon-cloud-upload primary font-large-2"></i>
          </span>
          <h6 class="upload-text">Drag and drop, or <span @click="browse">browse</span> your files</h6>
          <span v-if="filelist[0]">
            {{filelist[0].name }} 
          </span>
          </div>
          <a class="col-12 btn btn-primary" @click="upload">Upload</a>
        </div>
      </div>
      
      <div v-if="showError">
      <SuccessTransaction @close="close" :fail=showError :error=errormsge ></SuccessTransaction>
      </div>
      <div v-if="showSuccess">
      <SuccessTransaction @close="close" :success=showSuccess title="file upload"></SuccessTransaction>
      </div>

    </div>
  </main>
</template>

<style>
.main-content {
  padding-top: 80px;
  padding-left: 20px;
  padding-right: 20px;
}

#assetsFieldHandle {
  display: none;
}

.upload-box {
  text-align: center;
  border: 2px dashed #777;
  padding: 50px;
  margin-bottom: 20px;
  border-radius: 10px;
}
.upload-box span {
  display: block;
}

.upload-icon {
  font-size: 40px;
}
.upload-text span{
  display: inline;
  color: #0078ef;
  cursor: pointer;
}

.btn{
  color: white !important;
}
</style>
