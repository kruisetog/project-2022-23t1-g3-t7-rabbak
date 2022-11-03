import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import {Amplify, Storage} from 'aws-amplify';
import process from 'process';
import dotenv from 'dotenv';

dotenv.config()
Amplify.configure({
    Auth: {
        identityPoolId: process.env.VUE_APP_IDENTITYPOOLID,
        region: process.envenv.VUE_APP_REGION
    },
    Storage: {
        AWSS3: {
            bucket: process.envenv.VUE_APP_BUCKETNAME, 
            region: process.envenv.VUE_APP_BUCKETREGION
        }
    }
});

const app = createApp(App);

app.use(router);

app.mount("#app");
