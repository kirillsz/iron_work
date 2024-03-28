const { defineConfig } = require('@vue/cli-service')

const path = require('path');
module.exports = defineConfig({
    transpileDependencies: true,

    devServer: {
      allowedHosts: [
         '1001-ad.ru',
         'k701.ru',
       ]
    },

    configureWebpack: {
      resolve: {
         alias: {
            src: path.resolve(__dirname, 'src')
         }
      }
    }
})
