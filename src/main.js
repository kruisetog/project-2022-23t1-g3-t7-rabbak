import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import {Amplify, Storage} from 'aws-amplify';

Amplify.configure({
    Auth: {
        identityPoolId: process.env.IDENTITYPOOLID, 
        region: process.env.REGION,
    },
    Storage: {
        AWSS3: {
            bucket: process.env.BUCKETNAME, 
            region: process.env.REGION, 
        }
    }
});

const app = createApp(App);

app.use(router);

app.mount("#app");
