<template>
    <div>
        <h2>Video List</h2>
        <ul>
            <!-- 문삼님 가라사대: 왼쪽 video 는 키를 말하는 거고(v-for -"video in videos" 부분) 오른쪽 video 는 하위 컴포넌트에서 사용할 변수 명 -->
            <VideoListItem v-for="video in videos" :key="video.id.videoId" :video="video" @select-video="SelectVideo"/>
        </ul>
     </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'

export default {

    name: 'VideoList',
    components: {
        VideoListItem,
    },
    props: {
        searchVideo: String,
        videos:{
            type:Array,
            required:true,
        }
    },

    methods:{
        SelectVideo(video){
            this.$emit('select-video', video)

        }
    }
    
}

</script>

<style>

</style>