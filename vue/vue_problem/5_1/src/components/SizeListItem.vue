<template>
 <h3>
    <button @click="updateSizeList"> 선택 </button> 
    {{ size.name }}
    <br>
  <div>
    {{ size.price }}
  </div>
</h3>
</template>

<script>
export default {
  name: 'SizeListItem',
  props: {
    size: Object,
  },
  methods:{
    updateSizeList() {
      this.$store.dispatch('updateSizeList', this.size)
    }
  }
}

</script>

<style>
</style>