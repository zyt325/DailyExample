<template>
    <div id="cmdb_list">
        <a-table
                :columns="columns"
                :row-key="record => record.id"
                :data-source="data"
                :pagination="pagination"
                :loading="loading"
                @change="handleHRChange">
            <span slot="action" slot-scope="text" class="table-action">
                <a>ssh</a>
            </span>
        </a-table>
    </div>

</template>
<style scoped>
    #cmdb_list {
        height: 100%;
    }

    #cmdb_list_search {
        /*float: right;*/
        /*right: 0px;*/
        padding-bottom: 5px;
    }
</style>
<script>
    const columns = [
        {
            title: 'Name',
            dataIndex: 'name',
            key: 'name',
            fixed: 'left',
            sorter: true,
        },
        {
            title: 'Hostname',
            dataIndex: 'hostname',
            key: 'hostname',
            sorter: true,
        },
        {
            title: 'Virtual',
            dataIndex: 'virtual',
            key: 'virtual',
            sorter: true,
        },
        {
            title: 'Action',
            key: 'action',
            scopedSlots: {customRender: 'action'}
        },
    ];

    export default {
        data() {
            return {
                data: [],
                pagination: {},
                loading: false,
                columns,
                order: '',
            };
        },
        mounted() {
            this.fetch({ordering: 'username'});
        },
        methods: {
            handleHRChange(pagination, filters, sorter) {
                // console.log(pagination);
                // console.log(filters);
                // console.log(sorter);
                const pager = {...this.pagination};
                pager.current = pagination.current;
                if (sorter.order === 'descend') {
                    this.order = '-' + sorter.field;
                } else {
                    this.order = sorter.field;
                }
                this.pagination = pager;
                this.fetch({
                    limit: pagination.pageSize,
                    offset: pagination.pageSize * (pagination.current - 1),
                    ordering: this.order,
                });
            },
            handlerSearch(value) {
                // console.log(value);
                if (value) {
                    this.fetch({
                        search: value,
                    });
                } else {
                    this.fetch()
                }

            },
            fetch(params = {}) {
                var _this = this;
                this.loading = true;
                _this.axios
                    .get("/api/v1/cmdb_host/", {
                        params: {
                            limit: 10,
                            offset: 0,
                            ...params,
                        },
                        headers: {
                            Authorization: "Token e1a0dbd73bc29e82883ea3bb7e5bf35d9e19b516"
                        }
                    })
                    .then(function (res) {
                        const pagination = {..._this.pagination};
                        pagination.total = res.data.count;
                        pagination.showSizeChanger = true;
                        pagination.showQuickJumper = true;
                        pagination.hideOnSinglePage = true;
                        pagination.pageSizeOptions = ['10', '15', '20', '40', '50'];
                        _this.loading = false;
                        _this.data = res.data.results;
                        _this.pagination = pagination;
                        // console.log(_this.pagination);
                    });
            }
        }
    };
</script>
