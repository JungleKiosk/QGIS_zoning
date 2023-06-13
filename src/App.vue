<script>

import BannerCards from './components/BannerCards.vue';
import Jumbotron from './components/Jumbotron.vue';
import { links } from './data/linkVideo.js';

export default {
  data() {
    return {

    };
  },
  components: { Jumbotron, BannerCards },
  computed: {
    linksData() {
      return links;
    }
  }
}


</script>

<template>
  
  <Jumbotron></Jumbotron>
  <BannerCards :links="linksData"></BannerCards>

</template>

<style></style>
