<template>
  <div>
    <AppComponent/>
  </div>
</template>

<script>
import AppComponent from '../components/AppComponent.vue'
export default {
    name: 'IndexView',
    components : {
        AppComponent
    }
}
</script>

<style>
.box {
    width: 700px;
    border: 1px solid black;
}

</style>