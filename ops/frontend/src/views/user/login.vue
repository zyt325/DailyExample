<template>
    <div class="login_container">
        <a-row class="login_logo"></a-row>
        <a-row class="login_content">
            <a-col :span="8">
            </a-col>
            <a-col :span="8">
                <a-form
                        id="components-form-demo-normal-login"
                        :form="form"
                        class="login-form"
                        @submit="handleSubmit"
                >
                    <a-form-item>
                        <a-input
                                v-decorator="[
                                'userName',
                                { rules: [{ required: true, message: 'Please input your username!' }] },
                            ]"
                                placeholder="Username"
                        >
                            <a-icon slot="prefix" type="user" style="color: rgba(0,0,0,.25)"/>
                        </a-input>
                    </a-form-item>
                    <a-form-item>
                        <a-input
                                v-decorator="[
                                'password',
                                { rules: [{ required: true, message: 'Please input your Password!' }] },
                            ]"
                                type="password"
                                placeholder="Password"
                        >
                            <a-icon slot="prefix" type="lock" style="color: rgba(0,0,0,.25)"/>
                        </a-input>
                    </a-form-item>
                    <a-form-item>
                        <a-checkbox
                                v-decorator="[
                                'remember',
                                {
                                valuePropName: 'checked',
                                initialValue: false,
                                },
                            ]"
                        >
                            Remember me
                        </a-checkbox>
                        <a class="login-form-forgot" href="">
                            Forgot password
                        </a>
                        <a-button type="primary" html-type="submit" class="login-form-button">
                            Log in
                        </a-button>
                        Or
                        <a href="">
                            register now!
                        </a>
                    </a-form-item>
                </a-form>
            </a-col>
            <a-col :span="8">
            </a-col>

        </a-row>
        <a-row class="login_footer"></a-row>
    </div>
</template>
<script>
    export default {
        beforeCreate() {
            this.form = this.$form.createForm(this, {name: 'normal_login'});
        },
        methods: {
            handleSubmit(e) {
                e.preventDefault();
                this.form.validateFields((err, values) => {
                    if (!err) {
                        console.log('Received values of form: ', values);
                    }
                });
            },
        },
    };
</script>
<style>
    #components-form-demo-normal-login .login-form {
        max-width: 300px;
    }

    #components-form-demo-normal-login .login-form-forgot {
        float: right;
    }

    #components-form-demo-normal-login .login-form-button {
        width: 100%;
    }

    .login_logo {
        padding-top: 70px;
    }

    .login_footer {
        padding-bottom: 70px;
    }
</style>