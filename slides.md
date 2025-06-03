
# Marine Turbulence
<!-- .slide: style="text-align: center; padding: 70px 0;"> -->
Ole Pinner

---

<!-- .slide: style="text-align: center;"> -->
<iframe width="700" height="500" src="https://www.youtube-nocookie.com/embed/dx60zMgrP8c?si=XigMQX2jLH0f9cK3&amp;controls=0&amp;start=270&amp;clip=UgkxFI5A1VWDtfoEXQW0F0Um66B-w0yU5rNk&amp;clipt=ELy5EBi3lhE" title="YouTube video player" frameborder="3" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>



---

## What is turbulence anyway?
<!-- .slide: style="text-align: left;"> -->

- <a href="/images/turbulence.png" data-preview-link>Chaotic movement of fluid </a> [(Source)](10.1175/2007JPO3773.1)
- "Turbulent hot spots" are patchy and intermittent
- [: Transport of energy in a cascade from large to small scales](#poem) 
- Finally, at Kolmogorov microscales allow for  molecular viscosity 
- Cause of diapycnal mixing 
- (in contrast to horizontal/isopycnal sub-mesoscale stirring)  

# :x poem
  Big whirls have little whirls  
  that feed on their velocity,  
  And little whirls have lesser whirls  
  and so on to viscosity  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [Lewis F. Richardson, 1922](https://en.wikipedia.org/wiki/Energy_cascade\#cite_note-1)

---

## Why is it important for Climate Research?

- Surface Mixing: Carbon & oxygen exchange, 
- Interior Mixing: Overturning
- Bottom Mixing: Upwelling, benthic life

Notes: Add examples and images

---

## Quantification
<!-- .slide: style="text-align: left;"> -->

The rate of kinetic energy $E = \frac{1}{2} u_i u_i$ dissipating/lost to heat per mass unit.
in units of $\frac{\mathrm{J}}{\mathrm{s} \mathrm{kg}}$ 
Appears as a sink term in TKE equation, dependent on tensor of small-scale shear variations.

$$
\frac{\partial E}{\partial t}+u_i \frac{\partial E}{\partial x_i}-2 \frac{\partial \nu u_i S_{i j}}{\partial x_j}+\frac{1}{\rho_0} \frac{\partial u_i p}{\partial x_i}=-2 \nu S_{i j} S_{i j}+\frac{\rho}{\rho_0} u_i g_i
$$


$$
\frac{\partial E}{\partial t}+u_i \frac{\partial E}{\partial x_i}-2 
$$

---

# :x Osborn 

# :x Gregg2018
[33 page review paper](https://doi.org/10.1146/annurev-marine-121916-063643) solely about the value of the mixing efficiency. It concludes
"*Nonetheless, observations should continue to be scaled with 0.2 until observations, laboratory experiments, and numerical simulations converge on a more accurate formulation. In the meantime, published results should include as many parameters as possible to aid in understanding efficiency and allow subsequent recalculation of turbulent diffusivity.*" 

## Relation to Mixing
<!-- .slide: style="text-align: left;"> -->

turbulent diffusivity $ \kappa_\rho = \varGamma \frac{\varepsilon}{N^2}$ (Osborn relation)
$$
\text{\small mixing efficiency }\varGamma := \frac{\substack{\text{\small change in background potential energy}\newline \text{\small due to mixing}}}{\text{\small Energy expended}} \approx 0.2 
$$
We are pretty sure $\varGamma$ is not constant. It can even vary over magnitudes. 
But we also have no consistent theory, so we are still using the value from the 80s [:(Gregg et al., 2018)](#Gregg2018)

---

# :x observations
For example[:eddy covariance](#eddy covariance) or [:PIV](#PIV)

# :x models
Direct numerical simulation (DNS) of the Navier Stokes equations. 

## Measuring marine turbulence
<!-- .slide: style="text-align: left;"> -->
- Very few [:observational methods](#observations) or [:numerical models](#models) can resolve turbulent scales directly 
- General need for parameterizations (in models and observations)

---

## So what is causing turbulence?
  - test1

---

# :x passive
Meaning, mixing does not change how the ocean adjusts to changes in climatic forcing. 
Diffusive coefficients in models are prescribed and not dynamically adjusted. But recent findings indicate otherwise. Many fast interactions between mixing processes and large scale behavior were found ([Meredith2022, Chapter 1 and references therein](https://doi.org/10.1016/C2019-0-03674-6))

# :x artemics
Development of a parameterization of internal waves in the Arctic Ocean and use in climate models to research links and feedback mechanisms between declining sea ice, wave-induced mixing, stratification and heat transport. 

## What are current research questions?
<!-- .slide: style="text-align: left;"> -->

- Ocean mixing is almost always described as [:dynamically passive.](#passive)

- At AWI: new [:Emmy Noether group Artemics](#artemics) in Climate Dynamics by Friederike Pollmann

---

# :x Caul2021
Layering, Instabilities, and Mixing in Turbulent Stratified Flows, 

# :x Bennetts2024
tba

## Some quotes
<!-- .slide: style="text-align: left;"> -->

"Although there has been a large range of deeply insightful research contributions to our understanding of transition, turbulence, and irreversible mixing in stratified fluids, it still remains extremely difficult to say anything generic about mixing." [:*(Caul et al., 2021)*](#Caul2021)

> The trends in mixing are difficult and, in many cases, nearly impossible to assess. [:(Bennetts et al., 2024)](#Bennetts2024)

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