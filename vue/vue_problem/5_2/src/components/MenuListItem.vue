<template>
 <h3>
    <button style="width:100%"
    @click="updateMenuList"
    :class= "{'is-selected' : menu.selected}" class="my-2"
    > 선택 
    </button> 
    {{ menu.title }}
    {{ menu.price }}

    <br>
    
    <img :src="menu.image" alt="" class="imgsize">
  </h3>
</template>

<script>
export default {
  name: 'MenuListItem',
  props: {
    menu: Object,
  },
  methods:{
    updateMenuList() {
      this.$store.dispatch('updateMenuList', this.menu)
    }
  }
}
</script>

<style>
  .imgsize {
    width: 200px;
    height: 200px;
  }
  .is-selected {
    background-color: green;
  }
</style>