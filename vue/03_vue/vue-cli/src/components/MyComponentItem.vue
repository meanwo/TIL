<template>
    <div>
        <h3> 나는 MyComponent의 하위 컴포넌트</h3>
        <p>{{ staticProps }}</p>
        <p>{{ dynamicProps }}</p>
        <button @click="childToParent">클릭!</button>
        <!-- 엔터를 눌렀을 때 childInput 메서드를 호출 -->
        <input 
            type="text" 
            v-model="childInputData"
            @keyup.enter="childInput">
    </div>
</template>

<script>
export default {
    name: 'MyComponentItem',
    props: {
        staticProps: String,
        dynamicProps: String,
    },
    data: function () {
        return {
            childInputData: null,
        }
    },
    methods: {
        childToParent: function () {
            // vue 객체의 기본 속성값이라는 의미의 $, name props도 $가 생략되어 있음
            // 'event-name' 이 첫 번째 인자로 들어감, 두 번째 인자는 데이터.
            this.$emit('child-to-parent', '나는 자식이 보낸 데이터다')
        },
        childInput: function name() {
            this.$emit('child-input', this.childInputData)
        }
    }
}
</script>

<style>

</style>