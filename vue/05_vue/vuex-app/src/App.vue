<template>
  <div id="app">
    <!-- 중앙저장소의 state의 message 로 접근 -->
    <h1>{{ message }} </h1>
    <h2>입력된 문자의 길이는 {{ messageLength }}</h2>
    <input 
      type="text"
      @keyup.enter="changeMessage"
      v-model="inputData"
    >
  </div>
</template>

<script>


export default {
  name: 'App',
  data() {
    return {
      inputData: null,
    }
  },
  components: {

  },
  computed : {
    message() {
      return this.$store.state.message
    },
    messageLength() {
      return this.$store.getters.messageLength
    },
  },
  methods : {
    // component 에서 dispatch() 에 의해 vuex의 actions 가 호출 됨
    // dispatch(A, B) --> A: 호출하고자 하는 actions함수, B: 넘겨주는 데이터
    changeMessage() {
      const newMessage = this.inputData
      this.$store.dispatch('changeMessage', newMessage)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
