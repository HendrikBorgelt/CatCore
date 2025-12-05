# Synthesis

The data class 'Synthesis' describes the minimum information which should be reported 
with research data concerning the field of catalyst synthesis.

## Slots

Fields for Metadata which should be described when using this Metadata Aspect.

- **Description:**A short description for Comprehension purposes

- **Range:** Further Aspects which are Important for describing a certain aspect

- **Cardinality:** A description how often it is allowed and how important it is to describe a certain aspect

- **Range:** Further Aspects which are Important for describing a certain aspect

- **CURIE:** The Abbreviated form of a URI, where the Prefix, e.g. voc4cat, described to which terminology a Concept belong. The Links are fully implemented here. For reusing these CURIE's you need to substitute the prefix against the URI for it.

- **Schema Reference:** A Link to the native LinkML Documentation on which this metadatacatalog and strucutre is based upon

<details markdown="1">
<summary><strong>nominal composition</strong> (Required)</summary>

**Description:** Nominal composition of the catalyst

**Range:** string

**Cardinality:**  Required

**CURIE:** [`catcore:nominal_composition`](https://w3id.org/nfdi4cat/catcore/nominal_composition)

**Schema Reference:** [nominal_composition](./elements/nominal_composition.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20nominal_composition" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>catalyst measured properties</strong> (Required)</summary>

**Description:** Measured properties of the catalyst (e.g., BET, sieve fraction, molar ratio)

**Range:** string

**Cardinality:**  Required

**CURIE:** [`catcore:catalyst_measured_properties`](https://w3id.org/nfdi4cat/catcore/catalyst_measured_properties)

**Schema Reference:** [catalyst_measured_properties](./elements/catalyst_measured_properties.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20catalyst_measured_properties" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>precursor</strong> (Required, Multivalued)</summary>

**Description:** Precursor material used in synthesis

**Range:** Precursor

**Cardinality:**  Required, Multivalued

**CURIE:** [`catcore:precursor`](https://w3id.org/nfdi4cat/catcore/precursor)

**Schema Reference:** [precursor](./elements/precursor.md)

**Range Class Details:**

<details markdown="1">
<summary><strong>Precursor</strong></summary>

**Description:** Precursor material used in catalyst synthesis

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Precursor" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**Schema Reference:** [Precursor](./elements/Precursor.md)

**Slots**

<details markdown="1">
<summary><strong>precursor quantity</strong> (Required, Multivalued)</summary>

**Description:** Quantity of precursor used

**Range:** float

**Cardinality:**  Required, Multivalued

**CURIE:** [`catcore:precursor_quantity`](https://w3id.org/nfdi4cat/catcore/precursor_quantity)

**Schema Reference:** [precursor_quantity](./elements/precursor_quantity.md)

**Unit:** g

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20precursor_quantity" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20precursor" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>preparation method</strong> (Required, Multivalued)</summary>

**Description:** Method used for catalyst preparation

**Range:** PreparationMethod

**Cardinality:**  Required, Multivalued

**CURIE:** [`voc4cat:0007016`](https://w3id.org/nfdi4cat/voc4cat_0007016)

**Schema Reference:** [preparation_method](./elements/preparation_method.md)

**Range Class Details:**

<details markdown="1">
<summary><strong>PreparationMethod</strong></summary>

**Abstract Class**

**Description:** Method used for catalyst preparation

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20PreparationMethod" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**Schema Reference:** [PreparationMethod](./elements/PreparationMethod.md)

</details>

**Possible Subclasses / Enumerations of PreparationMethod:**

<details markdown="1">
<summary><strong>Impregnation</strong></summary>

**Description:** Impregnation method for catalyst preparation

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Impregnation" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:Impregnation`](https://w3id.org/nfdi4cat/catcore/Impregnation)

**Schema Reference:** [Impregnation](./elements/Impregnation.md)

**Slots**

<details markdown="1">
<summary><strong>impregnation type</strong> (Optional, Multivalued)</summary>

**Description:** Type of impregnation method

**Range:** ImpregnationTypeEnum

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:impregnation_type`](https://w3id.org/nfdi4cat/catcore/impregnation_type)

**Schema Reference:** [impregnation_type](./elements/impregnation_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20impregnation_type" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>impregnation duration</strong> (Optional, Multivalued)</summary>

**Description:** Duration of impregnation process

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:impregnation_duration`](https://w3id.org/nfdi4cat/catcore/impregnation_duration)

**Schema Reference:** [impregnation_duration](./elements/impregnation_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20impregnation_duration" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>impregnation temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during impregnation

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:impregnation_temperature`](https://w3id.org/nfdi4cat/catcore/impregnation_temperature)

**Schema Reference:** [impregnation_temperature](./elements/impregnation_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20impregnation_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying device</strong> (Optional, Multivalued)</summary>

**Description:** Device used for drying

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_device`](https://w3id.org/nfdi4cat/catcore/drying_device)

**Schema Reference:** [drying_device](./elements/drying_device.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_device" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during drying

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_temperature`](https://w3id.org/nfdi4cat/catcore/drying_temperature)

**Schema Reference:** [drying_temperature](./elements/drying_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of drying process

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_time`](https://w3id.org/nfdi4cat/catcore/drying_time)

**Schema Reference:** [drying_time](./elements/drying_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_time" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Atmosphere during drying

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_atmosphere`](https://w3id.org/nfdi4cat/catcore/drying_atmosphere)

**Schema Reference:** [drying_atmosphere](./elements/drying_atmosphere.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_atmosphere" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination initial temperature</strong> (Optional, Multivalued)</summary>

**Description:** Initial temperature for calcination

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000057`](https://w3id.org/nfdi4cat/voc4cat_0000057)

**Schema Reference:** [calcination_initial_temperature](./elements/calcination_initial_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_initial_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination final temperature</strong> (Optional, Multivalued)</summary>

**Description:** Final temperature for calcination

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000058`](https://w3id.org/nfdi4cat/voc4cat_0000058)

**Schema Reference:** [calcination_final_temperature](./elements/calcination_final_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_final_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination dwelling time</strong> (Optional, Multivalued)</summary>

**Description:** Dwelling time at calcination temperature

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000060`](https://w3id.org/nfdi4cat/voc4cat_0000060)

**Schema Reference:** [calcination_dwelling_time](./elements/calcination_dwelling_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_dwelling_time" target="_blank" class="md-button md-button--primary">
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
<summary><strong>calcination gaseous environment</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment during calcination

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000055`](https://w3id.org/nfdi4cat/voc4cat_0000055)

**Schema Reference:** [calcination_gaseous_environment](./elements/calcination_gaseous_environment.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gaseous_environment" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination heating rate</strong> (Optional, Multivalued)</summary>

**Description:** Heating rate during calcination

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000059`](https://w3id.org/nfdi4cat/voc4cat_0000059)

**Schema Reference:** [calcination_heating_rate](./elements/calcination_heating_rate.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_heating_rate" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination gas flow rate</strong> (Optional, Multivalued)</summary>

**Description:** Gas flow rate during calcination

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000056`](https://w3id.org/nfdi4cat/voc4cat_0000056)

**Schema Reference:** [calcination_gas_flow_rate](./elements/calcination_gas_flow_rate.md)

**Unit:** mL/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gas_flow_rate" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>CoPrecipitation</strong></summary>

**Description:** Co-precipitation method for catalyst preparation

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20CoPrecipitation" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:CoPrecipitation`](https://w3id.org/nfdi4cat/catcore/CoPrecipitation)

**Schema Reference:** [CoPrecipitation](./elements/CoPrecipitation.md)

**Slots**

<details markdown="1">
<summary><strong>precipitating agent</strong> (Optional, Multivalued)</summary>

**Description:** Agent used for precipitation

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:precipitating_agent`](https://w3id.org/nfdi4cat/catcore/precipitating_agent)

**Schema Reference:** [precipitating_agent](./elements/precipitating_agent.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20precipitating_agent" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>precipitating concentration</strong> (Optional, Multivalued)</summary>

**Description:** Concentration of precipitating agent

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:precipitating_concentration`](https://w3id.org/nfdi4cat/catcore/precipitating_concentration)

**Schema Reference:** [precipitating_concentration](./elements/precipitating_concentration.md)

**Unit:** mol/L

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20precipitating_concentration" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis ph</strong> (Optional, Multivalued)</summary>

**Description:** pH during synthesis

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000052`](https://w3id.org/nfdi4cat/voc4cat_0000052)

**Schema Reference:** [synthesis_ph](./elements/synthesis_ph.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_ph" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mixing rate</strong> (Optional, Multivalued)</summary>

**Description:** Rate of mixing

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:mixing_rate`](https://w3id.org/nfdi4cat/catcore/mixing_rate)

**Schema Reference:** [mixing_rate](./elements/mixing_rate.md)

**Unit:** rpm

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mixing_rate" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mixing time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of mixing

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:mixing_time`](https://w3id.org/nfdi4cat/catcore/mixing_time)

**Schema Reference:** [mixing_time](./elements/mixing_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mixing_time" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mixing temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during mixing

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:mixing_temperature`](https://w3id.org/nfdi4cat/catcore/mixing_temperature)

**Schema Reference:** [mixing_temperature](./elements/mixing_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mixing_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying device</strong> (Optional, Multivalued)</summary>

**Description:** Device used for drying

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_device`](https://w3id.org/nfdi4cat/catcore/drying_device)

**Schema Reference:** [drying_device](./elements/drying_device.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_device" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during drying

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_temperature`](https://w3id.org/nfdi4cat/catcore/drying_temperature)

**Schema Reference:** [drying_temperature](./elements/drying_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of drying process

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_time`](https://w3id.org/nfdi4cat/catcore/drying_time)

**Schema Reference:** [drying_time](./elements/drying_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_time" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Atmosphere during drying

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_atmosphere`](https://w3id.org/nfdi4cat/catcore/drying_atmosphere)

**Schema Reference:** [drying_atmosphere](./elements/drying_atmosphere.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_atmosphere" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination initial temperature</strong> (Optional, Multivalued)</summary>

**Description:** Initial temperature for calcination

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000057`](https://w3id.org/nfdi4cat/voc4cat_0000057)

**Schema Reference:** [calcination_initial_temperature](./elements/calcination_initial_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_initial_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination final temperature</strong> (Optional, Multivalued)</summary>

**Description:** Final temperature for calcination

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000058`](https://w3id.org/nfdi4cat/voc4cat_0000058)

**Schema Reference:** [calcination_final_temperature](./elements/calcination_final_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_final_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination dwelling time</strong> (Optional, Multivalued)</summary>

**Description:** Dwelling time at calcination temperature

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000060`](https://w3id.org/nfdi4cat/voc4cat_0000060)

**Schema Reference:** [calcination_dwelling_time](./elements/calcination_dwelling_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_dwelling_time" target="_blank" class="md-button md-button--primary">
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
<summary><strong>calcination gaseous environment</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment during calcination

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000055`](https://w3id.org/nfdi4cat/voc4cat_0000055)

**Schema Reference:** [calcination_gaseous_environment](./elements/calcination_gaseous_environment.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gaseous_environment" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination heating rate</strong> (Optional, Multivalued)</summary>

**Description:** Heating rate during calcination

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000059`](https://w3id.org/nfdi4cat/voc4cat_0000059)

**Schema Reference:** [calcination_heating_rate](./elements/calcination_heating_rate.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_heating_rate" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination gas flow rate</strong> (Optional, Multivalued)</summary>

**Description:** Gas flow rate during calcination

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000056`](https://w3id.org/nfdi4cat/voc4cat_0000056)

**Schema Reference:** [calcination_gas_flow_rate](./elements/calcination_gas_flow_rate.md)

**Unit:** mL/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gas_flow_rate" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>order of addition</strong> (Optional, Multivalued)</summary>

**Description:** Order in which components are added

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:order_of_addition`](https://w3id.org/nfdi4cat/catcore/order_of_addition)

**Schema Reference:** [order_of_addition](./elements/order_of_addition.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20order_of_addition" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>filtration</strong> (Optional, Multivalued)</summary>

**Description:** Filtration method used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:filtration`](https://w3id.org/nfdi4cat/catcore/filtration)

**Schema Reference:** [filtration](./elements/filtration.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20filtration" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>purification</strong> (Optional, Multivalued)</summary>

**Description:** Purification method used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:purification`](https://w3id.org/nfdi4cat/catcore/purification)

**Schema Reference:** [purification](./elements/purification.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20purification" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>aging temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during aging

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:aging_temperature`](https://w3id.org/nfdi4cat/catcore/aging_temperature)

**Schema Reference:** [aging_temperature](./elements/aging_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20aging_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>aging time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of aging process

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:aging_time`](https://w3id.org/nfdi4cat/catcore/aging_time)

**Schema Reference:** [aging_time](./elements/aging_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20aging_time" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>SolGel</strong></summary>

**Description:** Sol-gel method for catalyst preparation

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20SolGel" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:SolGel`](https://w3id.org/nfdi4cat/catcore/SolGel)

**Schema Reference:** [SolGel](./elements/SolGel.md)

**Slots**

<details markdown="1">
<summary><strong>hydrolysis ratio</strong> (Optional, Multivalued)</summary>

**Description:** Ratio for hydrolysis

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:hydrolysis_ratio`](https://w3id.org/nfdi4cat/catcore/hydrolysis_ratio)

**Schema Reference:** [hydrolysis_ratio](./elements/hydrolysis_ratio.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20hydrolysis_ratio" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>aging time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of aging process

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:aging_time`](https://w3id.org/nfdi4cat/catcore/aging_time)

**Schema Reference:** [aging_time](./elements/aging_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20aging_time" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying</strong> (Optional, Multivalued)</summary>

**Description:** Drying process description

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying`](https://w3id.org/nfdi4cat/catcore/drying)

**Schema Reference:** [drying](./elements/drying.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>surfactant template</strong> (Optional, Multivalued)</summary>

**Description:** Surfactant template used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:surfactant_template`](https://w3id.org/nfdi4cat/catcore/surfactant_template)

**Schema Reference:** [surfactant_template](./elements/surfactant_template.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20surfactant_template" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>Solvothermal</strong></summary>

**Description:** Solvothermal method for catalyst preparation

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Solvothermal" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:Solvothermal`](https://w3id.org/nfdi4cat/catcore/Solvothermal)

**Schema Reference:** [Solvothermal](./elements/Solvothermal.md)

**Slots**

<details markdown="1">
<summary><strong>filling volume</strong> (Optional, Multivalued)</summary>

**Description:** Filling volume of vessel

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:filling_volume`](https://w3id.org/nfdi4cat/catcore/filling_volume)

**Schema Reference:** [filling_volume](./elements/filling_volume.md)

**Unit:** mL

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20filling_volume" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during synthesis

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000051`](https://w3id.org/nfdi4cat/voc4cat_0000051)

**Schema Reference:** [synthesis_temperature](./elements/synthesis_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis duration</strong> (Optional, Multivalued)</summary>

**Description:** Duration of synthesis

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000050`](https://w3id.org/nfdi4cat/voc4cat_0000050)

**Schema Reference:** [synthesis_duration](./elements/synthesis_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_duration" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>vessel type</strong> (Optional, Multivalued)</summary>

**Description:** Type of vessel used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:vessel_type`](https://w3id.org/nfdi4cat/catcore/vessel_type)

**Schema Reference:** [vessel_type](./elements/vessel_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20vessel_type" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>equipment</strong> (Optional, Multivalued)</summary>

**Description:** Equipment used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000187`](https://w3id.org/nfdi4cat/voc4cat_0000187)

**Schema Reference:** [equipment](./elements/equipment.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20equipment" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>stirring speed</strong> (Optional, Multivalued)</summary>

**Description:** Speed of stirring

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:stirring_speed`](https://w3id.org/nfdi4cat/catcore/stirring_speed)

**Schema Reference:** [stirring_speed](./elements/stirring_speed.md)

**Unit:** rpm

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20stirring_speed" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>stirrer type</strong> (Optional, Multivalued)</summary>

**Description:** Type of stirrer used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:stirrer_type`](https://w3id.org/nfdi4cat/catcore/stirrer_type)

**Schema Reference:** [stirrer_type](./elements/stirrer_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20stirrer_type" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>cooling rate</strong> (Optional, Multivalued)</summary>

**Description:** Rate of cooling

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:cooling_rate`](https://w3id.org/nfdi4cat/catcore/cooling_rate)

**Schema Reference:** [cooling_rate](./elements/cooling_rate.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20cooling_rate" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>PlasmaAssisted</strong></summary>

**Description:** Plasma-assisted method for catalyst preparation

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20PlasmaAssisted" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:PlasmaAssisted`](https://w3id.org/nfdi4cat/catcore/PlasmaAssisted)

**Schema Reference:** [PlasmaAssisted](./elements/PlasmaAssisted.md)

**Slots**

<details markdown="1">
<summary><strong>plasma type</strong> (Optional, Multivalued)</summary>

**Description:** Type of plasma used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:plasma_type`](https://w3id.org/nfdi4cat/catcore/plasma_type)

**Schema Reference:** [plasma_type](./elements/plasma_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20plasma_type" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>equipment</strong> (Optional, Multivalued)</summary>

**Description:** Equipment used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000187`](https://w3id.org/nfdi4cat/voc4cat_0000187)

**Schema Reference:** [equipment](./elements/equipment.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20equipment" target="_blank" class="md-button md-button--primary">
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
<summary><strong>power input</strong> (Optional, Multivalued)</summary>

**Description:** Power input for the process

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:power_input`](https://w3id.org/nfdi4cat/catcore/power_input)

**Schema Reference:** [power_input](./elements/power_input.md)

**Unit:** W

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20power_input" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>exposure time</strong> (Optional, Multivalued)</summary>

**Description:** Time of exposure

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:exposure_time`](https://w3id.org/nfdi4cat/catcore/exposure_time)

**Schema Reference:** [exposure_time](./elements/exposure_time.md)

**Unit:** min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20exposure_time" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis pressure</strong> (Optional, Multivalued)</summary>

**Description:** Pressure during synthesis

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000053`](https://w3id.org/nfdi4cat/voc4cat_0000053)

**Schema Reference:** [synthesis_pressure](./elements/synthesis_pressure.md)

**Unit:** bar

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_pressure" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during synthesis

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000051`](https://w3id.org/nfdi4cat/voc4cat_0000051)

**Schema Reference:** [synthesis_temperature](./elements/synthesis_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>CombustionSynthesis</strong></summary>

**Description:** Combustion synthesis method for catalyst preparation

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20CombustionSynthesis" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:CombustionSynthesis`](https://w3id.org/nfdi4cat/catcore/CombustionSynthesis)

**Schema Reference:** [CombustionSynthesis](./elements/CombustionSynthesis.md)

**Slots**

<details markdown="1">
<summary><strong>fuel</strong> (Optional, Multivalued)</summary>

**Description:** Fuel used in combustion

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:fuel`](https://w3id.org/nfdi4cat/catcore/fuel)

**Schema Reference:** [fuel](./elements/fuel.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20fuel" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>oxidizer</strong> (Optional, Multivalued)</summary>

**Description:** Oxidizer used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:oxidizer`](https://w3id.org/nfdi4cat/catcore/oxidizer)

**Schema Reference:** [oxidizer](./elements/oxidizer.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20oxidizer" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>fuel to oxidizer ratio</strong> (Optional, Multivalued)</summary>

**Description:** Ratio of fuel to oxidizer

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:fuel_to_oxidizer_ratio`](https://w3id.org/nfdi4cat/catcore/fuel_to_oxidizer_ratio)

**Schema Reference:** [fuel_to_oxidizer_ratio](./elements/fuel_to_oxidizer_ratio.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20fuel_to_oxidizer_ratio" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>set temperature</strong> (Optional, Multivalued)</summary>

**Description:** Set temperature for the process

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:set_temperature`](https://w3id.org/nfdi4cat/catcore/set_temperature)

**Schema Reference:** [set_temperature](./elements/set_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20set_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>post treatment</strong> (Optional, Multivalued)</summary>

**Description:** Post-treatment process

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:post_treatment`](https://w3id.org/nfdi4cat/catcore/post_treatment)

**Schema Reference:** [post_treatment](./elements/post_treatment.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20post_treatment" target="_blank" class="md-button md-button--primary">
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
<summary><strong>vessel type</strong> (Optional, Multivalued)</summary>

**Description:** Type of vessel used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:vessel_type`](https://w3id.org/nfdi4cat/catcore/vessel_type)

**Schema Reference:** [vessel_type](./elements/vessel_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20vessel_type" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>equipment</strong> (Optional, Multivalued)</summary>

**Description:** Equipment used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000187`](https://w3id.org/nfdi4cat/voc4cat_0000187)

**Schema Reference:** [equipment](./elements/equipment.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20equipment" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>AtomicLayerDeposition</strong></summary>

**Description:** Atomic layer deposition method for catalyst preparation

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20AtomicLayerDeposition" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:AtomicLayerDeposition`](https://w3id.org/nfdi4cat/catcore/AtomicLayerDeposition)

**Schema Reference:** [AtomicLayerDeposition](./elements/AtomicLayerDeposition.md)

**Slots**

<details markdown="1">
<summary><strong>substrate</strong> (Optional, Multivalued)</summary>

**Description:** Substrate material

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000024`](https://w3id.org/nfdi4cat/voc4cat_0000024)

**Schema Reference:** [substrate](./elements/substrate.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20substrate" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>pulse time</strong> (Optional, Multivalued)</summary>

**Description:** Pulse time for deposition

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:pulse_time`](https://w3id.org/nfdi4cat/catcore/pulse_time)

**Schema Reference:** [pulse_time](./elements/pulse_time.md)

**Unit:** s

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20pulse_time" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>purging duration</strong> (Optional, Multivalued)</summary>

**Description:** Duration of purging

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000112`](https://w3id.org/nfdi4cat/voc4cat_0000112)

**Schema Reference:** [purging_duration](./elements/purging_duration.md)

**Unit:** s

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20purging_duration" target="_blank" class="md-button md-button--primary">
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
<summary><strong>deposition temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during deposition

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:deposition_temperature`](https://w3id.org/nfdi4cat/catcore/deposition_temperature)

**Schema Reference:** [deposition_temperature](./elements/deposition_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20deposition_temperature" target="_blank" class="md-button md-button--primary">
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
<summary><strong>DepositionPrecipitation</strong></summary>

**Description:** Deposition-precipitation method for catalyst preparation

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20DepositionPrecipitation" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:DepositionPrecipitation`](https://w3id.org/nfdi4cat/catcore/DepositionPrecipitation)

**Schema Reference:** [DepositionPrecipitation](./elements/DepositionPrecipitation.md)

**Slots**

<details markdown="1">
<summary><strong>precipitating agent</strong> (Optional, Multivalued)</summary>

**Description:** Agent used for precipitation

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:precipitating_agent`](https://w3id.org/nfdi4cat/catcore/precipitating_agent)

**Schema Reference:** [precipitating_agent](./elements/precipitating_agent.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20precipitating_agent" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis ph</strong> (Optional, Multivalued)</summary>

**Description:** pH during synthesis

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000052`](https://w3id.org/nfdi4cat/voc4cat_0000052)

**Schema Reference:** [synthesis_ph](./elements/synthesis_ph.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_ph" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>deposition temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during deposition

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:deposition_temperature`](https://w3id.org/nfdi4cat/catcore/deposition_temperature)

**Schema Reference:** [deposition_temperature](./elements/deposition_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20deposition_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>deposition time</strong> (Optional, Multivalued)</summary>

**Description:** Time for deposition

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:deposition_time`](https://w3id.org/nfdi4cat/catcore/deposition_time)

**Schema Reference:** [deposition_time](./elements/deposition_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20deposition_time" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mixing rate</strong> (Optional, Multivalued)</summary>

**Description:** Rate of mixing

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:mixing_rate`](https://w3id.org/nfdi4cat/catcore/mixing_rate)

**Schema Reference:** [mixing_rate](./elements/mixing_rate.md)

**Unit:** rpm

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mixing_rate" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mixing time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of mixing

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:mixing_time`](https://w3id.org/nfdi4cat/catcore/mixing_time)

**Schema Reference:** [mixing_time](./elements/mixing_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mixing_time" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mixing temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during mixing

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:mixing_temperature`](https://w3id.org/nfdi4cat/catcore/mixing_temperature)

**Schema Reference:** [mixing_temperature](./elements/mixing_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mixing_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying device</strong> (Optional, Multivalued)</summary>

**Description:** Device used for drying

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_device`](https://w3id.org/nfdi4cat/catcore/drying_device)

**Schema Reference:** [drying_device](./elements/drying_device.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_device" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during drying

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_temperature`](https://w3id.org/nfdi4cat/catcore/drying_temperature)

**Schema Reference:** [drying_temperature](./elements/drying_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of drying process

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_time`](https://w3id.org/nfdi4cat/catcore/drying_time)

**Schema Reference:** [drying_time](./elements/drying_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_time" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Atmosphere during drying

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_atmosphere`](https://w3id.org/nfdi4cat/catcore/drying_atmosphere)

**Schema Reference:** [drying_atmosphere](./elements/drying_atmosphere.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_atmosphere" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination initial temperature</strong> (Optional, Multivalued)</summary>

**Description:** Initial temperature for calcination

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000057`](https://w3id.org/nfdi4cat/voc4cat_0000057)

**Schema Reference:** [calcination_initial_temperature](./elements/calcination_initial_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_initial_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination final temperature</strong> (Optional, Multivalued)</summary>

**Description:** Final temperature for calcination

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000058`](https://w3id.org/nfdi4cat/voc4cat_0000058)

**Schema Reference:** [calcination_final_temperature](./elements/calcination_final_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_final_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination dwelling time</strong> (Optional, Multivalued)</summary>

**Description:** Dwelling time at calcination temperature

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000060`](https://w3id.org/nfdi4cat/voc4cat_0000060)

**Schema Reference:** [calcination_dwelling_time](./elements/calcination_dwelling_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_dwelling_time" target="_blank" class="md-button md-button--primary">
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
<summary><strong>calcination gaseous environment</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment during calcination

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000055`](https://w3id.org/nfdi4cat/voc4cat_0000055)

**Schema Reference:** [calcination_gaseous_environment](./elements/calcination_gaseous_environment.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gaseous_environment" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination heating rate</strong> (Optional, Multivalued)</summary>

**Description:** Heating rate during calcination

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000059`](https://w3id.org/nfdi4cat/voc4cat_0000059)

**Schema Reference:** [calcination_heating_rate](./elements/calcination_heating_rate.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_heating_rate" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination gas flow rate</strong> (Optional, Multivalued)</summary>

**Description:** Gas flow rate during calcination

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000056`](https://w3id.org/nfdi4cat/voc4cat_0000056)

**Schema Reference:** [calcination_gas_flow_rate](./elements/calcination_gas_flow_rate.md)

**Unit:** mL/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gas_flow_rate" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>order of addition</strong> (Optional, Multivalued)</summary>

**Description:** Order in which components are added

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:order_of_addition`](https://w3id.org/nfdi4cat/catcore/order_of_addition)

**Schema Reference:** [order_of_addition](./elements/order_of_addition.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20order_of_addition" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>filtration</strong> (Optional, Multivalued)</summary>

**Description:** Filtration method used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:filtration`](https://w3id.org/nfdi4cat/catcore/filtration)

**Schema Reference:** [filtration](./elements/filtration.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20filtration" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>purification</strong> (Optional, Multivalued)</summary>

**Description:** Purification method used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:purification`](https://w3id.org/nfdi4cat/catcore/purification)

**Schema Reference:** [purification](./elements/purification.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20purification" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>aging temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during aging

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:aging_temperature`](https://w3id.org/nfdi4cat/catcore/aging_temperature)

**Schema Reference:** [aging_temperature](./elements/aging_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20aging_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>aging time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of aging process

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:aging_time`](https://w3id.org/nfdi4cat/catcore/aging_time)

**Schema Reference:** [aging_time](./elements/aging_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20aging_time" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>MicrowaveAssisted</strong></summary>

**Description:** Microwave-assisted method for catalyst preparation

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20MicrowaveAssisted" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:MicrowaveAssisted`](https://w3id.org/nfdi4cat/catcore/MicrowaveAssisted)

**Schema Reference:** [MicrowaveAssisted](./elements/MicrowaveAssisted.md)

**Slots**

<details markdown="1">
<summary><strong>equipment</strong> (Optional, Multivalued)</summary>

**Description:** Equipment used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000187`](https://w3id.org/nfdi4cat/voc4cat_0000187)

**Schema Reference:** [equipment](./elements/equipment.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20equipment" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>power</strong> (Optional, Multivalued)</summary>

**Description:** Power setting

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:power`](https://w3id.org/nfdi4cat/catcore/power)

**Schema Reference:** [power](./elements/power.md)

**Unit:** W

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20power" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis duration</strong> (Optional, Multivalued)</summary>

**Description:** Duration of synthesis

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000050`](https://w3id.org/nfdi4cat/voc4cat_0000050)

**Schema Reference:** [synthesis_duration](./elements/synthesis_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_duration" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during synthesis

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000051`](https://w3id.org/nfdi4cat/voc4cat_0000051)

**Schema Reference:** [synthesis_temperature](./elements/synthesis_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>microwave frequency</strong> (Optional, Multivalued)</summary>

**Description:** Frequency of microwave

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:microwave_frequency`](https://w3id.org/nfdi4cat/catcore/microwave_frequency)

**Schema Reference:** [microwave_frequency](./elements/microwave_frequency.md)

**Unit:** GHz

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20microwave_frequency" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>vessel type</strong> (Optional, Multivalued)</summary>

**Description:** Type of vessel used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:vessel_type`](https://w3id.org/nfdi4cat/catcore/vessel_type)

**Schema Reference:** [vessel_type](./elements/vessel_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20vessel_type" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>SonochemicalSynthesis</strong></summary>

**Description:** Sonochemical synthesis method for catalyst preparation

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20SonochemicalSynthesis" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:SonochemicalSynthesis`](https://w3id.org/nfdi4cat/catcore/SonochemicalSynthesis)

**Schema Reference:** [SonochemicalSynthesis](./elements/SonochemicalSynthesis.md)

**Slots**

<details markdown="1">
<summary><strong>stirring duration</strong> (Optional, Multivalued)</summary>

**Description:** Duration of stirring

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:stirring_duration`](https://w3id.org/nfdi4cat/catcore/stirring_duration)

**Schema Reference:** [stirring_duration](./elements/stirring_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20stirring_duration" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>sonication power</strong> (Optional, Multivalued)</summary>

**Description:** Power of sonication

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:sonication_power`](https://w3id.org/nfdi4cat/catcore/sonication_power)

**Schema Reference:** [sonication_power](./elements/sonication_power.md)

**Unit:** W

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20sonication_power" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>sonication duration</strong> (Optional, Multivalued)</summary>

**Description:** Duration of sonication

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:sonication_duration`](https://w3id.org/nfdi4cat/catcore/sonication_duration)

**Schema Reference:** [sonication_duration](./elements/sonication_duration.md)

**Unit:** min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20sonication_duration" target="_blank" class="md-button md-button--primary">
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
<summary><strong>drying device</strong> (Optional, Multivalued)</summary>

**Description:** Device used for drying

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_device`](https://w3id.org/nfdi4cat/catcore/drying_device)

**Schema Reference:** [drying_device](./elements/drying_device.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_device" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during drying

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_temperature`](https://w3id.org/nfdi4cat/catcore/drying_temperature)

**Schema Reference:** [drying_temperature](./elements/drying_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of drying process

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_time`](https://w3id.org/nfdi4cat/catcore/drying_time)

**Schema Reference:** [drying_time](./elements/drying_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_time" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying atmosphere</strong> (Optional, Multivalued)</summary>

**Description:** Atmosphere during drying

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_atmosphere`](https://w3id.org/nfdi4cat/catcore/drying_atmosphere)

**Schema Reference:** [drying_atmosphere](./elements/drying_atmosphere.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_atmosphere" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination initial temperature</strong> (Optional, Multivalued)</summary>

**Description:** Initial temperature for calcination

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000057`](https://w3id.org/nfdi4cat/voc4cat_0000057)

**Schema Reference:** [calcination_initial_temperature](./elements/calcination_initial_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_initial_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination final temperature</strong> (Optional, Multivalued)</summary>

**Description:** Final temperature for calcination

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000058`](https://w3id.org/nfdi4cat/voc4cat_0000058)

**Schema Reference:** [calcination_final_temperature](./elements/calcination_final_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_final_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination dwelling time</strong> (Optional, Multivalued)</summary>

**Description:** Dwelling time at calcination temperature

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000060`](https://w3id.org/nfdi4cat/voc4cat_0000060)

**Schema Reference:** [calcination_dwelling_time](./elements/calcination_dwelling_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_dwelling_time" target="_blank" class="md-button md-button--primary">
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
<summary><strong>calcination gaseous environment</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment during calcination

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000055`](https://w3id.org/nfdi4cat/voc4cat_0000055)

**Schema Reference:** [calcination_gaseous_environment](./elements/calcination_gaseous_environment.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gaseous_environment" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination heating rate</strong> (Optional, Multivalued)</summary>

**Description:** Heating rate during calcination

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000059`](https://w3id.org/nfdi4cat/voc4cat_0000059)

**Schema Reference:** [calcination_heating_rate](./elements/calcination_heating_rate.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_heating_rate" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination gas flow rate</strong> (Optional, Multivalued)</summary>

**Description:** Gas flow rate during calcination

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000056`](https://w3id.org/nfdi4cat/voc4cat_0000056)

**Schema Reference:** [calcination_gas_flow_rate](./elements/calcination_gas_flow_rate.md)

**Unit:** mL/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gas_flow_rate" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>FlameSprayPyrolysis</strong></summary>

**Description:** Flame spray pyrolysis method for catalyst preparation

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20FlameSprayPyrolysis" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`voc4cat:0007031`](https://w3id.org/nfdi4cat/voc4cat_0007031)

**Schema Reference:** [FlameSprayPyrolysis](./elements/FlameSprayPyrolysis.md)

**Slots**

<details markdown="1">
<summary><strong>flame type</strong> (Optional, Multivalued)</summary>

**Description:** Type of flame used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:flame_type`](https://w3id.org/nfdi4cat/catcore/flame_type)

**Schema Reference:** [flame_type](./elements/flame_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20flame_type" target="_blank" class="md-button md-button--primary">
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
<summary><strong>inlet system</strong> (Optional, Multivalued)</summary>

**Description:** Inlet system configuration

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:inlet_system`](https://w3id.org/nfdi4cat/catcore/inlet_system)

**Schema Reference:** [inlet_system](./elements/inlet_system.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20inlet_system" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>flame ring</strong> (Optional, Multivalued)</summary>

**Description:** Flame ring configuration

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:flame_ring`](https://w3id.org/nfdi4cat/catcore/flame_ring)

**Schema Reference:** [flame_ring](./elements/flame_ring.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20flame_ring" target="_blank" class="md-button md-button--primary">
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
<summary><strong>capillary pressure</strong> (Optional, Multivalued)</summary>

**Description:** Capillary pressure

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:capillary_pressure`](https://w3id.org/nfdi4cat/catcore/capillary_pressure)

**Schema Reference:** [capillary_pressure](./elements/capillary_pressure.md)

**Unit:** bar

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20capillary_pressure" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>fuel dispersant ratio</strong> (Optional, Multivalued)</summary>

**Description:** Ratio of fuel to dispersant

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:fuel_dispersant_ratio`](https://w3id.org/nfdi4cat/catcore/fuel_dispersant_ratio)

**Schema Reference:** [fuel_dispersant_ratio](./elements/fuel_dispersant_ratio.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20fuel_dispersant_ratio" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>filtration device</strong> (Optional, Multivalued)</summary>

**Description:** Device used for filtration

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:filtration_device`](https://w3id.org/nfdi4cat/catcore/filtration_device)

**Schema Reference:** [filtration_device](./elements/filtration_device.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20filtration_device" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>filter type</strong> (Optional, Multivalued)</summary>

**Description:** Type of filter used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:filter_type`](https://w3id.org/nfdi4cat/catcore/filter_type)

**Schema Reference:** [filter_type](./elements/filter_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20filter_type" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>MechanochemicalSynthesis</strong></summary>

**Description:** Mechanochemical synthesis method for catalyst preparation

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20MechanochemicalSynthesis" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:MechanochemicalSynthesis`](https://w3id.org/nfdi4cat/catcore/MechanochemicalSynthesis)

**Schema Reference:** [MechanochemicalSynthesis](./elements/MechanochemicalSynthesis.md)

**Slots**

<details markdown="1">
<summary><strong>equipment</strong> (Optional, Multivalued)</summary>

**Description:** Equipment used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000187`](https://w3id.org/nfdi4cat/voc4cat_0000187)

**Schema Reference:** [equipment](./elements/equipment.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20equipment" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>vessel volume</strong> (Optional, Multivalued)</summary>

**Description:** Volume of vessel

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:vessel_volume`](https://w3id.org/nfdi4cat/catcore/vessel_volume)

**Schema Reference:** [vessel_volume](./elements/vessel_volume.md)

**Unit:** mL

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20vessel_volume" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>size and material</strong> (Optional, Multivalued)</summary>

**Description:** Size and material of components

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:size_and_material`](https://w3id.org/nfdi4cat/catcore/size_and_material)

**Schema Reference:** [size_and_material](./elements/size_and_material.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20size_and_material" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>milling speed</strong> (Optional, Multivalued)</summary>

**Description:** Speed of milling

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:milling_speed`](https://w3id.org/nfdi4cat/catcore/milling_speed)

**Schema Reference:** [milling_speed](./elements/milling_speed.md)

**Unit:** rpm

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20milling_speed" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>milling duration</strong> (Optional, Multivalued)</summary>

**Description:** Duration of milling

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:milling_duration`](https://w3id.org/nfdi4cat/catcore/milling_duration)

**Schema Reference:** [milling_duration](./elements/milling_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20milling_duration" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during synthesis

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000051`](https://w3id.org/nfdi4cat/voc4cat_0000051)

**Schema Reference:** [synthesis_temperature](./elements/synthesis_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_temperature" target="_blank" class="md-button md-button--primary">
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
<summary><strong>ball material</strong> (Optional, Multivalued)</summary>

**Description:** Material of milling balls

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:ball_material`](https://w3id.org/nfdi4cat/catcore/ball_material)

**Schema Reference:** [ball_material](./elements/ball_material.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ball_material" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>ball size</strong> (Optional, Multivalued)</summary>

**Description:** Size of milling balls

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:ball_size`](https://w3id.org/nfdi4cat/catcore/ball_size)

**Schema Reference:** [ball_size](./elements/ball_size.md)

**Unit:** mm

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ball_size" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>ball to powder ratio</strong> (Optional, Multivalued)</summary>

**Description:** Ratio of ball to powder

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:ball_to_powder_ratio`](https://w3id.org/nfdi4cat/catcore/ball_to_powder_ratio)

**Schema Reference:** [ball_to_powder_ratio](./elements/ball_to_powder_ratio.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ball_to_powder_ratio" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>Sublimation</strong></summary>

**Description:** Sublimation method for catalyst preparation

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Sublimation" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:Sublimation`](https://w3id.org/nfdi4cat/catcore/Sublimation)

**Schema Reference:** [Sublimation](./elements/Sublimation.md)

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
<summary><strong>synthesis pressure</strong> (Optional, Multivalued)</summary>

**Description:** Pressure during synthesis

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000053`](https://w3id.org/nfdi4cat/voc4cat_0000053)

**Schema Reference:** [synthesis_pressure](./elements/synthesis_pressure.md)

**Unit:** bar

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_pressure" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>synthesis duration</strong> (Optional, Multivalued)</summary>

**Description:** Duration of synthesis

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000050`](https://w3id.org/nfdi4cat/voc4cat_0000050)

**Schema Reference:** [synthesis_duration](./elements/synthesis_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_duration" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>MolecularSynthesis</strong></summary>

**Description:** Molecular synthesis method for catalyst preparation

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20MolecularSynthesis" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:MolecularSynthesis`](https://w3id.org/nfdi4cat/catcore/MolecularSynthesis)

**Schema Reference:** [MolecularSynthesis](./elements/MolecularSynthesis.md)

**Slots**

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
<summary><strong>synthesis duration</strong> (Optional, Multivalued)</summary>

**Description:** Duration of synthesis

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000050`](https://w3id.org/nfdi4cat/voc4cat_0000050)

**Schema Reference:** [synthesis_duration](./elements/synthesis_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20synthesis_duration" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>reaction vessel</strong> (Optional, Multivalued)</summary>

**Description:** Vessel used for reaction

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:reaction_vessel`](https://w3id.org/nfdi4cat/catcore/reaction_vessel)

**Schema Reference:** [reaction_vessel](./elements/reaction_vessel.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20reaction_vessel" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mixing device</strong> (Optional, Multivalued)</summary>

**Description:** Device used for mixing

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:mixing_device`](https://w3id.org/nfdi4cat/catcore/mixing_device)

**Schema Reference:** [mixing_device](./elements/mixing_device.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mixing_device" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>stirring duration</strong> (Optional, Multivalued)</summary>

**Description:** Duration of stirring

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:stirring_duration`](https://w3id.org/nfdi4cat/catcore/stirring_duration)

**Schema Reference:** [stirring_duration](./elements/stirring_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20stirring_duration" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>stirring speed</strong> (Optional, Multivalued)</summary>

**Description:** Speed of stirring

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:stirring_speed`](https://w3id.org/nfdi4cat/catcore/stirring_speed)

**Schema Reference:** [stirring_speed](./elements/stirring_speed.md)

**Unit:** rpm

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20stirring_speed" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>mixing temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during mixing

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:mixing_temperature`](https://w3id.org/nfdi4cat/catcore/mixing_temperature)

**Schema Reference:** [mixing_temperature](./elements/mixing_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20mixing_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>filtration device</strong> (Optional, Multivalued)</summary>

**Description:** Device used for filtration

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:filtration_device`](https://w3id.org/nfdi4cat/catcore/filtration_device)

**Schema Reference:** [filtration_device](./elements/filtration_device.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20filtration_device" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>filter type</strong> (Optional, Multivalued)</summary>

**Description:** Type of filter used

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:filter_type`](https://w3id.org/nfdi4cat/catcore/filter_type)

**Schema Reference:** [filter_type](./elements/filter_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20filter_type" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>crystallisation solvents</strong> (Optional, Multivalued)</summary>

**Description:** Solvents used for crystallisation

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:crystallisation_solvents`](https://w3id.org/nfdi4cat/catcore/crystallisation_solvents)

**Schema Reference:** [crystallisation_solvents](./elements/crystallisation_solvents.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20crystallisation_solvents" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>precipitation agent</strong> (Optional, Multivalued)</summary>

**Description:** Agent used for precipitation

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:precipitation_agent`](https://w3id.org/nfdi4cat/catcore/precipitation_agent)

**Schema Reference:** [precipitation_agent](./elements/precipitation_agent.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20precipitation_agent" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>crystallisation duration</strong> (Optional, Multivalued)</summary>

**Description:** Duration of crystallisation

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:crystallisation_duration`](https://w3id.org/nfdi4cat/catcore/crystallisation_duration)

**Schema Reference:** [crystallisation_duration](./elements/crystallisation_duration.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20crystallisation_duration" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>purification solvent</strong> (Optional, Multivalued)</summary>

**Description:** Solvent used for purification

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:purification_solvent`](https://w3id.org/nfdi4cat/catcore/purification_solvent)

**Schema Reference:** [purification_solvent](./elements/purification_solvent.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20purification_solvent" target="_blank" class="md-button md-button--primary">
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
<summary><strong>drying device</strong> (Optional, Multivalued)</summary>

**Description:** Device used for drying

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_device`](https://w3id.org/nfdi4cat/catcore/drying_device)

**Schema Reference:** [drying_device](./elements/drying_device.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_device" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying temperature</strong> (Optional, Multivalued)</summary>

**Description:** Temperature during drying

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_temperature`](https://w3id.org/nfdi4cat/catcore/drying_temperature)

**Schema Reference:** [drying_temperature](./elements/drying_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>temperature ramp</strong> (Optional, Multivalued)</summary>

**Description:** Temperature ramp rate

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:temperature_ramp`](https://w3id.org/nfdi4cat/catcore/temperature_ramp)

**Schema Reference:** [temperature_ramp](./elements/temperature_ramp.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20temperature_ramp" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>drying time</strong> (Optional, Multivalued)</summary>

**Description:** Duration of drying process

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:drying_time`](https://w3id.org/nfdi4cat/catcore/drying_time)

**Schema Reference:** [drying_time](./elements/drying_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20drying_time" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<details markdown="1">
<summary><strong>ExsolutionSynthesis</strong></summary>

**Description:** Exsolution synthesis method for catalyst preparation

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ExsolutionSynthesis" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:ExsolutionSynthesis`](https://w3id.org/nfdi4cat/catcore/ExsolutionSynthesis)

**Schema Reference:** [ExsolutionSynthesis](./elements/ExsolutionSynthesis.md)

**Slots**

<details markdown="1">
<summary><strong>calcination initial temperature</strong> (Optional, Multivalued)</summary>

**Description:** Initial temperature for calcination

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000057`](https://w3id.org/nfdi4cat/voc4cat_0000057)

**Schema Reference:** [calcination_initial_temperature](./elements/calcination_initial_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_initial_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination final temperature</strong> (Optional, Multivalued)</summary>

**Description:** Final temperature for calcination

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000058`](https://w3id.org/nfdi4cat/voc4cat_0000058)

**Schema Reference:** [calcination_final_temperature](./elements/calcination_final_temperature.md)

**Unit:** Cel

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_final_temperature" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination dwelling time</strong> (Optional, Multivalued)</summary>

**Description:** Dwelling time at calcination temperature

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000060`](https://w3id.org/nfdi4cat/voc4cat_0000060)

**Schema Reference:** [calcination_dwelling_time](./elements/calcination_dwelling_time.md)

**Unit:** h

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_dwelling_time" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination gaseous environment</strong> (Optional, Multivalued)</summary>

**Description:** Gaseous environment during calcination

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000055`](https://w3id.org/nfdi4cat/voc4cat_0000055)

**Schema Reference:** [calcination_gaseous_environment](./elements/calcination_gaseous_environment.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gaseous_environment" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination heating rate</strong> (Optional, Multivalued)</summary>

**Description:** Heating rate during calcination

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000059`](https://w3id.org/nfdi4cat/voc4cat_0000059)

**Schema Reference:** [calcination_heating_rate](./elements/calcination_heating_rate.md)

**Unit:** Cel/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_heating_rate" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>calcination gas flow rate</strong> (Optional, Multivalued)</summary>

**Description:** Gas flow rate during calcination

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000056`](https://w3id.org/nfdi4cat/voc4cat_0000056)

**Schema Reference:** [calcination_gas_flow_rate](./elements/calcination_gas_flow_rate.md)

**Unit:** mL/min

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20calcination_gas_flow_rate" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20preparation_method" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>storage conditions</strong> (Recommended, Multivalued)</summary>

**Description:** Conditions for storage

**Range:** string

**Cardinality:**  Recommended, Multivalued

**CURIE:** [`catcore:storage_conditions`](https://w3id.org/nfdi4cat/catcore/storage_conditions)

**Schema Reference:** [storage_conditions](./elements/storage_conditions.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20storage_conditions" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>support</strong> (Optional, Multivalued)</summary>

**Description:** Support material

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:support`](https://w3id.org/nfdi4cat/catcore/support)

**Schema Reference:** [support](./elements/support.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20support" target="_blank" class="md-button md-button--primary">
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
    src="assets/chart_synthesis.html"
    width="100%"
    height= "800vh"
    style="border: 2px solid #5C88DA; background-color: #F0F8FF;
    "
    allowfullscreen
></iframe>