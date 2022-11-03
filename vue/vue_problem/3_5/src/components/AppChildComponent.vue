<template>
  <div class="child-box">
    <h2>App Child</h2>
    <!-- v-on이 트리거 되면 js를 실행할 수 있다. 이벤트 리스너로 동작 -->
    <input type="text" v-model="childData" @input="onChildInputChange">
    <p>appData : {{ appData }}</p>
    <p>parentData : {{ parentData }}</p>
    <p>childData : {{ childData }}</p>
  </div>
</template>

<script>
export default {
    name: 'AppChildComponent',
    props: {
        appData: String,
        parentData: String,
    },
    data () {
        return {
            childData: ''
        }

    },
    methods: {
        onChildInputChange(event) {
            this.$emit('child-input-change', event.target.value)
            
        }
    }
    
}
</script>

<style scoped>
.child-box {
    border: 1px solid blue;
}
</style>