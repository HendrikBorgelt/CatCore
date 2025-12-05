# Characterization

The data class 'Characterization' describes the minimum information which should be 
reported with research data to describe the nature of the catalyst.

## Slots

Fields for Metadata which should be described when using this Metadata Aspect.

- **Description:**A short description for Comprehension purposes

- **Range:** Further Aspects which are Important for describing a certain aspect

- **Cardinality:** A description how often it is allowed and how important it is to describe a certain aspect

- **Range:** Further Aspects which are Important for describing a certain aspect

- **CURIE:** The Abbreviated form of a URI, where the Prefix, e.g. voc4cat, described to which terminology a Concept belong. The Links are fully implemented here. For reusing these CURIE's you need to substitute the prefix against the URI for it.

- **Schema Reference:** A Link to the native LinkML Documentation on which this metadatacatalog and strucutre is based upon

<details markdown="1">
<summary><strong>equipment</strong> (Required, Multivalued)</summary>

**Description:** Equipment used

**Range:** string

**Cardinality:**  Required, Multivalued

**CURIE:** [`voc4cat:0000187`](https://w3id.org/nfdi4cat/voc4cat_0000187)

**Schema Reference:** [equipment](./elements/equipment.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20equipment" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>characterization technique</strong> (Required, Multivalued)</summary>

**Description:** Technique used for characterization

**Range:** CharacterizationTechnique

**Cardinality:**  Required, Multivalued

**CURIE:** [`voc4cat:0000066`](https://w3id.org/nfdi4cat/voc4cat_0000066)

**Schema Reference:** [characterization_technique](./elements/characterization_technique.md)

**Range Class Details:**

<details markdown="1">
<summary><strong>CharacterizationTechnique</strong></summary>

**Abstract Class**

**Description:** Characterization technique used for catalyst analysis

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20CharacterizationTechnique" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**Schema Reference:** [CharacterizationTechnique](./elements/CharacterizationTechnique.md)

</details>

**Possible Subclasses / Enumerations of CharacterizationTechnique:**

<details markdown="1">
<summary><strong>PowderXRD</strong></summary>

**Description:** Powder X-ray diffraction

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20PowderXRD" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`CHMO:0000158`](http://purl.obolibrary.org/obo/CHMO_0000158)

**Schema Reference:** [PowderXRD](./elements/PowderXRD.md)

**Slots**

<details markdown="1">
<summary><strong>xray source</strong> (Optional, Multivalued)</summary>

**Description:** X-ray source used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`OBI:0001138`](http://purl.obolibrary.org/obo/OBI_0001138)

**Schema Reference:** [xray_source](./elements/xray_source.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20xray_source" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Atmospheric conditions

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:atmosphere`](https://w3id.org/nfdi4cat/catcore/atmosphere)

**Schema Reference:** [atmosphere](./elements/atmosphere.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20atmosphere" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>operation mode</strong> (Optional, Multivalued)</summary>

**Description:** Operation mode of the instrument

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000108`](https://w3id.org/nfdi4cat/voc4cat_0000108)

**Schema Reference:** [operation_mode](./elements/operation_mode.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20operation_mode" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>minimum 2theta</strong> (Optional, Multivalued)</summary>

**Description:** Minimum 2-theta angle

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:minimum_2theta`](https://w3id.org/nfdi4cat/catcore/minimum_2theta)

**Schema Reference:** [minimum_2theta](./elements/minimum_2theta.md)

**Unit:** deg

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20minimum_2theta" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>maximum 2theta</strong> (Optional, Multivalued)</summary>

**Description:** Maximum 2-theta angle

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:maximum_2theta`](https://w3id.org/nfdi4cat/catcore/maximum_2theta)

**Schema Reference:** [maximum_2theta](./elements/maximum_2theta.md)

**Unit:** deg

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20maximum_2theta" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>step size</strong> (Optional, Multivalued)</summary>

**Description:** Step size for measurements

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0000950`](http://purl.allotrope.org/ontologies/result#AFR_0000950)

**Schema Reference:** [step_size](./elements/step_size.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20step_size" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>monochromator</strong> (Optional, Multivalued)</summary>

**Description:** Monochromator type used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`CHMO:0002120`](http://purl.obolibrary.org/obo/CHMO_0002120)

**Schema Reference:** [monochromator](./elements/monochromator.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20monochromator" target="_blank" class="md-button md-button--primary">
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
<summary><strong>sample spinning speed</strong> (Optional, Multivalued)</summary>

**Description:** Sample spinning speed

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:sample_spinning_speed`](https://w3id.org/nfdi4cat/catcore/sample_spinning_speed)

**Schema Reference:** [sample_spinning_speed](./elements/sample_spinning_speed.md)

**Unit:** rpm

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20sample_spinning_speed" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>experiment duration</strong> (Optional, Multivalued)</summary>

**Description:** Duration of the experiment

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0002455`](http://purl.allotrope.org/ontologies/result#AFR_0002455)

**Schema Reference:** [experiment_duration](./elements/experiment_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20experiment_duration" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>XRayAbsorptionSpectroscopy</strong></summary>

**Description:** X-ray absorption spectroscopy

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20XRayAbsorptionSpectroscopy" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`voc4cat:0000286`](https://w3id.org/nfdi4cat/voc4cat_0000286)

**Schema Reference:** [XRayAbsorptionSpectroscopy](./elements/XRayAbsorptionSpectroscopy.md)

**Slots**

<details markdown="1">
<summary><strong>operation mode</strong> (Optional, Multivalued)</summary>

**Description:** Operation mode of the instrument

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000108`](https://w3id.org/nfdi4cat/voc4cat_0000108)

**Schema Reference:** [operation_mode](./elements/operation_mode.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20operation_mode" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>element analyzed</strong> (Optional, Multivalued)</summary>

**Description:** Chemical element being analyzed

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:element_analyzed`](https://w3id.org/nfdi4cat/catcore/element_analyzed)

**Schema Reference:** [element_analyzed](./elements/element_analyzed.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20element_analyzed" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>absorption edge</strong> (Optional, Multivalued)</summary>

**Description:** Absorption edge measured

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:absorption_edge`](https://w3id.org/nfdi4cat/catcore/absorption_edge)

**Schema Reference:** [absorption_edge](./elements/absorption_edge.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20absorption_edge" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>monochromator</strong> (Optional, Multivalued)</summary>

**Description:** Monochromator type used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`CHMO:0002120`](http://purl.obolibrary.org/obo/CHMO_0002120)

**Schema Reference:** [monochromator](./elements/monochromator.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20monochromator" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>minimum energy</strong> (Optional, Multivalued)</summary>

**Description:** Minimum energy value

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:minimum_energy`](https://w3id.org/nfdi4cat/catcore/minimum_energy)

**Schema Reference:** [minimum_energy](./elements/minimum_energy.md)

**Unit:** eV

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20minimum_energy" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>maximum energy</strong> (Optional, Multivalued)</summary>

**Description:** Maximum energy value

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:maximum_energy`](https://w3id.org/nfdi4cat/catcore/maximum_energy)

**Schema Reference:** [maximum_energy](./elements/maximum_energy.md)

**Unit:** eV

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20maximum_energy" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>energy resolution</strong> (Optional, Multivalued)</summary>

**Description:** Energy resolution of the measurement

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0000950`](http://purl.allotrope.org/ontologies/result#AFR_0000950)

**Schema Reference:** [energy_resolution](./elements/energy_resolution.md)

**Unit:** eV

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20energy_resolution" target="_blank" class="md-button md-button--primary">
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
<summary><strong>beamline source</strong> (Optional, Multivalued)</summary>

**Description:** Beamline source identification

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:beamline_source`](https://w3id.org/nfdi4cat/catcore/beamline_source)

**Schema Reference:** [beamline_source](./elements/beamline_source.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20beamline_source" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>noise of measurement</strong> (Optional, Multivalued)</summary>

**Description:** Noise level of the measurement

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:noise_of_measurement`](https://w3id.org/nfdi4cat/catcore/noise_of_measurement)

**Schema Reference:** [noise_of_measurement](./elements/noise_of_measurement.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20noise_of_measurement" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of cycles</strong> (Optional, Multivalued)</summary>

**Description:** Number of cycles in the process

**Range:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:number_of_cycles`](https://w3id.org/nfdi4cat/catcore/number_of_cycles)

**Schema Reference:** [number_of_cycles](./elements/number_of_cycles.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_cycles" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>InfraredSpectroscopy</strong></summary>

**Description:** Infrared spectroscopy

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20InfraredSpectroscopy" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:InfraredSpectroscopy`](https://w3id.org/nfdi4cat/catcore/InfraredSpectroscopy)

**Schema Reference:** [InfraredSpectroscopy](./elements/InfraredSpectroscopy.md)

**Slots**

<details markdown="1">
<summary><strong>operation mode</strong> (Optional, Multivalued)</summary>

**Description:** Operation mode of the instrument

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000108`](https://w3id.org/nfdi4cat/voc4cat_0000108)

**Schema Reference:** [operation_mode](./elements/operation_mode.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20operation_mode" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>minimum wavenumber</strong> (Optional, Multivalued)</summary>

**Description:** Minimum wavenumber

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:minimum_wavenumber`](https://w3id.org/nfdi4cat/catcore/minimum_wavenumber)

**Schema Reference:** [minimum_wavenumber](./elements/minimum_wavenumber.md)

**Unit:** cm-1

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20minimum_wavenumber" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>maximum wavenumber</strong> (Optional, Multivalued)</summary>

**Description:** Maximum wavenumber

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:maximum_wavenumber`](https://w3id.org/nfdi4cat/catcore/maximum_wavenumber)

**Schema Reference:** [maximum_wavenumber](./elements/maximum_wavenumber.md)

**Unit:** cm-1

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20maximum_wavenumber" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>step size</strong> (Optional, Multivalued)</summary>

**Description:** Step size for measurements

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0000950`](http://purl.allotrope.org/ontologies/result#AFR_0000950)

**Schema Reference:** [step_size](./elements/step_size.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20step_size" target="_blank" class="md-button md-button--primary">
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
<summary><strong>background correction</strong> (Optional, Multivalued)</summary>

**Description:** Background correction method

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFP:0003721`](http://purl.allotrope.org/ontologies/process#AFP_0003721)

**Schema Reference:** [background_correction](./elements/background_correction.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20background_correction" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of scans</strong> (Optional, Multivalued)</summary>

**Description:** Number of scans performed

**Range:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0003051`](http://purl.allotrope.org/ontologies/result#AFR_0003051)

**Schema Reference:** [number_of_scans](./elements/number_of_scans.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_scans" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Atmospheric conditions

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:atmosphere`](https://w3id.org/nfdi4cat/catcore/atmosphere)

**Schema Reference:** [atmosphere](./elements/atmosphere.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20atmosphere" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>RamanSpectroscopy</strong></summary>

**Description:** Raman spectroscopy

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20RamanSpectroscopy" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`voc4cat:0000069`](https://w3id.org/nfdi4cat/voc4cat_0000069)

**Schema Reference:** [RamanSpectroscopy](./elements/RamanSpectroscopy.md)

**Slots**

<details markdown="1">
<summary><strong>excitation laser wavelength</strong> (Optional, Multivalued)</summary>

**Description:** Excitation laser wavelength

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0001594`](http://purl.allotrope.org/ontologies/result#AFR_0001594)

**Schema Reference:** [excitation_laser_wavelength](./elements/excitation_laser_wavelength.md)

**Unit:** nm

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20excitation_laser_wavelength" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>excitation laser power</strong> (Optional, Multivalued)</summary>

**Description:** Excitation laser power

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0001595`](http://purl.allotrope.org/ontologies/result#AFR_0001595)

**Schema Reference:** [excitation_laser_power](./elements/excitation_laser_power.md)

**Unit:** mW

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20excitation_laser_power" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>magnification setting</strong> (Optional, Multivalued)</summary>

**Description:** Magnification setting

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0002226`](http://purl.allotrope.org/ontologies/result#AFR_0002226)

**Schema Reference:** [magnification_setting](./elements/magnification_setting.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20magnification_setting" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>integration time</strong> (Optional, Multivalued)</summary>

**Description:** Integration time

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0001671`](http://purl.allotrope.org/ontologies/result#AFR_0001671)

**Schema Reference:** [integration_time](./elements/integration_time.md)

**Unit:** s

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20integration_time" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of scans</strong> (Optional, Multivalued)</summary>

**Description:** Number of scans performed

**Range:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0003051`](http://purl.allotrope.org/ontologies/result#AFR_0003051)

**Schema Reference:** [number_of_scans](./elements/number_of_scans.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_scans" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Atmospheric conditions

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:atmosphere`](https://w3id.org/nfdi4cat/catcore/atmosphere)

**Schema Reference:** [atmosphere](./elements/atmosphere.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20atmosphere" target="_blank" class="md-button md-button--primary">
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
<summary><strong>filter or grating</strong> (Optional, Multivalued)</summary>

**Description:** Filter or grating used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:filter_or_grating`](https://w3id.org/nfdi4cat/catcore/filter_or_grating)

**Schema Reference:** [filter_or_grating](./elements/filter_or_grating.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20filter_or_grating" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>GCMS</strong></summary>

**Description:** Gas chromatography-mass spectrometry

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20GCMS" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`CHMO:0000497`](http://purl.obolibrary.org/obo/CHMO_0000497)

**Schema Reference:** [GCMS](./elements/GCMS.md)

**Slots**

<details markdown="1">
<summary><strong>external standard</strong> (Optional, Multivalued)</summary>

**Description:** External standard used for calibration

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:external_standard`](https://w3id.org/nfdi4cat/catcore/external_standard)

**Schema Reference:** [external_standard](./elements/external_standard.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20external_standard" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>internal standard</strong> (Optional, Multivalued)</summary>

**Description:** Internal standard used for calibration

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:internal_standard`](https://w3id.org/nfdi4cat/catcore/internal_standard)

**Schema Reference:** [internal_standard](./elements/internal_standard.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20internal_standard" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>column type</strong> (Optional, Multivalued)</summary>

**Description:** Type of chromatography column

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0002026`](http://purl.allotrope.org/ontologies/result#AFR_0002026)

**Schema Reference:** [column_type](./elements/column_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20column_type" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>carrier gas</strong> (Optional, Multivalued)</summary>

**Description:** Carrier gas used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:carrier_gas`](https://w3id.org/nfdi4cat/catcore/carrier_gas)

**Schema Reference:** [carrier_gas](./elements/carrier_gas.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20carrier_gas" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>carrier gas purity</strong> (Optional, Multivalued)</summary>

**Description:** Purity of carrier gas

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:carrier_gas_purity`](https://w3id.org/nfdi4cat/catcore/carrier_gas_purity)

**Schema Reference:** [carrier_gas_purity](./elements/carrier_gas_purity.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20carrier_gas_purity" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>inlet temperature</strong> (Optional, Multivalued)</summary>

**Description:** Inlet temperature

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:inlet_temperature`](https://w3id.org/nfdi4cat/catcore/inlet_temperature)

**Schema Reference:** [inlet_temperature](./elements/inlet_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20inlet_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>minimum oven temperature</strong> (Optional, Multivalued)</summary>

**Description:** Minimum oven temperature

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:minimum_oven_temperature`](https://w3id.org/nfdi4cat/catcore/minimum_oven_temperature)

**Schema Reference:** [minimum_oven_temperature](./elements/minimum_oven_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20minimum_oven_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>maximum oven temperature</strong> (Optional, Multivalued)</summary>

**Description:** Maximum oven temperature

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:maximum_oven_temperature`](https://w3id.org/nfdi4cat/catcore/maximum_oven_temperature)

**Schema Reference:** [maximum_oven_temperature](./elements/maximum_oven_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20maximum_oven_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>heating ramp</strong> (Optional, Multivalued)</summary>

**Description:** Heating ramp rate

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:heating_ramp`](https://w3id.org/nfdi4cat/catcore/heating_ramp)

**Schema Reference:** [heating_ramp](./elements/heating_ramp.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20heating_ramp" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>heating procedure</strong> (Optional, Multivalued)</summary>

**Description:** Heating procedure used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:heating_procedure`](https://w3id.org/nfdi4cat/catcore/heating_procedure)

**Schema Reference:** [heating_procedure](./elements/heating_procedure.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20heating_procedure" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>acquisition mode</strong> (Optional, Multivalued)</summary>

**Description:** Data acquisition mode

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:acquisition_mode`](https://w3id.org/nfdi4cat/catcore/acquisition_mode)

**Schema Reference:** [acquisition_mode](./elements/acquisition_mode.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20acquisition_mode" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>solvent delay</strong> (Optional, Multivalued)</summary>

**Description:** Solvent delay time

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:solvent_delay`](https://w3id.org/nfdi4cat/catcore/solvent_delay)

**Schema Reference:** [solvent_delay](./elements/solvent_delay.md)

**Unit:** min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20solvent_delay" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>trace ion detection</strong> (Optional, Multivalued)</summary>

**Description:** Trace ion detection setting

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:trace_ion_detection`](https://w3id.org/nfdi4cat/catcore/trace_ion_detection)

**Schema Reference:** [trace_ion_detection](./elements/trace_ion_detection.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20trace_ion_detection" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mz minimum</strong> (Optional, Multivalued)</summary>

**Description:** Minimum m/z value

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0002652`](http://purl.allotrope.org/ontologies/result#AFR_0002652)

**Schema Reference:** [mz_minimum](./elements/mz_minimum.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mz_minimum" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mz maximum</strong> (Optional, Multivalued)</summary>

**Description:** Maximum m/z value

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0002653`](http://purl.allotrope.org/ontologies/result#AFR_0002653)

**Schema Reference:** [mz_maximum](./elements/mz_maximum.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mz_maximum" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>split ratio</strong> (Optional, Multivalued)</summary>

**Description:** Split ratio for injection

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:split_ratio`](https://w3id.org/nfdi4cat/catcore/split_ratio)

**Schema Reference:** [split_ratio](./elements/split_ratio.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20split_ratio" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>injection volume</strong> (Optional, Multivalued)</summary>

**Description:** Injection volume

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0001577`](http://purl.allotrope.org/ontologies/result#AFR_0001577)

**Schema Reference:** [injection_volume](./elements/injection_volume.md)

**Unit:** uL

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20injection_volume" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>NMRSpectroscopy</strong></summary>

**Description:** Nuclear magnetic resonance spectroscopy

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20NMRSpectroscopy" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`voc4cat:0000073`](https://w3id.org/nfdi4cat/voc4cat_0000073)

**Schema Reference:** [NMRSpectroscopy](./elements/NMRSpectroscopy.md)

**Slots**

<details markdown="1">
<summary><strong>nucleus</strong> (Optional, Multivalued)</summary>

**Description:** Nucleus being observed

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:nucleus`](https://w3id.org/nfdi4cat/catcore/nucleus)

**Schema Reference:** [nucleus](./elements/nucleus.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20nucleus" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>solvent</strong> (Optional, Multivalued)</summary>

**Description:** Solvent used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0007246`](https://w3id.org/nfdi4cat/voc4cat_0007246)

**Schema Reference:** [solvent](./elements/solvent.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20solvent" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>irradiation frequency</strong> (Optional, Multivalued)</summary>

**Description:** Irradiation frequency

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`nmrCV:1400026`](http://nmrML.org/nmrCV#NMR:1400026)

**Schema Reference:** [irradiation_frequency](./elements/irradiation_frequency.md)

**Unit:** MHz

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20irradiation_frequency" target="_blank" class="md-button md-button--primary">
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
<summary><strong>nmr pulse sequence</strong> (Optional, Multivalued)</summary>

**Description:** NMR pulse sequence used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`nmrCV:1400037`](http://nmrML.org/nmrCV#NMR:1400037)

**Schema Reference:** [nmr_pulse_sequence](./elements/nmr_pulse_sequence.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20nmr_pulse_sequence" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>nmr sample tube</strong> (Optional, Multivalued)</summary>

**Description:** NMR sample tube type

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`nmrCV:1400132`](http://nmrML.org/nmrCV#NMR:1400132)

**Schema Reference:** [nmr_sample_tube](./elements/nmr_sample_tube.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20nmr_sample_tube" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of scans</strong> (Optional, Multivalued)</summary>

**Description:** Number of scans performed

**Range:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0003051`](http://purl.allotrope.org/ontologies/result#AFR_0003051)

**Schema Reference:** [number_of_scans](./elements/number_of_scans.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_scans" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Atmospheric conditions

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:atmosphere`](https://w3id.org/nfdi4cat/catcore/atmosphere)

**Schema Reference:** [atmosphere](./elements/atmosphere.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20atmosphere" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>TransmissionElectronMicroscopy</strong></summary>

**Description:** Transmission electron microscopy

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20TransmissionElectronMicroscopy" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`voc4cat:0000078`](https://w3id.org/nfdi4cat/voc4cat_0000078)

**Schema Reference:** [TransmissionElectronMicroscopy](./elements/TransmissionElectronMicroscopy.md)

**Slots**

<details markdown="1">
<summary><strong>operation mode</strong> (Optional, Multivalued)</summary>

**Description:** Operation mode of the instrument

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000108`](https://w3id.org/nfdi4cat/voc4cat_0000108)

**Schema Reference:** [operation_mode](./elements/operation_mode.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20operation_mode" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>gun type</strong> (Optional, Multivalued)</summary>

**Description:** Type of electron gun

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:gun_type`](https://w3id.org/nfdi4cat/catcore/gun_type)

**Schema Reference:** [gun_type](./elements/gun_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20gun_type" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>acceleration voltage</strong> (Optional, Multivalued)</summary>

**Description:** Acceleration voltage

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:acceleration_voltage`](https://w3id.org/nfdi4cat/catcore/acceleration_voltage)

**Schema Reference:** [acceleration_voltage](./elements/acceleration_voltage.md)

**Unit:** kV

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20acceleration_voltage" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>magnification setting</strong> (Optional, Multivalued)</summary>

**Description:** Magnification setting

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0002226`](http://purl.allotrope.org/ontologies/result#AFR_0002226)

**Schema Reference:** [magnification_setting](./elements/magnification_setting.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20magnification_setting" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>ICPAES</strong></summary>

**Description:** Inductively-coupled plasma atomic emission spectroscopy

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ICPAES" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`CHMO:0000267`](http://purl.obolibrary.org/obo/CHMO_0000267)

**Schema Reference:** [ICPAES](./elements/ICPAES.md)

**Slots**

<details markdown="1">
<summary><strong>element analyzed</strong> (Optional, Multivalued)</summary>

**Description:** Chemical element being analyzed

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:element_analyzed`](https://w3id.org/nfdi4cat/catcore/element_analyzed)

**Schema Reference:** [element_analyzed](./elements/element_analyzed.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20element_analyzed" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calibration method</strong> (Optional, Multivalued)</summary>

**Description:** Calibration method used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:calibration_method`](https://w3id.org/nfdi4cat/catcore/calibration_method)

**Schema Reference:** [calibration_method](./elements/calibration_method.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calibration_method" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>detection limit</strong> (Optional, Multivalued)</summary>

**Description:** Detection limit

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`NCIT:C105701`](http://purl.obolibrary.org/obo/NCIT_C105701)

**Schema Reference:** [detection_limit](./elements/detection_limit.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20detection_limit" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>matrix effect correction</strong> (Optional, Multivalued)</summary>

**Description:** Matrix effect correction method

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:matrix_effect_correction`](https://w3id.org/nfdi4cat/catcore/matrix_effect_correction)

**Schema Reference:** [matrix_effect_correction](./elements/matrix_effect_correction.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20matrix_effect_correction" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>ScanningElectronMicroscopy</strong></summary>

**Description:** Scanning electron microscopy

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ScanningElectronMicroscopy" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`voc4cat:0000075`](https://w3id.org/nfdi4cat/voc4cat_0000075)

**Schema Reference:** [ScanningElectronMicroscopy](./elements/ScanningElectronMicroscopy.md)

**Slots**

<details markdown="1">
<summary><strong>gun type</strong> (Optional, Multivalued)</summary>

**Description:** Type of electron gun

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:gun_type`](https://w3id.org/nfdi4cat/catcore/gun_type)

**Schema Reference:** [gun_type](./elements/gun_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20gun_type" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>acceleration voltage</strong> (Optional, Multivalued)</summary>

**Description:** Acceleration voltage

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:acceleration_voltage`](https://w3id.org/nfdi4cat/catcore/acceleration_voltage)

**Schema Reference:** [acceleration_voltage](./elements/acceleration_voltage.md)

**Unit:** kV

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20acceleration_voltage" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>image resolution</strong> (Optional, Multivalued)</summary>

**Description:** Image resolution

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:image_resolution`](https://w3id.org/nfdi4cat/catcore/image_resolution)

**Schema Reference:** [image_resolution](./elements/image_resolution.md)

**Unit:** nm

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20image_resolution" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>field emitter</strong> (Optional, Multivalued)</summary>

**Description:** Field emitter type

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:field_emitter`](https://w3id.org/nfdi4cat/catcore/field_emitter)

**Schema Reference:** [field_emitter](./elements/field_emitter.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20field_emitter" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>Thermogravimetry</strong></summary>

**Description:** Thermogravimetry

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Thermogravimetry" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`CHMO:0000690`](http://purl.obolibrary.org/obo/CHMO_0000690)

**Schema Reference:** [Thermogravimetry](./elements/Thermogravimetry.md)

**Slots**

<details markdown="1">
<summary><strong>operation mode</strong> (Optional, Multivalued)</summary>

**Description:** Operation mode of the instrument

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000108`](https://w3id.org/nfdi4cat/voc4cat_0000108)

**Schema Reference:** [operation_mode](./elements/operation_mode.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20operation_mode" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Atmospheric conditions

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:atmosphere`](https://w3id.org/nfdi4cat/catcore/atmosphere)

**Schema Reference:** [atmosphere](./elements/atmosphere.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20atmosphere" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>initial temperature</strong> (Optional, Multivalued)</summary>

**Description:** Initial temperature

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`NCIT:C164644`](http://purl.obolibrary.org/obo/NCIT_C164644)

**Schema Reference:** [initial_temperature](./elements/initial_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20initial_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>final temperature</strong> (Optional, Multivalued)</summary>

**Description:** Final temperature

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`NCIT:C164644`](http://purl.obolibrary.org/obo/NCIT_C164644)

**Schema Reference:** [final_temperature](./elements/final_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20final_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>heating rate</strong> (Optional, Multivalued)</summary>

**Description:** Heating rate

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:heating_rate`](https://w3id.org/nfdi4cat/catcore/heating_rate)

**Schema Reference:** [heating_rate](./elements/heating_rate.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20heating_rate" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>heating procedure</strong> (Optional, Multivalued)</summary>

**Description:** Heating procedure used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:heating_procedure`](https://w3id.org/nfdi4cat/catcore/heating_procedure)

**Schema Reference:** [heating_procedure](./elements/heating_procedure.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20heating_procedure" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>sample mass</strong> (Optional, Multivalued)</summary>

**Description:** Mass of sample

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0007038`](https://w3id.org/nfdi4cat/voc4cat_0007038)

**Schema Reference:** [sample_mass](./elements/sample_mass.md)

**Unit:** mg

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20sample_mass" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>XPS</strong></summary>

**Description:** X-ray photoelectron spectroscopy

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20XPS" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`CHMO:0000404`](http://purl.obolibrary.org/obo/CHMO_0000404)

**Schema Reference:** [XPS](./elements/XPS.md)

**Slots**

<details markdown="1">
<summary><strong>xray source</strong> (Optional, Multivalued)</summary>

**Description:** X-ray source used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`OBI:0001138`](http://purl.obolibrary.org/obo/OBI_0001138)

**Schema Reference:** [xray_source](./elements/xray_source.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20xray_source" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>total acquisition time</strong> (Optional, Multivalued)</summary>

**Description:** Total acquisition time

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:total_acquisition_time`](https://w3id.org/nfdi4cat/catcore/total_acquisition_time)

**Schema Reference:** [total_acquisition_time](./elements/total_acquisition_time.md)

**Unit:** s

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20total_acquisition_time" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of scans</strong> (Optional, Multivalued)</summary>

**Description:** Number of scans performed

**Range:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0003051`](http://purl.allotrope.org/ontologies/result#AFR_0003051)

**Schema Reference:** [number_of_scans](./elements/number_of_scans.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_scans" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>spot size</strong> (Optional, Multivalued)</summary>

**Description:** Spot size for analysis

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:spot_size`](https://w3id.org/nfdi4cat/catcore/spot_size)

**Schema Reference:** [spot_size](./elements/spot_size.md)

**Unit:** mm

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20spot_size" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>lense mode</strong> (Optional, Multivalued)</summary>

**Description:** Lens mode setting

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000108`](https://w3id.org/nfdi4cat/voc4cat_0000108)

**Schema Reference:** [lense_mode](./elements/lense_mode.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20lense_mode" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>minimum energy</strong> (Optional, Multivalued)</summary>

**Description:** Minimum energy value

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:minimum_energy`](https://w3id.org/nfdi4cat/catcore/minimum_energy)

**Schema Reference:** [minimum_energy](./elements/minimum_energy.md)

**Unit:** eV

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20minimum_energy" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>maximum energy</strong> (Optional, Multivalued)</summary>

**Description:** Maximum energy value

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:maximum_energy`](https://w3id.org/nfdi4cat/catcore/maximum_energy)

**Schema Reference:** [maximum_energy](./elements/maximum_energy.md)

**Unit:** eV

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20maximum_energy" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>step size</strong> (Optional, Multivalued)</summary>

**Description:** Step size for measurements

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0000950`](http://purl.allotrope.org/ontologies/result#AFR_0000950)

**Schema Reference:** [step_size](./elements/step_size.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20step_size" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>pass energy</strong> (Optional, Multivalued)</summary>

**Description:** Pass energy setting

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:pass_energy`](https://w3id.org/nfdi4cat/catcore/pass_energy)

**Schema Reference:** [pass_energy](./elements/pass_energy.md)

**Unit:** eV

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20pass_energy" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>charge compensation</strong> (Optional, Multivalued)</summary>

**Description:** Charge compensation method

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:charge_compensation`](https://w3id.org/nfdi4cat/catcore/charge_compensation)

**Schema Reference:** [charge_compensation](./elements/charge_compensation.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20charge_compensation" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Atmospheric conditions

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:atmosphere`](https://w3id.org/nfdi4cat/catcore/atmosphere)

**Schema Reference:** [atmosphere](./elements/atmosphere.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20atmosphere" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>BET</strong></summary>

**Description:** Brunauer-Emmett-Teller surface area analysis

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20BET" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:BET`](https://w3id.org/nfdi4cat/catcore/BET)

**Schema Reference:** [BET](./elements/BET.md)

**Slots**

<details markdown="1">
<summary><strong>adsorbate gas</strong> (Optional, Multivalued)</summary>

**Description:** Adsorbate gas used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:adsorbate_gas`](https://w3id.org/nfdi4cat/catcore/adsorbate_gas)

**Schema Reference:** [adsorbate_gas](./elements/adsorbate_gas.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20adsorbate_gas" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>degassing temperature</strong> (Optional, Multivalued)</summary>

**Description:** Degassing temperature

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:degassing_temperature`](https://w3id.org/nfdi4cat/catcore/degassing_temperature)

**Schema Reference:** [degassing_temperature](./elements/degassing_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20degassing_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>measurement temperature</strong> (Optional, Multivalued)</summary>

**Description:** Measurement temperature

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:measurement_temperature`](https://w3id.org/nfdi4cat/catcore/measurement_temperature)

**Schema Reference:** [measurement_temperature](./elements/measurement_temperature.md)

**Unit:** K

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20measurement_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>pore size distribution method</strong> (Optional, Multivalued)</summary>

**Description:** Method for pore size distribution analysis

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:pore_size_distribution_method`](https://w3id.org/nfdi4cat/catcore/pore_size_distribution_method)

**Schema Reference:** [pore_size_distribution_method](./elements/pore_size_distribution_method.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20pore_size_distribution_method" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>sample mass</strong> (Optional, Multivalued)</summary>

**Description:** Mass of sample

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0007038`](https://w3id.org/nfdi4cat/voc4cat_0007038)

**Schema Reference:** [sample_mass](./elements/sample_mass.md)

**Unit:** mg

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20sample_mass" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>ElementalAnalysis</strong></summary>

**Description:** Elemental analysis

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ElementalAnalysis" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`CHMO:0001075`](http://purl.obolibrary.org/obo/CHMO_0001075)

**Schema Reference:** [ElementalAnalysis](./elements/ElementalAnalysis.md)

**Slots**

<details markdown="1">
<summary><strong>elements analyzed</strong> (Optional, Multivalued)</summary>

**Description:** Elements analyzed

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:elements_analyzed`](https://w3id.org/nfdi4cat/catcore/elements_analyzed)

**Schema Reference:** [elements_analyzed](./elements/elements_analyzed.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20elements_analyzed" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>combustion temperature</strong> (Optional, Multivalued)</summary>

**Description:** Combustion temperature

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:combustion_temperature`](https://w3id.org/nfdi4cat/catcore/combustion_temperature)

**Schema Reference:** [combustion_temperature](./elements/combustion_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20combustion_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>carrier gas</strong> (Optional, Multivalued)</summary>

**Description:** Carrier gas used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:carrier_gas`](https://w3id.org/nfdi4cat/catcore/carrier_gas)

**Schema Reference:** [carrier_gas](./elements/carrier_gas.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20carrier_gas" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>UVVisSpectroscopy</strong></summary>

**Description:** Ultraviolet-visible spectroscopy

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20UVVisSpectroscopy" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`voc4cat:0000079`](https://w3id.org/nfdi4cat/voc4cat_0000079)

**Schema Reference:** [UVVisSpectroscopy](./elements/UVVisSpectroscopy.md)

**Slots**

<details markdown="1">
<summary><strong>minimum wavelength</strong> (Optional, Multivalued)</summary>

**Description:** Minimum wavelength

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:minimum_wavelength`](https://w3id.org/nfdi4cat/catcore/minimum_wavelength)

**Schema Reference:** [minimum_wavelength](./elements/minimum_wavelength.md)

**Unit:** nm

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20minimum_wavelength" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>maximum wavelength</strong> (Optional, Multivalued)</summary>

**Description:** Maximum wavelength

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:maximum_wavelength`](https://w3id.org/nfdi4cat/catcore/maximum_wavelength)

**Schema Reference:** [maximum_wavelength](./elements/maximum_wavelength.md)

**Unit:** nm

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20maximum_wavelength" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>path length</strong> (Optional, Multivalued)</summary>

**Description:** Path length of cell

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFQ:0000268`](http://purl.allotrope.org/ontologies/quality#AFQ_0000268)

**Schema Reference:** [path_length](./elements/path_length.md)

**Unit:** cm

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20path_length" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>solvent</strong> (Optional, Multivalued)</summary>

**Description:** Solvent used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0007246`](https://w3id.org/nfdi4cat/voc4cat_0007246)

**Schema Reference:** [solvent](./elements/solvent.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20solvent" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>concentration</strong> (Optional, Multivalued)</summary>

**Description:** Concentration of sample

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0007244`](https://w3id.org/nfdi4cat/voc4cat_0007244)

**Schema Reference:** [concentration](./elements/concentration.md)

**Unit:** mol/L

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20concentration" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>DRIFTS</strong></summary>

**Description:** Diffuse reflectance infrared Fourier transform spectroscopy

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20DRIFTS" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`CHMO:0000645`](http://purl.obolibrary.org/obo/CHMO_0000645)

**Schema Reference:** [DRIFTS](./elements/DRIFTS.md)

**Slots**

<details markdown="1">
<summary><strong>adsorption gas</strong> (Optional, Multivalued)</summary>

**Description:** Adsorption gas used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:adsorption_gas`](https://w3id.org/nfdi4cat/catcore/adsorption_gas)

**Schema Reference:** [adsorption_gas](./elements/adsorption_gas.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20adsorption_gas" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Atmospheric conditions

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:atmosphere`](https://w3id.org/nfdi4cat/catcore/atmosphere)

**Schema Reference:** [atmosphere](./elements/atmosphere.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20atmosphere" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>flow rate</strong> (Optional, Multivalued)</summary>

**Description:** Flow rate

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:flow_rate`](https://w3id.org/nfdi4cat/catcore/flow_rate)

**Schema Reference:** [flow_rate](./elements/flow_rate.md)

**Unit:** mL/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20flow_rate" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>diluting reference</strong> (Optional, Multivalued)</summary>

**Description:** Diluting reference material

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:diluting_reference`](https://w3id.org/nfdi4cat/catcore/diluting_reference)

**Schema Reference:** [diluting_reference](./elements/diluting_reference.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20diluting_reference" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>ratio reference sample</strong> (Optional, Multivalued)</summary>

**Description:** Ratio of reference to sample

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:ratio_reference_sample`](https://w3id.org/nfdi4cat/catcore/ratio_reference_sample)

**Schema Reference:** [ratio_reference_sample](./elements/ratio_reference_sample.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ratio_reference_sample" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>step size</strong> (Optional, Multivalued)</summary>

**Description:** Step size for measurements

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0000950`](http://purl.allotrope.org/ontologies/result#AFR_0000950)

**Schema Reference:** [step_size](./elements/step_size.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20step_size" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>resolution</strong> (Optional, Multivalued)</summary>

**Description:** Spectral resolution

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:resolution`](https://w3id.org/nfdi4cat/catcore/resolution)

**Schema Reference:** [resolution](./elements/resolution.md)

**Unit:** cm-1

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20resolution" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>background correction method</strong> (Optional, Multivalued)</summary>

**Description:** Background correction method used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:background_correction_method`](https://w3id.org/nfdi4cat/catcore/background_correction_method)

**Schema Reference:** [background_correction_method](./elements/background_correction_method.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20background_correction_method" target="_blank" class="md-button md-button--primary">
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
<summary><strong>number of scans</strong> (Optional, Multivalued)</summary>

**Description:** Number of scans performed

**Range:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0003051`](http://purl.allotrope.org/ontologies/result#AFR_0003051)

**Schema Reference:** [number_of_scans](./elements/number_of_scans.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_scans" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>CyclicVoltammetry</strong></summary>

**Description:** Cyclic voltammetry

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20CyclicVoltammetry" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`CHMO:0000025`](http://purl.obolibrary.org/obo/CHMO_0000025)

**Schema Reference:** [CyclicVoltammetry](./elements/CyclicVoltammetry.md)

**Slots**

<details markdown="1">
<summary><strong>scan rate</strong> (Optional, Multivalued)</summary>

**Description:** Scan rate for voltammetry

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0007213`](https://w3id.org/nfdi4cat/voc4cat_0007213)

**Schema Reference:** [scan_rate](./elements/scan_rate.md)

**Unit:** mV/s

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20scan_rate" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>minimum potential</strong> (Optional, Multivalued)</summary>

**Description:** Minimum potential

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:minimum_potential`](https://w3id.org/nfdi4cat/catcore/minimum_potential)

**Schema Reference:** [minimum_potential](./elements/minimum_potential.md)

**Unit:** V

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20minimum_potential" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>maximum potential</strong> (Optional, Multivalued)</summary>

**Description:** Maximum potential

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:maximum_potential`](https://w3id.org/nfdi4cat/catcore/maximum_potential)

**Schema Reference:** [maximum_potential](./elements/maximum_potential.md)

**Unit:** V

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20maximum_potential" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>step size potential</strong> (Optional, Multivalued)</summary>

**Description:** Step size for potential

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0007218`](https://w3id.org/nfdi4cat/voc4cat_0007218)

**Schema Reference:** [step_size_potential](./elements/step_size_potential.md)

**Unit:** mV

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20step_size_potential" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>electrolyte composition</strong> (Optional, Multivalued)</summary>

**Description:** Composition of electrolyte

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:electrolyte_composition`](https://w3id.org/nfdi4cat/catcore/electrolyte_composition)

**Schema Reference:** [electrolyte_composition](./elements/electrolyte_composition.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20electrolyte_composition" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>electrolyte concentration</strong> (Optional, Multivalued)</summary>

**Description:** Concentration of electrolyte

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:electrolyte_concentration`](https://w3id.org/nfdi4cat/catcore/electrolyte_concentration)

**Schema Reference:** [electrolyte_concentration](./elements/electrolyte_concentration.md)

**Unit:** mol/L

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20electrolyte_concentration" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>reference electrode</strong> (Optional, Multivalued)</summary>

**Description:** Reference electrode used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0007204`](https://w3id.org/nfdi4cat/voc4cat_0007204)

**Schema Reference:** [reference_electrode](./elements/reference_electrode.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20reference_electrode" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of cycles</strong> (Optional, Multivalued)</summary>

**Description:** Number of cycles in the process

**Range:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:number_of_cycles`](https://w3id.org/nfdi4cat/catcore/number_of_cycles)

**Schema Reference:** [number_of_cycles](./elements/number_of_cycles.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_cycles" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>working electrode</strong> (Optional, Multivalued)</summary>

**Description:** Working electrode used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0007202`](https://w3id.org/nfdi4cat/voc4cat_0007202)

**Schema Reference:** [working_electrode](./elements/working_electrode.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20working_electrode" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>counter electrode</strong> (Optional, Multivalued)</summary>

**Description:** Counter electrode used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0007203`](https://w3id.org/nfdi4cat/voc4cat_0007203)

**Schema Reference:** [counter_electrode](./elements/counter_electrode.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20counter_electrode" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Atmospheric conditions

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:atmosphere`](https://w3id.org/nfdi4cat/catcore/atmosphere)

**Schema Reference:** [atmosphere](./elements/atmosphere.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20atmosphere" target="_blank" class="md-button md-button--primary">
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
<summary><strong>DynamicLightScattering</strong></summary>

**Description:** Dynamic light scattering

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20DynamicLightScattering" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`CHMO:0000167`](http://purl.obolibrary.org/obo/CHMO_0000167)

**Schema Reference:** [DynamicLightScattering](./elements/DynamicLightScattering.md)

**Slots**

<details markdown="1">
<summary><strong>solvent</strong> (Optional, Multivalued)</summary>

**Description:** Solvent used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0007246`](https://w3id.org/nfdi4cat/voc4cat_0007246)

**Schema Reference:** [solvent](./elements/solvent.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20solvent" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>concentration</strong> (Optional, Multivalued)</summary>

**Description:** Concentration of sample

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0007244`](https://w3id.org/nfdi4cat/voc4cat_0007244)

**Schema Reference:** [concentration](./elements/concentration.md)

**Unit:** mol/L

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20concentration" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>light wavelength</strong> (Optional, Multivalued)</summary>

**Description:** Light wavelength used

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000176`](https://w3id.org/nfdi4cat/voc4cat_0000176)

**Schema Reference:** [light_wavelength](./elements/light_wavelength.md)

**Unit:** nm

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20light_wavelength" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>scattering angle</strong> (Optional, Multivalued)</summary>

**Description:** Scattering angle

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:scattering_angle`](https://w3id.org/nfdi4cat/catcore/scattering_angle)

**Schema Reference:** [scattering_angle](./elements/scattering_angle.md)

**Unit:** deg

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20scattering_angle" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>refractive index</strong> (Optional, Multivalued)</summary>

**Description:** Refractive index

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:refractive_index`](https://w3id.org/nfdi4cat/catcore/refractive_index)

**Schema Reference:** [refractive_index](./elements/refractive_index.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20refractive_index" target="_blank" class="md-button md-button--primary">
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
<summary><strong>dispersant</strong> (Optional, Multivalued)</summary>

**Description:** Dispersant used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:dispersant`](https://w3id.org/nfdi4cat/catcore/dispersant)

**Schema Reference:** [dispersant](./elements/dispersant.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20dispersant" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>measurement duration</strong> (Optional, Multivalued)</summary>

**Description:** Duration of measurement

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:measurement_duration`](https://w3id.org/nfdi4cat/catcore/measurement_duration)

**Schema Reference:** [measurement_duration](./elements/measurement_duration.md)

**Unit:** s

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20measurement_duration" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>ESI MS</strong></summary>

**Description:** Electrospray ionisation mass spectrometry

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ESI_MS" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`CHMO:0000482`](http://purl.obolibrary.org/obo/CHMO_0000482)

**Schema Reference:** [ESI_MS](./elements/ESI_MS.md)

**Slots**

<details markdown="1">
<summary><strong>operation mode</strong> (Optional, Multivalued)</summary>

**Description:** Operation mode of the instrument

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000108`](https://w3id.org/nfdi4cat/voc4cat_0000108)

**Schema Reference:** [operation_mode](./elements/operation_mode.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20operation_mode" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mz minimum</strong> (Optional, Multivalued)</summary>

**Description:** Minimum m/z value

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0002652`](http://purl.allotrope.org/ontologies/result#AFR_0002652)

**Schema Reference:** [mz_minimum](./elements/mz_minimum.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mz_minimum" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mz maximum</strong> (Optional, Multivalued)</summary>

**Description:** Maximum m/z value

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0002653`](http://purl.allotrope.org/ontologies/result#AFR_0002653)

**Schema Reference:** [mz_maximum](./elements/mz_maximum.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mz_maximum" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>spray voltage</strong> (Optional, Multivalued)</summary>

**Description:** Spray voltage for ionization

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`CHMO:0002792`](http://purl.obolibrary.org/obo/CHMO_0002792)

**Schema Reference:** [spray_voltage](./elements/spray_voltage.md)

**Unit:** kV

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20spray_voltage" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>capillary temperature</strong> (Optional, Multivalued)</summary>

**Description:** Capillary temperature

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:capillary_temperature`](https://w3id.org/nfdi4cat/catcore/capillary_temperature)

**Schema Reference:** [capillary_temperature](./elements/capillary_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20capillary_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>solvent composition</strong> (Optional, Multivalued)</summary>

**Description:** Solvent composition

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0007246`](https://w3id.org/nfdi4cat/voc4cat_0007246)

**Schema Reference:** [solvent_composition](./elements/solvent_composition.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20solvent_composition" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>flow rate</strong> (Optional, Multivalued)</summary>

**Description:** Flow rate

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:flow_rate`](https://w3id.org/nfdi4cat/catcore/flow_rate)

**Schema Reference:** [flow_rate](./elements/flow_rate.md)

**Unit:** mL/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20flow_rate" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>carrier gas</strong> (Optional, Multivalued)</summary>

**Description:** Carrier gas used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:carrier_gas`](https://w3id.org/nfdi4cat/catcore/carrier_gas)

**Schema Reference:** [carrier_gas](./elements/carrier_gas.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20carrier_gas" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>concentration</strong> (Optional, Multivalued)</summary>

**Description:** Concentration of sample

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0007244`](https://w3id.org/nfdi4cat/voc4cat_0007244)

**Schema Reference:** [concentration](./elements/concentration.md)

**Unit:** mol/L

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20concentration" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>PhotoluminescenceSpectroscopy</strong></summary>

**Description:** Photoluminescence spectroscopy

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20PhotoluminescenceSpectroscopy" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:PhotoluminescenceSpectroscopy`](https://w3id.org/nfdi4cat/catcore/PhotoluminescenceSpectroscopy)

**Schema Reference:** [PhotoluminescenceSpectroscopy](./elements/PhotoluminescenceSpectroscopy.md)

**Slots**

<details markdown="1">
<summary><strong>excitation wavelength</strong> (Optional, Multivalued)</summary>

**Description:** Excitation wavelength

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0002479`](http://purl.allotrope.org/ontologies/result#AFR_0002479)

**Schema Reference:** [excitation_wavelength](./elements/excitation_wavelength.md)

**Unit:** nm

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20excitation_wavelength" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>emission wavelength</strong> (Optional, Multivalued)</summary>

**Description:** Emission wavelength

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`NCIT:C204101`](http://purl.obolibrary.org/obo/NCIT_C204101)

**Schema Reference:** [emission_wavelength](./elements/emission_wavelength.md)

**Unit:** nm

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20emission_wavelength" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>optical filter</strong> (Optional, Multivalued)</summary>

**Description:** Optical filter used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:optical_filter`](https://w3id.org/nfdi4cat/catcore/optical_filter)

**Schema Reference:** [optical_filter](./elements/optical_filter.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20optical_filter" target="_blank" class="md-button md-button--primary">
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
<summary><strong>emission range</strong> (Optional, Multivalued)</summary>

**Description:** Emission range measured

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:emission_range`](https://w3id.org/nfdi4cat/catcore/emission_range)

**Schema Reference:** [emission_range](./elements/emission_range.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20emission_range" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>slit width</strong> (Optional, Multivalued)</summary>

**Description:** Slit width setting

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:slit_width`](https://w3id.org/nfdi4cat/catcore/slit_width)

**Schema Reference:** [slit_width](./elements/slit_width.md)

**Unit:** nm

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20slit_width" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>step size</strong> (Optional, Multivalued)</summary>

**Description:** Step size for measurements

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0000950`](http://purl.allotrope.org/ontologies/result#AFR_0000950)

**Schema Reference:** [step_size](./elements/step_size.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20step_size" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>integration time</strong> (Optional, Multivalued)</summary>

**Description:** Integration time

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0001671`](http://purl.allotrope.org/ontologies/result#AFR_0001671)

**Schema Reference:** [integration_time](./elements/integration_time.md)

**Unit:** s

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20integration_time" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>PhotoluminescenceLifetime</strong></summary>

**Description:** Photoluminescence lifetime measurement

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20PhotoluminescenceLifetime" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:PhotoluminescenceLifetime`](https://w3id.org/nfdi4cat/catcore/PhotoluminescenceLifetime)

**Schema Reference:** [PhotoluminescenceLifetime](./elements/PhotoluminescenceLifetime.md)

**Slots**

<details markdown="1">
<summary><strong>excitation wavelength</strong> (Optional, Multivalued)</summary>

**Description:** Excitation wavelength

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0002479`](http://purl.allotrope.org/ontologies/result#AFR_0002479)

**Schema Reference:** [excitation_wavelength](./elements/excitation_wavelength.md)

**Unit:** nm

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20excitation_wavelength" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>emission wavelength</strong> (Optional, Multivalued)</summary>

**Description:** Emission wavelength

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`NCIT:C204101`](http://purl.obolibrary.org/obo/NCIT_C204101)

**Schema Reference:** [emission_wavelength](./elements/emission_wavelength.md)

**Unit:** nm

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20emission_wavelength" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>optical filter</strong> (Optional, Multivalued)</summary>

**Description:** Optical filter used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:optical_filter`](https://w3id.org/nfdi4cat/catcore/optical_filter)

**Schema Reference:** [optical_filter](./elements/optical_filter.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20optical_filter" target="_blank" class="md-button md-button--primary">
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
<summary><strong>lifetime fitting model</strong> (Optional, Multivalued)</summary>

**Description:** Lifetime fitting model used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:lifetime_fitting_model`](https://w3id.org/nfdi4cat/catcore/lifetime_fitting_model)

**Schema Reference:** [lifetime_fitting_model](./elements/lifetime_fitting_model.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20lifetime_fitting_model" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>number of shots</strong> (Optional, Multivalued)</summary>

**Description:** Number of shots for measurement

**Range:** integer

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:number_of_shots`](https://w3id.org/nfdi4cat/catcore/number_of_shots)

**Schema Reference:** [number_of_shots](./elements/number_of_shots.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20number_of_shots" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>SizeExclusionChromatography</strong></summary>

**Description:** Size-exclusion chromatography

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20SizeExclusionChromatography" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`AFP:0000843`](http://purl.allotrope.org/ontologies/process#AFP_0000843)

**Schema Reference:** [SizeExclusionChromatography](./elements/SizeExclusionChromatography.md)

**Slots**

<details markdown="1">
<summary><strong>column type</strong> (Optional, Multivalued)</summary>

**Description:** Type of chromatography column

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0002026`](http://purl.allotrope.org/ontologies/result#AFR_0002026)

**Schema Reference:** [column_type](./elements/column_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20column_type" target="_blank" class="md-button md-button--primary">
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
<summary><strong>eluent</strong> (Optional, Multivalued)</summary>

**Description:** Eluent used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFRL:0000011`](http://purl.allotrope.org/ontologies/role#AFRL_0000011)

**Schema Reference:** [eluent](./elements/eluent.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20eluent" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>flow rate</strong> (Optional, Multivalued)</summary>

**Description:** Flow rate

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:flow_rate`](https://w3id.org/nfdi4cat/catcore/flow_rate)

**Schema Reference:** [flow_rate](./elements/flow_rate.md)

**Unit:** mL/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20flow_rate" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calibration standard</strong> (Optional, Multivalued)</summary>

**Description:** Calibration standard used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:calibration_standard`](https://w3id.org/nfdi4cat/catcore/calibration_standard)

**Schema Reference:** [calibration_standard](./elements/calibration_standard.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calibration_standard" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>injection volume</strong> (Optional, Multivalued)</summary>

**Description:** Injection volume

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0001577`](http://purl.allotrope.org/ontologies/result#AFR_0001577)

**Schema Reference:** [injection_volume](./elements/injection_volume.md)

**Unit:** uL

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20injection_volume" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>HPLC MS</strong></summary>

**Description:** High-performance liquid chromatography mass spectrometry

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20HPLC_MS" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`CHMO:0000796`](http://purl.obolibrary.org/obo/CHMO_0000796)

**Schema Reference:** [HPLC_MS](./elements/HPLC_MS.md)

**Slots**

<details markdown="1">
<summary><strong>column type</strong> (Optional, Multivalued)</summary>

**Description:** Type of chromatography column

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0002026`](http://purl.allotrope.org/ontologies/result#AFR_0002026)

**Schema Reference:** [column_type](./elements/column_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20column_type" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>eluent</strong> (Optional, Multivalued)</summary>

**Description:** Eluent used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFRL:0000011`](http://purl.allotrope.org/ontologies/role#AFRL_0000011)

**Schema Reference:** [eluent](./elements/eluent.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20eluent" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>gradient program</strong> (Optional, Multivalued)</summary>

**Description:** Gradient program for elution

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:gradient_program`](https://w3id.org/nfdi4cat/catcore/gradient_program)

**Schema Reference:** [gradient_program](./elements/gradient_program.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20gradient_program" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>ionization mode</strong> (Optional, Multivalued)</summary>

**Description:** Ionization mode used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:ionization_mode`](https://w3id.org/nfdi4cat/catcore/ionization_mode)

**Schema Reference:** [ionization_mode](./elements/ionization_mode.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ionization_mode" target="_blank" class="md-button md-button--primary">
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
<summary><strong>flow rate</strong> (Optional, Multivalued)</summary>

**Description:** Flow rate

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:flow_rate`](https://w3id.org/nfdi4cat/catcore/flow_rate)

**Schema Reference:** [flow_rate](./elements/flow_rate.md)

**Unit:** mL/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20flow_rate" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>injection volume</strong> (Optional, Multivalued)</summary>

**Description:** Injection volume

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0001577`](http://purl.allotrope.org/ontologies/result#AFR_0001577)

**Schema Reference:** [injection_volume](./elements/injection_volume.md)

**Unit:** uL

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20injection_volume" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>external standard</strong> (Optional, Multivalued)</summary>

**Description:** External standard used for calibration

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:external_standard`](https://w3id.org/nfdi4cat/catcore/external_standard)

**Schema Reference:** [external_standard](./elements/external_standard.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20external_standard" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>internal standard</strong> (Optional, Multivalued)</summary>

**Description:** Internal standard used for calibration

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:internal_standard`](https://w3id.org/nfdi4cat/catcore/internal_standard)

**Schema Reference:** [internal_standard](./elements/internal_standard.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20internal_standard" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>SingleCrystalXRD</strong></summary>

**Description:** Single crystal X-ray diffraction

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20SingleCrystalXRD" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`CHMO:0000852`](http://purl.obolibrary.org/obo/CHMO_0000852)

**Schema Reference:** [SingleCrystalXRD](./elements/SingleCrystalXRD.md)

**Slots**

<details markdown="1">
<summary><strong>xray source</strong> (Optional, Multivalued)</summary>

**Description:** X-ray source used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`OBI:0001138`](http://purl.obolibrary.org/obo/OBI_0001138)

**Schema Reference:** [xray_source](./elements/xray_source.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20xray_source" target="_blank" class="md-button md-button--primary">
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
<summary><strong>EDX</strong></summary>

**Description:** Energy-dispersive X-ray emission spectroscopy

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20EDX" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`CHMO:0000309`](http://purl.obolibrary.org/obo/CHMO_0000309)

**Schema Reference:** [EDX](./elements/EDX.md)

**Slots**

<details markdown="1">
<summary><strong>primary energy</strong> (Optional, Multivalued)</summary>

**Description:** Primary energy of electron beam

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:primary_energy`](https://w3id.org/nfdi4cat/catcore/primary_energy)

**Schema Reference:** [primary_energy](./elements/primary_energy.md)

**Unit:** keV

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20primary_energy" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>counting time</strong> (Optional, Multivalued)</summary>

**Description:** Counting time for detection

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:counting_time`](https://w3id.org/nfdi4cat/catcore/counting_time)

**Schema Reference:** [counting_time](./elements/counting_time.md)

**Unit:** s

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20counting_time" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>resolution</strong> (Optional, Multivalued)</summary>

**Description:** Spectral resolution

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:resolution`](https://w3id.org/nfdi4cat/catcore/resolution)

**Schema Reference:** [resolution](./elements/resolution.md)

**Unit:** cm-1

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20resolution" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calibration method</strong> (Optional, Multivalued)</summary>

**Description:** Calibration method used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:calibration_method`](https://w3id.org/nfdi4cat/catcore/calibration_method)

**Schema Reference:** [calibration_method](./elements/calibration_method.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calibration_method" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>TPO</strong></summary>

**Description:** Temperature-programmed oxidation

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20TPO" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`CHMO:0002907`](http://purl.obolibrary.org/obo/CHMO_0002907)

**Schema Reference:** [TPO](./elements/TPO.md)

**Slots**

<details markdown="1">
<summary><strong>oxidizing gas composition</strong> (Optional, Multivalued)</summary>

**Description:** Composition of oxidizing gas

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:oxidizing_gas_composition`](https://w3id.org/nfdi4cat/catcore/oxidizing_gas_composition)

**Schema Reference:** [oxidizing_gas_composition](./elements/oxidizing_gas_composition.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20oxidizing_gas_composition" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>heating rate</strong> (Optional, Multivalued)</summary>

**Description:** Heating rate

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:heating_rate`](https://w3id.org/nfdi4cat/catcore/heating_rate)

**Schema Reference:** [heating_rate](./elements/heating_rate.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20heating_rate" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>minimum temperature</strong> (Optional, Multivalued)</summary>

**Description:** Minimum temperature

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:minimum_temperature`](https://w3id.org/nfdi4cat/catcore/minimum_temperature)

**Schema Reference:** [minimum_temperature](./elements/minimum_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20minimum_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>maximum temperature</strong> (Optional, Multivalued)</summary>

**Description:** Maximum temperature

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:maximum_temperature`](https://w3id.org/nfdi4cat/catcore/maximum_temperature)

**Schema Reference:** [maximum_temperature](./elements/maximum_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20maximum_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>TPR</strong></summary>

**Description:** Temperature-programmed reduction

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20TPR" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`CHMO:0002908`](http://purl.obolibrary.org/obo/CHMO_0002908)

**Schema Reference:** [TPR](./elements/TPR.md)

**Slots**

<details markdown="1">
<summary><strong>reducing gas composition</strong> (Optional, Multivalued)</summary>

**Description:** Composition of reducing gas

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:reducing_gas_composition`](https://w3id.org/nfdi4cat/catcore/reducing_gas_composition)

**Schema Reference:** [reducing_gas_composition](./elements/reducing_gas_composition.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20reducing_gas_composition" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>heating rate</strong> (Optional, Multivalued)</summary>

**Description:** Heating rate

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:heating_rate`](https://w3id.org/nfdi4cat/catcore/heating_rate)

**Schema Reference:** [heating_rate](./elements/heating_rate.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20heating_rate" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>minimum temperature</strong> (Optional, Multivalued)</summary>

**Description:** Minimum temperature

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:minimum_temperature`](https://w3id.org/nfdi4cat/catcore/minimum_temperature)

**Schema Reference:** [minimum_temperature](./elements/minimum_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20minimum_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>maximum temperature</strong> (Optional, Multivalued)</summary>

**Description:** Maximum temperature

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:maximum_temperature`](https://w3id.org/nfdi4cat/catcore/maximum_temperature)

**Schema Reference:** [maximum_temperature](./elements/maximum_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20maximum_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>ConductivityMeasurement</strong></summary>

**Description:** Conductivity measurement

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ConductivityMeasurement" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:ConductivityMeasurement`](https://w3id.org/nfdi4cat/catcore/ConductivityMeasurement)

**Schema Reference:** [ConductivityMeasurement](./elements/ConductivityMeasurement.md)

**Slots**

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
<summary><strong>electrode configuration</strong> (Optional, Multivalued)</summary>

**Description:** Configuration of electrodes

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:electrode_configuration`](https://w3id.org/nfdi4cat/catcore/electrode_configuration)

**Schema Reference:** [electrode_configuration](./elements/electrode_configuration.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20electrode_configuration" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>frequency</strong> (Optional, Multivalued)</summary>

**Description:** Frequency of measurement

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0007239`](https://w3id.org/nfdi4cat/voc4cat_0007239)

**Schema Reference:** [frequency](./elements/frequency.md)

**Unit:** Hz

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20frequency" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>ac dc mode</strong> (Optional, Multivalued)</summary>

**Description:** AC or DC measurement mode

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:ac_dc_mode`](https://w3id.org/nfdi4cat/catcore/ac_dc_mode)

**Schema Reference:** [ac_dc_mode](./elements/ac_dc_mode.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ac_dc_mode" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>sample geometry</strong> (Optional, Multivalued)</summary>

**Description:** Geometry of the sample

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:sample_geometry`](https://w3id.org/nfdi4cat/catcore/sample_geometry)

**Schema Reference:** [sample_geometry](./elements/sample_geometry.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20sample_geometry" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20characterization_technique" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>sample state</strong> (Optional, Multivalued)</summary>

**Description:** State of the sample

**Range:** SampleStateEnum

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:sample_state`](https://w3id.org/nfdi4cat/catcore/sample_state)

**Schema Reference:** [sample_state](./elements/sample_state.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20sample_state" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>sample description</strong> (Optional, Multivalued)</summary>

**Description:** Description of the sample

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:sample_description`](https://w3id.org/nfdi4cat/catcore/sample_description)

**Schema Reference:** [sample_description](./elements/sample_description.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20sample_description" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>detector type</strong> (Optional, Multivalued)</summary>

**Description:** Type of detector used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFR:0000317`](http://purl.allotrope.org/ontologies/result#AFR_0000317)

**Schema Reference:** [detector_type](./elements/detector_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20detector_type" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>sample preparation</strong> (Optional, Multivalued)</summary>

**Description:** Preparation of sample

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`AFP:0001159`](http://purl.allotrope.org/ontologies/process#AFP_0001159)

**Schema Reference:** [sample_preparation](./elements/sample_preparation.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20sample_preparation" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>sample pretreatment</strong> (Optional, Multivalued)</summary>

**Description:** Pre-treatment of sample

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000122`](https://w3id.org/nfdi4cat/voc4cat_0000122)

**Schema Reference:** [sample_pretreatment](./elements/sample_pretreatment.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20sample_pretreatment" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<iframe
    src="assets/chart_characterization.html"
    width="100%"
    height= "800vh"
    style="border: 2px solid #5C88DA; background-color: #F0F8FF;
    "
    allowfullscreen
></iframe>