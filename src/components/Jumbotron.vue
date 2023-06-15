<script>

export default {
    data() {
        return {

        };
    }
}

</script>



<template>
    <div class="container my-5 jumbo txt_jumbo rounded-4">
        <div class="row justify-content-center ">
            <div class="col-12 col-lg-8 col-md-8">
                <h1 class="title">Welcome</h1>
                <p>
                    This project is a collection of videos dedicated to chestnut zoning and contour calculation using <span
                        class="q_qgis">Q</span><span class="gis_qgis">GIS</span>
                    and the <span class="py_python">Py</span><span class="thon_python">thon</span> shell.
                    <br> You will see how to exploit QGIS, a versatile geoprocessing tool, to identify ideal areas for
                    chestnut cultivation. <br>
                    Through raster and vector data a suitability map will be created; <br> identifying the most suitable
                    areas in terms of Altitude, Slope and Sun Exposure. <br>
                    You will also see how to implement a Python code to calculate contour lines and extrapolate the main
                    ones (every 100m). <br>
                    Through this combination of QGIS and Python you will get an initial schema for a zonal analysis. <br>
                    You can find the Python code at my <a class="link_github_jumbo" href="https://github.com/JungleKiosk/QGIS_zoning/tree/main/py_code" target="_blank">GitHub</a> page. Enjoy!
                </p>
            </div>
        </div>

    </div>
</template>




<style>
.q_qgis {
    color: #ffab1a;
    font-weight: bold;
}

.gis_qgis {
    color: #bddf41;
    font-weight: bold;
}

.py_python {
    color: #fcd648;
    font-weight: bold;
}

.thon_python {
    color: #3da8ff;
    font-weight: bold;
}

.link_github_jumbo{
    color: #dd99fd;
    text-decoration: none;
}


</style>

