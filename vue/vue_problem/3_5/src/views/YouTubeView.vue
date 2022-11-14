<template>
  <div class="container">
    <div>
        <!-- {{ videos }} -->
        <h1 class='text-primary'>SSAFY TUBE</h1>
    </div>
    <section v-if='isselectedVideo' class='mt-2'>
        <div class="ratio ratio-16x9">
            <iframe :src="videoSrc" frameborder="0"></iframe>
        </div>
        <div class="video-title shadow p-3 mb-5 bg-body rounded">
            <h4>{{ selectedVideo.snippet.title }}</h4>
        </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
// import _ from 'lodash'

const API_URL = 'https://www.googleapis.com/youtube/v3/search'
// secret_key 처리해야할 api key
const API_KEY = 'AIzaSyBN0bxfy-GlhDBC563zgQ4H-AA06g-RE_Q'


export default {
    name: 'YouTubeView',
    created() {
        axios.get(API_URL, {
            params: {
                key: API_KEY,
                type: 'video',
                part: 'snippet',
                q: '코딩노래'
            }
        }).then((response)=>{
            this.videos = response.data.items
            this.selectedVideo = this.videos[0]
            console.log(response)
        }).catch((error)=> {
            console.error(error)
        })
        console.log('created')
    },
    data() {
        return {
            videos: [],
            selectedVideo: {}
        }
    },
    
    computed: {    
        videoSrc() {
            const url = 'http://www.youtube.com/embed/'
            return url + this.selectedVideo.id.videoId
        },
        // !! : true 일 때 1 반환 
        isselectedVideo() {
            return !!Object.keys(this.selectedVideo).length
        }
    }
}
</script>

<style>
    *{
        font-family: 'Noto Sans KR', sans-serif;
    }
    .video-title {
        border: 1px solid gray;
    }
</style>