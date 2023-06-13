<script>

export default {
    data() {
        return {

        };
    }
}

</script>



<template>
    <section class="section_jumbo"></section>
    <section class="jumbo">

        <div class="container jumbotron">
            <div class="row justify-content-center ">
                <div class="col-12 col-lg-8 col-md-8">
                    <div class="image-container">
                        <img src="../assets/img/chestnut_three.png" alt="Background Image" class="fixed-image" />
                    </div>
                    <h1>Welcome</h1>
                    <p>
                        This project is dedicated to chestnut zoning and contour calculation using QGIS and the Python shell.
                        <br> We will explore how to harness the power of QGIS, a versatile and intuitive
                        geoprocessing tool, to identify ideal areas for chestnut cultivation. <br>
                        You will see the use of raster and vector data, to analyze the altimetry, the inclination of the land
                        and the exposure of the slope to determine the suitability of the different areas for the cultivation of
                        chestnut trees. <br>
                        Also leveraging the Python shell, we will discover how to calculate contour lines to
                        identify lines of equal altitude, providing a clear and detailed representation of the surrounding
                        terrain. <br>
                        Through this combination of QGIS and Python, we will be able to obtain accurate and meaningful results
                        for chestnut cultivation, providing a start for the sampling campaign and related future analyses.
                    </p>
                </div>
            </div>
    
        </div>
    </section>
</template>




<style>
.section_jumbo{
    margin-top: 300px;
}
.jumbo{
    background-color: rgba(0, 0, 0, 0.7);
}

.jumbotron{
    padding-top: 100px;
}

</style>

