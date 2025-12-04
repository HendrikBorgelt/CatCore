# Simulation

The data class 'Simulation' describes the minimum information which should be reported 
with research data for conducting simulations in the field of catalysis.

**Schema Reference:** [Simulation](https://w3id.org/nfdi4cat/catcore/elements/Simulation)

## Slots

<details markdown="1">
<summary><strong>software package (Required, Multivalued)</strong></summary>

**Description:** Software or package used for simulation

**Range:** string

**URI:** [`catcore:software_package`](catcore:software_package)

**Schema Reference:** [software_package](elements/software_package.md)

</details>

<details markdown="1">
<summary><strong>simulation method (Required, Multivalued)</strong></summary>

**Description:** Simulation method used

**Range:** SimulationMethod

**URI:** [`catcore:simulation_method`](catcore:simulation_method)

**Schema Reference:** [simulation_method](elements/simulation_method.md)

**Range Class Details:**

<details markdown="1">
<summary><strong>SimulationMethod</strong></summary>

**Abstract Class**

**Description:** Simulation method used

**Schema Reference:** [SimulationMethod](elements/SimulationMethod.md)

</details>

**Subclasses of SimulationMethod:**

<details markdown="1">
<summary><strong>DFT</strong></summary>

**Description:** Density functional theory

**URI:** [`catcore:DFT`](catcore:DFT)

**Schema Reference:** [DFT](elements/DFT.md)

**Slots**

<details markdown="1">
<summary><strong>exchange correlation functional (Optional, Multivalued)</strong></summary>

**Description:** Exchange-correlation functional used (e.g., PBE, B3LYP)

**Range:** string

**URI:** [`catcore:exchange_correlation_functional`](catcore:exchange_correlation_functional)

**Schema Reference:** [exchange_correlation_functional](elements/exchange_correlation_functional.md)

</details>

<details markdown="1">
<summary><strong>energy cutoff (Optional, Multivalued)</strong></summary>

**Description:** Energy cutoff for plane wave basis

**Range:** float

**URI:** [`catcore:energy_cutoff`](catcore:energy_cutoff)

**Schema Reference:** [energy_cutoff](elements/energy_cutoff.md)

**Unit:** eV

</details>

<details markdown="1">
<summary><strong>convergence criteria (Optional, Multivalued)</strong></summary>

**Description:** Convergence criteria (e.g., energy, force)

**Range:** string

**URI:** [`catcore:convergence_criteria`](catcore:convergence_criteria)

**Schema Reference:** [convergence_criteria](elements/convergence_criteria.md)

</details>

<details markdown="1">
<summary><strong>dft u parameters (Optional, Multivalued)</strong></summary>

**Description:** DFT+U parameters used

**Range:** string

**URI:** [`catcore:dft_u_parameters`](catcore:dft_u_parameters)

**Schema Reference:** [dft_u_parameters](elements/dft_u_parameters.md)

</details>

<details markdown="1">
<summary><strong>spin polarization (Optional, Multivalued)</strong></summary>

**Description:** Spin polarization setting

**Range:** boolean

**URI:** [`catcore:spin_polarization`](catcore:spin_polarization)

**Schema Reference:** [spin_polarization](elements/spin_polarization.md)

</details>

<details markdown="1">
<summary><strong>total energy per atom (Optional, Multivalued)</strong></summary>

**Description:** Total energy per atom

**Range:** float

**URI:** [`catcore:total_energy_per_atom`](catcore:total_energy_per_atom)

**Schema Reference:** [total_energy_per_atom](elements/total_energy_per_atom.md)

**Unit:** eV

</details>

</details>

<details markdown="1">
<summary><strong>MolecularDynamics</strong></summary>

**Description:** Molecular dynamics

**URI:** [`NCIT:C18097`](NCIT:C18097)

**Schema Reference:** [MolecularDynamics](elements/MolecularDynamics.md)

**Slots**

<details markdown="1">
<summary><strong>force field (Optional, Multivalued)</strong></summary>

**Description:** Force field used

**Range:** string

**URI:** [`catcore:force_field`](catcore:force_field)

**Schema Reference:** [force_field](elements/force_field.md)

</details>

<details markdown="1">
<summary><strong>simulation timestep (Optional, Multivalued)</strong></summary>

**Description:** Time step for simulation

**Range:** float

**URI:** [`APOLLO_SV:00000012`](APOLLO_SV:00000012)

**Schema Reference:** [simulation_timestep](elements/simulation_timestep.md)

**Unit:** fs

</details>

<details markdown="1">
<summary><strong>simulation time (Optional, Multivalued)</strong></summary>

**Description:** Total simulation time

**Range:** float

**URI:** [`catcore:simulation_time`](catcore:simulation_time)

**Schema Reference:** [simulation_time](elements/simulation_time.md)

**Unit:** ps

</details>

<details markdown="1">
<summary><strong>ensemble type (Optional, Multivalued)</strong></summary>

**Description:** Ensemble type (e.g., NVT, NPT)

**Range:** string

**URI:** [`catcore:ensemble_type`](catcore:ensemble_type)

**Schema Reference:** [ensemble_type](elements/ensemble_type.md)

</details>

<details markdown="1">
<summary><strong>number of atoms (Optional, Multivalued)</strong></summary>

**Description:** Number of atoms in simulation

**Range:** integer

**URI:** [`catcore:number_of_atoms`](catcore:number_of_atoms)

**Schema Reference:** [number_of_atoms](elements/number_of_atoms.md)

</details>

</details>

<details markdown="1">
<summary><strong>Microkinetics</strong></summary>

**Description:** Microkinetics simulation

**URI:** [`catcore:Microkinetics`](catcore:Microkinetics)

**Schema Reference:** [Microkinetics](elements/Microkinetics.md)

**Slots**

<details markdown="1">
<summary><strong>rate constants (Optional, Multivalued)</strong></summary>

**Description:** Rate constants or Arrhenius parameters

**Range:** string

**URI:** [`NCIT:C94967`](NCIT:C94967)

**Schema Reference:** [rate_constants](elements/rate_constants.md)

</details>

<details markdown="1">
<summary><strong>solver type (Optional, Multivalued)</strong></summary>

**Description:** Type of solver used

**Range:** string

**URI:** [`catcore:solver_type`](catcore:solver_type)

**Schema Reference:** [solver_type](elements/solver_type.md)

</details>

<details markdown="1">
<summary><strong>temperature (Optional, Multivalued)</strong></summary>

**Description:** Temperature

**Range:** float

**URI:** [`AFR:0001584`](AFR:0001584)

**Schema Reference:** [temperature](elements/temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>pressure (Optional, Multivalued)</strong></summary>

**Description:** Pressure in simulation

**Range:** float

**URI:** [`catcore:pressure`](catcore:pressure)

**Schema Reference:** [pressure](elements/pressure.md)

**Unit:** bar

</details>

<details markdown="1">
<summary><strong>surface coverage (Optional, Multivalued)</strong></summary>

**Description:** Surface coverage of species

**Range:** float

**URI:** [`catcore:surface_coverage`](catcore:surface_coverage)

**Schema Reference:** [surface_coverage](elements/surface_coverage.md)

</details>

<details markdown="1">
<summary><strong>activation energy (Optional, Multivalued)</strong></summary>

**Description:** Activation energy for each step

**Range:** float

**URI:** [`catcore:activation_energy`](catcore:activation_energy)

**Schema Reference:** [activation_energy](elements/activation_energy.md)

**Unit:** eV

</details>

</details>

<details markdown="1">
<summary><strong>MonteCarlo</strong></summary>

**Description:** Monte Carlo simulation

**URI:** [`catcore:MonteCarlo`](catcore:MonteCarlo)

**Schema Reference:** [MonteCarlo](elements/MonteCarlo.md)

**Slots**

<details markdown="1">
<summary><strong>interaction potential (Optional, Multivalued)</strong></summary>

**Description:** Interaction potential used

**Range:** string

**URI:** [`catcore:interaction_potential`](catcore:interaction_potential)

**Schema Reference:** [interaction_potential](elements/interaction_potential.md)

</details>

<details markdown="1">
<summary><strong>number of steps (Optional, Multivalued)</strong></summary>

**Description:** Number of Monte Carlo steps

**Range:** integer

**URI:** [`catcore:number_of_steps`](catcore:number_of_steps)

**Schema Reference:** [number_of_steps](elements/number_of_steps.md)

</details>

<details markdown="1">
<summary><strong>temperature (Optional, Multivalued)</strong></summary>

**Description:** Temperature

**Range:** float

**URI:** [`AFR:0001584`](AFR:0001584)

**Schema Reference:** [temperature](elements/temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>lattice size type (Optional, Multivalued)</strong></summary>

**Description:** Lattice size and type

**Range:** string

**URI:** [`catcore:lattice_size_type`](catcore:lattice_size_type)

**Schema Reference:** [lattice_size_type](elements/lattice_size_type.md)

</details>

<details markdown="1">
<summary><strong>acceptance criteria (Optional, Multivalued)</strong></summary>

**Description:** Acceptance criteria for Monte Carlo moves

**Range:** string

**URI:** [`catcore:acceptance_criteria`](catcore:acceptance_criteria)

**Schema Reference:** [acceptance_criteria](elements/acceptance_criteria.md)

</details>

<details markdown="1">
<summary><strong>equilibration steps (Optional, Multivalued)</strong></summary>

**Description:** Number of equilibration steps

**Range:** integer

**URI:** [`catcore:equilibration_steps`](catcore:equilibration_steps)

**Schema Reference:** [equilibration_steps](elements/equilibration_steps.md)

</details>

<details markdown="1">
<summary><strong>sampling interval (Optional, Multivalued)</strong></summary>

**Description:** Sampling interval for data collection

**Range:** integer

**URI:** [`catcore:sampling_interval`](catcore:sampling_interval)

**Schema Reference:** [sampling_interval](elements/sampling_interval.md)

</details>

</details>

</details>

<details markdown="1">
<summary><strong>calculated property (Required, Multivalued)</strong></summary>

**Description:** Property calculated from simulation

**Range:** CalculatedProperty

**URI:** [`catcore:calculated_property`](catcore:calculated_property)

**Schema Reference:** [calculated_property](elements/calculated_property.md)

**Range Class Details:**

<details markdown="1">
<summary><strong>CalculatedProperty</strong></summary>

**Abstract Class**

**Description:** Property calculated from simulation

**Schema Reference:** [CalculatedProperty](elements/CalculatedProperty.md)

</details>

**Subclasses of CalculatedProperty:**

<details markdown="1">
<summary><strong>ThermodynamicStability</strong></summary>

**Description:** Thermodynamic stability property

**URI:** [`catcore:ThermodynamicStability`](catcore:ThermodynamicStability)

**Schema Reference:** [ThermodynamicStability](elements/ThermodynamicStability.md)

**Slots**

<details markdown="1">
<summary><strong>formation energy (Optional, Multivalued)</strong></summary>

**Description:** Formation energy per atom

**Range:** float

**URI:** [`catcore:formation_energy`](catcore:formation_energy)

**Schema Reference:** [formation_energy](elements/formation_energy.md)

**Unit:** eV

</details>

<details markdown="1">
<summary><strong>reference energies (Optional, Multivalued)</strong></summary>

**Description:** Reference elemental energies

**Range:** string

**URI:** [`catcore:reference_energies`](catcore:reference_energies)

**Schema Reference:** [reference_energies](elements/reference_energies.md)

</details>

<details markdown="1">
<summary><strong>energy above hull (Optional, Multivalued)</strong></summary>

**Description:** Energy above convex hull

**Range:** float

**URI:** [`catcore:energy_above_hull`](catcore:energy_above_hull)

**Schema Reference:** [energy_above_hull](elements/energy_above_hull.md)

**Unit:** eV

</details>

<details markdown="1">
<summary><strong>phase diagram type (Optional, Multivalued)</strong></summary>

**Description:** Phase diagram type (e.g., binary, ternary)

**Range:** string

**URI:** [`catcore:phase_diagram_type`](catcore:phase_diagram_type)

**Schema Reference:** [phase_diagram_type](elements/phase_diagram_type.md)

</details>

<details markdown="1">
<summary><strong>competing phases (Optional, Multivalued)</strong></summary>

**Description:** Competing phase list

**Range:** string

**URI:** [`catcore:competing_phases`](catcore:competing_phases)

**Schema Reference:** [competing_phases](elements/competing_phases.md)

</details>

</details>

<details markdown="1">
<summary><strong>Piezoelectricity</strong></summary>

**Description:** Piezoelectricity property

**URI:** [`catcore:Piezoelectricity`](catcore:Piezoelectricity)

**Schema Reference:** [Piezoelectricity](elements/Piezoelectricity.md)

**Slots**

<details markdown="1">
<summary><strong>piezoelectric tensor (Optional, Multivalued)</strong></summary>

**Description:** Piezoelectric tensor components

**Range:** string

**URI:** [`catcore:piezoelectric_tensor`](catcore:piezoelectric_tensor)

**Schema Reference:** [piezoelectric_tensor](elements/piezoelectric_tensor.md)

</details>

<details markdown="1">
<summary><strong>crystal symmetry (Optional, Multivalued)</strong></summary>

**Description:** Crystal symmetry

**Range:** string

**URI:** [`catcore:crystal_symmetry`](catcore:crystal_symmetry)

**Schema Reference:** [crystal_symmetry](elements/crystal_symmetry.md)

</details>

<details markdown="1">
<summary><strong>strain applied (Optional, Multivalued)</strong></summary>

**Description:** Strain applied

**Range:** float

**URI:** [`catcore:strain_applied`](catcore:strain_applied)

**Schema Reference:** [strain_applied](elements/strain_applied.md)

</details>

<details markdown="1">
<summary><strong>ionic electronic contributions (Optional, Multivalued)</strong></summary>

**Description:** Ionic and electronic contributions

**Range:** string

**URI:** [`catcore:ionic_electronic_contributions`](catcore:ionic_electronic_contributions)

**Schema Reference:** [ionic_electronic_contributions](elements/ionic_electronic_contributions.md)

</details>

</details>

<details markdown="1">
<summary><strong>ElasticConstants</strong></summary>

**Description:** Elastic constants property

**URI:** [`catcore:ElasticConstants`](catcore:ElasticConstants)

**Schema Reference:** [ElasticConstants](elements/ElasticConstants.md)

**Slots**

<details markdown="1">
<summary><strong>elastic tensor (Optional, Multivalued)</strong></summary>

**Description:** Elastic tensor components

**Range:** string

**URI:** [`catcore:elastic_tensor`](catcore:elastic_tensor)

**Schema Reference:** [elastic_tensor](elements/elastic_tensor.md)

</details>

<details markdown="1">
<summary><strong>bulk modulus (Optional, Multivalued)</strong></summary>

**Description:** Bulk modulus

**Range:** float

**URI:** [`catcore:bulk_modulus`](catcore:bulk_modulus)

**Schema Reference:** [bulk_modulus](elements/bulk_modulus.md)

**Unit:** GPa

</details>

<details markdown="1">
<summary><strong>shear modulus (Optional, Multivalued)</strong></summary>

**Description:** Shear modulus

**Range:** float

**URI:** [`catcore:shear_modulus`](catcore:shear_modulus)

**Schema Reference:** [shear_modulus](elements/shear_modulus.md)

**Unit:** GPa

</details>

<details markdown="1">
<summary><strong>poisson ratio (Optional, Multivalued)</strong></summary>

**Description:** Poisson's ratio

**Range:** float

**URI:** [`catcore:poisson_ratio`](catcore:poisson_ratio)

**Schema Reference:** [poisson_ratio](elements/poisson_ratio.md)

</details>

<details markdown="1">
<summary><strong>young modulus (Optional, Multivalued)</strong></summary>

**Description:** Young's modulus

**Range:** float

**URI:** [`catcore:young_modulus`](catcore:young_modulus)

**Schema Reference:** [young_modulus](elements/young_modulus.md)

**Unit:** GPa

</details>

</details>

<details markdown="1">
<summary><strong>Surfaces</strong></summary>

**Description:** Surface property

**URI:** [`catcore:Surfaces`](catcore:Surfaces)

**Schema Reference:** [Surfaces](elements/Surfaces.md)

**Slots**

<details markdown="1">
<summary><strong>surface energy (Optional, Multivalued)</strong></summary>

**Description:** Surface energy

**Range:** float

**URI:** [`catcore:surface_energy`](catcore:surface_energy)

**Schema Reference:** [surface_energy](elements/surface_energy.md)

**Unit:** J/m2

</details>

<details markdown="1">
<summary><strong>miller indices (Optional, Multivalued)</strong></summary>

**Description:** Miller indices of surface

**Range:** string

**URI:** [`catcore:miller_indices`](catcore:miller_indices)

**Schema Reference:** [miller_indices](elements/miller_indices.md)

</details>

<details markdown="1">
<summary><strong>slab thickness (Optional, Multivalued)</strong></summary>

**Description:** Slab thickness

**Range:** float

**URI:** [`catcore:slab_thickness`](catcore:slab_thickness)

**Schema Reference:** [slab_thickness](elements/slab_thickness.md)

**Unit:** angstrom

</details>

<details markdown="1">
<summary><strong>vacuum spacing (Optional, Multivalued)</strong></summary>

**Description:** Vacuum spacing

**Range:** float

**URI:** [`catcore:vacuum_spacing`](catcore:vacuum_spacing)

**Schema Reference:** [vacuum_spacing](elements/vacuum_spacing.md)

**Unit:** angstrom

</details>

<details markdown="1">
<summary><strong>surface termination method (Optional, Multivalued)</strong></summary>

**Description:** Surface termination method

**Range:** string

**URI:** [`catcore:surface_termination_method`](catcore:surface_termination_method)

**Schema Reference:** [surface_termination_method](elements/surface_termination_method.md)

</details>

</details>

<details markdown="1">
<summary><strong>DielectricTensors</strong></summary>

**Description:** Dielectric tensors property

**URI:** [`catcore:DielectricTensors`](catcore:DielectricTensors)

**Schema Reference:** [DielectricTensors](elements/DielectricTensors.md)

**Slots**

<details markdown="1">
<summary><strong>material composition (Optional, Multivalued)</strong></summary>

**Description:** Material composition

**Range:** string

**URI:** [`catcore:material_composition`](catcore:material_composition)

**Schema Reference:** [material_composition](elements/material_composition.md)

</details>

<details markdown="1">
<summary><strong>crystal structure (Optional, Multivalued)</strong></summary>

**Description:** Crystal structure (space group, lattice parameters)

**Range:** string

**URI:** [`SIO:001100`](SIO:001100)

**Schema Reference:** [crystal_structure](elements/crystal_structure.md)

</details>

<details markdown="1">
<summary><strong>energy cutoff (Optional, Multivalued)</strong></summary>

**Description:** Energy cutoff for plane wave basis

**Range:** float

**URI:** [`catcore:energy_cutoff`](catcore:energy_cutoff)

**Schema Reference:** [energy_cutoff](elements/energy_cutoff.md)

**Unit:** eV

</details>

<details markdown="1">
<summary><strong>convergence criteria (Optional, Multivalued)</strong></summary>

**Description:** Convergence criteria (e.g., energy, force)

**Range:** string

**URI:** [`catcore:convergence_criteria`](catcore:convergence_criteria)

**Schema Reference:** [convergence_criteria](elements/convergence_criteria.md)

</details>

<details markdown="1">
<summary><strong>k point mesh (Optional, Multivalued)</strong></summary>

**Description:** k-point mesh for sampling

**Range:** string

**URI:** [`catcore:k_point_mesh`](catcore:k_point_mesh)

**Schema Reference:** [k_point_mesh](elements/k_point_mesh.md)

</details>

</details>

<details markdown="1">
<summary><strong>PhononDispersion</strong></summary>

**Description:** Phonon dispersion property

**URI:** [`catcore:PhononDispersion`](catcore:PhononDispersion)

**Schema Reference:** [PhononDispersion](elements/PhononDispersion.md)

**Slots**

<details markdown="1">
<summary><strong>material composition (Optional, Multivalued)</strong></summary>

**Description:** Material composition

**Range:** string

**URI:** [`catcore:material_composition`](catcore:material_composition)

**Schema Reference:** [material_composition](elements/material_composition.md)

</details>

<details markdown="1">
<summary><strong>crystal structure (Optional, Multivalued)</strong></summary>

**Description:** Crystal structure (space group, lattice parameters)

**Range:** string

**URI:** [`SIO:001100`](SIO:001100)

**Schema Reference:** [crystal_structure](elements/crystal_structure.md)

</details>

<details markdown="1">
<summary><strong>force constant method (Optional, Multivalued)</strong></summary>

**Description:** Force constant calculation method

**Range:** string

**URI:** [`catcore:force_constant_method`](catcore:force_constant_method)

**Schema Reference:** [force_constant_method](elements/force_constant_method.md)

</details>

<details markdown="1">
<summary><strong>kq point mesh (Optional, Multivalued)</strong></summary>

**Description:** k/q-point mesh for phonons

**Range:** string

**URI:** [`catcore:kq_point_mesh`](catcore:kq_point_mesh)

**Schema Reference:** [kq_point_mesh](elements/kq_point_mesh.md)

</details>

<details markdown="1">
<summary><strong>smearing parameter (Optional, Multivalued)</strong></summary>

**Description:** Smearing/broadening parameter

**Range:** float

**URI:** [`catcore:smearing_parameter`](catcore:smearing_parameter)

**Schema Reference:** [smearing_parameter](elements/smearing_parameter.md)

**Unit:** eV

</details>

<details markdown="1">
<summary><strong>imaginary modes (Optional, Multivalued)</strong></summary>

**Description:** Imaginary modes present

**Range:** boolean

**URI:** [`catcore:imaginary_modes`](catcore:imaginary_modes)

**Schema Reference:** [imaginary_modes](elements/imaginary_modes.md)

</details>

</details>

<details markdown="1">
<summary><strong>EquationsOfState</strong></summary>

**Description:** Equations of state property

**URI:** [`catcore:EquationsOfState`](catcore:EquationsOfState)

**Schema Reference:** [EquationsOfState](elements/EquationsOfState.md)

**Slots**

<details markdown="1">
<summary><strong>material composition (Optional, Multivalued)</strong></summary>

**Description:** Material composition

**Range:** string

**URI:** [`catcore:material_composition`](catcore:material_composition)

**Schema Reference:** [material_composition](elements/material_composition.md)

</details>

<details markdown="1">
<summary><strong>crystal structure (Optional, Multivalued)</strong></summary>

**Description:** Crystal structure (space group, lattice parameters)

**Range:** string

**URI:** [`SIO:001100`](SIO:001100)

**Schema Reference:** [crystal_structure](elements/crystal_structure.md)

</details>

<details markdown="1">
<summary><strong>fit method (Optional, Multivalued)</strong></summary>

**Description:** Fit method (e.g., Birch-Murnaghan, Vinet)

**Range:** string

**URI:** [`catcore:fit_method`](catcore:fit_method)

**Schema Reference:** [fit_method](elements/fit_method.md)

</details>

<details markdown="1">
<summary><strong>energy cutoff (Optional, Multivalued)</strong></summary>

**Description:** Energy cutoff for plane wave basis

**Range:** float

**URI:** [`catcore:energy_cutoff`](catcore:energy_cutoff)

**Schema Reference:** [energy_cutoff](elements/energy_cutoff.md)

**Unit:** eV

</details>

<details markdown="1">
<summary><strong>k point mesh (Optional, Multivalued)</strong></summary>

**Description:** k-point mesh for sampling

**Range:** string

**URI:** [`catcore:k_point_mesh`](catcore:k_point_mesh)

**Schema Reference:** [k_point_mesh](elements/k_point_mesh.md)

</details>

<details markdown="1">
<summary><strong>bulk modulus (Optional, Multivalued)</strong></summary>

**Description:** Bulk modulus

**Range:** float

**URI:** [`catcore:bulk_modulus`](catcore:bulk_modulus)

**Schema Reference:** [bulk_modulus](elements/bulk_modulus.md)

**Unit:** GPa

</details>

<details markdown="1">
<summary><strong>pressure derivative (Optional, Multivalued)</strong></summary>

**Description:** Pressure derivative of bulk modulus

**Range:** float

**URI:** [`catcore:pressure_derivative`](catcore:pressure_derivative)

**Schema Reference:** [pressure_derivative](elements/pressure_derivative.md)

</details>

<details markdown="1">
<summary><strong>fit residuals (Optional, Multivalued)</strong></summary>

**Description:** Residuals of fit

**Range:** float

**URI:** [`catcore:fit_residuals`](catcore:fit_residuals)

**Schema Reference:** [fit_residuals](elements/fit_residuals.md)

</details>

</details>

<details markdown="1">
<summary><strong>AqueousStability</strong></summary>

**Description:** Aqueous stability property

**URI:** [`catcore:AqueousStability`](catcore:AqueousStability)

**Schema Reference:** [AqueousStability](elements/AqueousStability.md)

**Slots**

<details markdown="1">
<summary><strong>material composition (Optional, Multivalued)</strong></summary>

**Description:** Material composition

**Range:** string

**URI:** [`catcore:material_composition`](catcore:material_composition)

**Schema Reference:** [material_composition](elements/material_composition.md)

</details>

<details markdown="1">
<summary><strong>crystal structure (Optional, Multivalued)</strong></summary>

**Description:** Crystal structure (space group, lattice parameters)

**Range:** string

**URI:** [`SIO:001100`](SIO:001100)

**Schema Reference:** [crystal_structure](elements/crystal_structure.md)

</details>

<details markdown="1">
<summary><strong>ph range (Optional, Multivalued)</strong></summary>

**Description:** pH range considered

**Range:** string

**URI:** [`catcore:ph_range`](catcore:ph_range)

**Schema Reference:** [ph_range](elements/ph_range.md)

</details>

<details markdown="1">
<summary><strong>potential range (Optional, Multivalued)</strong></summary>

**Description:** Potential range considered

**Range:** string

**URI:** [`catcore:potential_range`](catcore:potential_range)

**Schema Reference:** [potential_range](elements/potential_range.md)

</details>

<details markdown="1">
<summary><strong>solvation model (Optional, Multivalued)</strong></summary>

**Description:** Solvation model used

**Range:** string

**URI:** [`catcore:solvation_model`](catcore:solvation_model)

**Schema Reference:** [solvation_model](elements/solvation_model.md)

</details>

<details markdown="1">
<summary><strong>ionic strength (Optional, Multivalued)</strong></summary>

**Description:** Ionic strength of solution

**Range:** float

**URI:** [`catcore:ionic_strength`](catcore:ionic_strength)

**Schema Reference:** [ionic_strength](elements/ionic_strength.md)

**Unit:** mol/L

</details>

<details markdown="1">
<summary><strong>temperature (Optional, Multivalued)</strong></summary>

**Description:** Temperature

**Range:** float

**URI:** [`AFR:0001584`](AFR:0001584)

**Schema Reference:** [temperature](elements/temperature.md)

**Unit:** Cel

</details>

</details>

<details markdown="1">
<summary><strong>GrainBoundaries</strong></summary>

**Description:** Grain boundaries property

**URI:** [`catcore:GrainBoundaries`](catcore:GrainBoundaries)

**Schema Reference:** [GrainBoundaries](elements/GrainBoundaries.md)

**Slots**

<details markdown="1">
<summary><strong>material composition (Optional, Multivalued)</strong></summary>

**Description:** Material composition

**Range:** string

**URI:** [`catcore:material_composition`](catcore:material_composition)

**Schema Reference:** [material_composition](elements/material_composition.md)

</details>

<details markdown="1">
<summary><strong>grain boundary plane (Optional, Multivalued)</strong></summary>

**Description:** Grain boundary plane

**Range:** string

**URI:** [`catcore:grain_boundary_plane`](catcore:grain_boundary_plane)

**Schema Reference:** [grain_boundary_plane](elements/grain_boundary_plane.md)

</details>

<details markdown="1">
<summary><strong>misorientation angle (Optional, Multivalued)</strong></summary>

**Description:** Misorientation angle

**Range:** float

**URI:** [`catcore:misorientation_angle`](catcore:misorientation_angle)

**Schema Reference:** [misorientation_angle](elements/misorientation_angle.md)

**Unit:** deg

</details>

<details markdown="1">
<summary><strong>grain boundary energy (Optional, Multivalued)</strong></summary>

**Description:** Grain boundary energy

**Range:** float

**URI:** [`catcore:grain_boundary_energy`](catcore:grain_boundary_energy)

**Schema Reference:** [grain_boundary_energy](elements/grain_boundary_energy.md)

**Unit:** J/m2

</details>

<details markdown="1">
<summary><strong>simulation cell size (Optional, Multivalued)</strong></summary>

**Description:** Simulation cell size

**Range:** string

**URI:** [`catcore:simulation_cell_size`](catcore:simulation_cell_size)

**Schema Reference:** [simulation_cell_size](elements/simulation_cell_size.md)

</details>

<details markdown="1">
<summary><strong>gb excess volume (Optional, Multivalued)</strong></summary>

**Description:** GB excess volume

**Range:** float

**URI:** [`catcore:gb_excess_volume`](catcore:gb_excess_volume)

**Schema Reference:** [gb_excess_volume](elements/gb_excess_volume.md)

</details>

<details markdown="1">
<summary><strong>gb structural units (Optional, Multivalued)</strong></summary>

**Description:** GB structural units description

**Range:** string

**URI:** [`catcore:gb_structural_units`](catcore:gb_structural_units)

**Schema Reference:** [gb_structural_units](elements/gb_structural_units.md)

</details>

<details markdown="1">
<summary><strong>charge defect segregation (Optional, Multivalued)</strong></summary>

**Description:** Charge or defect segregation data

**Range:** string

**URI:** [`catcore:charge_defect_segregation`](catcore:charge_defect_segregation)

**Schema Reference:** [charge_defect_segregation](elements/charge_defect_segregation.md)

</details>

</details>

<details markdown="1">
<summary><strong>ElectronicStructure</strong></summary>

**Description:** Electronic structure property

**URI:** [`catcore:ElectronicStructure`](catcore:ElectronicStructure)

**Schema Reference:** [ElectronicStructure](elements/ElectronicStructure.md)

**Slots**

<details markdown="1">
<summary><strong>material composition (Optional, Multivalued)</strong></summary>

**Description:** Material composition

**Range:** string

**URI:** [`catcore:material_composition`](catcore:material_composition)

**Schema Reference:** [material_composition](elements/material_composition.md)

</details>

<details markdown="1">
<summary><strong>crystal structure (Optional, Multivalued)</strong></summary>

**Description:** Crystal structure (space group, lattice parameters)

**Range:** string

**URI:** [`SIO:001100`](SIO:001100)

**Schema Reference:** [crystal_structure](elements/crystal_structure.md)

</details>

<details markdown="1">
<summary><strong>k point mesh (Optional, Multivalued)</strong></summary>

**Description:** k-point mesh for sampling

**Range:** string

**URI:** [`catcore:k_point_mesh`](catcore:k_point_mesh)

**Schema Reference:** [k_point_mesh](elements/k_point_mesh.md)

</details>

<details markdown="1">
<summary><strong>energy cutoff (Optional, Multivalued)</strong></summary>

**Description:** Energy cutoff for plane wave basis

**Range:** float

**URI:** [`catcore:energy_cutoff`](catcore:energy_cutoff)

**Schema Reference:** [energy_cutoff](elements/energy_cutoff.md)

**Unit:** eV

</details>

<details markdown="1">
<summary><strong>smearing method (Optional, Multivalued)</strong></summary>

**Description:** Smearing method and width

**Range:** string

**URI:** [`catcore:smearing_method`](catcore:smearing_method)

**Schema Reference:** [smearing_method](elements/smearing_method.md)

</details>

<details markdown="1">
<summary><strong>spin polarized (Optional, Multivalued)</strong></summary>

**Description:** Spin-polarized calculation

**Range:** boolean

**URI:** [`catcore:spin_polarized`](catcore:spin_polarized)

**Schema Reference:** [spin_polarized](elements/spin_polarized.md)

</details>

<details markdown="1">
<summary><strong>band path (Optional, Multivalued)</strong></summary>

**Description:** Band path used

**Range:** string

**URI:** [`catcore:band_path`](catcore:band_path)

**Schema Reference:** [band_path](elements/band_path.md)

</details>

<details markdown="1">
<summary><strong>fermi energy (Optional, Multivalued)</strong></summary>

**Description:** Fermi energy

**Range:** float

**URI:** [`catcore:fermi_energy`](catcore:fermi_energy)

**Schema Reference:** [fermi_energy](elements/fermi_energy.md)

**Unit:** eV

</details>

</details>

<details markdown="1">
<summary><strong>Ferroelectrics</strong></summary>

**Description:** Ferroelectric property

**URI:** [`catcore:Ferroelectrics`](catcore:Ferroelectrics)

**Schema Reference:** [Ferroelectrics](elements/Ferroelectrics.md)

**Slots**

<details markdown="1">
<summary><strong>material composition (Optional, Multivalued)</strong></summary>

**Description:** Material composition

**Range:** string

**URI:** [`catcore:material_composition`](catcore:material_composition)

**Schema Reference:** [material_composition](elements/material_composition.md)

</details>

<details markdown="1">
<summary><strong>crystal structure (Optional, Multivalued)</strong></summary>

**Description:** Crystal structure (space group, lattice parameters)

**Range:** string

**URI:** [`SIO:001100`](SIO:001100)

**Schema Reference:** [crystal_structure](elements/crystal_structure.md)

</details>

<details markdown="1">
<summary><strong>polarization direction (Optional, Multivalued)</strong></summary>

**Description:** Polarization direction

**Range:** string

**URI:** [`catcore:polarization_direction`](catcore:polarization_direction)

**Schema Reference:** [polarization_direction](elements/polarization_direction.md)

</details>

<details markdown="1">
<summary><strong>spontaneous polarization (Optional, Multivalued)</strong></summary>

**Description:** Spontaneous polarization magnitude

**Range:** float

**URI:** [`catcore:spontaneous_polarization`](catcore:spontaneous_polarization)

**Schema Reference:** [spontaneous_polarization](elements/spontaneous_polarization.md)

**Unit:** uC/cm2

</details>

<details markdown="1">
<summary><strong>reference structure (Optional, Multivalued)</strong></summary>

**Description:** Reference paraelectric structure

**Range:** string

**URI:** [`catcore:reference_structure`](catcore:reference_structure)

**Schema Reference:** [reference_structure](elements/reference_structure.md)

</details>

<details markdown="1">
<summary><strong>switching barrier (Optional, Multivalued)</strong></summary>

**Description:** Switching barrier

**Range:** float

**URI:** [`catcore:switching_barrier`](catcore:switching_barrier)

**Schema Reference:** [switching_barrier](elements/switching_barrier.md)

**Unit:** eV

</details>

<details markdown="1">
<summary><strong>coercive field (Optional, Multivalued)</strong></summary>

**Description:** Coercive field

**Range:** float

**URI:** [`catcore:coercive_field`](catcore:coercive_field)

**Schema Reference:** [coercive_field](elements/coercive_field.md)

**Unit:** kV/cm

</details>

<details markdown="1">
<summary><strong>temperature dependence (Optional, Multivalued)</strong></summary>

**Description:** Temperature dependence

**Range:** string

**URI:** [`catcore:temperature_dependence`](catcore:temperature_dependence)

**Schema Reference:** [temperature_dependence](elements/temperature_dependence.md)

</details>

</details>

<details markdown="1">
<summary><strong>BandGap</strong></summary>

**Description:** Band gap property

**URI:** [`catcore:BandGap`](catcore:BandGap)

**Schema Reference:** [BandGap](elements/BandGap.md)

**Slots**

<details markdown="1">
<summary><strong>material sample (Optional, Multivalued)</strong></summary>

**Description:** Material sample

**Range:** string

**URI:** [`voc4cat:0005056`](voc4cat:0005056)

**Schema Reference:** [material_sample](elements/material_sample.md)

</details>

<details markdown="1">
<summary><strong>structure model (Optional, Multivalued)</strong></summary>

**Description:** Structure or model used

**Range:** string

**URI:** [`catcore:structure_model`](catcore:structure_model)

**Schema Reference:** [structure_model](elements/structure_model.md)

</details>

<details markdown="1">
<summary><strong>k point mesh (Optional, Multivalued)</strong></summary>

**Description:** k-point mesh for sampling

**Range:** string

**URI:** [`catcore:k_point_mesh`](catcore:k_point_mesh)

**Schema Reference:** [k_point_mesh](elements/k_point_mesh.md)

</details>

<details markdown="1">
<summary><strong>smearing broadening (Optional, Multivalued)</strong></summary>

**Description:** Smearing or broadening parameter

**Range:** float

**URI:** [`catcore:smearing_broadening`](catcore:smearing_broadening)

**Schema Reference:** [smearing_broadening](elements/smearing_broadening.md)

**Unit:** eV

</details>

<details markdown="1">
<summary><strong>direct indirect (Optional, Multivalued)</strong></summary>

**Description:** Direct or indirect band gap

**Range:** string

**URI:** [`catcore:direct_indirect`](catcore:direct_indirect)

**Schema Reference:** [direct_indirect](elements/direct_indirect.md)

</details>

<details markdown="1">
<summary><strong>experimental reference (Optional, Multivalued)</strong></summary>

**Description:** Experimental reference value

**Range:** float

**URI:** [`catcore:experimental_reference`](catcore:experimental_reference)

**Schema Reference:** [experimental_reference](elements/experimental_reference.md)

**Unit:** eV

</details>

<details markdown="1">
<summary><strong>gw hybrid correction (Optional, Multivalued)</strong></summary>

**Description:** GW or hybrid correction used

**Range:** boolean

**URI:** [`catcore:gw_hybrid_correction`](catcore:gw_hybrid_correction)

**Schema Reference:** [gw_hybrid_correction](elements/gw_hybrid_correction.md)

</details>

<details markdown="1">
<summary><strong>excitonic correction (Optional, Multivalued)</strong></summary>

**Description:** Excitonic correction applied

**Range:** float

**URI:** [`catcore:excitonic_correction`](catcore:excitonic_correction)

**Schema Reference:** [excitonic_correction](elements/excitonic_correction.md)

**Unit:** eV

</details>

</details>

</details>

