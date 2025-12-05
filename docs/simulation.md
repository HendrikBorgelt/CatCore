# Simulation

The data class 'Simulation' describes the minimum information which should be reported 
with research data for conducting simulations in the field of catalysis.

## Slots

Fields for Metadata which should be described when using this Metadata Aspect.

- **Description:**A short description for Comprehension purposes

- **Range:** Further Aspects which are Important for describing a certain aspect

- **Cardinality:** A description how often it is allowed and how important it is to describe a certain aspect

- **Range:** Further Aspects which are Important for describing a certain aspect

- **CURIE:** The Abbreviated form of a URI, where the Prefix, e.g. voc4cat, described to which terminology a Concept belong. The Links are fully implemented here. For reusing these CURIE's you need to substitute the prefix against the URI for it.

- **Schema Reference:** A Link to the native LinkML Documentation on which this metadatacatalog and strucutre is based upon

<details markdown="1">
<summary><strong>software package</strong> (Required, Multivalued)</summary>

**Description:** Software or package used for simulation

**Range:** string

**Cardinality:**  Required, Multivalued

**CURIE:** [`catcore:software_package`](https://w3id.org/nfdi4cat/catcore/software_package)

**Schema Reference:** [software_package](./elements/software_package.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20software_package" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>simulation method</strong> (Required, Multivalued)</summary>

**Description:** Simulation method used

**Range:** SimulationMethod

**Cardinality:**  Required, Multivalued

**CURIE:** [`catcore:simulation_method`](https://w3id.org/nfdi4cat/catcore/simulation_method)

**Schema Reference:** [simulation_method](./elements/simulation_method.md)

**Range Class Details:**

<details markdown="1">
<summary><strong>SimulationMethod</strong></summary>

**Abstract Class**

**Description:** Simulation method used

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20SimulationMethod" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**Schema Reference:** [SimulationMethod](./elements/SimulationMethod.md)

</details>

**Possible Subclasses / Enumerations of SimulationMethod:**

<details markdown="1">
<summary><strong>DFT</strong></summary>

**Description:** Density functional theory

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20DFT" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:DFT`](https://w3id.org/nfdi4cat/catcore/DFT)

**Schema Reference:** [DFT](./elements/DFT.md)

**Slots**

<details markdown="1">
<summary><strong>exchange correlation functional</strong> (Optional, Multivalued)</summary>

**Description:** Exchange-correlation functional used (e.g., PBE, B3LYP)

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:exchange_correlation_functional`](https://w3id.org/nfdi4cat/catcore/exchange_correlation_functional)

**Schema Reference:** [exchange_correlation_functional](./elements/exchange_correlation_functional.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20exchange_correlation_functional" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>energy cutoff</strong> (Optional, Multivalued)</summary>

**Description:** Energy cutoff for plane wave basis

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:energy_cutoff`](https://w3id.org/nfdi4cat/catcore/energy_cutoff)

**Schema Reference:** [energy_cutoff](./elements/energy_cutoff.md)

**Unit:** eV

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20energy_cutoff" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>convergence criteria</strong> (Optional, Multivalued)</summary>

**Description:** Convergence criteria (e.g., energy, force)

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:convergence_criteria`](https://w3id.org/nfdi4cat/catcore/convergence_criteria)

**Schema Reference:** [convergence_criteria](./elements/convergence_criteria.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20convergence_criteria" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>dft u parameters</strong> (Optional, Multivalued)</summary>

**Description:** DFT+U parameters used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:dft_u_parameters`](https://w3id.org/nfdi4cat/catcore/dft_u_parameters)

**Schema Reference:** [dft_u_parameters](./elements/dft_u_parameters.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20dft_u_parameters" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>spin polarization</strong> (Optional, Multivalued)</summary>

**Description:** Spin polarization setting

**Range:** boolean

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:spin_polarization`](https://w3id.org/nfdi4cat/catcore/spin_polarization)

**Schema Reference:** [spin_polarization](./elements/spin_polarization.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20spin_polarization" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>total energy per atom</strong> (Optional, Multivalued)</summary>

**Description:** Total energy per atom

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:total_energy_per_atom`](https://w3id.org/nfdi4cat/catcore/total_energy_per_atom)

**Schema Reference:** [total_energy_per_atom](./elements/total_energy_per_atom.md)

**Unit:** eV

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20total_energy_per_atom" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>MolecularDynamics</strong></summary>

**Description:** Molecular dynamics

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20MolecularDynamics" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`NCIT:C18097`](http://purl.obolibrary.org/obo/NCIT_C18097)

**Schema Reference:** [MolecularDynamics](./elements/MolecularDynamics.md)

**Slots**

<details markdown="1">
<summary><strong>force field</strong> (Optional, Multivalued)</summary>

**Description:** Force field used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:force_field`](https://w3id.org/nfdi4cat/catcore/force_field)

**Schema Reference:** [force_field](./elements/force_field.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20force_field" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>simulation timestep</strong> (Optional, Multivalued)</summary>

**Description:** Time step for simulation

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`APOLLO_SV:00000012`](http://purl.obolibrary.org/obo/APOLLO_SV_00000012)

**Schema Reference:** [simulation_timestep](./elements/simulation_timestep.md)

**Unit:** fs

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20simulation_timestep" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>simulation time</strong> (Optional, Multivalued)</summary>

**Description:** Total simulation time

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:simulation_time`](https://w3id.org/nfdi4cat/catcore/simulation_time)

**Schema Reference:** [simulation_time](./elements/simulation_time.md)

**Unit:** ps

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20simulation_time" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>ensemble type</strong> (Optional, Multivalued)</summary>

**Description:** Ensemble type (e.g., NVT, NPT)

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:ensemble_type`](https://w3id.org/nfdi4cat/catcore/ensemble_type)

**Schema Reference:** [ensemble_type](./elements/ensemble_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ensemble_type" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of atoms</strong> (Optional, Multivalued)</summary>

**Description:** Number of atoms in simulation

**Range:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:number_of_atoms`](https://w3id.org/nfdi4cat/catcore/number_of_atoms)

**Schema Reference:** [number_of_atoms](./elements/number_of_atoms.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_atoms" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>Microkinetics</strong></summary>

**Description:** Microkinetics simulation

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Microkinetics" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:Microkinetics`](https://w3id.org/nfdi4cat/catcore/Microkinetics)

**Schema Reference:** [Microkinetics](./elements/Microkinetics.md)

**Slots**

<details markdown="1">
<summary><strong>rate constants</strong> (Optional, Multivalued)</summary>

**Description:** Rate constants or Arrhenius parameters

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`NCIT:C94967`](http://purl.obolibrary.org/obo/NCIT_C94967)

**Schema Reference:** [rate_constants](./elements/rate_constants.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20rate_constants" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>solver type</strong> (Optional, Multivalued)</summary>

**Description:** Type of solver used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:solver_type`](https://w3id.org/nfdi4cat/catcore/solver_type)

**Schema Reference:** [solver_type](./elements/solver_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20solver_type" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0001584`](http://purl.allotrope.org/ontologies/result#AFR_0001584)

**Schema Reference:** [temperature](./elements/temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>pressure</strong> (Optional, Multivalued)</summary>

**Description:** Pressure in simulation

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:pressure`](https://w3id.org/nfdi4cat/catcore/pressure)

**Schema Reference:** [pressure](./elements/pressure.md)

**Unit:** bar

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20pressure" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>surface coverage</strong> (Optional, Multivalued)</summary>

**Description:** Surface coverage of species

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:surface_coverage`](https://w3id.org/nfdi4cat/catcore/surface_coverage)

**Schema Reference:** [surface_coverage](./elements/surface_coverage.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20surface_coverage" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>activation energy</strong> (Optional, Multivalued)</summary>

**Description:** Activation energy for each step

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:activation_energy`](https://w3id.org/nfdi4cat/catcore/activation_energy)

**Schema Reference:** [activation_energy](./elements/activation_energy.md)

**Unit:** eV

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20activation_energy" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>MonteCarlo</strong></summary>

**Description:** Monte Carlo simulation

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20MonteCarlo" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:MonteCarlo`](https://w3id.org/nfdi4cat/catcore/MonteCarlo)

**Schema Reference:** [MonteCarlo](./elements/MonteCarlo.md)

**Slots**

<details markdown="1">
<summary><strong>interaction potential</strong> (Optional, Multivalued)</summary>

**Description:** Interaction potential used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:interaction_potential`](https://w3id.org/nfdi4cat/catcore/interaction_potential)

**Schema Reference:** [interaction_potential](./elements/interaction_potential.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20interaction_potential" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of steps</strong> (Optional, Multivalued)</summary>

**Description:** Number of Monte Carlo steps

**Range:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:number_of_steps`](https://w3id.org/nfdi4cat/catcore/number_of_steps)

**Schema Reference:** [number_of_steps](./elements/number_of_steps.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_steps" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0001584`](http://purl.allotrope.org/ontologies/result#AFR_0001584)

**Schema Reference:** [temperature](./elements/temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>lattice size type</strong> (Optional, Multivalued)</summary>

**Description:** Lattice size and type

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:lattice_size_type`](https://w3id.org/nfdi4cat/catcore/lattice_size_type)

**Schema Reference:** [lattice_size_type](./elements/lattice_size_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20lattice_size_type" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>acceptance criteria</strong> (Optional, Multivalued)</summary>

**Description:** Acceptance criteria for Monte Carlo moves

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:acceptance_criteria`](https://w3id.org/nfdi4cat/catcore/acceptance_criteria)

**Schema Reference:** [acceptance_criteria](./elements/acceptance_criteria.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20acceptance_criteria" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>equilibration steps</strong> (Optional, Multivalued)</summary>

**Description:** Number of equilibration steps

**Range:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:equilibration_steps`](https://w3id.org/nfdi4cat/catcore/equilibration_steps)

**Schema Reference:** [equilibration_steps](./elements/equilibration_steps.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20equilibration_steps" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>sampling interval</strong> (Optional, Multivalued)</summary>

**Description:** Sampling interval for data collection

**Range:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:sampling_interval`](https://w3id.org/nfdi4cat/catcore/sampling_interval)

**Schema Reference:** [sampling_interval](./elements/sampling_interval.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20sampling_interval" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20simulation_method" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calculated property</strong> (Required, Multivalued)</summary>

**Description:** Property calculated from simulation

**Range:** CalculatedProperty

**Cardinality:**  Required, Multivalued

**CURIE:** [`catcore:calculated_property`](https://w3id.org/nfdi4cat/catcore/calculated_property)

**Schema Reference:** [calculated_property](./elements/calculated_property.md)

**Range Class Details:**

<details markdown="1">
<summary><strong>CalculatedProperty</strong></summary>

**Abstract Class**

**Description:** Property calculated from simulation

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20CalculatedProperty" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**Schema Reference:** [CalculatedProperty](./elements/CalculatedProperty.md)

</details>

**Possible Subclasses / Enumerations of CalculatedProperty:**

<details markdown="1">
<summary><strong>ThermodynamicStability</strong></summary>

**Description:** Thermodynamic stability property

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ThermodynamicStability" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:ThermodynamicStability`](https://w3id.org/nfdi4cat/catcore/ThermodynamicStability)

**Schema Reference:** [ThermodynamicStability](./elements/ThermodynamicStability.md)

**Slots**

<details markdown="1">
<summary><strong>formation energy</strong> (Optional, Multivalued)</summary>

**Description:** Formation energy per atom

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:formation_energy`](https://w3id.org/nfdi4cat/catcore/formation_energy)

**Schema Reference:** [formation_energy](./elements/formation_energy.md)

**Unit:** eV

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20formation_energy" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>reference energies</strong> (Optional, Multivalued)</summary>

**Description:** Reference elemental energies

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:reference_energies`](https://w3id.org/nfdi4cat/catcore/reference_energies)

**Schema Reference:** [reference_energies](./elements/reference_energies.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20reference_energies" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>energy above hull</strong> (Optional, Multivalued)</summary>

**Description:** Energy above convex hull

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:energy_above_hull`](https://w3id.org/nfdi4cat/catcore/energy_above_hull)

**Schema Reference:** [energy_above_hull](./elements/energy_above_hull.md)

**Unit:** eV

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20energy_above_hull" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>phase diagram type</strong> (Optional, Multivalued)</summary>

**Description:** Phase diagram type (e.g., binary, ternary)

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:phase_diagram_type`](https://w3id.org/nfdi4cat/catcore/phase_diagram_type)

**Schema Reference:** [phase_diagram_type](./elements/phase_diagram_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20phase_diagram_type" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>competing phases</strong> (Optional, Multivalued)</summary>

**Description:** Competing phase list

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:competing_phases`](https://w3id.org/nfdi4cat/catcore/competing_phases)

**Schema Reference:** [competing_phases](./elements/competing_phases.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20competing_phases" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>Piezoelectricity</strong></summary>

**Description:** Piezoelectricity property

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Piezoelectricity" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:Piezoelectricity`](https://w3id.org/nfdi4cat/catcore/Piezoelectricity)

**Schema Reference:** [Piezoelectricity](./elements/Piezoelectricity.md)

**Slots**

<details markdown="1">
<summary><strong>piezoelectric tensor</strong> (Optional, Multivalued)</summary>

**Description:** Piezoelectric tensor components

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:piezoelectric_tensor`](https://w3id.org/nfdi4cat/catcore/piezoelectric_tensor)

**Schema Reference:** [piezoelectric_tensor](./elements/piezoelectric_tensor.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20piezoelectric_tensor" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>crystal symmetry</strong> (Optional, Multivalued)</summary>

**Description:** Crystal symmetry

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:crystal_symmetry`](https://w3id.org/nfdi4cat/catcore/crystal_symmetry)

**Schema Reference:** [crystal_symmetry](./elements/crystal_symmetry.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20crystal_symmetry" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>strain applied</strong> (Optional, Multivalued)</summary>

**Description:** Strain applied

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:strain_applied`](https://w3id.org/nfdi4cat/catcore/strain_applied)

**Schema Reference:** [strain_applied](./elements/strain_applied.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20strain_applied" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>ionic electronic contributions</strong> (Optional, Multivalued)</summary>

**Description:** Ionic and electronic contributions

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:ionic_electronic_contributions`](https://w3id.org/nfdi4cat/catcore/ionic_electronic_contributions)

**Schema Reference:** [ionic_electronic_contributions](./elements/ionic_electronic_contributions.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ionic_electronic_contributions" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>ElasticConstants</strong></summary>

**Description:** Elastic constants property

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ElasticConstants" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:ElasticConstants`](https://w3id.org/nfdi4cat/catcore/ElasticConstants)

**Schema Reference:** [ElasticConstants](./elements/ElasticConstants.md)

**Slots**

<details markdown="1">
<summary><strong>elastic tensor</strong> (Optional, Multivalued)</summary>

**Description:** Elastic tensor components

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:elastic_tensor`](https://w3id.org/nfdi4cat/catcore/elastic_tensor)

**Schema Reference:** [elastic_tensor](./elements/elastic_tensor.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20elastic_tensor" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>bulk modulus</strong> (Optional, Multivalued)</summary>

**Description:** Bulk modulus

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:bulk_modulus`](https://w3id.org/nfdi4cat/catcore/bulk_modulus)

**Schema Reference:** [bulk_modulus](./elements/bulk_modulus.md)

**Unit:** GPa

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20bulk_modulus" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>shear modulus</strong> (Optional, Multivalued)</summary>

**Description:** Shear modulus

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:shear_modulus`](https://w3id.org/nfdi4cat/catcore/shear_modulus)

**Schema Reference:** [shear_modulus](./elements/shear_modulus.md)

**Unit:** GPa

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20shear_modulus" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>poisson ratio</strong> (Optional, Multivalued)</summary>

**Description:** Poisson's ratio

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:poisson_ratio`](https://w3id.org/nfdi4cat/catcore/poisson_ratio)

**Schema Reference:** [poisson_ratio](./elements/poisson_ratio.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20poisson_ratio" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>young modulus</strong> (Optional, Multivalued)</summary>

**Description:** Young's modulus

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:young_modulus`](https://w3id.org/nfdi4cat/catcore/young_modulus)

**Schema Reference:** [young_modulus](./elements/young_modulus.md)

**Unit:** GPa

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20young_modulus" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>Surfaces</strong></summary>

**Description:** Surface property

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Surfaces" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:Surfaces`](https://w3id.org/nfdi4cat/catcore/Surfaces)

**Schema Reference:** [Surfaces](./elements/Surfaces.md)

**Slots**

<details markdown="1">
<summary><strong>surface energy</strong> (Optional, Multivalued)</summary>

**Description:** Surface energy

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:surface_energy`](https://w3id.org/nfdi4cat/catcore/surface_energy)

**Schema Reference:** [surface_energy](./elements/surface_energy.md)

**Unit:** J/m2

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20surface_energy" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>miller indices</strong> (Optional, Multivalued)</summary>

**Description:** Miller indices of surface

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:miller_indices`](https://w3id.org/nfdi4cat/catcore/miller_indices)

**Schema Reference:** [miller_indices](./elements/miller_indices.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20miller_indices" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>slab thickness</strong> (Optional, Multivalued)</summary>

**Description:** Slab thickness

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:slab_thickness`](https://w3id.org/nfdi4cat/catcore/slab_thickness)

**Schema Reference:** [slab_thickness](./elements/slab_thickness.md)

**Unit:** angstrom

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20slab_thickness" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>vacuum spacing</strong> (Optional, Multivalued)</summary>

**Description:** Vacuum spacing

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:vacuum_spacing`](https://w3id.org/nfdi4cat/catcore/vacuum_spacing)

**Schema Reference:** [vacuum_spacing](./elements/vacuum_spacing.md)

**Unit:** angstrom

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20vacuum_spacing" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>surface termination method</strong> (Optional, Multivalued)</summary>

**Description:** Surface termination method

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:surface_termination_method`](https://w3id.org/nfdi4cat/catcore/surface_termination_method)

**Schema Reference:** [surface_termination_method](./elements/surface_termination_method.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20surface_termination_method" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>DielectricTensors</strong></summary>

**Description:** Dielectric tensors property

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20DielectricTensors" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:DielectricTensors`](https://w3id.org/nfdi4cat/catcore/DielectricTensors)

**Schema Reference:** [DielectricTensors](./elements/DielectricTensors.md)

**Slots**

<details markdown="1">
<summary><strong>material composition</strong> (Optional, Multivalued)</summary>

**Description:** Material composition

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:material_composition`](https://w3id.org/nfdi4cat/catcore/material_composition)

**Schema Reference:** [material_composition](./elements/material_composition.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20material_composition" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>crystal structure</strong> (Optional, Multivalued)</summary>

**Description:** Crystal structure (space group, lattice parameters)

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`SIO:001100`](http://semanticscience.org/resource/SIO_001100)

**Schema Reference:** [crystal_structure](./elements/crystal_structure.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20crystal_structure" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>energy cutoff</strong> (Optional, Multivalued)</summary>

**Description:** Energy cutoff for plane wave basis

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:energy_cutoff`](https://w3id.org/nfdi4cat/catcore/energy_cutoff)

**Schema Reference:** [energy_cutoff](./elements/energy_cutoff.md)

**Unit:** eV

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20energy_cutoff" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>convergence criteria</strong> (Optional, Multivalued)</summary>

**Description:** Convergence criteria (e.g., energy, force)

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:convergence_criteria`](https://w3id.org/nfdi4cat/catcore/convergence_criteria)

**Schema Reference:** [convergence_criteria](./elements/convergence_criteria.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20convergence_criteria" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>k point mesh</strong> (Optional, Multivalued)</summary>

**Description:** k-point mesh for sampling

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:k_point_mesh`](https://w3id.org/nfdi4cat/catcore/k_point_mesh)

**Schema Reference:** [k_point_mesh](./elements/k_point_mesh.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20k_point_mesh" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>PhononDispersion</strong></summary>

**Description:** Phonon dispersion property

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20PhononDispersion" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:PhononDispersion`](https://w3id.org/nfdi4cat/catcore/PhononDispersion)

**Schema Reference:** [PhononDispersion](./elements/PhononDispersion.md)

**Slots**

<details markdown="1">
<summary><strong>material composition</strong> (Optional, Multivalued)</summary>

**Description:** Material composition

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:material_composition`](https://w3id.org/nfdi4cat/catcore/material_composition)

**Schema Reference:** [material_composition](./elements/material_composition.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20material_composition" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>crystal structure</strong> (Optional, Multivalued)</summary>

**Description:** Crystal structure (space group, lattice parameters)

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`SIO:001100`](http://semanticscience.org/resource/SIO_001100)

**Schema Reference:** [crystal_structure](./elements/crystal_structure.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20crystal_structure" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>force constant method</strong> (Optional, Multivalued)</summary>

**Description:** Force constant calculation method

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:force_constant_method`](https://w3id.org/nfdi4cat/catcore/force_constant_method)

**Schema Reference:** [force_constant_method](./elements/force_constant_method.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20force_constant_method" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>kq point mesh</strong> (Optional, Multivalued)</summary>

**Description:** k/q-point mesh for phonons

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:kq_point_mesh`](https://w3id.org/nfdi4cat/catcore/kq_point_mesh)

**Schema Reference:** [kq_point_mesh](./elements/kq_point_mesh.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20kq_point_mesh" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>smearing parameter</strong> (Optional, Multivalued)</summary>

**Description:** Smearing/broadening parameter

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:smearing_parameter`](https://w3id.org/nfdi4cat/catcore/smearing_parameter)

**Schema Reference:** [smearing_parameter](./elements/smearing_parameter.md)

**Unit:** eV

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20smearing_parameter" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>imaginary modes</strong> (Optional, Multivalued)</summary>

**Description:** Imaginary modes present

**Range:** boolean

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:imaginary_modes`](https://w3id.org/nfdi4cat/catcore/imaginary_modes)

**Schema Reference:** [imaginary_modes](./elements/imaginary_modes.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20imaginary_modes" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>EquationsOfState</strong></summary>

**Description:** Equations of state property

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20EquationsOfState" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:EquationsOfState`](https://w3id.org/nfdi4cat/catcore/EquationsOfState)

**Schema Reference:** [EquationsOfState](./elements/EquationsOfState.md)

**Slots**

<details markdown="1">
<summary><strong>material composition</strong> (Optional, Multivalued)</summary>

**Description:** Material composition

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:material_composition`](https://w3id.org/nfdi4cat/catcore/material_composition)

**Schema Reference:** [material_composition](./elements/material_composition.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20material_composition" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>crystal structure</strong> (Optional, Multivalued)</summary>

**Description:** Crystal structure (space group, lattice parameters)

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`SIO:001100`](http://semanticscience.org/resource/SIO_001100)

**Schema Reference:** [crystal_structure](./elements/crystal_structure.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20crystal_structure" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>fit method</strong> (Optional, Multivalued)</summary>

**Description:** Fit method (e.g., Birch-Murnaghan, Vinet)

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:fit_method`](https://w3id.org/nfdi4cat/catcore/fit_method)

**Schema Reference:** [fit_method](./elements/fit_method.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20fit_method" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>energy cutoff</strong> (Optional, Multivalued)</summary>

**Description:** Energy cutoff for plane wave basis

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:energy_cutoff`](https://w3id.org/nfdi4cat/catcore/energy_cutoff)

**Schema Reference:** [energy_cutoff](./elements/energy_cutoff.md)

**Unit:** eV

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20energy_cutoff" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>k point mesh</strong> (Optional, Multivalued)</summary>

**Description:** k-point mesh for sampling

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:k_point_mesh`](https://w3id.org/nfdi4cat/catcore/k_point_mesh)

**Schema Reference:** [k_point_mesh](./elements/k_point_mesh.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20k_point_mesh" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>bulk modulus</strong> (Optional, Multivalued)</summary>

**Description:** Bulk modulus

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:bulk_modulus`](https://w3id.org/nfdi4cat/catcore/bulk_modulus)

**Schema Reference:** [bulk_modulus](./elements/bulk_modulus.md)

**Unit:** GPa

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20bulk_modulus" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>pressure derivative</strong> (Optional, Multivalued)</summary>

**Description:** Pressure derivative of bulk modulus

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:pressure_derivative`](https://w3id.org/nfdi4cat/catcore/pressure_derivative)

**Schema Reference:** [pressure_derivative](./elements/pressure_derivative.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20pressure_derivative" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>fit residuals</strong> (Optional, Multivalued)</summary>

**Description:** Residuals of fit

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:fit_residuals`](https://w3id.org/nfdi4cat/catcore/fit_residuals)

**Schema Reference:** [fit_residuals](./elements/fit_residuals.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20fit_residuals" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>AqueousStability</strong></summary>

**Description:** Aqueous stability property

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20AqueousStability" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:AqueousStability`](https://w3id.org/nfdi4cat/catcore/AqueousStability)

**Schema Reference:** [AqueousStability](./elements/AqueousStability.md)

**Slots**

<details markdown="1">
<summary><strong>material composition</strong> (Optional, Multivalued)</summary>

**Description:** Material composition

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:material_composition`](https://w3id.org/nfdi4cat/catcore/material_composition)

**Schema Reference:** [material_composition](./elements/material_composition.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20material_composition" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>crystal structure</strong> (Optional, Multivalued)</summary>

**Description:** Crystal structure (space group, lattice parameters)

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`SIO:001100`](http://semanticscience.org/resource/SIO_001100)

**Schema Reference:** [crystal_structure](./elements/crystal_structure.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20crystal_structure" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>ph range</strong> (Optional, Multivalued)</summary>

**Description:** pH range considered

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:ph_range`](https://w3id.org/nfdi4cat/catcore/ph_range)

**Schema Reference:** [ph_range](./elements/ph_range.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ph_range" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>potential range</strong> (Optional, Multivalued)</summary>

**Description:** Potential range considered

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:potential_range`](https://w3id.org/nfdi4cat/catcore/potential_range)

**Schema Reference:** [potential_range](./elements/potential_range.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20potential_range" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>solvation model</strong> (Optional, Multivalued)</summary>

**Description:** Solvation model used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:solvation_model`](https://w3id.org/nfdi4cat/catcore/solvation_model)

**Schema Reference:** [solvation_model](./elements/solvation_model.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20solvation_model" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>ionic strength</strong> (Optional, Multivalued)</summary>

**Description:** Ionic strength of solution

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:ionic_strength`](https://w3id.org/nfdi4cat/catcore/ionic_strength)

**Schema Reference:** [ionic_strength](./elements/ionic_strength.md)

**Unit:** mol/L

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ionic_strength" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0001584`](http://purl.allotrope.org/ontologies/result#AFR_0001584)

**Schema Reference:** [temperature](./elements/temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>GrainBoundaries</strong></summary>

**Description:** Grain boundaries property

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20GrainBoundaries" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:GrainBoundaries`](https://w3id.org/nfdi4cat/catcore/GrainBoundaries)

**Schema Reference:** [GrainBoundaries](./elements/GrainBoundaries.md)

**Slots**

<details markdown="1">
<summary><strong>material composition</strong> (Optional, Multivalued)</summary>

**Description:** Material composition

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:material_composition`](https://w3id.org/nfdi4cat/catcore/material_composition)

**Schema Reference:** [material_composition](./elements/material_composition.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20material_composition" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>grain boundary plane</strong> (Optional, Multivalued)</summary>

**Description:** Grain boundary plane

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:grain_boundary_plane`](https://w3id.org/nfdi4cat/catcore/grain_boundary_plane)

**Schema Reference:** [grain_boundary_plane](./elements/grain_boundary_plane.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20grain_boundary_plane" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>misorientation angle</strong> (Optional, Multivalued)</summary>

**Description:** Misorientation angle

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:misorientation_angle`](https://w3id.org/nfdi4cat/catcore/misorientation_angle)

**Schema Reference:** [misorientation_angle](./elements/misorientation_angle.md)

**Unit:** deg

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20misorientation_angle" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>grain boundary energy</strong> (Optional, Multivalued)</summary>

**Description:** Grain boundary energy

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:grain_boundary_energy`](https://w3id.org/nfdi4cat/catcore/grain_boundary_energy)

**Schema Reference:** [grain_boundary_energy](./elements/grain_boundary_energy.md)

**Unit:** J/m2

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20grain_boundary_energy" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>simulation cell size</strong> (Optional, Multivalued)</summary>

**Description:** Simulation cell size

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:simulation_cell_size`](https://w3id.org/nfdi4cat/catcore/simulation_cell_size)

**Schema Reference:** [simulation_cell_size](./elements/simulation_cell_size.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20simulation_cell_size" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>gb excess volume</strong> (Optional, Multivalued)</summary>

**Description:** GB excess volume

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:gb_excess_volume`](https://w3id.org/nfdi4cat/catcore/gb_excess_volume)

**Schema Reference:** [gb_excess_volume](./elements/gb_excess_volume.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20gb_excess_volume" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>gb structural units</strong> (Optional, Multivalued)</summary>

**Description:** GB structural units description

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:gb_structural_units`](https://w3id.org/nfdi4cat/catcore/gb_structural_units)

**Schema Reference:** [gb_structural_units](./elements/gb_structural_units.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20gb_structural_units" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>charge defect segregation</strong> (Optional, Multivalued)</summary>

**Description:** Charge or defect segregation data

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:charge_defect_segregation`](https://w3id.org/nfdi4cat/catcore/charge_defect_segregation)

**Schema Reference:** [charge_defect_segregation](./elements/charge_defect_segregation.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20charge_defect_segregation" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>ElectronicStructure</strong></summary>

**Description:** Electronic structure property

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ElectronicStructure" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:ElectronicStructure`](https://w3id.org/nfdi4cat/catcore/ElectronicStructure)

**Schema Reference:** [ElectronicStructure](./elements/ElectronicStructure.md)

**Slots**

<details markdown="1">
<summary><strong>material composition</strong> (Optional, Multivalued)</summary>

**Description:** Material composition

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:material_composition`](https://w3id.org/nfdi4cat/catcore/material_composition)

**Schema Reference:** [material_composition](./elements/material_composition.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20material_composition" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>crystal structure</strong> (Optional, Multivalued)</summary>

**Description:** Crystal structure (space group, lattice parameters)

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`SIO:001100`](http://semanticscience.org/resource/SIO_001100)

**Schema Reference:** [crystal_structure](./elements/crystal_structure.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20crystal_structure" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>k point mesh</strong> (Optional, Multivalued)</summary>

**Description:** k-point mesh for sampling

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:k_point_mesh`](https://w3id.org/nfdi4cat/catcore/k_point_mesh)

**Schema Reference:** [k_point_mesh](./elements/k_point_mesh.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20k_point_mesh" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>energy cutoff</strong> (Optional, Multivalued)</summary>

**Description:** Energy cutoff for plane wave basis

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:energy_cutoff`](https://w3id.org/nfdi4cat/catcore/energy_cutoff)

**Schema Reference:** [energy_cutoff](./elements/energy_cutoff.md)

**Unit:** eV

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20energy_cutoff" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>smearing method</strong> (Optional, Multivalued)</summary>

**Description:** Smearing method and width

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:smearing_method`](https://w3id.org/nfdi4cat/catcore/smearing_method)

**Schema Reference:** [smearing_method](./elements/smearing_method.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20smearing_method" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>spin polarized</strong> (Optional, Multivalued)</summary>

**Description:** Spin-polarized calculation

**Range:** boolean

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:spin_polarized`](https://w3id.org/nfdi4cat/catcore/spin_polarized)

**Schema Reference:** [spin_polarized](./elements/spin_polarized.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20spin_polarized" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>band path</strong> (Optional, Multivalued)</summary>

**Description:** Band path used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:band_path`](https://w3id.org/nfdi4cat/catcore/band_path)

**Schema Reference:** [band_path](./elements/band_path.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20band_path" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>fermi energy</strong> (Optional, Multivalued)</summary>

**Description:** Fermi energy

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:fermi_energy`](https://w3id.org/nfdi4cat/catcore/fermi_energy)

**Schema Reference:** [fermi_energy](./elements/fermi_energy.md)

**Unit:** eV

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20fermi_energy" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>Ferroelectrics</strong></summary>

**Description:** Ferroelectric property

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Ferroelectrics" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:Ferroelectrics`](https://w3id.org/nfdi4cat/catcore/Ferroelectrics)

**Schema Reference:** [Ferroelectrics](./elements/Ferroelectrics.md)

**Slots**

<details markdown="1">
<summary><strong>material composition</strong> (Optional, Multivalued)</summary>

**Description:** Material composition

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:material_composition`](https://w3id.org/nfdi4cat/catcore/material_composition)

**Schema Reference:** [material_composition](./elements/material_composition.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20material_composition" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>crystal structure</strong> (Optional, Multivalued)</summary>

**Description:** Crystal structure (space group, lattice parameters)

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`SIO:001100`](http://semanticscience.org/resource/SIO_001100)

**Schema Reference:** [crystal_structure](./elements/crystal_structure.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20crystal_structure" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>polarization direction</strong> (Optional, Multivalued)</summary>

**Description:** Polarization direction

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:polarization_direction`](https://w3id.org/nfdi4cat/catcore/polarization_direction)

**Schema Reference:** [polarization_direction](./elements/polarization_direction.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20polarization_direction" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>spontaneous polarization</strong> (Optional, Multivalued)</summary>

**Description:** Spontaneous polarization magnitude

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:spontaneous_polarization`](https://w3id.org/nfdi4cat/catcore/spontaneous_polarization)

**Schema Reference:** [spontaneous_polarization](./elements/spontaneous_polarization.md)

**Unit:** uC/cm2

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20spontaneous_polarization" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>reference structure</strong> (Optional, Multivalued)</summary>

**Description:** Reference paraelectric structure

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:reference_structure`](https://w3id.org/nfdi4cat/catcore/reference_structure)

**Schema Reference:** [reference_structure](./elements/reference_structure.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20reference_structure" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>switching barrier</strong> (Optional, Multivalued)</summary>

**Description:** Switching barrier

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:switching_barrier`](https://w3id.org/nfdi4cat/catcore/switching_barrier)

**Schema Reference:** [switching_barrier](./elements/switching_barrier.md)

**Unit:** eV

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20switching_barrier" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>coercive field</strong> (Optional, Multivalued)</summary>

**Description:** Coercive field

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:coercive_field`](https://w3id.org/nfdi4cat/catcore/coercive_field)

**Schema Reference:** [coercive_field](./elements/coercive_field.md)

**Unit:** kV/cm

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20coercive_field" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>temperature dependence</strong> (Optional, Multivalued)</summary>

**Description:** Temperature dependence

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:temperature_dependence`](https://w3id.org/nfdi4cat/catcore/temperature_dependence)

**Schema Reference:** [temperature_dependence](./elements/temperature_dependence.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20temperature_dependence" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>BandGap</strong></summary>

**Description:** Band gap property

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20BandGap" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:BandGap`](https://w3id.org/nfdi4cat/catcore/BandGap)

**Schema Reference:** [BandGap](./elements/BandGap.md)

**Slots**

<details markdown="1">
<summary><strong>material sample</strong> (Optional, Multivalued)</summary>

**Description:** Material sample

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0005056`](https://w3id.org/nfdi4cat/voc4cat_0005056)

**Schema Reference:** [material_sample](./elements/material_sample.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20material_sample" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>structure model</strong> (Optional, Multivalued)</summary>

**Description:** Structure or model used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:structure_model`](https://w3id.org/nfdi4cat/catcore/structure_model)

**Schema Reference:** [structure_model](./elements/structure_model.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20structure_model" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>k point mesh</strong> (Optional, Multivalued)</summary>

**Description:** k-point mesh for sampling

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:k_point_mesh`](https://w3id.org/nfdi4cat/catcore/k_point_mesh)

**Schema Reference:** [k_point_mesh](./elements/k_point_mesh.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20k_point_mesh" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>smearing broadening</strong> (Optional, Multivalued)</summary>

**Description:** Smearing or broadening parameter

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:smearing_broadening`](https://w3id.org/nfdi4cat/catcore/smearing_broadening)

**Schema Reference:** [smearing_broadening](./elements/smearing_broadening.md)

**Unit:** eV

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20smearing_broadening" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>direct indirect</strong> (Optional, Multivalued)</summary>

**Description:** Direct or indirect band gap

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:direct_indirect`](https://w3id.org/nfdi4cat/catcore/direct_indirect)

**Schema Reference:** [direct_indirect](./elements/direct_indirect.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20direct_indirect" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>experimental reference</strong> (Optional, Multivalued)</summary>

**Description:** Experimental reference value

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:experimental_reference`](https://w3id.org/nfdi4cat/catcore/experimental_reference)

**Schema Reference:** [experimental_reference](./elements/experimental_reference.md)

**Unit:** eV

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20experimental_reference" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>gw hybrid correction</strong> (Optional, Multivalued)</summary>

**Description:** GW or hybrid correction used

**Range:** boolean

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:gw_hybrid_correction`](https://w3id.org/nfdi4cat/catcore/gw_hybrid_correction)

**Schema Reference:** [gw_hybrid_correction](./elements/gw_hybrid_correction.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20gw_hybrid_correction" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>excitonic correction</strong> (Optional, Multivalued)</summary>

**Description:** Excitonic correction applied

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:excitonic_correction`](https://w3id.org/nfdi4cat/catcore/excitonic_correction)

**Schema Reference:** [excitonic_correction](./elements/excitonic_correction.md)

**Unit:** eV

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20excitonic_correction" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calculated_property" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<iframe
    src="assets/chart_simulation.html"
    width="100%"
    height= "800vh"
    style="border: 2px solid #5C88DA; background-color: #F0F8FF;
    "
    allowfullscreen
></iframe>