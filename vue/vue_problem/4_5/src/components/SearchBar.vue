<template>
  <div>
    <input 
    type="text"
    v-model.trim="searchText"
    @keyup.enter="createText"
    >
    <button @click='createText'>검색</button><br>
    <!-- {{ searchText }} -->
  </div>
</template>

<script>

export default {
    name: 'SearchBar',
    data() {
        return {
            searchText: null,
        }
    },
    methods: {
        createText() {
            this.$emit('create-text', this.searchText)
            this.searchText = null
            
        }
    }
}
</script>

<style>

</style>