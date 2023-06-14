<script>


import { goalsArray } from "../data/goalsOnuGrid.js"


export default {
    name: "AppFooter",
    data() {
        return {
            goalsArray
        }
    },
    methods: {
        getImagePath: function (name) {
            return new URL(`../assets/img/goals2030/${name}`, import.meta.url).href
        }
    }
}

</script>

<template>
  <footer>

    <section id="footer">

      <div class="container">
        <div class="row justify-content-center align-items-center">

          <div class="col-12 col-lg-6 bg_intro rounded-4 py-5 my-2 align-content-center introduce">
            <h1><strong>Hi, I'm </strong><span class="txt_thin">FRA</span></h1>
            <p>
              I have a master's degree in Analysis and Management of Agronomic and Forestry Ecosystems: <a
                href="https://corsi.unibo.it/magistrale/ProgettazioneGestioneEcosistemi"><span
                  class="txt_primary color_txt_link" target="_blank"> PROGESA</span> </a><br>
              The study programs contribute to the pursuit of the <br> <a
                href="https://www.un.org/sustainabledevelopment/"><span class="txt_primary color_txt_link"
                  target="_blank">Sustainable
                  Development Goals</span> </a> of the ONU Agenda 2030. <br>
              I have a passion for the environment and for technology.<br>
            </p>

          </div>

          <div class="col-12 col-lg-4 d-flex flex-wrap goals mx-4 col_goals_onu">

            <div class="col-3 text-center p-2" v-for="goal in goalsArray" :key="goal.img">
              <a :href="goal.link" target="_blank">
                <img class="rounded-4 zoom-effect-goals" :src="getImagePath(goal.img)" alt="Goal Image">
              </a>

            </div>

          </div>

          <div class="container">
            <div class="row align-items-center">
              <!-- <div class="col-4 col-md-4 col-lg-2 rounded-pill text-center col_github">
                <h6 class=" txt_neutral_github bg-dark rounded-pill">visit my <span class="txt_github">GitHub</span></h6>
              </div> -->
              <div class="col-6 col-lg-2 mx-5 col_github">
                <a href="https://github.com/JungleKiosk" target="_blank">
                  <img class="text-center my_contact zoom-effect-contact" src="../assets/img/linkedin_footer.svg" alt="">
                  <img class="text-center my_contact zoom-effect-contact" src="../assets/img/github_footer.svg" alt="">
                  <img class="text-center my_contact zoom-effect-contact" src="../assets/img/youtube_footer.svg" alt="">
                </a>
              </div>


            </div>
          </div>



        </div>



      </div>

    </section>

  </footer>
</template>