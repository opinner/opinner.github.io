
# Marine Turbulence
<!-- .slide: style="text-align: center; padding: 70px 0;"> -->
Ole Pinner

---

## Quote
<!-- .slide: style="text-align: left;"> -->
<iframe width="800" height="600" src="https://www.youtube-nocookie.com/embed/dx60zMgrP8c?si=XigMQX2jLH0f9cK3&amp;controls=0&amp;start=270&amp;clip=UgkxFI5A1VWDtfoEXQW0F0Um66B-w0yU5rNk&amp;clipt=ELy5EBi3lhE" title="YouTube video player" frameborder="0" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

## What is turbulence anyway?
<!-- .slide: style="text-align: left;"> -->
- Cause of diapycnal mixing (in contrast to horizontal/isopycnal sub-mesoscale stirring)


---

## Some definitions
<!-- .slide: style="text-align: left;"> -->
The rate of kinetic energy $E = \frac{1}{2} u_i u_i$ dissipating/lost to heat. 
Appears as a sink term in TKE equation, dependent on tensor of small-scale shear variations.

<!--
$$
\frac{\partial E}{\partial t}+u_i \frac{\partial E}{\partial x_i}-2 \frac{\partial \nu u_i S_{i j}}{\partial x_j}+\frac{1}{\rho_0} \frac{\partial u_i p}{\partial x_i}=-2 \nu S_{i j} S_{i j}+\frac{\rho}{\rho_0} u_i g_i
$$
-->

$$
\frac{\partial E}{\partial t}+u_i \frac{\partial E}{\partial x_i}-2 
$$

---

# :x Gregg2018
[33 pages of review paper just about the value of the mixing efficiency ](https://doi.org/10.1146/annurev-marine-121916-063643)
> Nonetheless, observations should continue to be scaled with 0.2 until observations, laboratory experiments, and numerical simulations converge on a more accurate formulation. In the meantime, published results should include as many parameters as possible to aid in understanding efficiency and allow subsequent recalculation of $K_\rho$. 

## Mixing

Osborn relation for turbulent diffusivity $ \kappa_\rho = \varGamma \frac{\varepsilon}{N^2}$. 

$$
\text{mixing efficiency}\:\varGamma := \frac{\text{\small change in background potential energy due to mixing}}{\text{Energy expended}} \approx 0.2 
$$

$$
\text{\small mixing efficiency}\:\varGamma := \frac{\substack{\text{\small change in background potential energy}\\ \text{\small due to mixing}}}{\text{\small Energy expended}} \approx 0.2 
$$

We are pretty sure $\varGamma$ is not constant and varies instead even in its magnitude. 
But we also have no consistent theory, so we are still using the value from the 80s [:(Gregg et al., 2018)](#Gregg2018)

---

# :x Caul2021
Layering, Instabilities, and Mixing in Turbulent Stratified Flows, 

# :x Bennetts2024
test2

## Some quotes

> Although there has been a large range of deeply insightful research contributions to our understanding of transition, turbulence, and irreversible mixing in stratified fluids, it still remains extremely difficult to say anything generic about mixing. [:*(Caul et al., 2021)*](#Caul2021)

> The trends in mixing are difficult and, in many cases, nearly impossible to assess. [:(Bennetts et al., 2024)](#Bennetts2024)

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

## Some definitions
<!-- .slide: style="text-align: left;"> -->

---

## Math test
<!-- .slide: style="text-align: left;"> -->

This should be  $\\sqrt{a^2 + b^2}$ rendered by: 
```
$\pm\sqrt{a^2 + b^2}$
```
This is subsequent text and a test of autorender.
The expected value or ensemble mean of $z(t)$ is
$$\eta(t)\equiv\mathrm{E}z(t)$$