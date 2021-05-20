import Vue from 'vue'

import {
    Layout, Col,
    Row, Menu,
    Form, Input,
    Icon, Checkbox,
    Button, Result,
    Table, Tag,
    Divider, Dropdown, Select,
} from 'ant-design-vue'
import axios from "axios";
import VueAxios from "vue-axios";

Vue.use(VueAxios, axios);


Vue.use(Layout);
Vue.use(Col);
Vue.use(Row);
Vue.use(Form);
Vue.use(Input);
Vue.use(Select);
Vue.use(Icon);
Vue.use(Checkbox);
Vue.use(Button);
Vue.use(Result);
Vue.use(Menu);
Vue.use(Table);
Vue.use(Tag);
Vue.use(Divider)
Vue.use(Dropdown)

import Nav from '@/views/dashboard/nav';
import Dashboard from '@/views/dashboard/index';
// import Login from '@/views/user/login';

const routes = [
    {
        key: '1',
        path: '/',
        title: 'Dashboard',
        icon: 'home',
        component: Nav,
        redirect: '/dashboard',
        children: [
            {
                key: '1.1',
                path: '/dashboard',
                title: 'Host',
                icon: 'cloud-server',
                component: Dashboard,
                hidden: true,
            },
        ]
    },
    {
        key: '2',
        path: '/cmdb',
        title: 'Machine',
        icon: 'cloud-server',
        component: Nav,
        children: [
            {
                key: '2.1',
                path: '/cmdb/host',
                title: 'Host',
                component: () => import(/* webpackChunkName: "cmdb" */ '@/views/cmdb/host'),
            },
            {
                key: '2.2',
                path: '/cmdb/exec',
                title: 'Exec',
                component: () => import(/* webpackChunkName: "cmdb" */ '@/views/cmdb/exec'),
            },
        ]
    },
    {
        key: '3',
        path: '/hr',
        title: 'HR',
        icon: 'user',
        component: Nav,
        children: [
            {
                key: '3.1',
                path: '/hr/list',
                title: 'Employee',
                component: () => import(/* webpackChunkName: "hr" */ '@/views/hr/list'),
            },
            {
                key: '3.2',
                path: '/hr/ignore',
                title: 'Ignore',
                component: () => import(/* webpackChunkName: "hr" */ '@/views/hr/ignore'),
            },
            {
                key: '3.3',
                path: '/hr/trend',
                title: 'Trend',
                component: () => import(/* webpackChunkName: "hr" */ '@/views/hr/trend'),
            },
        ]
    },
    // {
    //     path: '/',
    //     // component: () => import(/* webpackChunkName: "dashboard" */ '@/views/dashboard/index'),
    //     component: Dashboard,
    //     // redirect: '/dashboard/welcome',
    //     children: [
    //         {
    //             path: '/dashboard',
    //             redirect: '/user/login'
    //         },
    //         {
    //             path: '/cmdb',
    //             // component: () => import(/* webpackChunkName: "dashboard" */ '@/views/cmdb/host')
    //             component: Host,
    //         },
    //         {
    //             path: '/exception',
    //             name: 'exception',
    //             redirect: '/exception/403',
    //             meta: {title: '异常页', icon: 'warning'},
    //             children: [
    //                 {
    //                     path: '/exception/403',
    //                     name: 'Exception403',
    //                     component: () => import(/* webpackChunkName: "fail" */ '@/views/exception/403'),
    //                     meta: {title: '403'}
    //                 },
    //                 {
    //                     path: '/exception/404',
    //                     name: 'Exception404',
    //                     component: () => import(/* webpackChunkName: "fail" */ '@/views/exception/404'),
    //                     meta: {title: '404'}
    //                 },
    //                 {
    //                     path: '/exception/500',
    //                     name: 'Exception500',
    //                     component: () => import(/* webpackChunkName: "fail" */ '@/views/exception/500'),
    //                     meta: {title: '500'}
    //                 }
    //             ]
    //         },
    //     ]
    // },

    // {
    //     path: '/user',
    //     // redirect: '/user/login',
    //     component: Login,
    //     hidden: true,
    //     children: [
    //         {
    //             path: '/user/logout',
    //             redirect: '/login'
    //         },
    //         {
    //             path: '/user/login',
    //             component: Login,
    //             // component: () => import(/* webpackChunkName: "user" */ '@/views/user/login')
    //         },
    //     ]
    // },
]

export default routes
