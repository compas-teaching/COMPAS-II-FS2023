# COMPAS II

> 064-0026-00L Introduction to Computational Methods for Digital Fabrication in Architecture

This PhD-level course introduces digital fabrication methods and tools building up on the theoretical and practical knowledge acquired in the prerequisite course. Students learn fundamentals of robotics, robot kinematics and planning, and basics of robot control applied in the domain of architecture and digital fabrication using the COMPAS framework and open source tools.

## Schedule, FS 2023

| Lecture | Date   | Session content                                                                                                                                                                                                                                                                                                                                                                                                                          | Session leads      |
|---------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| 01      | 20.02. | **Introduction**<br>Introduction to digital fabrication methods and the COMPAS ecosystem for digital fabrication: `core`, `fab`, `rrc`, `slicer`.<br>Brief overview of geometry kernel and core data structures (network, mesh).<br>Remote procedure calls.<br>👉 [Go to lecture](lecture_01)                                                                                                                                            | All                |
| 02      | 27.02. | **Robotic fundamentals**<br>Introduction to robotics: anatomy of an industrial robot, coordinate systems, transformations.<br>Kinematic functions and path planning.<br> 👉 [Go to lecture](lecture_02)                                                                                                                                                                                                                                  | GKR (GC)           |
| 03      | 06.03. | **Robot models**<br>URDF and programmatic API.<br>Robot model visualization in Rhino / Grasshopper.<br>Forward kinematics of open chain manipulators.<br>Assignment: model your own robot.<br> 👉 [Go to lecture](lecture_03)                                                                                                                                                                                                            | GKR (GC)           |
| 04      | 13.03. | **Path planning with ROS & MoveIt in the design environment**<br>Introduction to ROS, topics, services, actions. Basic interprocess communication via ROS nodes.<br>Robot planning: forward and inverse kinematic functions, cartesian and kinematic planning.<br>Planning scene operations. End effectors and discrete build elements.<br>👉 [Go to lecture](lecture_04)                                                                | GKR (GC)           |
| 05      | 27.03. | **Robot control with COMPAS RRC**<br>Online non-real time control of industrial robots. Components of an RRC deployment. Communication primitives (blocking, futures, cyclic). Instructions. Multi controller & location coordination.<br>                                                                                                                                                                                               | GKR (GC)           |
| 06      | 03.04. | **Assembly of discrete elements I**<br>Brief introduction to directed acyclic graphs. Modelling assembly processes as DAGs. Reachability Maps. Designing an assembly for fabrication.<br>                                                                                                                                                                                                                                                | GKR (GC)           |
| 07      | 24.04. | **Assembly of discrete elements II**<br>Applied exercise from design to planning fabrication for an assembly of discrete elements<br>                                                                                                                                                                                                                                                                                                    | GKR (GC)           |
| 08      | 08.05. | **Assembly of discrete elements III**<br>Continued applied exercise from planning data to robot control for an assembly of discrete elements.<br>                                                                                                                                                                                                                                                                                        | GKR (GC)           |
| 09      | 15.05. | **COMPAS SLICER**<br>Introduction to COMPAS SLICER.<br>Planar and non-planar slicing of simple geometry<br>Introducion to scalar field slicing<br>Customizing compas_slicer functions<br>                                                                                                                                                                                                                                                | DBT (IM)           |
| 10      | 22.05. | **Design to Fabrication workflows & Advancing computational research**                                                                                                                                                                                                                                                                                                                                                                   | GKR (GC)           |

## Information

Links:
[Course info on ETHZ Catalog](https://www.vvz.ethz.ch/Vorlesungsverzeichnis/lerneinheit.view?semkez=2023S&ansicht=ALLE&lerneinheitId=168977&lang=en) |
[Slack workspace](https://join.slack.com/t/compasii/shared_invite/zt-1pmf19rxu-a1K~2b9EuCqN9Tz49~szZg) |
[COMPAS docs](https://compas.dev)

![COMPAS II course](cover.jpg)

### Objectives

1. Understand fundamentals of robotics, coordinate systems, transformations and orientation representations.
1. Learn forward and inverse kinematic functions and their application.
1. Learn Cartesian and kinematic robot planning methods
1. Apply these concepts to design and implement digital fabrication processes.
1. Gain an understanding of different robot control methods and their application.
1. Learn how to generate fabrication data for a (robotic) 3D printing process using a custom slicing method.

### Content

Lectures, tutorials and project-based exercises will focus on:

* Introduction to fundamentals of robotics.
* Introduction to COMPAS framework and core extensions for digital fabrication (fab, rrc, slicer)
* Robot model representations.
* Robot forward and inverse kinematics.
* Robot path planning: Cartesian motion planning and kinematic motion planning, planning scene and collision detection.
* Integration of planning tools into parametric design environment (CAD).
* Overview and usage of ROS (Robot Operating System).
* Design of digital fabrication processes (assembly of discrete elements, 3D printing, etc.).

## Requirements

* Minimum OS: Windows 10 Pro or Mac OS Sierra 10.12
* [Anaconda 3](https://www.anaconda.com/distribution/)
* [Docker Desktop](https://www.docker.com/products/docker-desktop) After installation on Windows, it is required to enable "Virtualization" on the BIOS of the computer.
* [Rhino 6/7 & Grasshopper](https://www.rhino3d.com/download)
* [Visual Studio Code](https://code.visualstudio.com/): Any python editor works, but we recommend VS Code + extensions [as mentioned in our docs](https://gramaziokohler.github.io/compas_fab/latest/getting_started.html#working-in-visual-studio-code-1)

## Installation

We use `conda` to make sure we have clean, isolated environment for dependencies.

<details><summary>First time using <code>conda</code>?</summary>
<p>

Make sure you run this at least once:

    (base) conda config --add channels conda-forge

</p>
</details>

    (base) conda env create -f https://dfab.link/fs2023.yml

### Add to Rhino

    (base)   conda activate fs2023
    (fs2023) python -m compas_rhino.install -v 7.0

### Get the workshop files

    (fs2023) cd Documents
    (fs2023) git clone https://github.com/compas-teaching/COMPAS-II-FS2023

### Verify installation

    (fs2023) python -m compas

    Yay! COMPAS is installed correctly!

    COMPAS: 1.17.5
    Python: 3.10.9 (CPython)
    Extensions: ['compas-occ', 'compas-cgal', 'compas-fab', 'compas-rrc', 'compas-slicer']

### Update installation

To update your environment:

    (fs2023) conda env update -f https://dfab.link/fs2023.yml
