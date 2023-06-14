<script>

import BannerCards from './components/BannerCards.vue';
import Jumbotron from './components/Jumbotron.vue';
import { links } from './data/linkVideo.js';
import AppFooter from './components/AppFooter.vue';

export default {
  data() {
    return {

    };
  },
  components: { Jumbotron, BannerCards, AppFooter },
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
  <AppFooter></AppFooter>

</template>

<style></style>
