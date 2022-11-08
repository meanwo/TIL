import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList: [],
    menuList: [
      {
        title: '아메리카노',
        price: 3000,
        selected: true,
        image: 'https://source.unsplash.com/featured/?americano'
      },
      {
        title: '얼그레이',
        price: 4000,
        selected: false,
        image: 'https://source.unsplash.com/featured/?earlgrey'
      },
      {
        title: '녹차',
        price: 3500,
        selected: false,
        image: 'https://source.unsplash.com/featured/?greentea'
      }
    ],
    sizeList: [
      {
        name:'small',
        price: 500,
        selected: true,
      },
      {
        name:'medium',
        price: 1000,
        selected: false,
      },      {
        name:'tall',
        price: 1500,
        selected:  false,
      }
    ],
  },
  getters: {
  },
  mutations: {
    ADD_ORDER: function (state) {
      const order_menu = state.menuList.filter(menu => 
        menu.selected === true)
      const order_size = state.sizeList.filter(size =>
        size.selected === true)
      state.orderList.push(order_menu[0])
      state.orderList.push(order_size[0])
    },
    UPDATE_MENU_LIST: function (state, selectedMenu) {
      state.selectedMenu = state.menuList.map((menu) => {
        if (menu === selectedMenu) {
          menu.selected = !menu.selected
        } else {
          menu.selected = false
        }
        return menu
      })
    },
    UPDATE_SIZE_LIST: function (state, selectedSize) {
      state.selectedSize = state.sizeList.map((size) => {
        if (size === selectedSize) {
          size.selected = !size.selected
        } else {
          size.selected = false
        }
        return size
      })
    },
  },
  actions: {
    updateMenuList(context, selectedMenu) {
      context.commit('UPDATE_MENU_LIST', selectedMenu)
    },
    updateSizeList(context, selectedSize) {
      context.commit('UPDATE_SIZE_LIST', selectedSize)
    },
    shoppingCart(context) {
      context.commit('ADD_ORDER')
    }
  },
  modules: {
  }
})
