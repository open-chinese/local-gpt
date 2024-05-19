import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(router)

// app.use(cors());

// Or enable CORS selectively
// app.use('/api', cors(), (req, res) => {
//   res.json({msg: 'This is CORS-enabled for all origins!'});
// });

app.mount('#app')
