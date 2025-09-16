import marimo

__generated_with = "0.15.5"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    babiaxr_html = """<!DOCTYPE html>
    <html lang="en">
      <head>
        ...
        <script src="https://aframe.io/releases/1.5.0/aframe.min.js"></script>
        <script src="https://unpkg.com/aframe-babia-components/dist/aframe-babia-components.min.js"></script>
        <script src="https://cdn.jsdelivr.net/gh/donmccurdy/aframe-extras@v7.2.0/dist/aframe-extras.min.js"></script>
      </head>  
      <body>
        <a-scene>

    <a-entity babia-pie='legend: true; palette: blues; key:model; size: sales;
        data:[{"model": "leon", "motor": "electric", "color": "red",
            "doors": 5, "sales": 10},
            {"model": "ibiza", "motor": "electric", "color": "white", 
            "doors": 3, "sales": 15},
            {"model": "cordoba", "motor": "diesel", "color": "black", 
            "doors": 5, "sales": 3},
            {"model": "toledo", "motor": "diesel", "color": "white", 
            "doors": 5, "sales": 18},
            {"model": "altea", "motor": "diesel", "color": "red", 
            "doors": 5, "sales": 4},
            {"model": "arosa", "motor": "electric", "color": "red", 
            "doors": 3, "sales": 12},
            {"model": "alhambra", "motor": "diesel", "color": "white", 
            "doors": 5, "sales": 5},
            {"model": "600", "motor": "gasoline", "color": "yellow", 
            "doors": 3, "sales": 20},
            {"model": "127", "motor": "gasoline", "color": "white", 
            "doors": 5, "sales": 2},
            {"model": "panda", "motor": "gasoline", "color": "black", 
            "doors": 3, "sales": 13}]'
        position="-1 0.5 -4" rotation="90 0 0"></a-entity>

            <!-- Light -->
             <a-light type="point" intensity="1" position="-10 20 30"></a-light>

            <!-- Camera -->
            <a-entity movement-controls="fly: true" position="0 0 0">
                <a-entity camera position="0 0 0" look-controls></a-entity>
                <a-entity cursor="rayOrigin:mouse"></a-entity>
                <a-entity laser-controls="hand: right"></a-entity>
            </a-entity>
        </a-scene>
      </body>
    </html>"""

    mo.iframe(babiaxr_html)
    return (mo,)


@app.cell
def _(mo):
    def build_scene():
        html = """<!DOCTYPE html>
    <html lang="en">
      <head>
        ...
        <script src="https://aframe.io/releases/1.5.0/aframe.min.js"></script>
        <script src="https://unpkg.com/aframe-babia-components/dist/aframe-babia-components.min.js"></script>
        <script src="https://cdn.jsdelivr.net/gh/donmccurdy/aframe-extras@v7.2.0/dist/aframe-extras.min.js"></script>
      </head>  
      <body>
        <a-scene>

            {chart}
            <!-- Light -->
             <a-light type="point" intensity="1" position="-10 20 30"></a-light>

            <!-- Camera -->
            <a-entity movement-controls="fly: true" position="0 0 0">
                <a-entity camera position="0 0 0" look-controls></a-entity>
                <a-entity cursor="rayOrigin:mouse"></a-entity>
                <a-entity laser-controls="hand: right"></a-entity>
            </a-entity>
        </a-scene>
      </body>
    </html>"""
        return html

    def build_pie():
        html = """<a-entity babia-pie='legend: true; palette: blues; key:model; size: sales;
        data:[{"model": "leon", "motor": "electric", "color": "red",
            "doors": 5, "sales": 10},
            {"model": "ibiza", "motor": "electric", "color": "white", 
            "doors": 3, "sales": 15},
            {"model": "cordoba", "motor": "diesel", "color": "black", 
            "doors": 5, "sales": 3},
            {"model": "toledo", "motor": "diesel", "color": "white", 
            "doors": 5, "sales": 18},
            {"model": "altea", "motor": "diesel", "color": "red", 
            "doors": 5, "sales": 4},
            {"model": "arosa", "motor": "electric", "color": "red", 
            "doors": 3, "sales": 12},
            {"model": "alhambra", "motor": "diesel", "color": "white", 
            "doors": 5, "sales": 5},
            {"model": "600", "motor": "gasoline", "color": "yellow", 
            "doors": 3, "sales": 20},
            {"model": "127", "motor": "gasoline", "color": "white", 
            "doors": 5, "sales": 2},
            {"model": "panda", "motor": "gasoline", "color": "black", 
            "doors": 3, "sales": 13}]'
        position="-1 0.5 -4" rotation="90 0 0"></a-entity>
        """
        return html

    pie = build_pie()
    scene = build_scene().format(chart=pie)
    mo.iframe(scene)
    return


if __name__ == "__main__":
    app.run()
