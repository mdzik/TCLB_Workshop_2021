---
title: "LBM Workshop: Role of diffusion-reaction equations in epidemic modelling"
author: G. Gruszczynski, M. Dzikowski
date: "November 25-26, 2021"
output: html_document
---

The lattice Boltzmann method (LBM) is a widely used numerical scheme for solving both the Navier-Stokes
equation (NSE) and advection-diﬀusion problems.
Its popularity has signiﬁcantly risen in the recent three decades due to its ability to handle complex boundary shapes and its relative ease of implementation and parallelisation.
Furthermore, its mesoscopic formulation allows physics to be introduced at a lower level than, for example, a ﬁnite-volume or ﬁnite-element discretisation of the governing equations may allow.

In this event, we will show the state-of-the-art application of the LBM to the diffusion-reaction problems.
During the workshop, a system of equations describing the dynamics of the epidemic will be solved using LBM.

<img src="../images/zaraza_0109.jpeg" alt="drawing" width="600"/>

<style>
.workshop_image {
display: inline-block;
width: 300px;
/* max-width: 20%;
max-height: 20%; */
}
</style>

The generic model encapsulated in the TCLB environment can be compiled to solve different sets of advection-reaction-diffusion equations coupled with Navier-Stokes equations.
Apart from forecasting the epidemic dynamics, the model can handle problems like phase change or rock dissolution.

<div id="banner" style="overflow: hidden; display: inline-block;">
    <div class="workshop_image">
        <img src ="../images/c1.jpg">
    </div>
    <div class="workshop_image">
        <img src ="../images/c8.jpg">
    </div>
</div>

**Where:**
Uniwersytet Wrocławski, pl. Maxa Borna 9, 50-204 Wrocław, sala 119 (1 piętro)/Online

**When:**
25-26 XI 2021

**Why:**
To share knowledge regarding the Lattice Boltzmann Method and better understand the epidemics' dynamic.

**Speakers:**
M. Dzikowski, G. Gruszczyński

**Target Audience:**
The expected audience are university students and researchers from both academia and industry.
No prior knowledge of the Lattice Boltzmann Method or epidemic modelling is required.

**Software/Hardware Requirements:**
Bring your own laptop with a recent web browser (workshop part).
The materials will be hosted online using the jupyter environment.

**Course Delivery:**
The workshops will be held in polish.
The materials will be available online, in english.

**Price:**
Free.

**Funded by:**
Warsaw University of Technology, IDUB against COVID-19

**Open workshop:**
The workshop is organised as a non-profit event.
It is open to the interested general public.

**Registration:**
Please contact us at:

m.dzikowski([monkey](https://en.wikipedia.org/wiki/At_sign#Names_in_other_languages))icm.edu.pl

ggruszczynski([monkey](https://en.wikipedia.org/wiki/At_sign#Names_in_other_languages))meil.pw.edu.pl

## Agenda

### Thursday, 25 XI

| Time     | Topic                                                                             |
-----------|-----------------------------------------------------------------------------------|
| 14:00    | Introduction to the Lattice Boltzmann Method                                      |
| 15:00    | LBM for reaction-diffusion equation                                               |
| 16:00    | Reaction-diffusion: system of ODE                                                 |
| 17:00    | Bring-Your-Own-Laptop: How to run TCLB                                            |
| 18:00    | Social event :)

### Friday, 26 XI

| Time     | Topic                                                                             |
-----------|-----------------------------------------------------------------------------------|
| 10:00    | Introduction to the SIR epidemiological model                                     |
| 11:00    | Convolution, stability, FD solvers                                                |
| 12:00    | Introduction to TCLB, simple flow model                                           |
| 14:00    | Benchmarking the spatial-SIR epidemiological model                                |
| 15:00    | Lunch break                                                                       |
| 16:00    | Dockerized examples, HDF5                                                         |
| 17:00    | R binding, Python binding                                                         |
| 18:00    | End of workshop                                                                   |
