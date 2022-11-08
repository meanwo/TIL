<template>
 <h3>
    <button style="width:100%" 
    @click="updateSizeList"
    :class= "{'is-selected' : size.selected}" class="my-2"
    >선택 </button> 
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
  .is-selected {
    background-color: green;
  }
</style>