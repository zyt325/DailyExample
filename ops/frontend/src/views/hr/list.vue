<template>
  <div id="hr_list">
    <div id="hr_list_search">
      <a-select
        style="width: 120px"
        mode="multiple"
        label-in-value
        :value="category"
        placeholder="Select Category"
        @change="getColume"
      >
      </a-select>
      <a-select
        style="width: 80px"
        mode="multiple"
        placeholder="Select Status"
        option-label-prop="label"
      >
        <a-select-option value="Active" label="Active">
          Active
        </a-select-option>
      </a-select>
      <a-select
        style="width: 80px"
        label-in-value
        :value="dep"
        placeholder="Select Dep"
        :filter-option="false"
        @focus="fetchDep"
        @change="handlerDep"
      >
        <a-select-option v-for="dep in deps" :key="dep.code">
          {{ dep.code }}
        </a-select-option>
      </a-select>
      <a-select
        style="width: 80px"
        label-in-value
        :value="office"
        placeholder="Select Office"
        :filter-option="false"
        @focus="fetchOffice"
        @change="handlerOffice"
      >
        <a-select-option v-for="o in Office" :key="o.code">
          {{ o.code }}
        </a-select-option>
      </a-select>

      <a-input-search
        style="width: 200px"
        placeholder="input search text"
        enter-button
        @search="handlerSearch"
      />
    </div>
    <a-table
      :scroll="{ x: 1800 }"
      :columns="columns"
      :row-key="(record) => record.id"
      :data-source="data"
      :pagination="pagination"
      :loading="loading"
      @change="handleHRChange"
    >
      <span slot="seatmap" slot-scope="text, record">
        <a
          :href="
            'https://seatmap.base-fx.com/index.php/employee/employee_edit/employee_id/' +
            record.id +
            '.html'
          "
          width="79px"
          height="105px"
          target="_blank"
        >
          <a-icon type="environment" />
        </a>
      </span>
      <span slot="Pic" slot-scope="text, record">
        <a
          :href="
            'https://hr.base-fx.com/index.php/api/staffPhoto/username/' +
            record.username
          "
          target="_blank"
        >
          <img
            :src="
              'https://hr.base-fx.com/index.php/api/staffPhoto/username/' +
              record.username
            "
            width="75px"
            height="105px"
            :alt="record.username"
          />
        </a>
      </span>
      <span slot="action" slot-scope="text, record">
        <a-dropdown :trigger="['click']">
          <a class="ant-dropdown-link" @click="(e) => e.preventDefault()">
            More<a-icon type="down" />
          </a>
          <a-menu slot="overlay" @click="hr_action">
            <a-menu-item key="check"> check </a-menu-item>
            <a-menu-item key="unlock"> unlock </a-menu-item>
            <a-menu-item key="enable"> enable </a-menu-item>
            <a-menu-item key="disable"> disable </a-menu-item>
          </a-menu>
        </a-dropdown>
      </span>
    </a-table>
  </div>
</template>
<style scoped>
#hr_list {
  height: 100%;
}

#hr_list_search {
  /*float: right;*/
  /*right: 0px;*/
  padding-bottom: 5px;
}

#hr_list_search .ant-select {
  margin-right: 5px;
}
</style>
<script>
const columns = [
  {
    title: "UserName",
    dataIndex: "username",
    key: "username",
    fixed: "left",
    sorter: true,
  },
  {
    title: "Seat",
    key: "Seat",
    width: "66px",
    scopedSlots: { customRender: "seatmap" },
  },
  {
    title: "Pic",
    key: "Pic",
    width: "120px",
    scopedSlots: { customRender: "Pic" },
  },
  {
    title: "Category",
    dataIndex: "category",
    key: "category",
    width: "110px",
    sorter: true,
  },
  {
    title: "Status",
    dataIndex: "status",
    key: "status",
    width: "100px",
    sorter: true,
  },
  {
    title: "Chinese_Name",
    dataIndex: "chinese_full_name",
    key: "chinese_full_name",
  },
  {
    title: "English_Name",
    dataIndex: "english_full_name",
    key: "english_full_name",
  },
  {
    title: "Gender",
    dataIndex: "gender",
    key: "gender",
    width: "80px",
  },
  {
    title: "Dep",
    dataIndex: "department_code",
    key: "department_code",
    sorter: true,
    width: "80px",
  },
  {
    title: "Office",
    dataIndex: "office_code",
    key: "office_code",
    sorter: true,
    width: "90px",
  },
  {
    title: "StartDate",
    dataIndex: "start_date",
    key: "start_date",
    width: "120px",
    sorter: true,
  },
  {
    title: "EStartDate",
    dataIndex: "employee_start_date",
    key: "employee_start_date",
    width: "120px",
  },
  {
    title: "EndDate",
    dataIndex: "end_date",
    key: "end_date",
    width: "120px",
    sorter: true,
  },
  {
    title: "Mobile",
    dataIndex: "mobile",
    key: "mobile",
  },
  {
    title: "Action",
    key: "operation",
    fixed: "right",
    width: 100,
    scopedSlots: { customRender: "action" },
  },
];

export default {
  data() {
    return {
      data: [],
      pagination: {},
      loading: false,
      columns,
      order: "",
      category: [],
      status: [],
      dep: "",
      deps: [],
      office: "",
      Office: [],
      search_field: "",
    };
  },
  mounted() {
    this.fetch({ ordering: "username" });
  },
  methods: {
    handleHRChange(pagination, filters, sorter) {
      // console.log(pagination);
      // console.log(filters);
      // console.log(sorter);
      const pager = { ...this.pagination };
      pager.current = pagination.current;
      if (sorter.order === "descend") {
        this.order = "-" + sorter.field;
      } else {
        this.order = sorter.field;
      }
      this.pagination = pager;
      this.fetch({
        limit: pagination.pageSize,
        offset: pagination.pageSize * (pagination.current - 1),
        ordering: this.order,
        department_code: this.dep.key,
        office_code: this.office.key,
      });
    },
    handlerSearch(value) {
      var _this = this;
      // console.log(value);
      if (value) {
        _this.search_field = value;
        this.fetch({
          search: value,
        });
      } else {
        this.fetch();
      }
    },
    fetch(params = {}) {
      var _this = this;
      this.loading = true;
      _this.axios
        .get("/api/v1/hr_people_view_itd/", {
          params: {
            limit: 10,
            offset: 0,
            ...params,
          },
          headers: {
            Authorization: "Token e1a0dbd73bc29e82883ea3bb7e5bf35d9e19b516",
          },
        })
        .then(function (res) {
          const pagination = { ..._this.pagination };
          pagination.total = res.data.count;
          pagination.showSizeChanger = true;
          pagination.showQuickJumper = true;
          pagination.hideOnSinglePage = true;
          pagination.pageSizeOptions = ["10", "15", "20", "40", "50"];
          _this.loading = false;
          _this.data = res.data.results;
          _this.pagination = pagination;
          // console.log(_this.pagination);
        });
    },
    hr_action(e) {
      console.log(e);
      var _this = this;
      _this.axios
        .get("/api/v1/hr_action/", {
          params: {
            action: "check",
            username: "a",
          },
          headers: {
            Authorization: "Token e1a0dbd73bc29e82883ea3bb7e5bf35d9e19b516",
          },
        })
        .then(function (res) {
          _this.res = res.data.results;
          console.log(_this.res);
        });
    },
    fetchDep() {
      var _this = this;
      _this.axios
        .get("/api/v1/hr_department/", {
          headers: {
            Authorization: "Token e1a0dbd73bc29e82883ea3bb7e5bf35d9e19b516",
          },
        })
        .then(function (res) {
          _this.deps = res.data;
          console.log(_this.deps);
        });
    },
    handlerDep(value) {
      this.dep = value;
      this.fetch({
        department_code: value.key,
        office_code: this.office.key,
      });
    },
    fetchOffice() {
      var _this = this;
      _this.axios
        .get("/api/v1/hr_office/", {
          headers: {
            Authorization: "Token e1a0dbd73bc29e82883ea3bb7e5bf35d9e19b516",
          },
        })
        .then(function (res) {
          _this.Office = res.data;
          console.log(_this.Office);
        });
    },
    handlerOffice(value) {
      this.office = value;
      // console.log(value.key);
      this.fetch({
        department_code: this.dep.key,
        office_code: value.key,
      });
    },
  },
};
</script>
