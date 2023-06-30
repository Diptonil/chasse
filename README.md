# Chasse

<div id="top"></div>
<span>
    <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
</span>

**Chasse** is a lightweight CLI tool to write reusable HTML *components* (much like JSX) instead of repetitive code, without too much of steps or learning. It strips down on the boring and redundant and makes HTML fun again! Just run a simple command on an HTML file inheriting components from a base HTML file to convert it into a complete HTML file. 


## Procedure

All you have to do is:
- Create a *parent* HTML file (or multiple parent files) for all the components you want to reuse. define components inside it like so (**note the duo of tailing exclamation marks**!), let this be called `template.chasse.html`:
  
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
- Create a *child* HTML file to import and use the components you need to. First declare the *parent* files that will be used in the *very first line* (**here it is `templates.html`, hence the first line**), then straightaway import the components (**note the use of two exclamation marks, followed by a space and a '/'**)! It is named as `child.chasse.html`.
  
    ```html
    <template!!>
    
    <!DOCTYPE HTML5>
    <html>
        ...
        <Navbar!! />
        ...
        <UniversalFooter!! />
    </html>
    ```
- That's it, you're all set! Run the command, passing in the *child* file and the *location to extract the generated HTML files* into:
    ```sh
    .\chasse child.chasse.html src
    ```
- That's all you have to do to convert the components into complete code! The resultant files are in `.html`, which browsers can understand with ease.
    
<p align="right">(<a href="#top">Top</a>)</p>


## About

**Chasse** borrows from the concepts of React components, Sass mixins and Django template inheritance to charge up simple and blazingly fast applications deployed on a web-server that don't require the overhead cast down by running `npm` (or any other processes). It is implemented using a simple Python application that uses `argparse` under the hood to power up the CLI. <br />
The current release is the among the early ones in the line and has somewhat limited operational capability, but is capable of getting the main job done. Further planned improvements are written down below.

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
1. **Improved Error Handling**: Make error (and success) messages more informative.

<p align="right">(<a href="#top">Top</a>)</p>


## Binaries

The current supported way to use the application:
1. **The `chasse` Folder**: The folder (with the binary) is sized at around 4 kB. The folder is to be kept in the system at a desired location. The PATH variable is to be updated accordingly to point to this folder itself (not the executable in it). Then the tool would be available globally across the system for use. This is the recommended use of the tool.
    ```sh
    chasse child.html src
    ```

<p align="right">(<a href="#top">Top</a>)</p>


## Options

1. `-h` or `--help`: Shows help with the complete guide to the use of the tool.
1. `-v` or `--version`: Shows the current version of the tool.
1. `-p` or `--parent-path`: To specify the path to the parent files. Defaults to the source path.
    ```sh
    chasse -p="components/home/" child.chasse.html src
    ```
1. `-l` or `--logs`: To enable display of the logs during the generation of the HTML files. This is helpful when the files fail to get generated and there is an error with the Chasse source files.
    ```sh
    chasse -l child.chasse.html src
    ```

<p align="right">(<a href="#top">Top</a>)</p>


## Terminology

1. **Parent HTML File**: This is the file wherein the components (reusable or otherwise) to be used by the children are defined.
1. **Child (or Source) HTML File**: This is the file wherein the HTML document is written with the use of components. Basically, this is where development is to be done. Later, this is the file that gets converted into the HTML code that is used and understood by the browser.
1. **Chasse File**: Any file having the extension `.chasse.html` is a Chasse file. This means both parent HTML and Child (or Source) HTML files are both collectively referred to as Chasse files.
1. **Resultant HTML File**: This is the file which gets generated and used by the browser.
1. **Components**: These are blocks of reusable code that can be represented by a name. These names can just be plugged into the HTML documents in place of huge redundant paragraphs of the same thing, over and over again.

<p align="right">(<a href="#top">Top</a>)</p>


## Development Log

Currrent stable version is v1.1.0
1. **Version 1.0.0**:
    - Basic child HTML file parsing to get required components.
    - Parsing parent HTML file for extracting components.
    - Generation of resultant HTML files with the components.
1. **Version 1.1.0**:
    - Option `-l` to view additional application-level logs added.
    - More responsive CLI, with respect to error and success messages.
    - Introduce code conventions and enrich terminologies.
1. **Version 1.1.1**:
    - Linter support for development.
    - Minor refactoring of code.
    - Profiling and metrics.

<p align="right">(<a href="#top">Top</a>)</p>


## Release Log

No official releases yet.

<p align="right">(<a href="#top">Top</a>)</p>
