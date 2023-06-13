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
                <div class="card my-3 d-flex">
                    <div class="card-header">
                        {{ link.title }}
                    </div>
                    <div class="card-body d-flex flex-column">
                        <p>{{ link.desc }}</p>
                        <img class="rounded-pill card_img_zoom" :src="getImagePath(link.img)" alt="Image"
                            style="height: 200px;" />
                        <div class="link_video py-1">
                            <a :href="link.video" target="_blank">
                                go to video
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  

<style></style>

