import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  // 데이터
  state: {
    message: 'message in store',
  },

  // computed
  getters: {
    messageLength(state) {
      return state.message.length
    }
  },

  // 기존의 methods 에 쓰던  함수들
  // mutations 는 state를 마지막에 직접적으로 변경하기 때문에 이름을 대문자로 구분
  mutations: {
    CHANGE_MESSAGE(state, newMessage) {
      console.log(state)
      console.log(newMessage)
      state.message = newMessage
    }
  },
  
  actions: {
    changeMessage(context, newMessage) {
      // console.log(context)
      // console.log(newMessage)
      context.commit('CHANGE_MESSAGE', newMessage)  
    }
  },


  modules: {
  }
})
