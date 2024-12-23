const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true
// })
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave:false,
  devServer: {
    host: '0.0.0.0'
    },
//主要是这部分
  devServer: {
    proxy: {
        '/api': {
            //对应的接口前缀，填入你对应的前缀，后面搭建Flask时会说明
            target: 'http://10.10.116.90:8000',//这里填入你要请求的接口的前缀
            ws:true,//代理websocked
            changeOrigin:true,//虚拟的站点需要更管origin
            secure: false,                   //是否https接口
            pathRewrite:{
                '^/api':''//重写路径
            }
        }
    }
}
 
 
})

