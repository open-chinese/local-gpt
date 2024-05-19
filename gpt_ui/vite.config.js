import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
//   devServer: {
//     proxy: {
//       'api': {
//         target: 'http://localhost:5050',
//         changeOrigin: true,
//         pathRewrite: {
//           '^/gpt': '/'
//         }
//       }
//     },
//     port: 5050
//     // allowedHosts: [
//     //   'host.com',
//     //   'subdomain.host.com',
//     //   'subdomain2.host.com',
//     //   'host2.com',
//     // ]
// }
})

