# Chasse

<div id="top"></div>
<span>
    <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
</span>

**Chasse** is a lightweight CLI tool to write reusable HTML *components* (much like JSX) instead of repetitive code, without too much of steps or learning. It strips down on the boring and redundant and makes HTML fun again! Just run a simple command on an HTML file inheriting components from a base HTML file to convert it into a complete HTML file. 


## Procedure

All you have to do is:
- Create a *parent* HTML file (or multiple parent files) for all the components you want to reuse. define components inside it like so (**note the duo of tailing exclamation marks**!), let this be called `template.html`:
  
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
- Create a *child* HTML file to import and use the components you need to. First declare the *parent* files that will be used (**here it is `templates.html`, hence the first line**), then straightaway import the components (**note the use of two exclamation marks, followed by a space and a '/'**)! It is named as `child.html`.
  
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

**Chasse** borrows from the concepts of React components, Sass mixins and Django template inheritance to charge up simple and blazingly fast applications deployed on a web-server that don't require the overhead cast down by running `npm` (or any other processes). It is implemented using a simple Python application that uses `argparse` under the hood to power up the CLI. <br />
The current release is the first in the line and has somewhat limited operational capability, but is capable of getting the main job done. Further planned improvements are written down below.

<p align="right">(<a href="#top">Top</a>)</p>


## Pros

1. **Static Websites? Maybe You Don't Need the `npm` Overhead...**: A great many good static websites can be shipped without the use of package managers or libraries (just plain HTML, CSS and JS). Content tends to get repetitive for HTML in such stacks, in which case this can be used to program sites without the use of heavier templating engines or utilities.
1. **Zero Dependencies**: The `chasse` binary is all that is needed to begin. No underlying installations or packages required.
1. **Similar to Sass**: Chasse generates HTML files in a similar manner to Sass. Hence, developers familiar with Sass would be already set to go.
1. **HTML-Only**: Unlike Sass, there are no foreign files that would require extensions or plugins in the IDE to work. Parent and child source files are in HTML. And so are the resultant files.
1. **Portable Binary**: The binaries in the repository are all cross-platform.

<p align="right">(<a href="#top">Top</a>)</p>


## Cons

1. **Too Young**: Lacks many features that can be added to make it more robust.
1. **Binary Size**: The `dist` folder has been removed `.gitignore` since the binary inside it is barely of 4 kB. The independent single-file binary (in the root folder), however, occupies 6 mB, which is somewhat large as a utility.
1. **Less Customizable**: There are fewer features and CLI options at present. However, the tool is expected to improve more in subsequent releases.

<p align="right">(<a href="#top">Top</a>)</p>


## Future

1. **Tests**: Tests written would be using the `pytest` framework.
1. **Passing Data**: Components would be allowed to have data passed on to them in form of variables.
1. **Nested Inheritance**: Components would be allowed to have components within themselves.
1. **Transition to Go**: Python is an interpreted language, due to which, despite the general programming ease, a release featuring Go would be introduced soon that would also be able to use concurrency in parsing multiple files at once, giving a binary that is extremely small and portable.
1. **Processing Multiple Files**: Multiple files would be parsed at once to generate HTML.
1. **Logging Architecture**: Place logging architecture to help in debugging and testing.
1. **Improved Error Handling**: Make error (and success) messages more informative.

<p align="right">(<a href="#top">Top</a>)</p>


## Binaries

There are two ways to use the application:
1. **The `chasse` Binary**: The binary in the root is of around 6 mB. We can simply use this binary to do quick and dirty conversions. This is not recommended for standard use. Use it like:

    ```sh
    .\chasse child.html src
    ```
1. **The `dist` Folder**: The folder (with the binary) is sized at around 4 kB. The folder is to be kept in the system at a desired location. The PATH variable is to be updated. Then the tool would be available globally across the system for use. This is the recommended use of the tool.

    ```sh
    chasse child.html src
    ```

<p align="right">(<a href="#top">Top</a>)</p>


## Options

1. `-h`: Shows help with the complete guide to the use of the tool.
    ```sh
    ./chasse -h
    usage: Chasse [-h] [-v] [-p PARENT_PATH] source destinationpath

    Convert Chasse files to HTML files.

    positional arguments:
    source                Enter the file path of the Chasse file to be converted into an HTML file.
    destinationpath       Enter the directory wherein the HTML files will get stored.

    options:
    -h, --help            show this help message and exit
    -v, --version         show program's version number and exit
    -p PARENT_PATH, --parent-path PARENT_PATH
                            To specify the path to the parent files. Defaults to the source path.
    ```
1. `-v`: Shows the current version of the tool.
    ```sh
    ./chasse -v
    Chasse 1.0.0
    ```
1. `-p`: To specify the path to the parent files. Defaults to the source path.
    ```sh
    .chasse -p="components/home/" child.html src
    ```

<p align="right">(<a href="#top">Top</a>)</p>


## Terminology

1. **Parent HTML File**: This is the file wherein the components (reusable or otherwise) to be used by the children are defined.
1. **Child (or Source) HTML File**: This is the file wherein the HTML document is written with the use of components. Basically, this is where development is to be done. Later, this is the file that gets converted into the HTML code that is used and understood by the browser.
1. **Resultant HTML File**: This is the file which gets generated and used by the browser.
1. **Components**: These are blocks of reusable code that can be represented by a name. These names can just be plugged into the HTML documents in place of huge redundant paragraphs of the same thing, over and over again.

<p align="right">(<a href="#top">Top</a>)</p>


## Release Log

1. **Version 1.0.0**:
    - Basic child HTML file parsing to get required components.
    - Parsing parent HTML file for extracting components.
    - Generation of resultant HTML files with the components.
1. **Version 1.1.0**:
    - Logging architecture established for development and debugging.
    - More responsive CLI, with respect to error and success messages.
    - Introduce code conventions.
