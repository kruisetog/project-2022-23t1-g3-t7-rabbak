<script>
export default {
    methods: {
        logout(){
            this.$router.push({ name: 'logOut', params: { logout: 'logout' } })
        }
    }
};
</script>

<template>
    <main class="nav-bar">
        <div class="nav">
            <a class="logo">
                <img src='./../assets/logo2.png' />
            </a>
            <ul>
                <li>
                    <RouterLink to="/activity">
                        <span>
                            <i class="icon-home primary font-large-2"></i>
                        </span>
                        <a>My Points activity</a>
                    </RouterLink>
                </li>
                <!-- <li>
                    <RouterLink to="/cards">
                        <span>
                            <i class="icon-credit-card primary font-large-2"></i>
                        </span>
                        <a>My Cards</a>
                    </RouterLink>
                </li> -->
                <li>
                    <RouterLink to="/settings">
                    <span>
                        <i class="icon-gear primary font-large-2"></i>
                    </span>
                    <a>Settings</a>
                    </RouterLink>
                </li>
                <li @click="logout">
                    <span>
                        <i class="icon-signout primary font-large-2"></i>
                    </span>
                    <a>Log Out</a>
                </li>
            </ul>
        </div>
    </main>
</template>

<style scoped>
.nav-bar {
    padding: 3px;
    position: fixed;
    height: 100vh;
    max-width: 130px;
}

.logo {
    padding: 15px;
    padding-top: 15px;
    margin-top: 15px;
    cursor: pointer;
}

.logo img {
    text-align: center;
}

.nav {
    text-align: center;
}


.nav ul li {
    list-style: none;
    text-align: center;
    cursor: pointer;
    padding: 10px;
}

ul{
    padding-left:inherit
}

.nav ul li span {
    display: block;
    color: #aaa;
    font-size: 24px;
}

.nav ul li a {
    display: block;
    font-weight: 600;
    font-size: 14px;
    color: #333;
}

.selected {
    border-left: 3px solid #2d87bf;
    background-color: #eee;
}

.selected span {
    color: #2d87bf !important;
}

a:hover{
    text-decoration: none;
}
</style>