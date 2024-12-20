<template>
    <div class="fileUpload_main">
        <div class="mb-3">
            <label for="formFile" class="form-label">Default file input example</label>
            <input @change="(event)=>handelFileChange(event)" class="form-control" type="file" id="formFile">
            <button type="button" class="btn btn-outline-primary" @click="uploadfile">上传</button>
        </div>
    </div>
</template>
<script>
import axios from 'axios';

export default{
    name:"fileUpload",
    data(){
        return{
            fileValue:"",
            data:{
                "姓名":"123321",
                "成绩":"321231"
            }
            
        }
    },
    methods:{
        handelFileChange(e){
            this.fileValue=e.target.files[0]
            console.log(e.target.files)
        },
        async uploadfile(){
            if(!this.fileValue){

                axios.post("api/getfile/insert",{
                    "data":this.data,
                    "tableName":"1734605430"
                })
                .then(res=>{
                    console.log(res)
                })
                .catch(res=>{
                    console.log(res)
                })


                alert("Please select a file first")
                return
            }
            try{
                const formData = new FormData();
                formData.append('file',this.fileValue)

                const request=axios.create({
                    timeout:100000
                })
                
             await  request.post('/api/getfile',
                        formData,
                    {headers:{'content-Type':'multipart/byteranges'}},
                ).then(res=>{
                    console.log(res)
                })
                .catch(res=>{
                    console.log(res)
                })
            }
            catch(error){
                console.log(error)
            }
        }
    }
}


</script>
<style>
</style>