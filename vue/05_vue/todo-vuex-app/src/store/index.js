import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    todos: [
    ]
  },
  getters: {
    allTodosCount(state) {
      return state.todos.length
    },
    completedTodosCount(state) {
      const completedTodos = state.todos.filter((todo) => {
        return todo.isCompleted == true
      })
      return completedTodos.length
    },
    unCompletedTodosCount(state, getters) {
      return getters.allTodosCount - getters.completedTodosCount
    },
  },
  mutations: {
    CREATE_TODO(state, todoItem) {
      state.todos.push(todoItem)
    },
    DELETE_TODO(state,todoItem) {
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index, 1)
    },
    UPDATE_TODO_STATUS(state, todoItem) {
      state.todos = state.todos.map((todo) => {
        if (todo === todoItem) {
          todo.isCompleted = !todo.isCompleted
        }
        return todo
      })
   },
  //  LOAD_TODOS(state) {
  //   const localStorageTodos = localStorage.getItem('todos')
  //   // 문자열 데이터를 다시 object 타입으로 변환
  //   const parsedTodos = JSON.parse(localStorageTodos)
  //   state.todos = parsedTodos
  //  },
  },
  actions: {
    createTodo(context, todoTitle) {
      const todoItem = {
        title: todoTitle,
        isCompleted: false,
      }
      // console.log(todoItem)
      context.commit('CREATE_TODO', todoItem)
      // context.dispatch('saveTodosToLocalStorage')
    },
    deleteTodo(context, todoItem) {
      context.commit('DELETE_TODO', todoItem)
      // context.dispatch('saveTodosToLocalStorage')
    },
    updateTodoStatus(context, todoItem) {
      context.commit('UPDATE_TODO_STATUS', todoItem)
      // context.dispatch('saveTodosToLocalStorage')
    },
    saveTodosToLocalStorage(context) {
      const jsonTodos = JSON.stringify(context.state.todos)
      // setItem(key, value) - key, value 형태로 데이터 저장
      // 개발자 도구- application - strage - Local Storage에 todo 데이터를 저장
      localStorage.setItem('todos', jsonTodos)
    },
    // loadTodos(context) {
    //   context.commit('LOAD_TODOS')
    // },
  },
  modules: {
  }
})
