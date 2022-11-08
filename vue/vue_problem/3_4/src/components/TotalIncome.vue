<template>
  <div>
    <h2>종합 소득 금액</h2>
    <p>종합소득금액: {{ income }} 만원 </p>
    <p>종합소득공제: (-) 150 만원 </p>
    <p>과세표준: {{ taxBase }} </p>

    <hr>

    <TaxRate :tax-credit="taxCredit" :tax-base="taxBase"/>
  </div>
</template>

<script>
import TaxRate from './TaxRate.vue'
export default {
    name: 'TotalIncome',
    components: {
      TaxRate
    },
  
    props: {
      income: Number,
      taxCredit: Number,
      
    },
    data () {
        return {
            
        }
    },
    computed: {
      // return 에 3항연산자 사용 (조건? 참일 때 출력 값 : 거짓일 때 출력값)
      taxBase() {
        return this.income - 150 >= 0 ? this.income - 150 : 0
      }
    }
}
</script>

<style>

</style>