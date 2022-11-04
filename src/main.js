import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import {Amplify, Storage} from 'aws-amplify';


Amplify.configure({
    Auth: {
        identityPoolId: process.env.VUE_APP_IDENTITYPOOLID,
        region: process.env.VUE_APP_REGION
    },
    Storage: {
        AWSS3: {
            bucket: process.env.VUE_APP_BUCKETNAME, 
            region: process.env.VUE_APP_BUCKETREGION
        }
    }
});

const app = createApp(App);

app.use(router);

app.mount("#app");
