<template>

    <div v-if="video">
        <h2>Video Detail</h2>
        <iframe :src="videoURI" frameborder="0"></iframe>
    </div>
    <div v-else>
        <h2> 이미지가 없습니다.</h2>
        <img src="../assets/logo.png" alt="">
    </div>
</template>

<script>
export default {
    props:{
        video:{
            type:Object,
        },
    },
    computed:{
        videoURI(){
            const videoId = this.video.id.videoId
            return `https://www.youtube.com/embed/${videoId}`
        }
    }
}
</script>

<style>

</style>