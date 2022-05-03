# openCV_projects
All my project to train openCV library in python
<div id="top"></div>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/zEhmsy/openCV_projects/images/logo">
    <img src="images/logo_auto.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">OPENCV_project</h3>

  <p align="center">
    project_description
    <br />
    <a href="https://github.com/zEhmsy/openCV_projects"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/zEhmsy/openCV_projects">View Demo</a>
    ·
    <a href="https://github.com/zEhmsy/openCV_projects/issues">Report Bug</a>
    ·
    <a href="https://github.com/zEhmsy/openCV_projects/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#progetto">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://docs.opencv.org/4.x/d1/dfb/intro.html)

### OpenCV project made for training this python library

OpenCV (Open Source Computer Vision Library: http://opencv.org) is an open-source library that includes several hundreds of computer vision algorithms. The document describes the so-called OpenCV 2.x API, which is essentially a C++ API, as opposed to the C-based OpenCV 1.x API (C API is deprecated and not tested with "C" compiler since OpenCV 2.4 releases)

OpenCV has a modular structure, which means that the package includes several shared or static libraries. The following modules are available:

* **Core functionality (core)** - a compact module defining basic data structures, including the dense multi-dimensional array Mat and basic functions used by all other modules.
* **Image Processing (imgproc)** - an image processing module that includes linear and non-linear image filtering, geometrical image transformations (resize, affine and perspective warping, generic table-based remapping), color space conversion, histograms, and so on.
* **Video Analysis (video)** - a video analysis module that includes motion estimation, background subtraction, and object tracking algorithms.
* **Camera Calibration and 3D Reconstruction (calib3d)** - basic multiple-view geometry algorithms, single and stereo camera calibration, object pose estimation, stereo correspondence algorithms, and elements of 3D reconstruction.
* **2D Features Framework (features2d)** - salient feature detectors, descriptors, and descriptor matchers.
* **Object Detection (objdetect)** - detection of objects and instances of the predefined classes (for example, faces, eyes, mugs, people, cars, and so on).
* **High-level GUI (highgui)** - an easy-to-use interface to simple UI capabilities.
* **Video I/O (videoio)** - an easy-to-use interface to video capturing and video codecs.
... some other helper modules, such as FLANN and Google test wrappers, Python bindings, and others.

![](images/object_detected.gif)

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [Pip](https://pypi.org/project/pip/)
* [OpenCV](https://opencv.org/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Project
### Repository overview
```txt
├── Object_Detect
|   ├── output_files
|   |   \\ Where all recordings are saved 
│   ├── coco.names
|   |   \\ common objects names
│   ├── frozen_inference_graph.pb
|   |   \\ frozen graph
|   ├── main.py
|   |   \\ program
│   ├── ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt
|   |   \\ model and text graph
│   └── test.png
|── OpenCV_tuto
|   ├── assets
|   |   \\ preset file for programs
|   ├── record
|   |   \\ Where all recordings are saved 
|   ├── [1]basic
|   |   ...
|   └── security_camera
|   |   \\ All tutorial followed to learn openCV
|── Security Cam
|   ├── output_files
|   |   \\ Where all recordings are saved 
|   └── main.py
|       \\ program
├── README.md
└── license.txt
```

<!-- ROADMAP -->

## Roadmap

- Topics
  - Manipulate images
  - Control Camera
  - Drawing elements
  - Detection elements
  - Recognize face and eyes
  - Make a security camera program

See the [open issues](https://github.com/zEhmsy/openCV_projects/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites & Installation

1. Clone the repo
   ```sh
   git clone https://github.com/zEhmsy/openCV_projects.git
   ```
2. Install pip packages
   * 1. Launch a command prompt if it isn't already open. To do so, open the Windows search bar, type cmd and click on the icon.
   * 2. Then, run the following command to download the get-pip.py file:

     ```sh
     curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
     ```
3. Install opencv library with pip
   ```python
   pip3 install opencv-python
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Giuseppe Tururro - [@instagram_handle](https://www.instagram.com/turturrogiuseppe/) - info.g.turturro@gmail.com

Project Link: [https://github.com/zEhmsy/openCV_projects](https://github.com/zEhmsy/openCV_projects)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

* [Coding in Python](https://www.wikiwand.com/it/Python)
* [Usage of Pip](https://www.wikiwand.com/en/Pip_(package_manager)#:~:text=pip%20is%20the%20de%20facto,called%20the%20Python%20Package%20Index.)
* [openCV library](https://www.wikiwand.com/it/OpenCV)
* [machine learning via Tensorflow](https://www.tensorflow.org/resources/learn-ml)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->

<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/zEhmsy/openCV_projects.svg?style=for-the-badge
[contributors-url]: https://github.com/zEhmsy/openCV_projects/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/zEhmsy/openCV_projects.svg?style=for-the-badge
[forks-url]: https://github.com/zEhmsy/openCV_projects/network/members
[stars-shield]: https://img.shields.io/github/stars/zEhmsy/openCV_projects.svg?style=for-the-badge
[stars-url]: https://github.com/zEhmsy/openCV_projects/stargazers
[issues-shield]: https://img.shields.io/github/issues/zEhmsy/openCV_projects.svg?style=for-the-badge
[issues-url]: https://github.com/zEhmsy/openCV_projects/issues
[license-shield]: https://img.shields.io/github/license/zEhmsy/openCV_projects.svg?style=for-the-badge
[license-url]: https://github.com/zEhmsy/openCV_projects/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/g-turturro
[product-screenshot]: images/proj_info.PNG
