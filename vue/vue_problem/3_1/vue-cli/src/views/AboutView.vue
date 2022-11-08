<template>
  <div>
    <h1>About</h1>
    <h2>첫 번째 박스</h2>
    <div class="global">
      <div class="box scoped-box"></div>
    </div>
    <h2>두 번째 박스</h2>
    <div class="global">
      <div class="box scoped-box"></div>
    </div>
  </div>
</template>


<style scoped>
/* scoped가 없으면 전역적으로 설정 */
.box {
  background-color: pink;
}
</style>