
   <!-- Turbulent flows generate stochastic data sets both in time and in space. Small uncertainties in the initial and boundary conditions quickly amplify, rendering a deterministic description of individual turbulent fluctuations impossible. Often possible is, however, the prediction of statistical quantities (statistical moments, correlations, probability distributions). 
   **Increased transport and mixing**:  the generation of sharp gradients and increased contact surfaces allow molecular diffusion to become relevant  Turbulent flows generally show strongly increased mixing and transport rates of matter, heat, and momentum. As shown above, the reason for this is the generation of sharp gradients and increased contact surfaces due to the complex strain field associated with the turbulent motions.  -->

   <!-- . These vortices (often called “eddies” in oceanography) involve a wide range of spatial wave lengths, ranging from the largest scales imposed by the bounding geometry down to the smallest scales, where eddies are dissipated due to molecular (viscous) smoothing.  -->

Turbulence is “dissipative”, meaning that kinetic energy is dissipated into heat due to viscous friction at the smallest scales. Similarly, also scalar fluctuations are smoothed (or dissipated) be molecular diffusion, implying that the overall scalar variance is reduced (see our coffee example). Thus, a mechanism must exist transporting energy and scalar variance from the largest scales, where they are introduced to the system, towards the smallest scales, where they are dissipated. As shown in later sections, this mechanism is tightly connected to the non-linear advection terms in the transport equations.


$
\text{Tracer flux} = \frac{\partial}{\partial z} \left( \kappa_\rho \frac{\partial \text{ Tracer density}}{\partial z} \right) \quad  \text{with}\quad  \kappa_\rho = \varGamma \frac{\varepsilon}{N^2}
$

$$
\frac{\partial \text{TKE}}{\partial t} + \frac{\partial \mathcal{T}_k}{\partial z} = P +G - \varepsilon
$$

$$
\partial_t \text{TKE} +\partial_j \left(\bar{u}_j \text{TKE}+\frac{1}{2}\left\langle u_i^{\prime} u_i^{\prime} u_j^{\prime}\right\rangle-2 \nu\left\langle u_i^{\prime} S_{i j}^{\prime}\right\rangle+\frac{\left\langle u_j^{\prime} p^{\prime}\right\rangle}{\rho_0}\right) =
$$

$$
-\langle u_i^{\prime} u_j^{\prime}\rangle \bar{S}_{i j}- \frac{g}{\rho_0}\langle u_3^{\prime} \rho^{\prime}\rangle- 2 \nu\langle S_{i j}^{\prime} S_{i j}^{\prime}\rangle 
$$