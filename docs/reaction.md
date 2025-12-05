# Reaction

The data class 'Reaction' describes the minimum information which should be reported 
with research data concerning the reaction for which the catalyst is applied.

## Slots

Fields for Metadata which should be described when using this Metadata Aspect.

- **Description:**A short description for Comprehension purposes

- **Range:** Further Aspects which are Important for describing a certain aspect

- **Cardinality:** A description how often it is allowed and how important it is to describe a certain aspect

- **Range:** Further Aspects which are Important for describing a certain aspect

- **CURIE:** The Abbreviated form of a URI, where the Prefix, e.g. voc4cat, described to which terminology a Concept belong. The Links are fully implemented here. For reusing these CURIE's you need to substitute the prefix against the URI for it.

- **Schema Reference:** A Link to the native LinkML Documentation on which this metadatacatalog and strucutre is based upon

<details markdown="1">
<summary><strong>catalyst quantity</strong> (Required, Multivalued)</summary>

**Description:** Quantity of catalyst used

**Range:** float

**Cardinality:**  Required, Multivalued

**CURIE:** [`catcore:catalyst_quantity`](https://w3id.org/nfdi4cat/catcore/catalyst_quantity)

**Schema Reference:** [catalyst_quantity](./elements/catalyst_quantity.md)

**Unit:** g

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20catalyst_quantity" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>reactor design type</strong> (Required, Multivalued)</summary>

**Description:** Type of reactor design

**Range:** ReactorDesignType

**Cardinality:**  Required, Multivalued

**CURIE:** [`voc4cat:0007018`](https://w3id.org/nfdi4cat/voc4cat_0007018)

**Schema Reference:** [reactor_design_type](./elements/reactor_design_type.md)

**Range Class Details:**

<details markdown="1">
<summary><strong>ReactorDesignType</strong></summary>

**Abstract Class**

**Description:** Type of reactor design used

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ReactorDesignType" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**Schema Reference:** [ReactorDesignType](./elements/ReactorDesignType.md)

</details>

**Possible Subclasses / Enumerations of ReactorDesignType:**

<details markdown="1">
<summary><strong>ElectrochemicalReactor</strong></summary>

**Description:** Electrochemical reactor

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ElectrochemicalReactor" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`voc4cat:0000193`](https://w3id.org/nfdi4cat/voc4cat_0000193)

**Schema Reference:** [ElectrochemicalReactor](./elements/ElectrochemicalReactor.md)

</details>

<details markdown="1">
<summary><strong>CSTR</strong></summary>

**Description:** Continuous stirred tank reactor

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20CSTR" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`voc4cat:0007019`](https://w3id.org/nfdi4cat/voc4cat_0007019)

**Schema Reference:** [CSTR](./elements/CSTR.md)

</details>

<details markdown="1">
<summary><strong>PlugFlowReactor</strong></summary>

**Description:** Plug flow reactor model

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20PlugFlowReactor" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`voc4cat:0007102`](https://w3id.org/nfdi4cat/voc4cat_0007102)

**Schema Reference:** [PlugFlowReactor](./elements/PlugFlowReactor.md)

</details>

<details markdown="1">
<summary><strong>Autoclave</strong></summary>

**Description:** Autoclave reactor

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Autoclave" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`NCIT:C93052`](http://purl.obolibrary.org/obo/NCIT_C93052)

**Schema Reference:** [Autoclave](./elements/Autoclave.md)

</details>

<details markdown="1">
<summary><strong>SlurryReactor</strong></summary>

**Description:** Slurry reactor

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20SlurryReactor" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:SlurryReactor`](https://w3id.org/nfdi4cat/catcore/SlurryReactor)

**Schema Reference:** [SlurryReactor](./elements/SlurryReactor.md)

</details>

<details markdown="1">
<summary><strong>Microreactor</strong></summary>

**Description:** Microreactor

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20Microreactor" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`voc4cat:0000234`](https://w3id.org/nfdi4cat/voc4cat_0000234)

**Schema Reference:** [Microreactor](./elements/Microreactor.md)

</details>

<details markdown="1">
<summary><strong>FixedBedReactor</strong></summary>

**Description:** Fixed bed reactor

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20FixedBedReactor" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:FixedBedReactor`](https://w3id.org/nfdi4cat/catcore/FixedBedReactor)

**Schema Reference:** [FixedBedReactor](./elements/FixedBedReactor.md)

</details>

<details markdown="1">
<summary><strong>FluidizedBedReactor</strong></summary>

**Description:** Fluidized bed reactor

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20FluidizedBedReactor" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**CURIE:** [`catcore:FluidizedBedReactor`](https://w3id.org/nfdi4cat/catcore/FluidizedBedReactor)

**Schema Reference:** [FluidizedBedReactor](./elements/FluidizedBedReactor.md)

**Slots**

<details markdown="1">
<summary><strong>gas distributor type</strong> (Optional, Multivalued)</summary>

**Description:** Type of gas distributor

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:gas_distributor_type`](https://w3id.org/nfdi4cat/catcore/gas_distributor_type)

**Schema Reference:** [gas_distributor_type](./elements/gas_distributor_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20gas_distributor_type" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>bed expansion height</strong> (Optional, Multivalued)</summary>

**Description:** Bed expansion height

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:bed_expansion_height`](https://w3id.org/nfdi4cat/catcore/bed_expansion_height)

**Schema Reference:** [bed_expansion_height](./elements/bed_expansion_height.md)

**Unit:** cm

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20bed_expansion_height" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>bubble size distribution</strong> (Optional)</summary>

**Description:** No description available

**Range:** string

**Cardinality:**  Optional

**Schema Reference:** [bubble_size_distribution](./elements/bubble_size_distribution.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20bubble_size_distribution" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

</details>

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20reactor_design_type" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>reactant</strong> (Required, Multivalued)</summary>

**Description:** Reactant used in the reaction

**Range:** string

**Cardinality:**  Required, Multivalued

**CURIE:** [`voc4cat:0000101`](https://w3id.org/nfdi4cat/voc4cat_0000101)

**Schema Reference:** [reactant](./elements/reactant.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20reactant" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>operation parameters</strong> (Required, Multivalued)</summary>

**Description:** Operation parameters for the reaction

**Range:** OperationParameters

**Cardinality:**  Required, Multivalued

**CURIE:** [`voc4cat:0000142`](https://w3id.org/nfdi4cat/voc4cat_0000142)

**Schema Reference:** [operation_parameters](./elements/operation_parameters.md)

**Range Class Details:**

<details markdown="1">
<summary><strong>OperationParameters</strong></summary>

**Description:** Operation parameters for the reaction

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20OperationParameters" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**Schema Reference:** [OperationParameters](./elements/OperationParameters.md)

**Slots**

<details markdown="1">
<summary><strong>reactor temperature range</strong> (Optional, Multivalued)</summary>

**Description:** Temperature range in reactor

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0007032`](https://w3id.org/nfdi4cat/voc4cat_0007032)

**Schema Reference:** [reactor_temperature_range](./elements/reactor_temperature_range.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20reactor_temperature_range" target="_blank" class="md-button md-button--primary">
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
<summary><strong>experiment pressure</strong> (Optional, Multivalued)</summary>

**Description:** Pressure during experiment

**Range:** float

**Cardinality:**  Optional, Multivalued

**CURIE:** [`voc4cat:0000118`](https://w3id.org/nfdi4cat/voc4cat_0000118)

**Schema Reference:** [experiment_pressure](./elements/experiment_pressure.md)

**Unit:** bar

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20experiment_pressure" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>feed composition range</strong> (Optional, Multivalued)</summary>

**Description:** Range of feed composition

**Range:** string

**Cardinality:**  Optional, Multivalued

**CURIE:** [`catcore:feed_composition_range`](https://w3id.org/nfdi4cat/catcore/feed_composition_range)

**Schema Reference:** [feed_composition_range](./elements/feed_composition_range.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20feed_composition_range" target="_blank" class="md-button md-button--primary">
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

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20operation_parameters" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>product identification method</strong> (Required, Multivalued)</summary>

**Description:** Method used for product identification

**Range:** ProductIdentificationMethod

**Cardinality:**  Required, Multivalued

**CURIE:** [`voc4cat:0000129`](https://w3id.org/nfdi4cat/voc4cat_0000129)

**Schema Reference:** [product_identification_method](./elements/product_identification_method.md)

**Range Class Details:**

<details markdown="1">
<summary><strong>ProductIdentificationMethod</strong></summary>

**Abstract Class**

**Description:** Method used for product identification

<p>
      <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20ProductIdentificationMethod" target="_blank" class="md-button md-button--primary">
        💡 Submit Documentation Feedback
      </a>
    </p>**Schema Reference:** [ProductIdentificationMethod](./elements/ProductIdentificationMethod.md)

</details>

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20product_identification_method" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<details markdown="1">
<summary><strong>catalyst type</strong> (Recommended, Multivalued)</summary>

**Description:** Type of catalyst

**Range:** string

**Cardinality:**  Recommended, Multivalued

**CURIE:** [`voc4cat:0007014`](https://w3id.org/nfdi4cat/voc4cat_0007014)

**Schema Reference:** [catalyst_type](./elements/catalyst_type.md)

<p>
  <a href=https://github.com/HendrikBorgelt/CatCore/issues/new?template=term_improvement.yaml&title=Term%20Feedback:%20catalyst_type" target="_blank" class="md-button md-button--primary">
    💡 Submit Documentation Feedback
  </a>
</p></details>

<iframe
    src="assets/chart_reaction.html"
    width="100%"
    height= "800vh"
    style="border: 2px solid #5C88DA; background-color: #F0F8FF;
    "
    allowfullscreen
></iframe>