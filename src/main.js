import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import {Amplify, Storage} from 'aws-amplify';
import { env } from 'process';


Amplify.configure({
    Auth: {
        identityPoolId: env.VUE_APP_IDENTITYPOOLID,
        region: env.VUE_APP_REGION
    },
    Storage: {
        AWSS3: {
            bucket: env.VUE_APP_BUCKETNAME, 
            region: env.VUE_APP_BUCKETREGION
        }
    }
});

const app = createApp(App);

app.use(router);

app.mount("#app");
