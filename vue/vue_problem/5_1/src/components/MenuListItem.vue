<template>
 <h3>
    <button @click="updateMenuList"> 선택 </button> 
    {{ menu.title }}
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
</style>