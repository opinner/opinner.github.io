
# Marine Turbulence
<!-- .slide: style="text-align: center; padding: 70px 0;"> -->
Ole Pinner

---

<!-- .slide: style="text-align: center;"> -->
<iframe width="750" height="500" src="https://www.youtube-nocookie.com/embed/dx60zMgrP8c?si=XigMQX2jLH0f9cK3&amp;controls=0&amp;start=270&amp;clip=UgkxFI5A1VWDtfoEXQW0F0Um66B-w0yU5rNk&amp;clipt=ELy5EBi3lhE" title="YouTube video player" frameborder="3" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

# :x poem
Big whirls have little whirls  
that feed on their velocity,  
And little whirls have lesser whirls  
and so on to viscosity  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Lewis F. Richardson, 1922](https://en.wikipedia.org/wiki/Energy_cascade\#cite_note-1)

### What is turbulence anyway?
<!-- .slide: style="text-align: left;"> -->

It is hard to define turbulence precisely. But we can describe by (at minimum) the following properties: <!-- Inspired by and adapted from the lecture script of Umlauf and Burchard --> 
  1. Random and chaotic: Turbulent "hot spots" are patchy and intermittent and can only be described statistically <!-- Turbulent flows generate stochastic data sets both in time and in space. Small uncertainties in the initial and boundary conditions quickly amplify, rendering a deterministic description of individual turbulent fluctuations impossible. Often possible is, however, the prediction of statistical quantities (statistical moments, correlations, probability distributions). --> 
  2. Increased transport and mixing:  the generation of sharp gradients and increased contact surfaces allow molecular diffusion to become relevant <!-- Turbulent flows generally show strongly increased mixing and transport rates of matter, heat, and momentum. As shown above, the reason for this is the generation of sharp gradients and increased contact surfaces due to the complex strain field associated with the turbulent motions.  -->
  3. Vorticity: Turbulent flows exhibit vortices, whirls, and eddying motions <!-- . These vortices (often called “eddies” in oceanography) involve a wide range of spatial wave lengths, ranging from the largest scales imposed by the bounding geometry down to the smallest scales, where eddies are dissipated due to molecular (viscous) smoothing.  -->
  4. Dissipative: Energy is transported from [: large to small scales](#poem) <!-- Turbulence is “dissipative”, meaning that kinetic energy is dissipated into heat due to viscous friction at the smallest scales. Similarly, also scalar fluctuations are smoothed (or dissipated) be molecular diffusion, implying that the overall scalar variance is reduced (see our coffee example). Thus, a mechanism must exist transporting energy and scalar variance from the largest scales, where they are introduced to the system, towards the smallest scales, where they are dissipated. As shown in later sections, this mechanism is tightly connected to the non-linear advection terms in the transport equations. -->

---

### What is turbulence anyway?
<!-- .slide: style="text-align: left;"> -->
- <a href="https://github.com/user-attachments/assets/2b0c657b-fbc5-4917-8bfb-1cd6881f042f" data-preview-link>Chaotic movement of fluid </a> [(Klein et al, 2008)](https://doi.org/10.1175/2007JPO3773.1)
- Chaotic movement of fluid [(Klein et al, 2008)](https://doi.org/10.1175/2007JPO3773.1) <img src="/images/turbulence.png" height="50" data-preview-image />
- [: Transport of energy in a cascade from large to small scales](#poem) 
- Finally, at Kolmogorov microscales 
- Cause of diapycnal mixing (in contrast to horizontal/isopycnal sub-mesoscale stirring)  
- Despite the chaos, turbulence exhibits [:self similarity across scales](https://www.youtube.com/watch?v=_UoTTq651dE)

---

### Why is it important for Climate Research?
<!-- .slide: style="text-align: left;"> -->

- Surface Mixing: carbon & oxygen exchange between tmosphere and ocean
- Interior Mixing: overturning circulation
- Bottom Mixing: upwelling, benthic life

Notes: Add examples and images

---

### Quantification
<!-- .slide: style="text-align: left;"> -->

Appears as a sink term in TKE equation, dependent on tensor of small-scale shear variations (Chap.7, Meredith2022)
$$
\begin{aligned}
\frac{1}{2}\Biggl[\frac{\partial \overline{u_i^{\prime} u_i^{\prime}}}{\partial t} &+ \bar{u}_j \frac{\partial \overline{u_i^{\prime} u_i^{\prime}}}{\partial x_j}\Biggr] &+ &\overline{u_i^{\prime} u_j^{\prime} \frac{\partial \bar{u}_i+u_i^{\prime}}{\partial x_j}} &\cong  &- \rho_0^{-1} \frac{\partial}{\partial x_i} \overline{u_i^{\prime} p^{\prime}} &+  &\overline{b^{\prime} w^{\prime}}  -\underbrace{\frac{\nu}{2} \overline{\Biggl(\frac{\partial u_i}{\partial x_j} + \frac{\partial u_j}{\partial x_i}\Biggr)^2}} \\
&\frac{d}{d t} \text{TKE} &- &\underbrace{\mathcal{P}_k}_{\mathclap{\text{turbulent production}\quad}} + \overbrace{\text{N.L.}}^{\mathclap{\text{nonlinear transports}}} &\cong &\underbrace{P_{\text{work}}}_{\mathclap{\text{pressure work}}} &+ &\overbrace{\mathcal{B}}^{\mathclap{\text{buoyancy flux}}} - \quad \quad \underbrace{\varepsilon}_{\mathclap{\text{dissipation rate}}}.
\end{aligned}
$$
The rate of kinetic energy $E = \frac{1}{2} u_i u_i$ dissipating/lost to heat (per mass unit), with the units $\mathrm{J}\,\mathrm{s}^{-1}\mathrm{kg}^{-1}=\mathrm{W}\,\mathrm{kg}^{-1}$.

---

### Some History
<!-- .slide: style="text-align: left;"> -->

- 1941 Kolmogorov, A. N. ()
- 1966 Munk Abyssal recipes
- 1972 Garret & Munk Theoretical description of the internal wave field
- 1980 Osborn Relation of turbulence and mixing
- 

Note: The Study of Mixing in the Ocean: A Brief History Gregg 1981 10.5670/oceanog.1991.21

---



---

# :x Osborn1980
tba

# :x Gregg2018
The [33 page review paper](https://doi.org/10.1146/annurev-marine-121916-063643) solely about the value of the mixing efficiency concludes that 
"*Nonetheless, observations should continue to be scaled with 0.2 until observations, laboratory experiments, and numerical simulations converge on a more accurate formulation. In the meantime, published results should include as many parameters as possible to aid in understanding efficiency and allow subsequent recalculation of turbulent diffusivity.*" 

### Relation to Mixing
<!-- .slide: style="text-align: left;"> -->

Assuming no advection and turbulent transport, the steady-
state budget equation for turbulent kinetic energy (TKE) simplifies to PS 1 B 5
e, with the production of TKE from mean
flow shear PS and the buoyancy flux B, balancing the viscous
dissipation
e (see methods section). In stable stratification,
B is a sink for the TKE budget. 

An often used approach is (turbulent) diapycnal diffusivity 
Time evolution fo bouyancy $b=-g \rho /\rho_0$

$ \frac{\partial b}{\partial t} $

$ \kappa_\rho = \varGamma \frac{\varepsilon}{N^2}$ ([Osborn relation](#Osborn1980))
$$
\text{\small mixing efficiency }\varGamma := \frac{\substack{\text{\small change in background potential energy}\newline \text{\small due to mixing}}}{\text{\small Energy expended}} \approx 0.2 
$$
We are pretty sure $\varGamma$ is not constant [:(Gregg et al., 2018)](#Gregg2018), but varies over magnitudes. But we also have no consistent theory, so we are still using a value from the 80s.

---

# :x internal waves
rabbit hole  ([near-inertial](https://www.annualreviews.org/doi/10.1146/annurev-marine-010814-015746), internal tides, [lee waves](https://www.annualreviews.org/doi/10.1146/annurev-fluid-051220-043904))

## So what is causing turbulence?
<!-- .slide: style="text-align: left;"> -->
  - Surface waves 
  - [: Internal Waves](#internalwaves)
  - Instabilities (symmetric, baroclinic)

Much of the mixing happens over rough bathymetry or at the continental 

---

# :x eddy covariance

# :x PIV

# :x observations
For example[:eddy covariance](#eddycovariance) or [:PIV](#PIV)

# :x models
Direct numerical simulation (DNS) of the Navier Stokes equations. 

### Estimating marine turbulence
<!-- .slide: style="text-align: left;"> -->
- Very few [:observational methods](#observations) or [:numerical models](#models) can resolve turbulent scales directly 
- General need for parameterizations (in models and observations)
- Parameterizations from observational data range from more to less trustworthy, dependent on their measured scales
    - Microstructure (often THE gold standard)
    - Finestructure
    - Overturns 
    

---

# :x passive
Meaning, mixing does not change how the ocean adjusts to changes in climatic forcing. 
Diffusive coefficients in models are prescribed and not dynamically adjusted. But recent findings indicate otherwise. Many fast interactions between mixing processes and large scale behavior were found ([Meredith2022, Chapter 1 and references therein](https://doi.org/10.1016/C2019-0-03674-6))

# :x artemics
Development of a parameterization of internal waves in the Arctic Ocean and use in climate models to research links and feedback mechanisms between declining sea ice, wave-induced mixing, stratification and heat transport. 

### What are current research questions?
<!-- .slide: style="text-align: left;"> -->

- Ocean mixing is almost always described as [:dynamically passive.](#passive)

- @AWI: new [:Emmy Noether group Artemics](#artemics) in Climate Dynamics by Friederike Pollmann

Notes: Arctic: Rippeth Changing Ocean Antarctic Silvano, Bennets2024
---

# :x Caul2021
Layering, Instabilities, and Mixing in Turbulent Stratified Flows, 

# :x Bennetts2024
tba

### Some quotes
<!-- .slide: style="text-align: left;"> -->

"Although there has been a large range of deeply insightful research contributions to our understanding of transition, turbulence, and irreversible mixing in stratified fluids, it still remains extremely difficult to say anything generic about mixing." [:*(Caul et al., 2021)*](#Caul2021)

"The trends in mixing are difficult and, in many cases, nearly impossible to assess." [:(Bennetts et al., 2024)](#Bennetts2024)

---

### Recommended Literature
<!-- .slide: style="text-align: left;"> -->

- [Lecture notes (2020) by Lars Umlauf and Hans Burchard](https://www.io-warnemuende.de/files/staff/umlauf/turbulence/turbulence.pdf)
- [Ocean mixing: drivers, mechanisms and impacts, Meredith, Naveira Garabato et al., 2022](https://doi.org/10.1016/C2019-0-03674-6)

---

## Math test
<!-- .slide: style="text-align: left;"> -->

This should be  $\sqrt{a^2 + b^2}$ rendered by: 
```
$\pm\sqrt{a^2 + b^2}$
```
This is subsequent text and a test of autorender.
The expected value or ensemble mean of $z(t)$ is
$$\eta(t)\equiv\mathrm{E}z(t)$$

---

## Lightbox Test

<img src="https://os.copernicus.org/articles/21/701/2025/os-21-701-2025-avatar-web.png" align="right" height="300" data-preview-image />

---

## Fragment test

- Item 1 <!-- .element: class="fragment" data-fragment-index="1" -->
- Item 2 <!-- .element: class="fragment" data-fragment-index="2" -->
