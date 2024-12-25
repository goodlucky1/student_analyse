<template>
  <div class="table-container" v-if="data.length">
    <!-- 按钮操作区 -->
    <div class="table-header">
      <button class="btn btn-rounded btn-primary" @click="openAddDialog">添加</button>
      <button
        class="btn btn-rounded btn-danger"
        :disabled="!selectedRows.length"
        @click="deleteSelectedRows"
      >
        删除
      </button>
      <div class="search-box">
        <input
          type="text"
          v-model="searchQuery"
          placeholder="请输入搜索内容"
        />
        <button class="btn btn-rounded btn-secondary" @click="searchData" id="select">
          搜索
        </button>
      </div>
    </div>

    <!-- 表格 -->
    <table class="table table-striped table-bordered">
      <thead>
        <tr>
          <th>
            <input
              type="checkbox"
              @change="toggleAllRowsSelection($event)"
              :checked="allRowsSelected"
            />
          </th>
          <th v-for="(col, index) in columns" :key="index">{{ col }}</th>
          <th>操作</th>
          <th>生成图</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(row, index) in pagedData"
          :key="index"
          @mouseover="hover = index"
          @mouseleave="hover = -1"
          :class="{ 'table-hover': hover === index }"
        >
          <td>
            <input
              type="checkbox"
              :value="row"
              @change="toggleRowSelection(row[union])"
              :checked="selectedRows.includes(row[union])"
            />
          </td>
          <td v-for="(col, colIndex) in columns" :key="colIndex">
            {{ row[col] }}
          </td>
          <td>
            <button class="btn btn-rounded btn-info" @click="openEditDialog(row)" id="update">
              更改
            </button>
          </td>
         
          <td>
  <button class="btn btn-rounded btn-success" @click="generateLineChart(row)">
    折线图
  </button>
  <button class="btn btn-rounded btn-warning" @click="generateRadarChart(row)">
    雷达图
  </button>
</td>

        </tr>
      </tbody>
    </table>

    <!-- 分页和统计 -->
    <div class="pagination-info">
      <span>总页数：{{ totalPages }}，总行数：{{ totalItems }}</span>
      <div class="page-control">
        <button
          class="btn btn-rounded btn-secondary"
          :disabled="currentPage === 1"
          @click="changePage(currentPage - 1)"
        >
          上一页
        </button>
        <input
          type="number"
          v-model.number="jumpPage"
          @keyup.enter="jumpToPage"
          min="1"
          :max="totalPages"
          placeholder="跳转页"
          writable: true
        />
        <button
          class="btn btn-rounded btn-secondary"
          :disabled="currentPage === totalPages"
          @click="changePage(currentPage + 1)"
        >
          下一页
        </button>
      </div>
      <span class="page-info">当前页：{{ currentPage }} / 每页：{{ pageSize }}</span>
    </div>
   
    <div v-if="showChartDialog" class="dialog-overlay">
  <div class="dialog">
    <h3>{{ chartTitle }}</h3>
    <component
      :is="chartComponent"
      :labels="chartLabels"
      :data="chartData"
    ></component>
    <div class="dialog-actions">
      <button class="btn btn-rounded btn-secondary" @click="closeChartDialog">
        关闭
      </button>
    </div>
  </div>
</div>

    
    <!-- 添加与编辑弹框 -->
    <div v-if="showAddDialog || showEditDialog" class="dialog-overlay">
      <div class="dialog">
        <h3 v-if="showAddDialog">添加新行数据</h3>
        <h3 v-else>更改行数据</h3>
        <form class="form" action="/api/getfile" method="post">
        <div v-for="col in columns" :key="col" class="input-group">
          <label>{{ col }}</label>
          <input
            v-model="editRow[col]"
            :placeholder="'请输入 ' + col"
            :name="col"
          />
        </div>
        <div class="dialog-actions">
          <button
            class="btn btn-rounded btn-primary"
            @click="showAddDialog ? addRow() : saveRowChanges()"
            
          >
            确认
          </button>
          <button
            class="btn btn-rounded btn-secondary"
            @click="closeDialog"
          >
            取消
          </button>
        </div>
      </form>
      </div>
    </div>
  </div>

  <!-- 初始无数据显示 -->
  <div v-else class="no-data">请导入 Excel 数据以查看内容。</div>
</template>

<script>
import { request } from '@/api';
// import LineChart from "@/components/LineChart.vue";
// import RadarChart from "@/components/RadarChart.vue";
import LineChart from './LineChart.vue';
import RadarChart from './RadarChart.vue';

/* global layer */
export default {
  props: {
    data: Array,
    "tableName":{
      type:String,
      default:''
    },
    lines:{
      type:Number
    },
  },
components:{
  LineChart,
  RadarChart
},
  data() {
    return {
      columns: [],
      currentPage: 1,
      pageSize: 10, // 每页固定 10 条
      totalItems: 0,
      totalPages: 0,
      hover: -1, // 高亮行索引
      selectedRows: [], // 存储选中的行
      jumpPage: 1, // 跳转页码输入框
      showAddDialog: false, // 是否显示添加弹框
      showEditDialog: false, // 是否显示编辑弹框
      editRow: {}, // 编辑行数据
      searchQuery: "", // 搜索关键词
      originalData: [], // 存储原始数据
      showChartDialog: false, // 控制图表弹框显示
      chartComponent: null, // 当前加载的图表组件
      chartLabels: [], // 图表横轴或雷达图标签
      chartData: [], // 图表数据
      chartTitle: "", // 图表标题
      row:{

      },

      union:"姓名",
      

    };
  },
  computed: {
    pagedData() {
     
      return this.data
    },
    allRowsSelected() {
      return (
        this.selectedRows.length === this.pagedData.length && this.pagedData.length > 0
      );
    },
  },
  watch: {
    data(newData) {
      if (newData.length) {
        this.columns = Object.keys(newData[0]);
        this.totalItems = this.lines;
        this.totalPages = Math.ceil(this.totalItems / this.pageSize);
        if (!this.originalData.length) {
          this.originalData = [...newData];
        }
      }
    },
  },
  methods: {
    async getData(start){

      let data_revise=null

      if(this.mode!="search"){
        await request.post("getfile/select",
          {
            start:start,
            size:"10",
            tableName:this.tableName
          }
        ).then(res=>{
            layer.msg('成功', {icon: 1});
          
            data_revise=res
          })
          .catch(res=>{
            layer.msg('失败', {icon: 2});
          })
          

          if(data_revise!=null)
          //  this.$emit("select2",data_revise)
           this.$emit("select4",data_revise.data.data,data_revise.data.lines[0]["count(*)"],this.tableName)
      }
      else{
        this.searchData()
      }
      
          // eslint-disable-next-line no-debugger
      
    },
    generateLineChart(row) {
      const labels = this.columns;
      const data = labels.map((col) => row[col]);
      const nameFieldIndex = labels.findIndex((col) => col.includes("姓名"));
    let chartTitle = "折线图"; 
    if (nameFieldIndex !== -1) {
      const name = row[labels[nameFieldIndex]]; 
      chartTitle = `${name} 的折线图`;
    }

    if (confirm("确定要查看折线图吗？")) {
      this.chartLabels = labels;
      this.chartData = data;
      this.chartComponent = "LineChart";
      this.chartTitle = chartTitle;
      this.showChartDialog = true;
    }
    },
    generateRadarChart(row) {
      const labels = this.columns;
      const data = labels.map((col) => row[col]);

      const nameFieldIndex = labels.findIndex((col) => col.includes("姓名"));
    
    let chartTitle = "雷达图";
    if (nameFieldIndex !== -1) {
      const name = row[labels[nameFieldIndex]];
      chartTitle = `${name} 的雷达图`;
    }

    if (confirm("确定要查看雷达图吗？")) {
      this.chartLabels = labels;
      this.chartData = data;
      this.chartComponent = "RadarChart";
      this.chartTitle = chartTitle;
      this.showChartDialog = true;
    }
    },
    closeChartDialog() {
      this.showChartDialog = false;
    },
    
    
    openAddDialog() {
      this.editRow = this.columns.reduce((acc, col) => ({ ...acc, [col]: "" }), {});
      this.showAddDialog = true;
      
    },
    openEditDialog(row) {
      this.editRow = { ...row };
      this.showEditDialog = true;
    },
    closeDialog() {
      this.showAddDialog = false;
      this.showEditDialog = false;
    },
    addRow() {
      request.post("getfile/insert",{
        data:this.editRow,
        tableName:this.tableName
      })
      .then(res=>{
        layer.msg('成功', {icon: 1});
        this.changePage(this.currentPage)
      })
      .catch(res=>{
        layer.msg('失败', {icon: 2});
      })


      const newData = [...this.data, { ...this.editRow }];
      this.$emit("update-data", newData);
      this.totalItems++;
      this.updateTotalPages();
      this.currentPage = this.totalPages;
      this.closeDialog();
    },
    saveRowChanges() {

      request.post("getfile/update",{
        data:this.editRow,
        tableName:this.tableName,
        union:this.union
      })
      .then(res=>{
        layer.msg('成功', {icon: 1});
        this.changePage(this.currentPage)
      })
      .catch(res=>{
        layer.msg('失败', {icon: 2});
      })

  // 确保每行都有唯一标识符（如 id）以便准确定位
  const rowIndex = this.data.findIndex((row) => row.id === this.editRow.id);
  if (rowIndex > -1) {
    // 更新数据行
    this.$emit("update-data", [
      ...this.data.slice(0, rowIndex),
      this.editRow,
      ...this.data.slice(rowIndex + 1),
    ]);
  } else {
    alert("未找到要修改的行！");
  }
  this.closeDialog();
},

    deleteSelectedRows() {
      request.post("getfile/delete",{
        data:this.selectedRows,
        tableName:this.tableName,
        union:this.union
      })
      .then(res=>{
        layer.msg('成功', {icon: 1});
        this.$emit("select3");
      })
      .catch(res=>{
        layer.msg('失败', {icon: 2});
      })


      // const newData = this.data.filter((row) => !this.selectedRows.includes(row));
      // this.$emit("update-data", newData);

      this.selectedRows = [];
      // this.totalItems = newData.length;
      // this.updateTotalPages();
    },
    searchData() {
      const lowerQuery = this.searchQuery.toLowerCase();
      // const filteredData = this.originalData.filter((row) =>
      //   this.columns.some((col) =>
      //     String(row[col]).toLowerCase().includes(lowerQuery)
      //   )
      // );
      // if (filteredData.length > 0) {
      //   this.$emit("update-data", filteredData);
      //   this.currentPage = 1;
      // } else {
      //   alert("未找到相关内容！");
      // }


      request.post("getfile/selectByWhere",
        {
          tableName:this.tableName,
          where:lowerQuery
        }
      ).then(res=>{
        layer.msg('成功', {icon: 1});
        let len=res.data.length+1
        if(this.currentPage>=Math.ceil(this.totalItems / this.pageSize)){
          this.currentPage=1
        }  
        if(len==1){
          layer.msg('未找到内容', {icon: 1});
          return
        }

        let tempdata=[]
        for(let p=(this.currentPage-1)* this.pageSize;p<(len-1)&&p<this.currentPage*this.pageSize;p++){
          tempdata.push(res.data[p])
        }

        this.mode="search"
        if(lowerQuery=="")
          this.mode=""

        this.$emit("select4",tempdata,len,this.tableName)
      })
      .catch(res=>{
        layer.msg('失败', {icon: 2});
      })


    },
    changePage(page) {
      this.currentPage = page;
      this.jumpPage=page;

      const start = (this.currentPage - 1) * this.pageSize;

      this.getData(start)
    },
    jumpToPage() {
      if (this.jumpPage >= 1 && this.jumpPage <= this.totalPages) {
        this.currentPage = this.jumpPage;
      } else {
        alert(`请输入 1 到 ${this.totalPages} 之间的页码`);
        return
      }

      this.changePage(this.jumpPage)
      
    },
    toggleRowSelection(row) {
      const index = this.selectedRows.indexOf(row);
      if (index === -1) {
        this.selectedRows.push(row);
      } else {
        this.selectedRows.splice(index, 1);
      }
    },
    toggleAllRowsSelection(event) {
      if (event.target.checked) {
        this.selectedRows = this.pagedData.map(data=>data[this.union])
      } else {
        this.selectedRows = [];
      }
    },
    updateTotalPages() {
      this.totalPages = Math.ceil(this.totalItems / this.pageSize);
      if (this.currentPage > this.totalPages) {
        this.currentPage = this.totalPages;
      }
    },
  },
};
</script>

<style >
*{
    font-family: Arial, sans-serif;
}
.table-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}
.search-box {
  display: flex;
  align-items: center;
}
.search-box input {
  margin-right: 10px;
}
.dialog-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}
.dialog {
  background: white;
  padding: 20px;
  border-radius: 10px;
  width: 400px;
  max-width: 100%;
}
.input-group {
  margin-bottom: 15px;
}
.input-group label {
  display: block;
  margin-bottom: 5px;
}
.input-group input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
.dialog-actions {
  text-align: right;
}
.dialog-actions button {
  margin-left: 10px;
}
.btn-success {
  background-color: #a3a0e4;
  font-family: Arial, sans-serif;
  color: white;
  border-color: #a3a0e4;
  
  margin-bottom: 5px;
}
.btn-warning {
  background-color: #7ec9e0;
  border-color: #7ec9e0;
 
  color: white;
  font-family: Arial, sans-serif;
}
.dialog-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* 半透明背景 */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.dialog {
  background: #fff;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  width: 80%; /* 宽度改为80% */
  max-width: 1200px; /* 最大宽度限制 */
  height: 80%; /* 高度改为80% */
  overflow-y: auto; /* 若内容过多，允许滚动 */
}

.dialog h3 {
  margin-bottom: 20px;
  font-size: 1.5rem;
  text-align: center;
}

.dialog-actions {
  display: flex;
  justify-content: flex-end;
  margin-top: 20px;
}

.dialog-actions button {
  margin-left: 10px;
}
#update{
  background-color: #c783b6;
  border: 1px solid #c783b6;
  color: white;
}
#select{
  background-color: #c0f5df;
  background-color: #c783b6;
  border: 1px solid #c783b6;
  color: white;
}
</style>


<style scoped>
*{
    font-family: Arial, sans-serif;
}
.table-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}
.search-box {
  display: flex;
  align-items: center;
}
.search-box input {
  margin-right: 10px;
}
.dialog-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}
.dialog {
  background: white;
  padding: 20px;
  border-radius: 10px;
  width: 400px;
  max-width: 100%;
}
.input-group {
  margin-bottom: 15px;
}
.input-group label {
  display: block;
  margin-bottom: 5px;
}
.input-group input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
.dialog-actions {
  text-align: right;
}
.dialog-actions button {
  margin-left: 10px;
}
.btn-success {
  background-color: #a3a0e4;
  font-family: Arial, sans-serif;
  color: white;
  border-color: #a3a0e4;
  
  margin-bottom: 5px;
}
.btn-warning {
  background-color: #7ec9e0;
  border-color: #7ec9e0;
 
  color: white;
  font-family: Arial, sans-serif;
}
.dialog-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* 半透明背景 */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.dialog {
  background: #fff;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  width: 80%; /* 宽度改为80% */
  max-width: 1200px; /* 最大宽度限制 */
  height: 80%; /* 高度改为80% */
  overflow-y: auto; /* 若内容过多，允许滚动 */
}

.dialog h3 {
  margin-bottom: 20px;
  font-size: 1.5rem;
  text-align: center;
}

.dialog-actions {
  display: flex;
  justify-content: flex-end;
  margin-top: 20px;
}

.dialog-actions button {
  margin-left: 10px;
}
#update{
  background-color: #c783b6;
  border: 1px solid #c783b6;
  color: white;
}
#select{
  background-color: #c0f5df;
  background-color: #c783b6;
  border: 1px solid #c783b6;
  color: white;
}
</style>
