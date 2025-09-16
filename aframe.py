import marimo

__generated_with = "0.15.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    aframe_html = """<html>
      <head>
        <script crossorigin="anonymous" src="https://aframe.io/releases/1.7.0/aframe.min.js"></script>
      </head>
      <body>
        <a-scene>
          <a-box position="-1 0.5 -3" rotation="0 45 0" color="#4CC3D9"></a-box>
          <a-sphere position="0 1.25 -5" radius="1.25" color="#EF2D5E"></a-sphere>
          <a-cylinder position="1 0.75 -3" radius="0.5" height="1.5" color="#FFC65D"></a-cylinder>
          <a-plane position="0 0 -4" rotation="-90 0 0" width="4" height="4" color="#7BC8A4"></a-plane>
          <a-sky color="#ECECEC"></a-sky>
        </a-scene>
      </body>
    </html>"""
    mo.iframe(aframe_html)
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Simple demo of A-Frame in Marimo

    This notebook can be converted into a WASM-based HTML page (with Python and Marimo running in the HTML page), and then served via HTTPS. If it is then opened from a WebXR-capable browser (such as the one in Quest), the user can work with the notebook, and see A-Frame scenes in XR.

    ```
    uv init
    uv add marimo
    uv run marimo export html-wasm aframe.py -o aframe.html --mode edit
    ```

    In case users are not expected to edit the notebook, only to "see" it, the following command can be used🥇

    ```
    uv run marimo export html-wasm aframe.py -o aframe.html --mode run
    ```
    """
    )
    return


if __name__ == "__main__":
    app.run()
