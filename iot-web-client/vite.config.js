import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  build: { // WARNING: Vite does not take base URLs into account. Must modify the index.html file in outDir to set 'assets' as relative path
    outDir: "E:\\Serveurs\\nginx-1.17.2\\html\\iot-web-client",
    emptyOutDir: true
  }
})
