<template>
    <div>
      <div class="mb-4">
        <input type="file" @change="handleFileUpload" class="form-control" />
        <div v-if="tableName != ''">
          <input type="text" :value="tableName" readonly />
        </div>
      </div>
      <button class="btn btn-primary" @click="uploadFile" :disabled="!fileData">上传</button>
    </div>
  </template>
  <script>
  import { request } from '@/api'; // 假设你有一个请求模块
  /* global layer */
  

  export default {
    data() {
      return {
        fileData: null, // 用来存储解析后的文件数据
        tableName:""
      };
    },
   
    methods: {
      handleFileUpload(event) {
        const file = event.target.files[0];
        if (!file) return;
        this.fileData = file;
      },
      uploadFile() {
        if (!this.fileData) return;
        
        this.loadExcelData2(this.fileData)
      },
      async loadExcelData2(data) {
        let formData=new FormData()
        formData.append("file",data)

        let issuccessful=false

        await request.post("getfile",
          formData
        )
        .then(res=>{
          this.tableName=res.data.tableName
          issuccessful=true
          layer.msg('成功', {icon: 1});
        })
        .catch(res=>{
          layer.msg('失败', {icon: 2});
        })

        if(issuccessful){
          this.getTableData()
        }

      },
      async getTableData(){
        await request.post("getfile/select",
          {
            start:"0",
            size:"10",
            tableName:this.tableName
          }
        ).then(res=>{
            layer.msg('成功', {icon: 1});
          
            this.$emit("file-loaded",res.data.data,res.data.lines[0]["count(*)"],this.tableName)

          })
          .catch(res=>{
            layer.msg('失败', {icon: 2});
          })
      }
    },
  };
  </script>
  