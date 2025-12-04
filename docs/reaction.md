# Reaction

The data class 'Reaction' describes the minimum information which should be reported 
with research data concerning the reaction for which the catalyst is applied.

**Schema Reference:** [Reaction](https://w3id.org/nfdi4cat/catcore/elements/Reaction)

## Slots

<details markdown="1">
<summary><strong>catalyst quantity (Required, Multivalued)</strong></summary>

**Description:** Quantity of catalyst used

**Range:** float

**URI:** [`catcore:catalyst_quantity`](catcore:catalyst_quantity)

**Schema Reference:** [catalyst_quantity](elements/catalyst_quantity.md)

**Unit:** g

</details>

<details markdown="1">
<summary><strong>reactor design type (Required, Multivalued)</strong></summary>

**Description:** Type of reactor design

**Range:** ReactorDesignType

**URI:** [`voc4cat:0007018`](voc4cat:0007018)

**Schema Reference:** [reactor_design_type](elements/reactor_design_type.md)

**Range Class Details:**

<details markdown="1">
<summary><strong>ReactorDesignType</strong></summary>

**Abstract Class**

**Description:** Type of reactor design used

**Schema Reference:** [ReactorDesignType](elements/ReactorDesignType.md)

</details>

**Subclasses of ReactorDesignType:**

<details markdown="1">
<summary><strong>ElectrochemicalReactor</strong></summary>

**Description:** Electrochemical reactor

**URI:** [`voc4cat:0000193`](voc4cat:0000193)

**Schema Reference:** [ElectrochemicalReactor](elements/ElectrochemicalReactor.md)

</details>

<details markdown="1">
<summary><strong>CSTR</strong></summary>

**Description:** Continuous stirred tank reactor

**URI:** [`voc4cat:0007019`](voc4cat:0007019)

**Schema Reference:** [CSTR](elements/CSTR.md)

</details>

<details markdown="1">
<summary><strong>PlugFlowReactor</strong></summary>

**Description:** Plug flow reactor model

**URI:** [`voc4cat:0007102`](voc4cat:0007102)

**Schema Reference:** [PlugFlowReactor](elements/PlugFlowReactor.md)

</details>

<details markdown="1">
<summary><strong>Autoclave</strong></summary>

**Description:** Autoclave reactor

**URI:** [`NCIT:C93052`](NCIT:C93052)

**Schema Reference:** [Autoclave](elements/Autoclave.md)

</details>

<details markdown="1">
<summary><strong>SlurryReactor</strong></summary>

**Description:** Slurry reactor

**URI:** [`catcore:SlurryReactor`](catcore:SlurryReactor)

**Schema Reference:** [SlurryReactor](elements/SlurryReactor.md)

</details>

<details markdown="1">
<summary><strong>Microreactor</strong></summary>

**Description:** Microreactor

**URI:** [`voc4cat:0000234`](voc4cat:0000234)

**Schema Reference:** [Microreactor](elements/Microreactor.md)

</details>

<details markdown="1">
<summary><strong>FixedBedReactor</strong></summary>

**Description:** Fixed bed reactor

**URI:** [`catcore:FixedBedReactor`](catcore:FixedBedReactor)

**Schema Reference:** [FixedBedReactor](elements/FixedBedReactor.md)

</details>

<details markdown="1">
<summary><strong>FluidizedBedReactor</strong></summary>

**Description:** Fluidized bed reactor

**URI:** [`catcore:FluidizedBedReactor`](catcore:FluidizedBedReactor)

**Schema Reference:** [FluidizedBedReactor](elements/FluidizedBedReactor.md)

**Slots**

<details markdown="1">
<summary><strong>gas distributor type (Optional, Multivalued)</strong></summary>

**Description:** Type of gas distributor

**Range:** string

**URI:** [`catcore:gas_distributor_type`](catcore:gas_distributor_type)

**Schema Reference:** [gas_distributor_type](elements/gas_distributor_type.md)

</details>

<details markdown="1">
<summary><strong>bed expansion height (Optional, Multivalued)</strong></summary>

**Description:** Bed expansion height

**Range:** float

**URI:** [`catcore:bed_expansion_height`](catcore:bed_expansion_height)

**Schema Reference:** [bed_expansion_height](elements/bed_expansion_height.md)

**Unit:** cm

</details>

<details markdown="1">
<summary><strong>bubble size distribution (Optional)</strong></summary>

**Description:** No description available

**Range:** string

**Schema Reference:** [bubble_size_distribution](elements/bubble_size_distribution.md)

</details>

</details>

</details>

<details markdown="1">
<summary><strong>reactant (Required, Multivalued)</strong></summary>

**Description:** Reactant used in the reaction

**Range:** string

**URI:** [`voc4cat:0000101`](voc4cat:0000101)

**Schema Reference:** [reactant](elements/reactant.md)

</details>

<details markdown="1">
<summary><strong>operation parameters (Required, Multivalued)</strong></summary>

**Description:** Operation parameters for the reaction

**Range:** OperationParameters

**URI:** [`voc4cat:0000142`](voc4cat:0000142)

**Schema Reference:** [operation_parameters](elements/operation_parameters.md)

**Range Class Details:**

<details markdown="1">
<summary><strong>OperationParameters</strong></summary>

**Description:** Operation parameters for the reaction

**Schema Reference:** [OperationParameters](elements/OperationParameters.md)

**Slots**

<details markdown="1">
<summary><strong>reactor temperature range (Optional, Multivalued)</strong></summary>

**Description:** Temperature range in reactor

**Range:** string

**URI:** [`voc4cat:0007032`](voc4cat:0007032)

**Schema Reference:** [reactor_temperature_range](elements/reactor_temperature_range.md)

</details>

<details markdown="1">
<summary><strong>atmosphere (Optional, Multivalued)</strong></summary>

**Description:** Atmospheric conditions

**Range:** string

**URI:** [`catcore:atmosphere`](catcore:atmosphere)

**Schema Reference:** [atmosphere](elements/atmosphere.md)

</details>

<details markdown="1">
<summary><strong>experiment pressure (Optional, Multivalued)</strong></summary>

**Description:** Pressure during experiment

**Range:** float

**URI:** [`voc4cat:0000118`](voc4cat:0000118)

**Schema Reference:** [experiment_pressure](elements/experiment_pressure.md)

**Unit:** bar

</details>

<details markdown="1">
<summary><strong>feed composition range (Optional, Multivalued)</strong></summary>

**Description:** Range of feed composition

**Range:** string

**URI:** [`catcore:feed_composition_range`](catcore:feed_composition_range)

**Schema Reference:** [feed_composition_range](elements/feed_composition_range.md)

</details>

<details markdown="1">
<summary><strong>experiment duration (Optional, Multivalued)</strong></summary>

**Description:** Duration of the experiment

**Range:** float

**URI:** [`AFR:0002455`](AFR:0002455)

**Schema Reference:** [experiment_duration](elements/experiment_duration.md)

**Unit:** h

</details>

</details>

</details>

<details markdown="1">
<summary><strong>product identification method (Required, Multivalued)</strong></summary>

**Description:** Method used for product identification

**Range:** ProductIdentificationMethod

**URI:** [`voc4cat:0000129`](voc4cat:0000129)

**Schema Reference:** [product_identification_method](elements/product_identification_method.md)

**Range Class Details:**

<details markdown="1">
<summary><strong>ProductIdentificationMethod</strong></summary>

**Abstract Class**

**Description:** Method used for product identification

**Schema Reference:** [ProductIdentificationMethod](elements/ProductIdentificationMethod.md)

</details>

</details>

<details markdown="1">
<summary><strong>catalyst type (Recommended, Multivalued)</strong></summary>

**Description:** Type of catalyst

**Range:** string

**URI:** [`voc4cat:0007014`](voc4cat:0007014)

**Schema Reference:** [catalyst_type](elements/catalyst_type.md)

</details>

