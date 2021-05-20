import Vue from 'vue';
import App from './App.vue'
import VueRouter from 'vue-router'
import routes from './router';

Vue.config.productionTip = false;
Vue.use(VueRouter)

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
    return originalPush.call(this, location).catch(err => err)
}

const router = new VueRouter({
    mode: 'history',
    routes,
})


new Vue({
    router,
    render: h => h(App)
}).$mount('#app');
