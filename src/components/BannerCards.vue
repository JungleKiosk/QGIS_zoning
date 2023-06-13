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
        <div class="row">
            <div v-for="link in links" :key="link.title" class="col-12 col-lg-3 col-md-6">
                <div class="card my-3">
                    <div class="card-header">
                        {{ link.title }}
                    </div>
                    <div class="card-body">
                        {{ link.desc }}
                        <img :src="getImagePath(link.img)" alt="Image" />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>





<style></style>

