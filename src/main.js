import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import {Amplify, Storage} from 'aws-amplify';
import os from 'os'


Amplify.configure({
    Auth: {
        identityPoolId: os.environ['VUE_APP_IDENTITYPOOLID'],
        region: os.environ['VUE_APP_REGION']
    },
    Storage: {
        AWSS3: {
            bucket: os.environ['VUE_APP_BUCKETNAME'],
            region: os.environ['VUE_APP_BUCKETREGION']
        }
    }
});

const app = createApp(App);

app.use(router);

app.mount("#app");
