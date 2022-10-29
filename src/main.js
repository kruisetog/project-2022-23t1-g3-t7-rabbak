import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import {Amplify, Storage} from 'aws-amplify';

Amplify.configure({
    Auth: {
        identityPoolId: 'us-east-1:a914bc24-32e4-412e-89fc-e16d34322aa8', //REQUIRED - Amazon Cognito Identity Pool ID
        region: 'us-east-1', // REQUIRED - Amazon Cognito Region
    },
    Storage: {
        AWSS3: {
            bucket: 'batchuploadbucket', 
            region: 'us-east-1', 
        }
    }
});

const app = createApp(App);

app.use(router);

app.mount("#app");
