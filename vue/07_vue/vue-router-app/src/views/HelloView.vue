<template>
  <div>
    <h1>hello, {{ userName }}</h1>
  </div>
</template>

<script>
export default {
    name: 'HelloView',
    data() {
        return {
            userName: this.$route.params.userName
        }
    },
    beforeRouteUpdate(to, from, next){
      // 이동할 url의 userName으로 변경해주기
      this.userName = to.params.userName
      next()
    }
}
</script>

<style>

</style>