<script setup>
import SuccessTransaction from "../components/SuccessTransaction.vue";
import {readFile, read, utils} from 'xlsx';
</script>


<script>
export default {
  data() {
    var filelist = [];
    return { 
      filetype: ['text/csv', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,', 'application/vnd.ms-excel'],
      filelist: [],
      showSuccess: false
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
      this.showSuccess=true;
      console.log(this.filelist[0])
      // this.ft = this.filelist[0].type
      // console.log(this.file.type in this.filetype)
      // if(this.ft in this.filetype == false){
      //   alert('only accept csv/xlxs files')
      // }
      // console.log(this.file)
//to read file in vue
      // let fileReader = new FileReader();
      // fileReader.readAsArrayBuffer(this.file);
      // fileReader.onload = (e) => {
      //   this.arrayBuffer = fileReader.result;
      //   var data = new Uint8Array(this.arrayBuffer);
      //   var arr = new Array();
      //   for (var i = 0; i != data.length; ++i)
      //     arr[i] = String.fromCharCode(data[i]);
      //   var bstr = arr.join("");
      //   var workbook = read(bstr, { type: "binary" });
      //   var first_sheet_name = workbook.SheetNames[0];
      //   var worksheet = workbook.Sheets[first_sheet_name];
      //   console.log(utils.sheet_to_json(worksheet, { raw: true }));
      //   var arraylist = utils.sheet_to_json(worksheet, { raw: true });
      //   this.filelist = [];
      //   console.log(this.filelist);
      // };
    } ,close(value){
        this.showSuccess = false;
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
      <div v-if="!showSuccess" class="row">
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
      
      <div v-if="showSuccess">
      <SuccessTransaction @close="close" title="file upload"></SuccessTransaction>
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
