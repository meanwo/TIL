<template>
  <div>
    <h1>
        소득세 계산기
    </h1>
    <div>
        <label for="income">연봉 입력 (만원):</label>
        <!-- .number를 통해 숫자로 형변환 -->
        <input type="number" id="income" v-model.number="income">
    </div>
    <div>
        <label for="tax-credit">세액감면액 (만원):</label>
        <input type="number" id="tax-credit" v-model.number="taxCredit">
    </div>
    <hr>
    <TotalIncome :income="income" :tax-credit="taxCredit"/>
  </div>



</template>

<script>
import TotalIncome from '@/components/TotalIncome'
export default {
    name: 'CalculatorView',
    components: {
        TotalIncome
    },
    // 데이터를 객체가 아닌 함수로 쓸것!
    data() {
        return {
            income: 0,
            taxCredit: 0,
        }
        
    }
}
</script>

<style>

</style>