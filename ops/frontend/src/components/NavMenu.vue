<template>
    <a-menu
            :default-selected-keys="[this.$route.path]"
            :default-open-keys="[this.$route.path.split('/').slice(0,-1).join('/')]"
            mode="inline"
            theme="dark"
            :inline-collapsed="collapsed"
            @click="menuClick"
    >
        <template v-for="item in menu_list" v-if="!item.hidden">
            <a-menu-item v-if="!item.children||item.path==='/'" :key="item.path">
                <a-icon :type="item.icon"></a-icon>
                <span>{{ item.title }}</span>
            </a-menu-item>
            <sub-menu v-else :key="item.path" :menu-info="item"/>
        </template>
    </a-menu>
</template>

<script>
    import {Menu} from 'ant-design-vue'
    const SubMenu = {
        template: `
            <a-sub-menu :key="menuInfo.path" v-bind="$props" v-on="$listeners">
                <span slot="title">
                  <a-icon :type="menuInfo.icon"/><span>{{ menuInfo.title }}</span>
                </span>
                <template v-for="item in menuInfo.children">
                    <a-menu-item v-if="!item.children" :key="item.path">
                        <span>{{ item.title }}</span>
                    </a-menu-item>
                    <sub-menu v-else :key="item.path" :menu-info="item"/>
                </template>
            </a-sub-menu>
        `,
        name: 'SubMenu',
        // must add isSubMenu: true
        isSubMenu: true,
        props: {
            ...Menu.SubMenu.props,
            // Cannot overlap with properties within Menu.SubMenu.props
            menuInfo: {
                type: Object,
                default: () => ({}),
            },
        },
    };
    import routes from "@/router";

    export default {
        name: "NavMenu",
        props: ['navMenus'],
        data() {
            return {
                menu_list: routes,
            }
        },
        methods: {
            menuClick({item, key, keyPath}) {
                // 获取到当前的key,并且跳转
                console.log(key,keyPath);
                this.$router.push({
                    path: key
                })
            },
        },
        components: {
            'sub-menu': SubMenu,
        },
    }
</script>

<style scoped>

</style>