<template>
  <div>
    <h2>App</h2>
    <input type="text" v-model="appData">
    <p>parentData: {{ parentData }} </p>
    <p>childData: {{ childData }}</p>

    <AppParentComponent :app-data="appData" @parent-input-change="fromParentInputChange" @child-input-change="fromChildInputChange"/>

  </div>
</template>

<script>
import AppParentComponent from './AppParentComponent.vue'
export default {
    name: 'AppComponent',
    components: {
        AppParentComponent
    },

    data() {
        return {
            appData: '',
            parentData: '',
            childData: '',
        }
    },
    methods: {
        fromParentInputChange(parentData) {
            this.parentData = parentData
        },
        fromChildInputChange(childData) {
            this.childData = childData
        }
    }
}
</script>

<style>

</style>