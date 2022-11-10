<template>
 <div id="app">
    <h1>SSAFY TUBE</h1>
    <SearchBar @create-text="createText"/>
    <b-container class="bv-example-row col-lg-12">
      <b-row>
        <b-col class="col-lg-8 col-12">
          <VideoDetail :video="selectedVideo"/>
        </b-col>
        <b-col class="col-lg-4">
          <VideoList :videos="videos" @select-video="SelectVideo" :search-video="searchVideo"/>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import VideoDetail from './components/VideoDetail.vue'
import VideoList from './components/VideoList.vue'
import SearchBar from './components/SearchBar.vue'
import axios from 'axios'
// import _ from 'lodash'

const API_URL = 'https://www.googleapis.com/youtube/v3/search'
// secret_key 처리해야할 api key

// 다른 계정(like lion)
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY


export default {
  name: 'App',
  components: {
    VideoDetail,
    VideoList,
    SearchBar,
  },
  created() {
    axios.get(API_URL, {
        params: {
            key: API_KEY,
            type: 'video',
            part: 'snippet',
            q: 'SSAFY'
        }
    }).then((response)=>{
        this.videos = response.data.items
        // this.selectedVideo = this.videos[0]
        console.log(response)
    }).catch((error)=> {
        console.error(error)
    })
    console.log('created')
  },
  data: function () {
    return {
      videos:[],
      selectedVideo: null,
      searchVideo: null,
    }
  },
  methods: {
    SelectVideo(video){
      this.selectedVideo=video
    },
    createText : function(searchText) {
      this.searchVideo = searchText
      axios.get(API_URL, {
          params: {
              key: API_KEY,
              type: 'video',
              part: 'snippet',
              q: this.searchVideo
            }
      }).then((response)=>{
          this.videos = response.data.items
          // this.selectedVideo = this.videos[0]
          console.log(response)
      }).catch((error)=> {
          console.error(error)
      })
      console.log('created')
        
      }
    },
  }

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
