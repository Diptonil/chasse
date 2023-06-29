# Chasse

<div id="top"></div>
<span>
    <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
</span>

**Chasse** is a lightweight CLI tool to write reusable HTML *components* (much like JSX) instead of repetitive code, without any fuss about learning curves. It strips down on the boring and redundant and makes HTML fun again! Run the command on an HTML file inheriting components from a base HTML file to convert it into a complete HTML file. 


## Procedure

All you have to do is:
- Create a *parent* HTML file (or multiple parent files) for all the components you want to reuse. define components inside it like so (note the duo of tailing exclamation marks!), let this be called `template.html`:
    ```html
    ...
    <Navbar!!>
        <nav>
            <ul>
                <li>About</li>
                <li>Contact</li>
                ...
            </ul>
        </nav>
    </Navbar!!>

    <UniversalFooter!!>
        <footer>
            All rights reserved (really, though? Are they?).
        </footer>
    </UniversalFooter!!>
    ...
    ```
- Create a *child* HTML file to import and use the components you need to. First declare the *parent* files that will be used (here it is `templates.html`, hence the first line), then straightaway import the components (note the use of two exclamation marks, followed by a space and a '/')! It is named as `child.html`.
    ```html
    <template!!>
    
    <html>
        ...
        <Navbar!! />
        ...
        <UniversalFooter!! />
    </html>
    ```
- That's it, you're all set! Run the command, passing in the *child* file and the *location to extract the generated HTML files* into:
    ```sh
    .\chasse child.html src
    ```
- That's all you have to do to convert the components into complete code!
    
<p align="right">(<a href="#top">Top</a>)</p>


## About

**Chasse** borrows from the concepts of React components, Sass mixins and Django template inheritance to charge up simple and blazingly fast applications deployed on a web-server that don't require the overhead cast down by `npm` (or any other processes). It is implemented using a simple Python application that uses `argparse` under the hood to power up the CLI. <br />
The current release is the first in the line and has somewhat limited operational capability, but is capable of getting the main job done. Further planned improvements are written down below.

<p align="right">(<a href="#top">Top</a>)</p>


## Pros

- HTML only - no file extension

<p align="right">(<a href="#top">Top</a>)</p>


## Terminology

<p align="right">(<a href="#top">Top</a>)</p>

