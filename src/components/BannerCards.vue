<script>

export default {
    props: ['links'],
    data() {
        return {

        };
    },

    methods: {
        getImagePath: function (name) {
            return new URL(`../assets/img/${name}`, import.meta.url).href
        }
    }
}

</script>

<template>
    <div class="container my-5">
        <div class="row align-items-stretch">
            <div v-for="link in links" :key="link.title" class="col-12 col-lg-3 col-md-6">
                <div class="card rounded-5 bg_card my-3 d-flex">
                    <div class="card-header card_title">
                        {{ link.title }}
                    </div>
                    <div class="card-body d-flex flex-column">
                        <p>{{ link.desc }}</p>
                        <img class="rounded-pill card_img_zoom" :src="getImagePath(link.img)" alt="Image"
                            style="height: 200px;" />
                        <div class="link_video py-1 text-center">
                            <a :href="link.video" target="_blank">
                                Go to video
                                <img class="yt_icon" src="./../assets/img/yt.svg" alt="">
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  

<style></style>

