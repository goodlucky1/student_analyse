<template>
   
    <div class="container mt-5">
      <h2>Excel 数据导入与管理</h2>
      
      <!-- 文件导入组件 -->
      <div class="mb-4">
        <ExcelImport ref="excelImport"  @file-loaded="loadExcelData"  />
      </div>
      
      <!-- 数据表格组件 -->
      <div class="table-responsive">
        <DataTable :tableName="tableName"  :lines="lines"  :data="tableData" @delete-row="confirmDeleteRow"  @select="loadExcelData2" />
      </div>
    </div>
  </template>
  
  <script>
  import ExcelImport from '../components/ExcelImport.vue';
  import DataTable from '../components/DataTable.vue';


  export default {
    name: 'dzy_S',
    components: { ExcelImport, DataTable },
    data() {
      return {
        tableData: [],  // 用于存储从 Excel 文件中导入的数据
        lines:0,
        tableName:''
      };
    },
    methods: {
      test2(){
        console.log(this.$refs.excelImport)
      },
      updateTableData(newData) {
      this.data = newData;
    },
      // 处理 Excel 文件上传并加载数据
      loadExcelData(data,lines2,tableName) {

        this.tableName=tableName
        this.lines=lines2
        for(let item in data){
          for(let item2 in data[item]){
            data[item][item2]=data[item][item2].replace("nan","")
          }
        }

        this.tableData=data

      },
      loadExcelData2(data){
        for(let item in data){
          for(let item2 in data[item]){
            data[item][item2]=data[item][item2].replace("nan","")
          }
        }

        this.tableData=data
      },
     
  
      // 删除行前的确认
      confirmDeleteRow(index) {
        if (window.confirm('确定要删除这一行数据吗？')) {
          this.deleteRow(index);
        }
      },
  
      // 删除指定行的数据
      deleteRow(index) {
        this.tableData.splice(index, 1); // 删除指定的行
      },
    },
  };
  </script>
  
  <style scoped>
  /* 使用 Bootstrap 类以简化样式 */
  .container {
    max-width: 900px;
    margin: 0 auto;
  }
  
  .table-responsive {
    margin-top: 20px;
  }
  
  .mb-4 {
    margin-bottom: 1.5rem;
  }
  </style>
  
  