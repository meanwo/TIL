<template>
  <div id="app">
    <h1>Coffee Order App</h1>
    <b-container class="bv-example-row">
      <b-row>
        <b-col><MenuList/></b-col>
        <b-col><SizeList/></b-col>
      </b-row>
    </b-container>
    <OptionList/>
    <OrderList/>

    <button @click="shoppingCart">장바구니에 담기</button>
  </div>
</template>

<script>
import MenuList from '@/components/MenuList'
import OptionList from '@/components/OptionList'
import OrderList from '@/components/OrderList'
import SizeList from '@/components/SizeList'
export default {
  name: 'App',
  components: {
    MenuList,
    OptionList,
    OrderList,
    SizeList
  },
  methods: {
    shoppingCart() {
      this.$store.dispatch('shoppingCart')
    }
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  font-family: 'Noto Sans KR', sans-serif;
  padding: 0;
  margin: 0;
}

ul {
  list-style: none;
}
</style>
