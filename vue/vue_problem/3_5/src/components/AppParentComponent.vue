<template>
  <div>
    <h2>App Parent</h2>
    <input type="text" v-model="parentData" @input="onChildInputChange">
    <p>appData: {{ appData }}</p>
    <p>childData: {{ childData }}</p>
    <AppChildComponent :app-data="appData" :parent-data="parentData" @child-input-change="fromChildInputChange"/>
  </div>
</template>

<script>
import AppChildComponent from './AppChildComponent.vue'
export default {
    name: 'AppParentComponent',
    components: {
        AppChildComponent
    },
    props: {
        appData: String
    },
    data() {
        return {
            parentData: '',
            childData: '',
        }
    },
    methods: {
        fromChildInputChange(childInputData) {
            this.childData = childInputData
            this.$emit('child-input-change', childInputData)
        },
        onChildInputChange(event) {
            this.$emit('parent-input-change', event.target.value)
        }
    }

}
</script>

<style scoped>
.box {
    border: red;
}
</style>