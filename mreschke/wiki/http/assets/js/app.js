// Import Vue 3
import { createApp } from "vue";

// Import main application bootstrap
require('./bootstrap');

// Import compoments bootstrap
//require('./components/bootstrap');
import components from "./components/bootstrap";

// Create Vue application with global components
const app = createApp({
    components: components,
});

// Mount Vue application to #app
app.mount("#app");
