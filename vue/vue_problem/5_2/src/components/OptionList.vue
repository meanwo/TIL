<template>
  <div>
    <!-- <h1>3. 옵션을 고르세요.</h1> -->
    <ul class="option-list">
    </ul>
    <OptionListItem/>
  </div>
</template>

<script>
import OptionListItem from '@/components/OptionListItem'
export default {
  name: 'OptionList',
  components: {
    OptionListItem,
  },
  computed: {
    // optionList: function () {
    // },
  },
  methods: {
    increase: function () {
    },
    decrease: function () {
    },
  },
}
</script>

<style>
</style>