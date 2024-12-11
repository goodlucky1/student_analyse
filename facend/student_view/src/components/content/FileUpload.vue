<template>
    <div class="fileUpload_main">
        <div class="mb-3">
            <label for="formFile" class="form-label">Default file input example</label>
            <input @change="(event)=>handelFileChange(event)" class="form-control" type="file" id="formFile">
            <button type="button" class="btn btn-outline-primary" @click="uploadfile">登录</button>
        </div>
    </div>
</template>
<script>
import axios from 'axios';

export default{
    name:"fileUpload",
    data(){
        return{
            fileValue:""
        }
    },
    methods:{
        handelFileChange(e){
            this.fileValue=e.target.files[0]
            console.log(e.target.files)
        },
        async uploadfile(){
            if(!this.fileValue){
                alert("Please select a file first")
                return
            }

           

            try{
                const formData = new FormData();
                formData.append('file',this.fileValue)
                

             await  axios.post('api/getfile',
                    formData,
                    {headers:{'content-Type':'multipart/form-data'}}
                ).then(res=>{
                    console.log(2)
                })
                .catch(res=>{
                    console.log(res)
                })

                console.log(res)
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