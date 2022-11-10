<template>
    <li @click="selectVideo">
        <img :src="video.snippet.thumbnails.default.url">
        {{ video.snippet.title }}
    </li>
</template>

<script>
export default {
    name: 'VideoListItem',
    props:{
        video:{
            type:Object,
            required:true,
        }
    },
    methods:{
        selectVideo(){
            console.log(this.video)
            this.$emit('select-video', this.video)
        }
    }
}
</script>

<style>

</style>