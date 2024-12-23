<template>
    <div class="fileUpload_main">
        <div class="mb-3">
            <label for="formFile" class="form-label">Default file input example</label>
            <input @change="(event) => handelFileChange(event)" class="form-control" type="file" id="formFile">
            <button type="button" class="btn btn-outline-primary" @click="uploadfile">登录</button>
        </div>

    </div>
    <table class="table table-bordered table-hover no-select" id="mytable">
        <thead>
            <tr>
                <th v-for="(k, v) in hello[0]" :key="v" @click="selectcol()">{{ v }}<input type="radio" name="colums1"
                        v-model="getvalue.text" /></th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(v, k) in hello" :key="k">
                <td v-for="(m, n) in v" :key="n" id="cell" @click="clickcolor()">
                    {{ m }}
                </td>
            </tr>
        </tbody>
    </table>
    <button @click="avgclick()">点击</button>
    <input type="text" v-model="sqldict.text">
    <button type="button" class="btn btn-outline-primary" @mousedown="selectfunction()">查询</button>
</template>
<script>
import axios from 'axios';
import Decimal from 'decimal.js'; 
export default {
    name: "fileUpload",
    data() {
        return {
            fileValue: "",
            hello: {},
            getvalue: {
                text: ''
            },
            sqldict: {
                text: ''
            },
        }
    },

    methods: {
        selectcol() {
            let table = document.getElementById('mytable')
            table.addEventListener('click', (event) => {
                if (event.target && event.target.nodeName === 'TH') {
                    for (let i = 0; i < table.rows.length; i++) {
                        let row = table.rows[i];

                        // 遍历当前行的每一个单元格
                        for (let j = 0; j < row.cells.length; j++) {
                            let cell = row.cells[j];
                            cell.classList.remove('selected-cell')
                            // 在这里可以对单元格进行操作，例如打印出单元格的文本内容
                        }
                    }
                    let th = event.target
                    let tr = th.parentElement
                    const cellText = event.target.textContent || event.target.innerText;
                    var colIndex = Array.prototype.indexOf.call(tr.children, th);
                    console.log(colIndex)
                    // console.log(table.)
                    var avgnum = Decimal(0)
                    for (let i = 1; i < table.rows.length; i++) {
                        table.rows[i].cells[colIndex].classList.add('selected-cell')
                        avgnum=avgnum.plus(Decimal(Number(Number(table.rows[i].cells[colIndex].innerText).toFixed(2))))

                    }
                    console.log(avgnum)
                    console.log(table.rows.length)
                    console.log(avgnum.dividedBy(Decimal(table.rows.length-1)).toString())
                }
            })
        },
        selectfunction() {
            axios.post('http://10.10.116.90:5000/selectsql', this.sqldict)
                .then(res => {
                    console.log(res.data)
                })
        },
        clickcolor() {
            let table = document.getElementById('mytable')
            table.addEventListener('mousedown', (event) => {
                var td = event.target
                var tr = td.parentElement;
                if (event.target && event.target.nodeName === 'TD') {
                    // 获取td的文本内容
                    const cellText = event.target.textContent || event.target.innerText;
                    event.target.classList.add('selected-cell')
                    table.addEventListener('mousemove', (event) => {
                        event.target.classList.add('selected-cell')


                        // 获取tr在table中的所有兄弟tr元素，并找到tr的索引（行号，从0开始）
                        var rowIndex = Array.prototype.indexOf.call(tr.parentElement.children, tr);

                        // 获取td在其父tr中的索引（列号，从0开始）
                        var colIndex = Array.prototype.indexOf.call(tr.children, td);

                        // 输出行号和列号
                        console.log('Row Index:', rowIndex);
                        console.log('Column Index:', colIndex);

                    })
                    table.addEventListener('mouseup', (event) => {
                        event.target.classList.remove('selected-cell')
                    })
                    var rowIndex = Array.prototype.indexOf.call(tr.parentElement.children, tr);

                    // 获取td在其父tr中的索引（列号，从0开始）
                    var colIndex = Array.prototype.indexOf.call(tr.children, td);
                    console.log('Row Index:', rowIndex);
                    console.log('Column Index:', colIndex);
                    console.log(event.target)
                    // 显示td的文本内容
                    console.log(cellText)
                }
            });
        },
        handelFileChange(e) {
            this.fileValue = e.target.files[0]
            console.log(e.target.files)
        },
        avgclick() {
            console.log(this.getvalue)
            axios.post('http://10.11.241.157:5000/avgmethod', this.getvalue)
                .then(res => {
                    console.log(res.data)
                })
        },
        async uploadfile() {
            if (!this.fileValue) {
                alert("Please select a file first")
                return
            }



            try {
                const formData = new FormData();
                formData.append('file', this.fileValue)


                await axios.post('api/getfile',
                    formData,
                    { headers: { 'content-Type': 'multipart/form-data' } }
                ).then(res => {
                    this.hello = res.data
                    //console.log(res.data)
                    // console.log(this.hello.length)
                })
                    .catch(res => {
                        console.log(res)
                    })


            }
            catch (error) {
                console.log(error)
            }
        }
    },
    
}


</script>
<style>
td {
    cursor: pointer;
}

.selected-cell {
    background-color: #007bff !important;
    /* 使用Bootstrap的蓝色主题 */
    color: white !important;
    /* 白色文本以提高可读性 */
}

.no-select {
    user-select: none;
    /* 标准语法 */
    -webkit-user-select: none;
    /* Chrome/Safari/Opera */
    -moz-user-select: none;
    /* Firefox */
    -ms-user-select: none;
    /* Internet Explorer/Edge */
}
</style>