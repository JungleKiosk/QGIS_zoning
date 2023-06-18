<script>

import AppHeader from './components/AppHeader.vue';

import BannerCards from './components/BannerCards.vue';
import Jumbotron from './components/Jumbotron.vue';
import { links } from './data/linkVideo.js';
import AppFooter from './components/AppFooter.vue';

export default {
  data() {
    return {

    };
  },
  components: { AppHeader, Jumbotron, BannerCards, AppFooter },
  computed: {
    linksData() {
      return links;
    }
  }
}


</script>

<template>
  <AppHeader></AppHeader>
  <Jumbotron></Jumbotron>
  <BannerCards :links="linksData"></BannerCards>
  <AppFooter></AppFooter>

</template>

<style></style>
