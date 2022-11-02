<template>
  <!-- 최상위 태그가 하나라도 있어야 오류가 나지 않는다 -->
  <!-- template 태그는 실제로 출력되지 않는다. -->
  <div class = 'border'>
    <h1> 이거는 내가 만든 새로운 컴포넌트다! </h1>
    <MyComponentItem 
      static-props="MyComponent에서 보낸 데이터"
      :dynamic-props="dynamicProps"
      @child-to-parent="parentGetEvent"
      @child-input="getDynamicData"
    />
  </div>
</template>

<script>
// 1. 불러오기
import MyComponentItem from '@/components/MyComponentItem'

export default {
    // 상위 컴포넌트에서 name을 통해 이 파일을 연결시킴.
    name: 'MyComponent',
    // 2. 등록하기
    components : {
        MyComponentItem,
    },
    // vue-cli 에서는 데이터가 함수의 리턴값이 되어야 함
    data: function () {
      return {
        dynamicProps: '이건 동적인 데이터!',
      }
    },
    methods: {
      parentGetEvent: function (childData) {
        console.log('자식 컴포넌트에서 발생한 emit 이벤트를 들었다!!')
        console.log(childData)
      },
      getDynamicData: function (childInputData) {
        console.log(`사용자가 입력한 값은 ${childInputData}입니다.`)
      }
    }

}
</script>

<style>
    .border {
        border: solid 1px black;
    }
</style>