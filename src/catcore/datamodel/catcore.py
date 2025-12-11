# Auto generated from catcore.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-12-11T14:30:24
# Schema: catcore-metadata
#
# id: https://w3id.org/nfdi4cat/catcore
# description: The CatCore describes the minimum information which must be reported with research data
#   concerning the field of catalysis. This guideline helps to handle and standardize data
#   based on the FAIR principle (Findable, Accessible, Interoperable, Reusable).
# license: CC-BY-4.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = "1.0.0"

# Namespaces
AFP = CurieNamespace('AFP', 'http://purl.allotrope.org/ontologies/process#AFP_')
AFQ = CurieNamespace('AFQ', 'http://purl.allotrope.org/ontologies/quality#AFQ_')
AFR = CurieNamespace('AFR', 'http://purl.allotrope.org/ontologies/result#AFR_')
AFRL = CurieNamespace('AFRL', 'http://purl.allotrope.org/ontologies/role#AFRL_')
APOLLO_SV = CurieNamespace('APOLLO_SV', 'http://purl.obolibrary.org/obo/APOLLO_SV_')
CHMO = CurieNamespace('CHMO', 'http://purl.obolibrary.org/obo/CHMO_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/SIO_')
CATCORE = CurieNamespace('catcore', 'https://w3id.org/nfdi4cat/catcore/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NMRCV = CurieNamespace('nmrCV', 'http://nmrML.org/nmrCV#NMR:')
VOC4CAT = CurieNamespace('voc4cat', 'https://w3id.org/nfdi4cat/voc4cat_')
DEFAULT_ = CATCORE


# Types

# Class references



@dataclass(repr=False)
class CatCoreEntity(YAMLRoot):
    """
    Root class for all CatCore entities
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["CatCoreEntity"]
    class_class_curie: ClassVar[str] = "catcore:CatCoreEntity"
    class_name: ClassVar[str] = "CatCoreEntity"
    class_model_uri: ClassVar[URIRef] = CATCORE.CatCoreEntity

    identifier: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CatCore(CatCoreEntity):
    """
    The CatCore describes the minimum information which must be reported with research data
    concerning the field of catalysis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["CatCore"]
    class_class_curie: ClassVar[str] = "catcore:CatCore"
    class_name: ClassVar[str] = "CatCore"
    class_model_uri: ClassVar[URIRef] = CATCORE.CatCore

    catalysis_research_field: Union[str, "CatalysisResearchFieldEnum"] = None
    reaction_type: str = None
    active_site: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.catalysis_research_field):
            self.MissingRequiredField("catalysis_research_field")
        if not isinstance(self.catalysis_research_field, CatalysisResearchFieldEnum):
            self.catalysis_research_field = CatalysisResearchFieldEnum(self.catalysis_research_field)

        if self._is_empty(self.reaction_type):
            self.MissingRequiredField("reaction_type")
        if not isinstance(self.reaction_type, str):
            self.reaction_type = str(self.reaction_type)

        if self.active_site is not None and not isinstance(self.active_site, str):
            self.active_site = str(self.active_site)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Synthesis(CatCoreEntity):
    """
    The data class 'Synthesis' describes the minimum information which should be reported
    with research data concerning the field of catalyst synthesis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["Synthesis"]
    class_class_curie: ClassVar[str] = "catcore:Synthesis"
    class_name: ClassVar[str] = "Synthesis"
    class_model_uri: ClassVar[URIRef] = CATCORE.Synthesis

    nominal_composition: str = None
    catalyst_measured_properties: str = None
    precursor: Union[Union[dict, "Precursor"], list[Union[dict, "Precursor"]]] = None
    preparation_method: Union[Union[dict, "PreparationMethod"], list[Union[dict, "PreparationMethod"]]] = None
    storage_conditions: Optional[Union[str, list[str]]] = empty_list()
    support: Optional[Union[str, list[str]]] = empty_list()
    solvent: Optional[Union[str, list[str]]] = empty_list()
    sample_pretreatment: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.nominal_composition):
            self.MissingRequiredField("nominal_composition")
        if not isinstance(self.nominal_composition, str):
            self.nominal_composition = str(self.nominal_composition)

        if self._is_empty(self.catalyst_measured_properties):
            self.MissingRequiredField("catalyst_measured_properties")
        if not isinstance(self.catalyst_measured_properties, str):
            self.catalyst_measured_properties = str(self.catalyst_measured_properties)

        if self._is_empty(self.precursor):
            self.MissingRequiredField("precursor")
        if not isinstance(self.precursor, list):
            self.precursor = [self.precursor] if self.precursor is not None else []
        self.precursor = [v if isinstance(v, Precursor) else Precursor(**as_dict(v)) for v in self.precursor]

        if self._is_empty(self.preparation_method):
            self.MissingRequiredField("preparation_method")
        if not isinstance(self.preparation_method, list):
            self.preparation_method = [self.preparation_method] if self.preparation_method is not None else []
        self.preparation_method = [v if isinstance(v, PreparationMethod) else PreparationMethod(**as_dict(v)) for v in self.preparation_method]

        if not isinstance(self.storage_conditions, list):
            self.storage_conditions = [self.storage_conditions] if self.storage_conditions is not None else []
        self.storage_conditions = [v if isinstance(v, str) else str(v) for v in self.storage_conditions]

        if not isinstance(self.support, list):
            self.support = [self.support] if self.support is not None else []
        self.support = [v if isinstance(v, str) else str(v) for v in self.support]

        if not isinstance(self.solvent, list):
            self.solvent = [self.solvent] if self.solvent is not None else []
        self.solvent = [v if isinstance(v, str) else str(v) for v in self.solvent]

        if not isinstance(self.sample_pretreatment, list):
            self.sample_pretreatment = [self.sample_pretreatment] if self.sample_pretreatment is not None else []
        self.sample_pretreatment = [v if isinstance(v, str) else str(v) for v in self.sample_pretreatment]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Precursor(CatCoreEntity):
    """
    Precursor material used in catalyst synthesis
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["Precursor"]
    class_class_curie: ClassVar[str] = "catcore:Precursor"
    class_name: ClassVar[str] = "Precursor"
    class_model_uri: ClassVar[URIRef] = CATCORE.Precursor

    precursor_quantity: Union[float, list[float]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.precursor_quantity):
            self.MissingRequiredField("precursor_quantity")
        if not isinstance(self.precursor_quantity, list):
            self.precursor_quantity = [self.precursor_quantity] if self.precursor_quantity is not None else []
        self.precursor_quantity = [v if isinstance(v, float) else float(v) for v in self.precursor_quantity]

        super().__post_init__(**kwargs)


class PreparationMethod(CatCoreEntity):
    """
    Method used for catalyst preparation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["PreparationMethod"]
    class_class_curie: ClassVar[str] = "catcore:PreparationMethod"
    class_name: ClassVar[str] = "PreparationMethod"
    class_model_uri: ClassVar[URIRef] = CATCORE.PreparationMethod


@dataclass(repr=False)
class Impregnation(PreparationMethod):
    """
    Impregnation method for catalyst preparation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["Impregnation"]
    class_class_curie: ClassVar[str] = "catcore:Impregnation"
    class_name: ClassVar[str] = "Impregnation"
    class_model_uri: ClassVar[URIRef] = CATCORE.Impregnation

    impregnation_type: Optional[Union[Union[str, "ImpregnationTypeEnum"], list[Union[str, "ImpregnationTypeEnum"]]]] = empty_list()
    impregnation_duration: Optional[Union[float, list[float]]] = empty_list()
    impregnation_temperature: Optional[Union[float, list[float]]] = empty_list()
    drying_device: Optional[Union[str, list[str]]] = empty_list()
    drying_temperature: Optional[Union[float, list[float]]] = empty_list()
    drying_time: Optional[Union[float, list[float]]] = empty_list()
    drying_atmosphere: Optional[Union[str, list[str]]] = empty_list()
    calcination_initial_temperature: Optional[Union[float, list[float]]] = empty_list()
    calcination_final_temperature: Optional[Union[float, list[float]]] = empty_list()
    calcination_dwelling_time: Optional[Union[float, list[float]]] = empty_list()
    number_of_cycles: Optional[Union[int, list[int]]] = empty_list()
    calcination_gaseous_environment: Optional[Union[str, list[str]]] = empty_list()
    calcination_heating_rate: Optional[Union[float, list[float]]] = empty_list()
    calcination_gas_flow_rate: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.impregnation_type, list):
            self.impregnation_type = [self.impregnation_type] if self.impregnation_type is not None else []
        self.impregnation_type = [v if isinstance(v, ImpregnationTypeEnum) else ImpregnationTypeEnum(v) for v in self.impregnation_type]

        if not isinstance(self.impregnation_duration, list):
            self.impregnation_duration = [self.impregnation_duration] if self.impregnation_duration is not None else []
        self.impregnation_duration = [v if isinstance(v, float) else float(v) for v in self.impregnation_duration]

        if not isinstance(self.impregnation_temperature, list):
            self.impregnation_temperature = [self.impregnation_temperature] if self.impregnation_temperature is not None else []
        self.impregnation_temperature = [v if isinstance(v, float) else float(v) for v in self.impregnation_temperature]

        if not isinstance(self.drying_device, list):
            self.drying_device = [self.drying_device] if self.drying_device is not None else []
        self.drying_device = [v if isinstance(v, str) else str(v) for v in self.drying_device]

        if not isinstance(self.drying_temperature, list):
            self.drying_temperature = [self.drying_temperature] if self.drying_temperature is not None else []
        self.drying_temperature = [v if isinstance(v, float) else float(v) for v in self.drying_temperature]

        if not isinstance(self.drying_time, list):
            self.drying_time = [self.drying_time] if self.drying_time is not None else []
        self.drying_time = [v if isinstance(v, float) else float(v) for v in self.drying_time]

        if not isinstance(self.drying_atmosphere, list):
            self.drying_atmosphere = [self.drying_atmosphere] if self.drying_atmosphere is not None else []
        self.drying_atmosphere = [v if isinstance(v, str) else str(v) for v in self.drying_atmosphere]

        if not isinstance(self.calcination_initial_temperature, list):
            self.calcination_initial_temperature = [self.calcination_initial_temperature] if self.calcination_initial_temperature is not None else []
        self.calcination_initial_temperature = [v if isinstance(v, float) else float(v) for v in self.calcination_initial_temperature]

        if not isinstance(self.calcination_final_temperature, list):
            self.calcination_final_temperature = [self.calcination_final_temperature] if self.calcination_final_temperature is not None else []
        self.calcination_final_temperature = [v if isinstance(v, float) else float(v) for v in self.calcination_final_temperature]

        if not isinstance(self.calcination_dwelling_time, list):
            self.calcination_dwelling_time = [self.calcination_dwelling_time] if self.calcination_dwelling_time is not None else []
        self.calcination_dwelling_time = [v if isinstance(v, float) else float(v) for v in self.calcination_dwelling_time]

        if not isinstance(self.number_of_cycles, list):
            self.number_of_cycles = [self.number_of_cycles] if self.number_of_cycles is not None else []
        self.number_of_cycles = [v if isinstance(v, int) else int(v) for v in self.number_of_cycles]

        if not isinstance(self.calcination_gaseous_environment, list):
            self.calcination_gaseous_environment = [self.calcination_gaseous_environment] if self.calcination_gaseous_environment is not None else []
        self.calcination_gaseous_environment = [v if isinstance(v, str) else str(v) for v in self.calcination_gaseous_environment]

        if not isinstance(self.calcination_heating_rate, list):
            self.calcination_heating_rate = [self.calcination_heating_rate] if self.calcination_heating_rate is not None else []
        self.calcination_heating_rate = [v if isinstance(v, float) else float(v) for v in self.calcination_heating_rate]

        if not isinstance(self.calcination_gas_flow_rate, list):
            self.calcination_gas_flow_rate = [self.calcination_gas_flow_rate] if self.calcination_gas_flow_rate is not None else []
        self.calcination_gas_flow_rate = [v if isinstance(v, float) else float(v) for v in self.calcination_gas_flow_rate]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CoPrecipitation(PreparationMethod):
    """
    Co-precipitation method for catalyst preparation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["CoPrecipitation"]
    class_class_curie: ClassVar[str] = "catcore:CoPrecipitation"
    class_name: ClassVar[str] = "CoPrecipitation"
    class_model_uri: ClassVar[URIRef] = CATCORE.CoPrecipitation

    precipitating_agent: Optional[Union[str, list[str]]] = empty_list()
    precipitating_concentration: Optional[Union[float, list[float]]] = empty_list()
    synthesis_ph: Optional[Union[float, list[float]]] = empty_list()
    mixing_rate: Optional[Union[float, list[float]]] = empty_list()
    mixing_time: Optional[Union[float, list[float]]] = empty_list()
    mixing_temperature: Optional[Union[float, list[float]]] = empty_list()
    drying_device: Optional[Union[str, list[str]]] = empty_list()
    drying_temperature: Optional[Union[float, list[float]]] = empty_list()
    drying_time: Optional[Union[float, list[float]]] = empty_list()
    drying_atmosphere: Optional[Union[str, list[str]]] = empty_list()
    calcination_initial_temperature: Optional[Union[float, list[float]]] = empty_list()
    calcination_final_temperature: Optional[Union[float, list[float]]] = empty_list()
    calcination_dwelling_time: Optional[Union[float, list[float]]] = empty_list()
    number_of_cycles: Optional[Union[int, list[int]]] = empty_list()
    calcination_gaseous_environment: Optional[Union[str, list[str]]] = empty_list()
    calcination_heating_rate: Optional[Union[float, list[float]]] = empty_list()
    calcination_gas_flow_rate: Optional[Union[float, list[float]]] = empty_list()
    order_of_addition: Optional[Union[str, list[str]]] = empty_list()
    filtration: Optional[Union[str, list[str]]] = empty_list()
    purification: Optional[Union[str, list[str]]] = empty_list()
    aging_temperature: Optional[Union[float, list[float]]] = empty_list()
    aging_time: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.precipitating_agent, list):
            self.precipitating_agent = [self.precipitating_agent] if self.precipitating_agent is not None else []
        self.precipitating_agent = [v if isinstance(v, str) else str(v) for v in self.precipitating_agent]

        if not isinstance(self.precipitating_concentration, list):
            self.precipitating_concentration = [self.precipitating_concentration] if self.precipitating_concentration is not None else []
        self.precipitating_concentration = [v if isinstance(v, float) else float(v) for v in self.precipitating_concentration]

        if not isinstance(self.synthesis_ph, list):
            self.synthesis_ph = [self.synthesis_ph] if self.synthesis_ph is not None else []
        self.synthesis_ph = [v if isinstance(v, float) else float(v) for v in self.synthesis_ph]

        if not isinstance(self.mixing_rate, list):
            self.mixing_rate = [self.mixing_rate] if self.mixing_rate is not None else []
        self.mixing_rate = [v if isinstance(v, float) else float(v) for v in self.mixing_rate]

        if not isinstance(self.mixing_time, list):
            self.mixing_time = [self.mixing_time] if self.mixing_time is not None else []
        self.mixing_time = [v if isinstance(v, float) else float(v) for v in self.mixing_time]

        if not isinstance(self.mixing_temperature, list):
            self.mixing_temperature = [self.mixing_temperature] if self.mixing_temperature is not None else []
        self.mixing_temperature = [v if isinstance(v, float) else float(v) for v in self.mixing_temperature]

        if not isinstance(self.drying_device, list):
            self.drying_device = [self.drying_device] if self.drying_device is not None else []
        self.drying_device = [v if isinstance(v, str) else str(v) for v in self.drying_device]

        if not isinstance(self.drying_temperature, list):
            self.drying_temperature = [self.drying_temperature] if self.drying_temperature is not None else []
        self.drying_temperature = [v if isinstance(v, float) else float(v) for v in self.drying_temperature]

        if not isinstance(self.drying_time, list):
            self.drying_time = [self.drying_time] if self.drying_time is not None else []
        self.drying_time = [v if isinstance(v, float) else float(v) for v in self.drying_time]

        if not isinstance(self.drying_atmosphere, list):
            self.drying_atmosphere = [self.drying_atmosphere] if self.drying_atmosphere is not None else []
        self.drying_atmosphere = [v if isinstance(v, str) else str(v) for v in self.drying_atmosphere]

        if not isinstance(self.calcination_initial_temperature, list):
            self.calcination_initial_temperature = [self.calcination_initial_temperature] if self.calcination_initial_temperature is not None else []
        self.calcination_initial_temperature = [v if isinstance(v, float) else float(v) for v in self.calcination_initial_temperature]

        if not isinstance(self.calcination_final_temperature, list):
            self.calcination_final_temperature = [self.calcination_final_temperature] if self.calcination_final_temperature is not None else []
        self.calcination_final_temperature = [v if isinstance(v, float) else float(v) for v in self.calcination_final_temperature]

        if not isinstance(self.calcination_dwelling_time, list):
            self.calcination_dwelling_time = [self.calcination_dwelling_time] if self.calcination_dwelling_time is not None else []
        self.calcination_dwelling_time = [v if isinstance(v, float) else float(v) for v in self.calcination_dwelling_time]

        if not isinstance(self.number_of_cycles, list):
            self.number_of_cycles = [self.number_of_cycles] if self.number_of_cycles is not None else []
        self.number_of_cycles = [v if isinstance(v, int) else int(v) for v in self.number_of_cycles]

        if not isinstance(self.calcination_gaseous_environment, list):
            self.calcination_gaseous_environment = [self.calcination_gaseous_environment] if self.calcination_gaseous_environment is not None else []
        self.calcination_gaseous_environment = [v if isinstance(v, str) else str(v) for v in self.calcination_gaseous_environment]

        if not isinstance(self.calcination_heating_rate, list):
            self.calcination_heating_rate = [self.calcination_heating_rate] if self.calcination_heating_rate is not None else []
        self.calcination_heating_rate = [v if isinstance(v, float) else float(v) for v in self.calcination_heating_rate]

        if not isinstance(self.calcination_gas_flow_rate, list):
            self.calcination_gas_flow_rate = [self.calcination_gas_flow_rate] if self.calcination_gas_flow_rate is not None else []
        self.calcination_gas_flow_rate = [v if isinstance(v, float) else float(v) for v in self.calcination_gas_flow_rate]

        if not isinstance(self.order_of_addition, list):
            self.order_of_addition = [self.order_of_addition] if self.order_of_addition is not None else []
        self.order_of_addition = [v if isinstance(v, str) else str(v) for v in self.order_of_addition]

        if not isinstance(self.filtration, list):
            self.filtration = [self.filtration] if self.filtration is not None else []
        self.filtration = [v if isinstance(v, str) else str(v) for v in self.filtration]

        if not isinstance(self.purification, list):
            self.purification = [self.purification] if self.purification is not None else []
        self.purification = [v if isinstance(v, str) else str(v) for v in self.purification]

        if not isinstance(self.aging_temperature, list):
            self.aging_temperature = [self.aging_temperature] if self.aging_temperature is not None else []
        self.aging_temperature = [v if isinstance(v, float) else float(v) for v in self.aging_temperature]

        if not isinstance(self.aging_time, list):
            self.aging_time = [self.aging_time] if self.aging_time is not None else []
        self.aging_time = [v if isinstance(v, float) else float(v) for v in self.aging_time]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SolGel(PreparationMethod):
    """
    Sol-gel method for catalyst preparation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["SolGel"]
    class_class_curie: ClassVar[str] = "catcore:SolGel"
    class_name: ClassVar[str] = "SolGel"
    class_model_uri: ClassVar[URIRef] = CATCORE.SolGel

    hydrolysis_ratio: Optional[Union[float, list[float]]] = empty_list()
    aging_time: Optional[Union[float, list[float]]] = empty_list()
    drying: Optional[Union[str, list[str]]] = empty_list()
    surfactant_template: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.hydrolysis_ratio, list):
            self.hydrolysis_ratio = [self.hydrolysis_ratio] if self.hydrolysis_ratio is not None else []
        self.hydrolysis_ratio = [v if isinstance(v, float) else float(v) for v in self.hydrolysis_ratio]

        if not isinstance(self.aging_time, list):
            self.aging_time = [self.aging_time] if self.aging_time is not None else []
        self.aging_time = [v if isinstance(v, float) else float(v) for v in self.aging_time]

        if not isinstance(self.drying, list):
            self.drying = [self.drying] if self.drying is not None else []
        self.drying = [v if isinstance(v, str) else str(v) for v in self.drying]

        if not isinstance(self.surfactant_template, list):
            self.surfactant_template = [self.surfactant_template] if self.surfactant_template is not None else []
        self.surfactant_template = [v if isinstance(v, str) else str(v) for v in self.surfactant_template]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Solvothermal(PreparationMethod):
    """
    Solvothermal method for catalyst preparation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["Solvothermal"]
    class_class_curie: ClassVar[str] = "catcore:Solvothermal"
    class_name: ClassVar[str] = "Solvothermal"
    class_model_uri: ClassVar[URIRef] = CATCORE.Solvothermal

    filling_volume: Optional[Union[float, list[float]]] = empty_list()
    synthesis_temperature: Optional[Union[float, list[float]]] = empty_list()
    synthesis_duration: Optional[Union[float, list[float]]] = empty_list()
    vessel_type: Optional[Union[str, list[str]]] = empty_list()
    equipment: Optional[Union[str, list[str]]] = empty_list()
    stirring_speed: Optional[Union[float, list[float]]] = empty_list()
    stirrer_type: Optional[Union[str, list[str]]] = empty_list()
    cooling_rate: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.filling_volume, list):
            self.filling_volume = [self.filling_volume] if self.filling_volume is not None else []
        self.filling_volume = [v if isinstance(v, float) else float(v) for v in self.filling_volume]

        if not isinstance(self.synthesis_temperature, list):
            self.synthesis_temperature = [self.synthesis_temperature] if self.synthesis_temperature is not None else []
        self.synthesis_temperature = [v if isinstance(v, float) else float(v) for v in self.synthesis_temperature]

        if not isinstance(self.synthesis_duration, list):
            self.synthesis_duration = [self.synthesis_duration] if self.synthesis_duration is not None else []
        self.synthesis_duration = [v if isinstance(v, float) else float(v) for v in self.synthesis_duration]

        if not isinstance(self.vessel_type, list):
            self.vessel_type = [self.vessel_type] if self.vessel_type is not None else []
        self.vessel_type = [v if isinstance(v, str) else str(v) for v in self.vessel_type]

        if not isinstance(self.equipment, list):
            self.equipment = [self.equipment] if self.equipment is not None else []
        self.equipment = [v if isinstance(v, str) else str(v) for v in self.equipment]

        if not isinstance(self.stirring_speed, list):
            self.stirring_speed = [self.stirring_speed] if self.stirring_speed is not None else []
        self.stirring_speed = [v if isinstance(v, float) else float(v) for v in self.stirring_speed]

        if not isinstance(self.stirrer_type, list):
            self.stirrer_type = [self.stirrer_type] if self.stirrer_type is not None else []
        self.stirrer_type = [v if isinstance(v, str) else str(v) for v in self.stirrer_type]

        if not isinstance(self.cooling_rate, list):
            self.cooling_rate = [self.cooling_rate] if self.cooling_rate is not None else []
        self.cooling_rate = [v if isinstance(v, float) else float(v) for v in self.cooling_rate]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PlasmaAssisted(PreparationMethod):
    """
    Plasma-assisted method for catalyst preparation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["PlasmaAssisted"]
    class_class_curie: ClassVar[str] = "catcore:PlasmaAssisted"
    class_name: ClassVar[str] = "PlasmaAssisted"
    class_model_uri: ClassVar[URIRef] = CATCORE.PlasmaAssisted

    plasma_type: Optional[Union[str, list[str]]] = empty_list()
    equipment: Optional[Union[str, list[str]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()
    power_input: Optional[Union[float, list[float]]] = empty_list()
    exposure_time: Optional[Union[float, list[float]]] = empty_list()
    synthesis_pressure: Optional[Union[float, list[float]]] = empty_list()
    synthesis_temperature: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.plasma_type, list):
            self.plasma_type = [self.plasma_type] if self.plasma_type is not None else []
        self.plasma_type = [v if isinstance(v, str) else str(v) for v in self.plasma_type]

        if not isinstance(self.equipment, list):
            self.equipment = [self.equipment] if self.equipment is not None else []
        self.equipment = [v if isinstance(v, str) else str(v) for v in self.equipment]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        if not isinstance(self.power_input, list):
            self.power_input = [self.power_input] if self.power_input is not None else []
        self.power_input = [v if isinstance(v, float) else float(v) for v in self.power_input]

        if not isinstance(self.exposure_time, list):
            self.exposure_time = [self.exposure_time] if self.exposure_time is not None else []
        self.exposure_time = [v if isinstance(v, float) else float(v) for v in self.exposure_time]

        if not isinstance(self.synthesis_pressure, list):
            self.synthesis_pressure = [self.synthesis_pressure] if self.synthesis_pressure is not None else []
        self.synthesis_pressure = [v if isinstance(v, float) else float(v) for v in self.synthesis_pressure]

        if not isinstance(self.synthesis_temperature, list):
            self.synthesis_temperature = [self.synthesis_temperature] if self.synthesis_temperature is not None else []
        self.synthesis_temperature = [v if isinstance(v, float) else float(v) for v in self.synthesis_temperature]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CombustionSynthesis(PreparationMethod):
    """
    Combustion synthesis method for catalyst preparation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["CombustionSynthesis"]
    class_class_curie: ClassVar[str] = "catcore:CombustionSynthesis"
    class_name: ClassVar[str] = "CombustionSynthesis"
    class_model_uri: ClassVar[URIRef] = CATCORE.CombustionSynthesis

    fuel: Optional[Union[str, list[str]]] = empty_list()
    oxidizer: Optional[Union[str, list[str]]] = empty_list()
    fuel_to_oxidizer_ratio: Optional[Union[float, list[float]]] = empty_list()
    set_temperature: Optional[Union[float, list[float]]] = empty_list()
    post_treatment: Optional[Union[str, list[str]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()
    vessel_type: Optional[Union[str, list[str]]] = empty_list()
    equipment: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.fuel, list):
            self.fuel = [self.fuel] if self.fuel is not None else []
        self.fuel = [v if isinstance(v, str) else str(v) for v in self.fuel]

        if not isinstance(self.oxidizer, list):
            self.oxidizer = [self.oxidizer] if self.oxidizer is not None else []
        self.oxidizer = [v if isinstance(v, str) else str(v) for v in self.oxidizer]

        if not isinstance(self.fuel_to_oxidizer_ratio, list):
            self.fuel_to_oxidizer_ratio = [self.fuel_to_oxidizer_ratio] if self.fuel_to_oxidizer_ratio is not None else []
        self.fuel_to_oxidizer_ratio = [v if isinstance(v, float) else float(v) for v in self.fuel_to_oxidizer_ratio]

        if not isinstance(self.set_temperature, list):
            self.set_temperature = [self.set_temperature] if self.set_temperature is not None else []
        self.set_temperature = [v if isinstance(v, float) else float(v) for v in self.set_temperature]

        if not isinstance(self.post_treatment, list):
            self.post_treatment = [self.post_treatment] if self.post_treatment is not None else []
        self.post_treatment = [v if isinstance(v, str) else str(v) for v in self.post_treatment]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        if not isinstance(self.vessel_type, list):
            self.vessel_type = [self.vessel_type] if self.vessel_type is not None else []
        self.vessel_type = [v if isinstance(v, str) else str(v) for v in self.vessel_type]

        if not isinstance(self.equipment, list):
            self.equipment = [self.equipment] if self.equipment is not None else []
        self.equipment = [v if isinstance(v, str) else str(v) for v in self.equipment]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AtomicLayerDeposition(PreparationMethod):
    """
    Atomic layer deposition method for catalyst preparation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["AtomicLayerDeposition"]
    class_class_curie: ClassVar[str] = "catcore:AtomicLayerDeposition"
    class_name: ClassVar[str] = "AtomicLayerDeposition"
    class_model_uri: ClassVar[URIRef] = CATCORE.AtomicLayerDeposition

    substrate: Optional[Union[str, list[str]]] = empty_list()
    pulse_time: Optional[Union[float, list[float]]] = empty_list()
    purging_duration: Optional[Union[float, list[float]]] = empty_list()
    number_of_cycles: Optional[Union[int, list[int]]] = empty_list()
    deposition_temperature: Optional[Union[float, list[float]]] = empty_list()
    carrier_gas: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.substrate, list):
            self.substrate = [self.substrate] if self.substrate is not None else []
        self.substrate = [v if isinstance(v, str) else str(v) for v in self.substrate]

        if not isinstance(self.pulse_time, list):
            self.pulse_time = [self.pulse_time] if self.pulse_time is not None else []
        self.pulse_time = [v if isinstance(v, float) else float(v) for v in self.pulse_time]

        if not isinstance(self.purging_duration, list):
            self.purging_duration = [self.purging_duration] if self.purging_duration is not None else []
        self.purging_duration = [v if isinstance(v, float) else float(v) for v in self.purging_duration]

        if not isinstance(self.number_of_cycles, list):
            self.number_of_cycles = [self.number_of_cycles] if self.number_of_cycles is not None else []
        self.number_of_cycles = [v if isinstance(v, int) else int(v) for v in self.number_of_cycles]

        if not isinstance(self.deposition_temperature, list):
            self.deposition_temperature = [self.deposition_temperature] if self.deposition_temperature is not None else []
        self.deposition_temperature = [v if isinstance(v, float) else float(v) for v in self.deposition_temperature]

        if not isinstance(self.carrier_gas, list):
            self.carrier_gas = [self.carrier_gas] if self.carrier_gas is not None else []
        self.carrier_gas = [v if isinstance(v, str) else str(v) for v in self.carrier_gas]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DepositionPrecipitation(PreparationMethod):
    """
    Deposition-precipitation method for catalyst preparation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["DepositionPrecipitation"]
    class_class_curie: ClassVar[str] = "catcore:DepositionPrecipitation"
    class_name: ClassVar[str] = "DepositionPrecipitation"
    class_model_uri: ClassVar[URIRef] = CATCORE.DepositionPrecipitation

    precipitating_agent: Optional[Union[str, list[str]]] = empty_list()
    synthesis_ph: Optional[Union[float, list[float]]] = empty_list()
    deposition_temperature: Optional[Union[float, list[float]]] = empty_list()
    deposition_time: Optional[Union[float, list[float]]] = empty_list()
    mixing_rate: Optional[Union[float, list[float]]] = empty_list()
    mixing_time: Optional[Union[float, list[float]]] = empty_list()
    mixing_temperature: Optional[Union[float, list[float]]] = empty_list()
    drying_device: Optional[Union[str, list[str]]] = empty_list()
    drying_temperature: Optional[Union[float, list[float]]] = empty_list()
    drying_time: Optional[Union[float, list[float]]] = empty_list()
    drying_atmosphere: Optional[Union[str, list[str]]] = empty_list()
    calcination_initial_temperature: Optional[Union[float, list[float]]] = empty_list()
    calcination_final_temperature: Optional[Union[float, list[float]]] = empty_list()
    calcination_dwelling_time: Optional[Union[float, list[float]]] = empty_list()
    number_of_cycles: Optional[Union[int, list[int]]] = empty_list()
    calcination_gaseous_environment: Optional[Union[str, list[str]]] = empty_list()
    calcination_heating_rate: Optional[Union[float, list[float]]] = empty_list()
    calcination_gas_flow_rate: Optional[Union[float, list[float]]] = empty_list()
    order_of_addition: Optional[Union[str, list[str]]] = empty_list()
    filtration: Optional[Union[str, list[str]]] = empty_list()
    purification: Optional[Union[str, list[str]]] = empty_list()
    aging_temperature: Optional[Union[float, list[float]]] = empty_list()
    aging_time: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.precipitating_agent, list):
            self.precipitating_agent = [self.precipitating_agent] if self.precipitating_agent is not None else []
        self.precipitating_agent = [v if isinstance(v, str) else str(v) for v in self.precipitating_agent]

        if not isinstance(self.synthesis_ph, list):
            self.synthesis_ph = [self.synthesis_ph] if self.synthesis_ph is not None else []
        self.synthesis_ph = [v if isinstance(v, float) else float(v) for v in self.synthesis_ph]

        if not isinstance(self.deposition_temperature, list):
            self.deposition_temperature = [self.deposition_temperature] if self.deposition_temperature is not None else []
        self.deposition_temperature = [v if isinstance(v, float) else float(v) for v in self.deposition_temperature]

        if not isinstance(self.deposition_time, list):
            self.deposition_time = [self.deposition_time] if self.deposition_time is not None else []
        self.deposition_time = [v if isinstance(v, float) else float(v) for v in self.deposition_time]

        if not isinstance(self.mixing_rate, list):
            self.mixing_rate = [self.mixing_rate] if self.mixing_rate is not None else []
        self.mixing_rate = [v if isinstance(v, float) else float(v) for v in self.mixing_rate]

        if not isinstance(self.mixing_time, list):
            self.mixing_time = [self.mixing_time] if self.mixing_time is not None else []
        self.mixing_time = [v if isinstance(v, float) else float(v) for v in self.mixing_time]

        if not isinstance(self.mixing_temperature, list):
            self.mixing_temperature = [self.mixing_temperature] if self.mixing_temperature is not None else []
        self.mixing_temperature = [v if isinstance(v, float) else float(v) for v in self.mixing_temperature]

        if not isinstance(self.drying_device, list):
            self.drying_device = [self.drying_device] if self.drying_device is not None else []
        self.drying_device = [v if isinstance(v, str) else str(v) for v in self.drying_device]

        if not isinstance(self.drying_temperature, list):
            self.drying_temperature = [self.drying_temperature] if self.drying_temperature is not None else []
        self.drying_temperature = [v if isinstance(v, float) else float(v) for v in self.drying_temperature]

        if not isinstance(self.drying_time, list):
            self.drying_time = [self.drying_time] if self.drying_time is not None else []
        self.drying_time = [v if isinstance(v, float) else float(v) for v in self.drying_time]

        if not isinstance(self.drying_atmosphere, list):
            self.drying_atmosphere = [self.drying_atmosphere] if self.drying_atmosphere is not None else []
        self.drying_atmosphere = [v if isinstance(v, str) else str(v) for v in self.drying_atmosphere]

        if not isinstance(self.calcination_initial_temperature, list):
            self.calcination_initial_temperature = [self.calcination_initial_temperature] if self.calcination_initial_temperature is not None else []
        self.calcination_initial_temperature = [v if isinstance(v, float) else float(v) for v in self.calcination_initial_temperature]

        if not isinstance(self.calcination_final_temperature, list):
            self.calcination_final_temperature = [self.calcination_final_temperature] if self.calcination_final_temperature is not None else []
        self.calcination_final_temperature = [v if isinstance(v, float) else float(v) for v in self.calcination_final_temperature]

        if not isinstance(self.calcination_dwelling_time, list):
            self.calcination_dwelling_time = [self.calcination_dwelling_time] if self.calcination_dwelling_time is not None else []
        self.calcination_dwelling_time = [v if isinstance(v, float) else float(v) for v in self.calcination_dwelling_time]

        if not isinstance(self.number_of_cycles, list):
            self.number_of_cycles = [self.number_of_cycles] if self.number_of_cycles is not None else []
        self.number_of_cycles = [v if isinstance(v, int) else int(v) for v in self.number_of_cycles]

        if not isinstance(self.calcination_gaseous_environment, list):
            self.calcination_gaseous_environment = [self.calcination_gaseous_environment] if self.calcination_gaseous_environment is not None else []
        self.calcination_gaseous_environment = [v if isinstance(v, str) else str(v) for v in self.calcination_gaseous_environment]

        if not isinstance(self.calcination_heating_rate, list):
            self.calcination_heating_rate = [self.calcination_heating_rate] if self.calcination_heating_rate is not None else []
        self.calcination_heating_rate = [v if isinstance(v, float) else float(v) for v in self.calcination_heating_rate]

        if not isinstance(self.calcination_gas_flow_rate, list):
            self.calcination_gas_flow_rate = [self.calcination_gas_flow_rate] if self.calcination_gas_flow_rate is not None else []
        self.calcination_gas_flow_rate = [v if isinstance(v, float) else float(v) for v in self.calcination_gas_flow_rate]

        if not isinstance(self.order_of_addition, list):
            self.order_of_addition = [self.order_of_addition] if self.order_of_addition is not None else []
        self.order_of_addition = [v if isinstance(v, str) else str(v) for v in self.order_of_addition]

        if not isinstance(self.filtration, list):
            self.filtration = [self.filtration] if self.filtration is not None else []
        self.filtration = [v if isinstance(v, str) else str(v) for v in self.filtration]

        if not isinstance(self.purification, list):
            self.purification = [self.purification] if self.purification is not None else []
        self.purification = [v if isinstance(v, str) else str(v) for v in self.purification]

        if not isinstance(self.aging_temperature, list):
            self.aging_temperature = [self.aging_temperature] if self.aging_temperature is not None else []
        self.aging_temperature = [v if isinstance(v, float) else float(v) for v in self.aging_temperature]

        if not isinstance(self.aging_time, list):
            self.aging_time = [self.aging_time] if self.aging_time is not None else []
        self.aging_time = [v if isinstance(v, float) else float(v) for v in self.aging_time]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MicrowaveAssisted(PreparationMethod):
    """
    Microwave-assisted method for catalyst preparation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["MicrowaveAssisted"]
    class_class_curie: ClassVar[str] = "catcore:MicrowaveAssisted"
    class_name: ClassVar[str] = "MicrowaveAssisted"
    class_model_uri: ClassVar[URIRef] = CATCORE.MicrowaveAssisted

    equipment: Optional[Union[str, list[str]]] = empty_list()
    power: Optional[Union[float, list[float]]] = empty_list()
    synthesis_duration: Optional[Union[float, list[float]]] = empty_list()
    synthesis_temperature: Optional[Union[float, list[float]]] = empty_list()
    microwave_frequency: Optional[Union[float, list[float]]] = empty_list()
    vessel_type: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.equipment, list):
            self.equipment = [self.equipment] if self.equipment is not None else []
        self.equipment = [v if isinstance(v, str) else str(v) for v in self.equipment]

        if not isinstance(self.power, list):
            self.power = [self.power] if self.power is not None else []
        self.power = [v if isinstance(v, float) else float(v) for v in self.power]

        if not isinstance(self.synthesis_duration, list):
            self.synthesis_duration = [self.synthesis_duration] if self.synthesis_duration is not None else []
        self.synthesis_duration = [v if isinstance(v, float) else float(v) for v in self.synthesis_duration]

        if not isinstance(self.synthesis_temperature, list):
            self.synthesis_temperature = [self.synthesis_temperature] if self.synthesis_temperature is not None else []
        self.synthesis_temperature = [v if isinstance(v, float) else float(v) for v in self.synthesis_temperature]

        if not isinstance(self.microwave_frequency, list):
            self.microwave_frequency = [self.microwave_frequency] if self.microwave_frequency is not None else []
        self.microwave_frequency = [v if isinstance(v, float) else float(v) for v in self.microwave_frequency]

        if not isinstance(self.vessel_type, list):
            self.vessel_type = [self.vessel_type] if self.vessel_type is not None else []
        self.vessel_type = [v if isinstance(v, str) else str(v) for v in self.vessel_type]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SonochemicalSynthesis(PreparationMethod):
    """
    Sonochemical synthesis method for catalyst preparation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["SonochemicalSynthesis"]
    class_class_curie: ClassVar[str] = "catcore:SonochemicalSynthesis"
    class_name: ClassVar[str] = "SonochemicalSynthesis"
    class_model_uri: ClassVar[URIRef] = CATCORE.SonochemicalSynthesis

    stirring_duration: Optional[Union[float, list[float]]] = empty_list()
    sonication_power: Optional[Union[float, list[float]]] = empty_list()
    sonication_duration: Optional[Union[float, list[float]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()
    drying_device: Optional[Union[str, list[str]]] = empty_list()
    drying_temperature: Optional[Union[float, list[float]]] = empty_list()
    drying_time: Optional[Union[float, list[float]]] = empty_list()
    drying_atmosphere: Optional[Union[str, list[str]]] = empty_list()
    calcination_initial_temperature: Optional[Union[float, list[float]]] = empty_list()
    calcination_final_temperature: Optional[Union[float, list[float]]] = empty_list()
    calcination_dwelling_time: Optional[Union[float, list[float]]] = empty_list()
    number_of_cycles: Optional[Union[int, list[int]]] = empty_list()
    calcination_gaseous_environment: Optional[Union[str, list[str]]] = empty_list()
    calcination_heating_rate: Optional[Union[float, list[float]]] = empty_list()
    calcination_gas_flow_rate: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.stirring_duration, list):
            self.stirring_duration = [self.stirring_duration] if self.stirring_duration is not None else []
        self.stirring_duration = [v if isinstance(v, float) else float(v) for v in self.stirring_duration]

        if not isinstance(self.sonication_power, list):
            self.sonication_power = [self.sonication_power] if self.sonication_power is not None else []
        self.sonication_power = [v if isinstance(v, float) else float(v) for v in self.sonication_power]

        if not isinstance(self.sonication_duration, list):
            self.sonication_duration = [self.sonication_duration] if self.sonication_duration is not None else []
        self.sonication_duration = [v if isinstance(v, float) else float(v) for v in self.sonication_duration]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.drying_device, list):
            self.drying_device = [self.drying_device] if self.drying_device is not None else []
        self.drying_device = [v if isinstance(v, str) else str(v) for v in self.drying_device]

        if not isinstance(self.drying_temperature, list):
            self.drying_temperature = [self.drying_temperature] if self.drying_temperature is not None else []
        self.drying_temperature = [v if isinstance(v, float) else float(v) for v in self.drying_temperature]

        if not isinstance(self.drying_time, list):
            self.drying_time = [self.drying_time] if self.drying_time is not None else []
        self.drying_time = [v if isinstance(v, float) else float(v) for v in self.drying_time]

        if not isinstance(self.drying_atmosphere, list):
            self.drying_atmosphere = [self.drying_atmosphere] if self.drying_atmosphere is not None else []
        self.drying_atmosphere = [v if isinstance(v, str) else str(v) for v in self.drying_atmosphere]

        if not isinstance(self.calcination_initial_temperature, list):
            self.calcination_initial_temperature = [self.calcination_initial_temperature] if self.calcination_initial_temperature is not None else []
        self.calcination_initial_temperature = [v if isinstance(v, float) else float(v) for v in self.calcination_initial_temperature]

        if not isinstance(self.calcination_final_temperature, list):
            self.calcination_final_temperature = [self.calcination_final_temperature] if self.calcination_final_temperature is not None else []
        self.calcination_final_temperature = [v if isinstance(v, float) else float(v) for v in self.calcination_final_temperature]

        if not isinstance(self.calcination_dwelling_time, list):
            self.calcination_dwelling_time = [self.calcination_dwelling_time] if self.calcination_dwelling_time is not None else []
        self.calcination_dwelling_time = [v if isinstance(v, float) else float(v) for v in self.calcination_dwelling_time]

        if not isinstance(self.number_of_cycles, list):
            self.number_of_cycles = [self.number_of_cycles] if self.number_of_cycles is not None else []
        self.number_of_cycles = [v if isinstance(v, int) else int(v) for v in self.number_of_cycles]

        if not isinstance(self.calcination_gaseous_environment, list):
            self.calcination_gaseous_environment = [self.calcination_gaseous_environment] if self.calcination_gaseous_environment is not None else []
        self.calcination_gaseous_environment = [v if isinstance(v, str) else str(v) for v in self.calcination_gaseous_environment]

        if not isinstance(self.calcination_heating_rate, list):
            self.calcination_heating_rate = [self.calcination_heating_rate] if self.calcination_heating_rate is not None else []
        self.calcination_heating_rate = [v if isinstance(v, float) else float(v) for v in self.calcination_heating_rate]

        if not isinstance(self.calcination_gas_flow_rate, list):
            self.calcination_gas_flow_rate = [self.calcination_gas_flow_rate] if self.calcination_gas_flow_rate is not None else []
        self.calcination_gas_flow_rate = [v if isinstance(v, float) else float(v) for v in self.calcination_gas_flow_rate]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FlameSprayPyrolysis(PreparationMethod):
    """
    Flame spray pyrolysis method for catalyst preparation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0007031"]
    class_class_curie: ClassVar[str] = "voc4cat:0007031"
    class_name: ClassVar[str] = "FlameSprayPyrolysis"
    class_model_uri: ClassVar[URIRef] = CATCORE.FlameSprayPyrolysis

    flame_type: Optional[Union[str, list[str]]] = empty_list()
    flow_rate: Optional[Union[float, list[float]]] = empty_list()
    inlet_system: Optional[Union[str, list[str]]] = empty_list()
    flame_ring: Optional[Union[str, list[str]]] = empty_list()
    dispersant: Optional[Union[str, list[str]]] = empty_list()
    capillary_pressure: Optional[Union[float, list[float]]] = empty_list()
    fuel_dispersant_ratio: Optional[Union[float, list[float]]] = empty_list()
    filtration_device: Optional[Union[str, list[str]]] = empty_list()
    filter_type: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.flame_type, list):
            self.flame_type = [self.flame_type] if self.flame_type is not None else []
        self.flame_type = [v if isinstance(v, str) else str(v) for v in self.flame_type]

        if not isinstance(self.flow_rate, list):
            self.flow_rate = [self.flow_rate] if self.flow_rate is not None else []
        self.flow_rate = [v if isinstance(v, float) else float(v) for v in self.flow_rate]

        if not isinstance(self.inlet_system, list):
            self.inlet_system = [self.inlet_system] if self.inlet_system is not None else []
        self.inlet_system = [v if isinstance(v, str) else str(v) for v in self.inlet_system]

        if not isinstance(self.flame_ring, list):
            self.flame_ring = [self.flame_ring] if self.flame_ring is not None else []
        self.flame_ring = [v if isinstance(v, str) else str(v) for v in self.flame_ring]

        if not isinstance(self.dispersant, list):
            self.dispersant = [self.dispersant] if self.dispersant is not None else []
        self.dispersant = [v if isinstance(v, str) else str(v) for v in self.dispersant]

        if not isinstance(self.capillary_pressure, list):
            self.capillary_pressure = [self.capillary_pressure] if self.capillary_pressure is not None else []
        self.capillary_pressure = [v if isinstance(v, float) else float(v) for v in self.capillary_pressure]

        if not isinstance(self.fuel_dispersant_ratio, list):
            self.fuel_dispersant_ratio = [self.fuel_dispersant_ratio] if self.fuel_dispersant_ratio is not None else []
        self.fuel_dispersant_ratio = [v if isinstance(v, float) else float(v) for v in self.fuel_dispersant_ratio]

        if not isinstance(self.filtration_device, list):
            self.filtration_device = [self.filtration_device] if self.filtration_device is not None else []
        self.filtration_device = [v if isinstance(v, str) else str(v) for v in self.filtration_device]

        if not isinstance(self.filter_type, list):
            self.filter_type = [self.filter_type] if self.filter_type is not None else []
        self.filter_type = [v if isinstance(v, str) else str(v) for v in self.filter_type]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MechanochemicalSynthesis(PreparationMethod):
    """
    Mechanochemical synthesis method for catalyst preparation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["MechanochemicalSynthesis"]
    class_class_curie: ClassVar[str] = "catcore:MechanochemicalSynthesis"
    class_name: ClassVar[str] = "MechanochemicalSynthesis"
    class_model_uri: ClassVar[URIRef] = CATCORE.MechanochemicalSynthesis

    equipment: Optional[Union[str, list[str]]] = empty_list()
    vessel_volume: Optional[Union[float, list[float]]] = empty_list()
    size_and_material: Optional[Union[str, list[str]]] = empty_list()
    milling_speed: Optional[Union[float, list[float]]] = empty_list()
    milling_duration: Optional[Union[float, list[float]]] = empty_list()
    synthesis_temperature: Optional[Union[float, list[float]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()
    ball_material: Optional[Union[str, list[str]]] = empty_list()
    ball_size: Optional[Union[float, list[float]]] = empty_list()
    ball_to_powder_ratio: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.equipment, list):
            self.equipment = [self.equipment] if self.equipment is not None else []
        self.equipment = [v if isinstance(v, str) else str(v) for v in self.equipment]

        if not isinstance(self.vessel_volume, list):
            self.vessel_volume = [self.vessel_volume] if self.vessel_volume is not None else []
        self.vessel_volume = [v if isinstance(v, float) else float(v) for v in self.vessel_volume]

        if not isinstance(self.size_and_material, list):
            self.size_and_material = [self.size_and_material] if self.size_and_material is not None else []
        self.size_and_material = [v if isinstance(v, str) else str(v) for v in self.size_and_material]

        if not isinstance(self.milling_speed, list):
            self.milling_speed = [self.milling_speed] if self.milling_speed is not None else []
        self.milling_speed = [v if isinstance(v, float) else float(v) for v in self.milling_speed]

        if not isinstance(self.milling_duration, list):
            self.milling_duration = [self.milling_duration] if self.milling_duration is not None else []
        self.milling_duration = [v if isinstance(v, float) else float(v) for v in self.milling_duration]

        if not isinstance(self.synthesis_temperature, list):
            self.synthesis_temperature = [self.synthesis_temperature] if self.synthesis_temperature is not None else []
        self.synthesis_temperature = [v if isinstance(v, float) else float(v) for v in self.synthesis_temperature]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        if not isinstance(self.ball_material, list):
            self.ball_material = [self.ball_material] if self.ball_material is not None else []
        self.ball_material = [v if isinstance(v, str) else str(v) for v in self.ball_material]

        if not isinstance(self.ball_size, list):
            self.ball_size = [self.ball_size] if self.ball_size is not None else []
        self.ball_size = [v if isinstance(v, float) else float(v) for v in self.ball_size]

        if not isinstance(self.ball_to_powder_ratio, list):
            self.ball_to_powder_ratio = [self.ball_to_powder_ratio] if self.ball_to_powder_ratio is not None else []
        self.ball_to_powder_ratio = [v if isinstance(v, float) else float(v) for v in self.ball_to_powder_ratio]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sublimation(PreparationMethod):
    """
    Sublimation method for catalyst preparation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["Sublimation"]
    class_class_curie: ClassVar[str] = "catcore:Sublimation"
    class_name: ClassVar[str] = "Sublimation"
    class_model_uri: ClassVar[URIRef] = CATCORE.Sublimation

    temperature: Optional[Union[float, list[float]]] = empty_list()
    synthesis_pressure: Optional[Union[float, list[float]]] = empty_list()
    synthesis_duration: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.synthesis_pressure, list):
            self.synthesis_pressure = [self.synthesis_pressure] if self.synthesis_pressure is not None else []
        self.synthesis_pressure = [v if isinstance(v, float) else float(v) for v in self.synthesis_pressure]

        if not isinstance(self.synthesis_duration, list):
            self.synthesis_duration = [self.synthesis_duration] if self.synthesis_duration is not None else []
        self.synthesis_duration = [v if isinstance(v, float) else float(v) for v in self.synthesis_duration]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolecularSynthesis(PreparationMethod):
    """
    Molecular synthesis method for catalyst preparation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["MolecularSynthesis"]
    class_class_curie: ClassVar[str] = "catcore:MolecularSynthesis"
    class_name: ClassVar[str] = "MolecularSynthesis"
    class_model_uri: ClassVar[URIRef] = CATCORE.MolecularSynthesis

    atmosphere: Optional[Union[str, list[str]]] = empty_list()
    synthesis_duration: Optional[Union[float, list[float]]] = empty_list()
    reaction_vessel: Optional[Union[str, list[str]]] = empty_list()
    mixing_device: Optional[Union[str, list[str]]] = empty_list()
    stirring_duration: Optional[Union[float, list[float]]] = empty_list()
    stirring_speed: Optional[Union[float, list[float]]] = empty_list()
    mixing_temperature: Optional[Union[float, list[float]]] = empty_list()
    filtration_device: Optional[Union[str, list[str]]] = empty_list()
    filter_type: Optional[Union[str, list[str]]] = empty_list()
    crystallisation_solvents: Optional[Union[str, list[str]]] = empty_list()
    precipitation_agent: Optional[Union[str, list[str]]] = empty_list()
    crystallisation_duration: Optional[Union[float, list[float]]] = empty_list()
    purification_solvent: Optional[Union[str, list[str]]] = empty_list()
    number_of_cycles: Optional[Union[int, list[int]]] = empty_list()
    drying_device: Optional[Union[str, list[str]]] = empty_list()
    drying_temperature: Optional[Union[float, list[float]]] = empty_list()
    temperature_ramp: Optional[Union[float, list[float]]] = empty_list()
    drying_time: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        if not isinstance(self.synthesis_duration, list):
            self.synthesis_duration = [self.synthesis_duration] if self.synthesis_duration is not None else []
        self.synthesis_duration = [v if isinstance(v, float) else float(v) for v in self.synthesis_duration]

        if not isinstance(self.reaction_vessel, list):
            self.reaction_vessel = [self.reaction_vessel] if self.reaction_vessel is not None else []
        self.reaction_vessel = [v if isinstance(v, str) else str(v) for v in self.reaction_vessel]

        if not isinstance(self.mixing_device, list):
            self.mixing_device = [self.mixing_device] if self.mixing_device is not None else []
        self.mixing_device = [v if isinstance(v, str) else str(v) for v in self.mixing_device]

        if not isinstance(self.stirring_duration, list):
            self.stirring_duration = [self.stirring_duration] if self.stirring_duration is not None else []
        self.stirring_duration = [v if isinstance(v, float) else float(v) for v in self.stirring_duration]

        if not isinstance(self.stirring_speed, list):
            self.stirring_speed = [self.stirring_speed] if self.stirring_speed is not None else []
        self.stirring_speed = [v if isinstance(v, float) else float(v) for v in self.stirring_speed]

        if not isinstance(self.mixing_temperature, list):
            self.mixing_temperature = [self.mixing_temperature] if self.mixing_temperature is not None else []
        self.mixing_temperature = [v if isinstance(v, float) else float(v) for v in self.mixing_temperature]

        if not isinstance(self.filtration_device, list):
            self.filtration_device = [self.filtration_device] if self.filtration_device is not None else []
        self.filtration_device = [v if isinstance(v, str) else str(v) for v in self.filtration_device]

        if not isinstance(self.filter_type, list):
            self.filter_type = [self.filter_type] if self.filter_type is not None else []
        self.filter_type = [v if isinstance(v, str) else str(v) for v in self.filter_type]

        if not isinstance(self.crystallisation_solvents, list):
            self.crystallisation_solvents = [self.crystallisation_solvents] if self.crystallisation_solvents is not None else []
        self.crystallisation_solvents = [v if isinstance(v, str) else str(v) for v in self.crystallisation_solvents]

        if not isinstance(self.precipitation_agent, list):
            self.precipitation_agent = [self.precipitation_agent] if self.precipitation_agent is not None else []
        self.precipitation_agent = [v if isinstance(v, str) else str(v) for v in self.precipitation_agent]

        if not isinstance(self.crystallisation_duration, list):
            self.crystallisation_duration = [self.crystallisation_duration] if self.crystallisation_duration is not None else []
        self.crystallisation_duration = [v if isinstance(v, float) else float(v) for v in self.crystallisation_duration]

        if not isinstance(self.purification_solvent, list):
            self.purification_solvent = [self.purification_solvent] if self.purification_solvent is not None else []
        self.purification_solvent = [v if isinstance(v, str) else str(v) for v in self.purification_solvent]

        if not isinstance(self.number_of_cycles, list):
            self.number_of_cycles = [self.number_of_cycles] if self.number_of_cycles is not None else []
        self.number_of_cycles = [v if isinstance(v, int) else int(v) for v in self.number_of_cycles]

        if not isinstance(self.drying_device, list):
            self.drying_device = [self.drying_device] if self.drying_device is not None else []
        self.drying_device = [v if isinstance(v, str) else str(v) for v in self.drying_device]

        if not isinstance(self.drying_temperature, list):
            self.drying_temperature = [self.drying_temperature] if self.drying_temperature is not None else []
        self.drying_temperature = [v if isinstance(v, float) else float(v) for v in self.drying_temperature]

        if not isinstance(self.temperature_ramp, list):
            self.temperature_ramp = [self.temperature_ramp] if self.temperature_ramp is not None else []
        self.temperature_ramp = [v if isinstance(v, float) else float(v) for v in self.temperature_ramp]

        if not isinstance(self.drying_time, list):
            self.drying_time = [self.drying_time] if self.drying_time is not None else []
        self.drying_time = [v if isinstance(v, float) else float(v) for v in self.drying_time]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExsolutionSynthesis(PreparationMethod):
    """
    Exsolution synthesis method for catalyst preparation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["ExsolutionSynthesis"]
    class_class_curie: ClassVar[str] = "catcore:ExsolutionSynthesis"
    class_name: ClassVar[str] = "ExsolutionSynthesis"
    class_model_uri: ClassVar[URIRef] = CATCORE.ExsolutionSynthesis

    calcination_initial_temperature: Optional[Union[float, list[float]]] = empty_list()
    calcination_final_temperature: Optional[Union[float, list[float]]] = empty_list()
    calcination_dwelling_time: Optional[Union[float, list[float]]] = empty_list()
    calcination_gaseous_environment: Optional[Union[str, list[str]]] = empty_list()
    calcination_heating_rate: Optional[Union[float, list[float]]] = empty_list()
    calcination_gas_flow_rate: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.calcination_initial_temperature, list):
            self.calcination_initial_temperature = [self.calcination_initial_temperature] if self.calcination_initial_temperature is not None else []
        self.calcination_initial_temperature = [v if isinstance(v, float) else float(v) for v in self.calcination_initial_temperature]

        if not isinstance(self.calcination_final_temperature, list):
            self.calcination_final_temperature = [self.calcination_final_temperature] if self.calcination_final_temperature is not None else []
        self.calcination_final_temperature = [v if isinstance(v, float) else float(v) for v in self.calcination_final_temperature]

        if not isinstance(self.calcination_dwelling_time, list):
            self.calcination_dwelling_time = [self.calcination_dwelling_time] if self.calcination_dwelling_time is not None else []
        self.calcination_dwelling_time = [v if isinstance(v, float) else float(v) for v in self.calcination_dwelling_time]

        if not isinstance(self.calcination_gaseous_environment, list):
            self.calcination_gaseous_environment = [self.calcination_gaseous_environment] if self.calcination_gaseous_environment is not None else []
        self.calcination_gaseous_environment = [v if isinstance(v, str) else str(v) for v in self.calcination_gaseous_environment]

        if not isinstance(self.calcination_heating_rate, list):
            self.calcination_heating_rate = [self.calcination_heating_rate] if self.calcination_heating_rate is not None else []
        self.calcination_heating_rate = [v if isinstance(v, float) else float(v) for v in self.calcination_heating_rate]

        if not isinstance(self.calcination_gas_flow_rate, list):
            self.calcination_gas_flow_rate = [self.calcination_gas_flow_rate] if self.calcination_gas_flow_rate is not None else []
        self.calcination_gas_flow_rate = [v if isinstance(v, float) else float(v) for v in self.calcination_gas_flow_rate]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Characterization(CatCoreEntity):
    """
    The data class 'Characterization' describes the minimum information which should be
    reported with research data to describe the nature of the catalyst.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["Characterization"]
    class_class_curie: ClassVar[str] = "catcore:Characterization"
    class_name: ClassVar[str] = "Characterization"
    class_model_uri: ClassVar[URIRef] = CATCORE.Characterization

    equipment: Union[str, list[str]] = None
    characterization_technique: Union[Union[dict, "CharacterizationTechnique"], list[Union[dict, "CharacterizationTechnique"]]] = None
    sample_state: Optional[Union[Union[str, "SampleStateEnum"], list[Union[str, "SampleStateEnum"]]]] = empty_list()
    sample_description: Optional[Union[str, list[str]]] = empty_list()
    detector_type: Optional[Union[str, list[str]]] = empty_list()
    sample_preparation: Optional[Union[str, list[str]]] = empty_list()
    sample_pretreatment: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.equipment):
            self.MissingRequiredField("equipment")
        if not isinstance(self.equipment, list):
            self.equipment = [self.equipment] if self.equipment is not None else []
        self.equipment = [v if isinstance(v, str) else str(v) for v in self.equipment]

        if self._is_empty(self.characterization_technique):
            self.MissingRequiredField("characterization_technique")
        if not isinstance(self.characterization_technique, list):
            self.characterization_technique = [self.characterization_technique] if self.characterization_technique is not None else []
        self.characterization_technique = [v if isinstance(v, CharacterizationTechnique) else CharacterizationTechnique(**as_dict(v)) for v in self.characterization_technique]

        if not isinstance(self.sample_state, list):
            self.sample_state = [self.sample_state] if self.sample_state is not None else []
        self.sample_state = [v if isinstance(v, SampleStateEnum) else SampleStateEnum(v) for v in self.sample_state]

        if not isinstance(self.sample_description, list):
            self.sample_description = [self.sample_description] if self.sample_description is not None else []
        self.sample_description = [v if isinstance(v, str) else str(v) for v in self.sample_description]

        if not isinstance(self.detector_type, list):
            self.detector_type = [self.detector_type] if self.detector_type is not None else []
        self.detector_type = [v if isinstance(v, str) else str(v) for v in self.detector_type]

        if not isinstance(self.sample_preparation, list):
            self.sample_preparation = [self.sample_preparation] if self.sample_preparation is not None else []
        self.sample_preparation = [v if isinstance(v, str) else str(v) for v in self.sample_preparation]

        if not isinstance(self.sample_pretreatment, list):
            self.sample_pretreatment = [self.sample_pretreatment] if self.sample_pretreatment is not None else []
        self.sample_pretreatment = [v if isinstance(v, str) else str(v) for v in self.sample_pretreatment]

        super().__post_init__(**kwargs)


class CharacterizationTechnique(CatCoreEntity):
    """
    Characterization technique used for catalyst analysis
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["CharacterizationTechnique"]
    class_class_curie: ClassVar[str] = "catcore:CharacterizationTechnique"
    class_name: ClassVar[str] = "CharacterizationTechnique"
    class_model_uri: ClassVar[URIRef] = CATCORE.CharacterizationTechnique


@dataclass(repr=False)
class PowderXRD(CharacterizationTechnique):
    """
    Powder X-ray diffraction
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000158"]
    class_class_curie: ClassVar[str] = "CHMO:0000158"
    class_name: ClassVar[str] = "PowderXRD"
    class_model_uri: ClassVar[URIRef] = CATCORE.PowderXRD

    xray_source: Optional[Union[str, list[str]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()
    operation_mode: Optional[Union[str, list[str]]] = empty_list()
    minimum_2theta: Optional[Union[float, list[float]]] = empty_list()
    maximum_2theta: Optional[Union[float, list[float]]] = empty_list()
    step_size: Optional[Union[float, list[float]]] = empty_list()
    monochromator: Optional[Union[str, list[str]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()
    sample_spinning_speed: Optional[Union[float, list[float]]] = empty_list()
    experiment_duration: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.xray_source, list):
            self.xray_source = [self.xray_source] if self.xray_source is not None else []
        self.xray_source = [v if isinstance(v, str) else str(v) for v in self.xray_source]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        if not isinstance(self.operation_mode, list):
            self.operation_mode = [self.operation_mode] if self.operation_mode is not None else []
        self.operation_mode = [v if isinstance(v, str) else str(v) for v in self.operation_mode]

        if not isinstance(self.minimum_2theta, list):
            self.minimum_2theta = [self.minimum_2theta] if self.minimum_2theta is not None else []
        self.minimum_2theta = [v if isinstance(v, float) else float(v) for v in self.minimum_2theta]

        if not isinstance(self.maximum_2theta, list):
            self.maximum_2theta = [self.maximum_2theta] if self.maximum_2theta is not None else []
        self.maximum_2theta = [v if isinstance(v, float) else float(v) for v in self.maximum_2theta]

        if not isinstance(self.step_size, list):
            self.step_size = [self.step_size] if self.step_size is not None else []
        self.step_size = [v if isinstance(v, float) else float(v) for v in self.step_size]

        if not isinstance(self.monochromator, list):
            self.monochromator = [self.monochromator] if self.monochromator is not None else []
        self.monochromator = [v if isinstance(v, str) else str(v) for v in self.monochromator]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.sample_spinning_speed, list):
            self.sample_spinning_speed = [self.sample_spinning_speed] if self.sample_spinning_speed is not None else []
        self.sample_spinning_speed = [v if isinstance(v, float) else float(v) for v in self.sample_spinning_speed]

        if not isinstance(self.experiment_duration, list):
            self.experiment_duration = [self.experiment_duration] if self.experiment_duration is not None else []
        self.experiment_duration = [v if isinstance(v, float) else float(v) for v in self.experiment_duration]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class XRayAbsorptionSpectroscopy(CharacterizationTechnique):
    """
    X-ray absorption spectroscopy
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0000286"]
    class_class_curie: ClassVar[str] = "voc4cat:0000286"
    class_name: ClassVar[str] = "XRayAbsorptionSpectroscopy"
    class_model_uri: ClassVar[URIRef] = CATCORE.XRayAbsorptionSpectroscopy

    operation_mode: Optional[Union[str, list[str]]] = empty_list()
    element_analyzed: Optional[Union[str, list[str]]] = empty_list()
    absorption_edge: Optional[Union[str, list[str]]] = empty_list()
    monochromator: Optional[Union[str, list[str]]] = empty_list()
    minimum_energy: Optional[Union[float, list[float]]] = empty_list()
    maximum_energy: Optional[Union[float, list[float]]] = empty_list()
    energy_resolution: Optional[Union[float, list[float]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()
    beamline_source: Optional[Union[str, list[str]]] = empty_list()
    noise_of_measurement: Optional[Union[float, list[float]]] = empty_list()
    number_of_cycles: Optional[Union[int, list[int]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.operation_mode, list):
            self.operation_mode = [self.operation_mode] if self.operation_mode is not None else []
        self.operation_mode = [v if isinstance(v, str) else str(v) for v in self.operation_mode]

        if not isinstance(self.element_analyzed, list):
            self.element_analyzed = [self.element_analyzed] if self.element_analyzed is not None else []
        self.element_analyzed = [v if isinstance(v, str) else str(v) for v in self.element_analyzed]

        if not isinstance(self.absorption_edge, list):
            self.absorption_edge = [self.absorption_edge] if self.absorption_edge is not None else []
        self.absorption_edge = [v if isinstance(v, str) else str(v) for v in self.absorption_edge]

        if not isinstance(self.monochromator, list):
            self.monochromator = [self.monochromator] if self.monochromator is not None else []
        self.monochromator = [v if isinstance(v, str) else str(v) for v in self.monochromator]

        if not isinstance(self.minimum_energy, list):
            self.minimum_energy = [self.minimum_energy] if self.minimum_energy is not None else []
        self.minimum_energy = [v if isinstance(v, float) else float(v) for v in self.minimum_energy]

        if not isinstance(self.maximum_energy, list):
            self.maximum_energy = [self.maximum_energy] if self.maximum_energy is not None else []
        self.maximum_energy = [v if isinstance(v, float) else float(v) for v in self.maximum_energy]

        if not isinstance(self.energy_resolution, list):
            self.energy_resolution = [self.energy_resolution] if self.energy_resolution is not None else []
        self.energy_resolution = [v if isinstance(v, float) else float(v) for v in self.energy_resolution]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.beamline_source, list):
            self.beamline_source = [self.beamline_source] if self.beamline_source is not None else []
        self.beamline_source = [v if isinstance(v, str) else str(v) for v in self.beamline_source]

        if not isinstance(self.noise_of_measurement, list):
            self.noise_of_measurement = [self.noise_of_measurement] if self.noise_of_measurement is not None else []
        self.noise_of_measurement = [v if isinstance(v, float) else float(v) for v in self.noise_of_measurement]

        if not isinstance(self.number_of_cycles, list):
            self.number_of_cycles = [self.number_of_cycles] if self.number_of_cycles is not None else []
        self.number_of_cycles = [v if isinstance(v, int) else int(v) for v in self.number_of_cycles]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InfraredSpectroscopy(CharacterizationTechnique):
    """
    Infrared spectroscopy
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["InfraredSpectroscopy"]
    class_class_curie: ClassVar[str] = "catcore:InfraredSpectroscopy"
    class_name: ClassVar[str] = "InfraredSpectroscopy"
    class_model_uri: ClassVar[URIRef] = CATCORE.InfraredSpectroscopy

    operation_mode: Optional[Union[str, list[str]]] = empty_list()
    minimum_wavenumber: Optional[Union[float, list[float]]] = empty_list()
    maximum_wavenumber: Optional[Union[float, list[float]]] = empty_list()
    step_size: Optional[Union[float, list[float]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()
    background_correction: Optional[Union[str, list[str]]] = empty_list()
    number_of_scans: Optional[Union[int, list[int]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.operation_mode, list):
            self.operation_mode = [self.operation_mode] if self.operation_mode is not None else []
        self.operation_mode = [v if isinstance(v, str) else str(v) for v in self.operation_mode]

        if not isinstance(self.minimum_wavenumber, list):
            self.minimum_wavenumber = [self.minimum_wavenumber] if self.minimum_wavenumber is not None else []
        self.minimum_wavenumber = [v if isinstance(v, float) else float(v) for v in self.minimum_wavenumber]

        if not isinstance(self.maximum_wavenumber, list):
            self.maximum_wavenumber = [self.maximum_wavenumber] if self.maximum_wavenumber is not None else []
        self.maximum_wavenumber = [v if isinstance(v, float) else float(v) for v in self.maximum_wavenumber]

        if not isinstance(self.step_size, list):
            self.step_size = [self.step_size] if self.step_size is not None else []
        self.step_size = [v if isinstance(v, float) else float(v) for v in self.step_size]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.background_correction, list):
            self.background_correction = [self.background_correction] if self.background_correction is not None else []
        self.background_correction = [v if isinstance(v, str) else str(v) for v in self.background_correction]

        if not isinstance(self.number_of_scans, list):
            self.number_of_scans = [self.number_of_scans] if self.number_of_scans is not None else []
        self.number_of_scans = [v if isinstance(v, int) else int(v) for v in self.number_of_scans]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RamanSpectroscopy(CharacterizationTechnique):
    """
    Raman spectroscopy
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0000069"]
    class_class_curie: ClassVar[str] = "voc4cat:0000069"
    class_name: ClassVar[str] = "RamanSpectroscopy"
    class_model_uri: ClassVar[URIRef] = CATCORE.RamanSpectroscopy

    excitation_laser_wavelength: Optional[Union[float, list[float]]] = empty_list()
    excitation_laser_power: Optional[Union[float, list[float]]] = empty_list()
    magnification_setting: Optional[Union[float, list[float]]] = empty_list()
    integration_time: Optional[Union[float, list[float]]] = empty_list()
    number_of_scans: Optional[Union[int, list[int]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()
    filter_or_grating: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.excitation_laser_wavelength, list):
            self.excitation_laser_wavelength = [self.excitation_laser_wavelength] if self.excitation_laser_wavelength is not None else []
        self.excitation_laser_wavelength = [v if isinstance(v, float) else float(v) for v in self.excitation_laser_wavelength]

        if not isinstance(self.excitation_laser_power, list):
            self.excitation_laser_power = [self.excitation_laser_power] if self.excitation_laser_power is not None else []
        self.excitation_laser_power = [v if isinstance(v, float) else float(v) for v in self.excitation_laser_power]

        if not isinstance(self.magnification_setting, list):
            self.magnification_setting = [self.magnification_setting] if self.magnification_setting is not None else []
        self.magnification_setting = [v if isinstance(v, float) else float(v) for v in self.magnification_setting]

        if not isinstance(self.integration_time, list):
            self.integration_time = [self.integration_time] if self.integration_time is not None else []
        self.integration_time = [v if isinstance(v, float) else float(v) for v in self.integration_time]

        if not isinstance(self.number_of_scans, list):
            self.number_of_scans = [self.number_of_scans] if self.number_of_scans is not None else []
        self.number_of_scans = [v if isinstance(v, int) else int(v) for v in self.number_of_scans]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.filter_or_grating, list):
            self.filter_or_grating = [self.filter_or_grating] if self.filter_or_grating is not None else []
        self.filter_or_grating = [v if isinstance(v, str) else str(v) for v in self.filter_or_grating]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GCMS(CharacterizationTechnique):
    """
    Gas chromatography-mass spectrometry
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000497"]
    class_class_curie: ClassVar[str] = "CHMO:0000497"
    class_name: ClassVar[str] = "GCMS"
    class_model_uri: ClassVar[URIRef] = CATCORE.GCMS

    external_standard: Optional[Union[str, list[str]]] = empty_list()
    internal_standard: Optional[Union[str, list[str]]] = empty_list()
    column_type: Optional[Union[str, list[str]]] = empty_list()
    carrier_gas: Optional[Union[str, list[str]]] = empty_list()
    carrier_gas_purity: Optional[Union[str, list[str]]] = empty_list()
    inlet_temperature: Optional[Union[float, list[float]]] = empty_list()
    minimum_oven_temperature: Optional[Union[float, list[float]]] = empty_list()
    maximum_oven_temperature: Optional[Union[float, list[float]]] = empty_list()
    heating_ramp: Optional[Union[float, list[float]]] = empty_list()
    heating_procedure: Optional[Union[str, list[str]]] = empty_list()
    acquisition_mode: Optional[Union[str, list[str]]] = empty_list()
    solvent_delay: Optional[Union[float, list[float]]] = empty_list()
    trace_ion_detection: Optional[Union[str, list[str]]] = empty_list()
    mz_minimum: Optional[Union[float, list[float]]] = empty_list()
    mz_maximum: Optional[Union[float, list[float]]] = empty_list()
    split_ratio: Optional[Union[float, list[float]]] = empty_list()
    injection_volume: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.external_standard, list):
            self.external_standard = [self.external_standard] if self.external_standard is not None else []
        self.external_standard = [v if isinstance(v, str) else str(v) for v in self.external_standard]

        if not isinstance(self.internal_standard, list):
            self.internal_standard = [self.internal_standard] if self.internal_standard is not None else []
        self.internal_standard = [v if isinstance(v, str) else str(v) for v in self.internal_standard]

        if not isinstance(self.column_type, list):
            self.column_type = [self.column_type] if self.column_type is not None else []
        self.column_type = [v if isinstance(v, str) else str(v) for v in self.column_type]

        if not isinstance(self.carrier_gas, list):
            self.carrier_gas = [self.carrier_gas] if self.carrier_gas is not None else []
        self.carrier_gas = [v if isinstance(v, str) else str(v) for v in self.carrier_gas]

        if not isinstance(self.carrier_gas_purity, list):
            self.carrier_gas_purity = [self.carrier_gas_purity] if self.carrier_gas_purity is not None else []
        self.carrier_gas_purity = [v if isinstance(v, str) else str(v) for v in self.carrier_gas_purity]

        if not isinstance(self.inlet_temperature, list):
            self.inlet_temperature = [self.inlet_temperature] if self.inlet_temperature is not None else []
        self.inlet_temperature = [v if isinstance(v, float) else float(v) for v in self.inlet_temperature]

        if not isinstance(self.minimum_oven_temperature, list):
            self.minimum_oven_temperature = [self.minimum_oven_temperature] if self.minimum_oven_temperature is not None else []
        self.minimum_oven_temperature = [v if isinstance(v, float) else float(v) for v in self.minimum_oven_temperature]

        if not isinstance(self.maximum_oven_temperature, list):
            self.maximum_oven_temperature = [self.maximum_oven_temperature] if self.maximum_oven_temperature is not None else []
        self.maximum_oven_temperature = [v if isinstance(v, float) else float(v) for v in self.maximum_oven_temperature]

        if not isinstance(self.heating_ramp, list):
            self.heating_ramp = [self.heating_ramp] if self.heating_ramp is not None else []
        self.heating_ramp = [v if isinstance(v, float) else float(v) for v in self.heating_ramp]

        if not isinstance(self.heating_procedure, list):
            self.heating_procedure = [self.heating_procedure] if self.heating_procedure is not None else []
        self.heating_procedure = [v if isinstance(v, str) else str(v) for v in self.heating_procedure]

        if not isinstance(self.acquisition_mode, list):
            self.acquisition_mode = [self.acquisition_mode] if self.acquisition_mode is not None else []
        self.acquisition_mode = [v if isinstance(v, str) else str(v) for v in self.acquisition_mode]

        if not isinstance(self.solvent_delay, list):
            self.solvent_delay = [self.solvent_delay] if self.solvent_delay is not None else []
        self.solvent_delay = [v if isinstance(v, float) else float(v) for v in self.solvent_delay]

        if not isinstance(self.trace_ion_detection, list):
            self.trace_ion_detection = [self.trace_ion_detection] if self.trace_ion_detection is not None else []
        self.trace_ion_detection = [v if isinstance(v, str) else str(v) for v in self.trace_ion_detection]

        if not isinstance(self.mz_minimum, list):
            self.mz_minimum = [self.mz_minimum] if self.mz_minimum is not None else []
        self.mz_minimum = [v if isinstance(v, float) else float(v) for v in self.mz_minimum]

        if not isinstance(self.mz_maximum, list):
            self.mz_maximum = [self.mz_maximum] if self.mz_maximum is not None else []
        self.mz_maximum = [v if isinstance(v, float) else float(v) for v in self.mz_maximum]

        if not isinstance(self.split_ratio, list):
            self.split_ratio = [self.split_ratio] if self.split_ratio is not None else []
        self.split_ratio = [v if isinstance(v, float) else float(v) for v in self.split_ratio]

        if not isinstance(self.injection_volume, list):
            self.injection_volume = [self.injection_volume] if self.injection_volume is not None else []
        self.injection_volume = [v if isinstance(v, float) else float(v) for v in self.injection_volume]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NMRSpectroscopy(CharacterizationTechnique):
    """
    Nuclear magnetic resonance spectroscopy
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0000073"]
    class_class_curie: ClassVar[str] = "voc4cat:0000073"
    class_name: ClassVar[str] = "NMRSpectroscopy"
    class_model_uri: ClassVar[URIRef] = CATCORE.NMRSpectroscopy

    nucleus: Optional[Union[str, list[str]]] = empty_list()
    solvent: Optional[Union[str, list[str]]] = empty_list()
    irradiation_frequency: Optional[Union[float, list[float]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()
    nmr_pulse_sequence: Optional[Union[str, list[str]]] = empty_list()
    nmr_sample_tube: Optional[Union[str, list[str]]] = empty_list()
    number_of_scans: Optional[Union[int, list[int]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.nucleus, list):
            self.nucleus = [self.nucleus] if self.nucleus is not None else []
        self.nucleus = [v if isinstance(v, str) else str(v) for v in self.nucleus]

        if not isinstance(self.solvent, list):
            self.solvent = [self.solvent] if self.solvent is not None else []
        self.solvent = [v if isinstance(v, str) else str(v) for v in self.solvent]

        if not isinstance(self.irradiation_frequency, list):
            self.irradiation_frequency = [self.irradiation_frequency] if self.irradiation_frequency is not None else []
        self.irradiation_frequency = [v if isinstance(v, float) else float(v) for v in self.irradiation_frequency]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.nmr_pulse_sequence, list):
            self.nmr_pulse_sequence = [self.nmr_pulse_sequence] if self.nmr_pulse_sequence is not None else []
        self.nmr_pulse_sequence = [v if isinstance(v, str) else str(v) for v in self.nmr_pulse_sequence]

        if not isinstance(self.nmr_sample_tube, list):
            self.nmr_sample_tube = [self.nmr_sample_tube] if self.nmr_sample_tube is not None else []
        self.nmr_sample_tube = [v if isinstance(v, str) else str(v) for v in self.nmr_sample_tube]

        if not isinstance(self.number_of_scans, list):
            self.number_of_scans = [self.number_of_scans] if self.number_of_scans is not None else []
        self.number_of_scans = [v if isinstance(v, int) else int(v) for v in self.number_of_scans]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TransmissionElectronMicroscopy(CharacterizationTechnique):
    """
    Transmission electron microscopy
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0000078"]
    class_class_curie: ClassVar[str] = "voc4cat:0000078"
    class_name: ClassVar[str] = "TransmissionElectronMicroscopy"
    class_model_uri: ClassVar[URIRef] = CATCORE.TransmissionElectronMicroscopy

    operation_mode: Optional[Union[str, list[str]]] = empty_list()
    gun_type: Optional[Union[str, list[str]]] = empty_list()
    acceleration_voltage: Optional[Union[float, list[float]]] = empty_list()
    magnification_setting: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.operation_mode, list):
            self.operation_mode = [self.operation_mode] if self.operation_mode is not None else []
        self.operation_mode = [v if isinstance(v, str) else str(v) for v in self.operation_mode]

        if not isinstance(self.gun_type, list):
            self.gun_type = [self.gun_type] if self.gun_type is not None else []
        self.gun_type = [v if isinstance(v, str) else str(v) for v in self.gun_type]

        if not isinstance(self.acceleration_voltage, list):
            self.acceleration_voltage = [self.acceleration_voltage] if self.acceleration_voltage is not None else []
        self.acceleration_voltage = [v if isinstance(v, float) else float(v) for v in self.acceleration_voltage]

        if not isinstance(self.magnification_setting, list):
            self.magnification_setting = [self.magnification_setting] if self.magnification_setting is not None else []
        self.magnification_setting = [v if isinstance(v, float) else float(v) for v in self.magnification_setting]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ICPAES(CharacterizationTechnique):
    """
    Inductively-coupled plasma atomic emission spectroscopy
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000267"]
    class_class_curie: ClassVar[str] = "CHMO:0000267"
    class_name: ClassVar[str] = "ICPAES"
    class_model_uri: ClassVar[URIRef] = CATCORE.ICPAES

    element_analyzed: Optional[Union[str, list[str]]] = empty_list()
    calibration_method: Optional[Union[str, list[str]]] = empty_list()
    detection_limit: Optional[Union[float, list[float]]] = empty_list()
    matrix_effect_correction: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.element_analyzed, list):
            self.element_analyzed = [self.element_analyzed] if self.element_analyzed is not None else []
        self.element_analyzed = [v if isinstance(v, str) else str(v) for v in self.element_analyzed]

        if not isinstance(self.calibration_method, list):
            self.calibration_method = [self.calibration_method] if self.calibration_method is not None else []
        self.calibration_method = [v if isinstance(v, str) else str(v) for v in self.calibration_method]

        if not isinstance(self.detection_limit, list):
            self.detection_limit = [self.detection_limit] if self.detection_limit is not None else []
        self.detection_limit = [v if isinstance(v, float) else float(v) for v in self.detection_limit]

        if not isinstance(self.matrix_effect_correction, list):
            self.matrix_effect_correction = [self.matrix_effect_correction] if self.matrix_effect_correction is not None else []
        self.matrix_effect_correction = [v if isinstance(v, str) else str(v) for v in self.matrix_effect_correction]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ScanningElectronMicroscopy(CharacterizationTechnique):
    """
    Scanning electron microscopy
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0000075"]
    class_class_curie: ClassVar[str] = "voc4cat:0000075"
    class_name: ClassVar[str] = "ScanningElectronMicroscopy"
    class_model_uri: ClassVar[URIRef] = CATCORE.ScanningElectronMicroscopy

    gun_type: Optional[Union[str, list[str]]] = empty_list()
    acceleration_voltage: Optional[Union[float, list[float]]] = empty_list()
    image_resolution: Optional[Union[float, list[float]]] = empty_list()
    field_emitter: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.gun_type, list):
            self.gun_type = [self.gun_type] if self.gun_type is not None else []
        self.gun_type = [v if isinstance(v, str) else str(v) for v in self.gun_type]

        if not isinstance(self.acceleration_voltage, list):
            self.acceleration_voltage = [self.acceleration_voltage] if self.acceleration_voltage is not None else []
        self.acceleration_voltage = [v if isinstance(v, float) else float(v) for v in self.acceleration_voltage]

        if not isinstance(self.image_resolution, list):
            self.image_resolution = [self.image_resolution] if self.image_resolution is not None else []
        self.image_resolution = [v if isinstance(v, float) else float(v) for v in self.image_resolution]

        if not isinstance(self.field_emitter, list):
            self.field_emitter = [self.field_emitter] if self.field_emitter is not None else []
        self.field_emitter = [v if isinstance(v, str) else str(v) for v in self.field_emitter]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Thermogravimetry(CharacterizationTechnique):
    """
    Thermogravimetry
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000690"]
    class_class_curie: ClassVar[str] = "CHMO:0000690"
    class_name: ClassVar[str] = "Thermogravimetry"
    class_model_uri: ClassVar[URIRef] = CATCORE.Thermogravimetry

    operation_mode: Optional[Union[str, list[str]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()
    initial_temperature: Optional[Union[float, list[float]]] = empty_list()
    final_temperature: Optional[Union[float, list[float]]] = empty_list()
    heating_rate: Optional[Union[float, list[float]]] = empty_list()
    heating_procedure: Optional[Union[str, list[str]]] = empty_list()
    sample_mass: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.operation_mode, list):
            self.operation_mode = [self.operation_mode] if self.operation_mode is not None else []
        self.operation_mode = [v if isinstance(v, str) else str(v) for v in self.operation_mode]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        if not isinstance(self.initial_temperature, list):
            self.initial_temperature = [self.initial_temperature] if self.initial_temperature is not None else []
        self.initial_temperature = [v if isinstance(v, float) else float(v) for v in self.initial_temperature]

        if not isinstance(self.final_temperature, list):
            self.final_temperature = [self.final_temperature] if self.final_temperature is not None else []
        self.final_temperature = [v if isinstance(v, float) else float(v) for v in self.final_temperature]

        if not isinstance(self.heating_rate, list):
            self.heating_rate = [self.heating_rate] if self.heating_rate is not None else []
        self.heating_rate = [v if isinstance(v, float) else float(v) for v in self.heating_rate]

        if not isinstance(self.heating_procedure, list):
            self.heating_procedure = [self.heating_procedure] if self.heating_procedure is not None else []
        self.heating_procedure = [v if isinstance(v, str) else str(v) for v in self.heating_procedure]

        if not isinstance(self.sample_mass, list):
            self.sample_mass = [self.sample_mass] if self.sample_mass is not None else []
        self.sample_mass = [v if isinstance(v, float) else float(v) for v in self.sample_mass]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class XPS(CharacterizationTechnique):
    """
    X-ray photoelectron spectroscopy
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000404"]
    class_class_curie: ClassVar[str] = "CHMO:0000404"
    class_name: ClassVar[str] = "XPS"
    class_model_uri: ClassVar[URIRef] = CATCORE.XPS

    xray_source: Optional[Union[str, list[str]]] = empty_list()
    total_acquisition_time: Optional[Union[float, list[float]]] = empty_list()
    number_of_scans: Optional[Union[int, list[int]]] = empty_list()
    spot_size: Optional[Union[float, list[float]]] = empty_list()
    lense_mode: Optional[Union[str, list[str]]] = empty_list()
    minimum_energy: Optional[Union[float, list[float]]] = empty_list()
    maximum_energy: Optional[Union[float, list[float]]] = empty_list()
    step_size: Optional[Union[float, list[float]]] = empty_list()
    pass_energy: Optional[Union[float, list[float]]] = empty_list()
    charge_compensation: Optional[Union[str, list[str]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.xray_source, list):
            self.xray_source = [self.xray_source] if self.xray_source is not None else []
        self.xray_source = [v if isinstance(v, str) else str(v) for v in self.xray_source]

        if not isinstance(self.total_acquisition_time, list):
            self.total_acquisition_time = [self.total_acquisition_time] if self.total_acquisition_time is not None else []
        self.total_acquisition_time = [v if isinstance(v, float) else float(v) for v in self.total_acquisition_time]

        if not isinstance(self.number_of_scans, list):
            self.number_of_scans = [self.number_of_scans] if self.number_of_scans is not None else []
        self.number_of_scans = [v if isinstance(v, int) else int(v) for v in self.number_of_scans]

        if not isinstance(self.spot_size, list):
            self.spot_size = [self.spot_size] if self.spot_size is not None else []
        self.spot_size = [v if isinstance(v, float) else float(v) for v in self.spot_size]

        if not isinstance(self.lense_mode, list):
            self.lense_mode = [self.lense_mode] if self.lense_mode is not None else []
        self.lense_mode = [v if isinstance(v, str) else str(v) for v in self.lense_mode]

        if not isinstance(self.minimum_energy, list):
            self.minimum_energy = [self.minimum_energy] if self.minimum_energy is not None else []
        self.minimum_energy = [v if isinstance(v, float) else float(v) for v in self.minimum_energy]

        if not isinstance(self.maximum_energy, list):
            self.maximum_energy = [self.maximum_energy] if self.maximum_energy is not None else []
        self.maximum_energy = [v if isinstance(v, float) else float(v) for v in self.maximum_energy]

        if not isinstance(self.step_size, list):
            self.step_size = [self.step_size] if self.step_size is not None else []
        self.step_size = [v if isinstance(v, float) else float(v) for v in self.step_size]

        if not isinstance(self.pass_energy, list):
            self.pass_energy = [self.pass_energy] if self.pass_energy is not None else []
        self.pass_energy = [v if isinstance(v, float) else float(v) for v in self.pass_energy]

        if not isinstance(self.charge_compensation, list):
            self.charge_compensation = [self.charge_compensation] if self.charge_compensation is not None else []
        self.charge_compensation = [v if isinstance(v, str) else str(v) for v in self.charge_compensation]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BET(CharacterizationTechnique):
    """
    Brunauer-Emmett-Teller surface area analysis
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["BET"]
    class_class_curie: ClassVar[str] = "catcore:BET"
    class_name: ClassVar[str] = "BET"
    class_model_uri: ClassVar[URIRef] = CATCORE.BET

    adsorbate_gas: Optional[Union[str, list[str]]] = empty_list()
    degassing_temperature: Optional[Union[float, list[float]]] = empty_list()
    measurement_temperature: Optional[Union[float, list[float]]] = empty_list()
    pore_size_distribution_method: Optional[Union[str, list[str]]] = empty_list()
    sample_mass: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.adsorbate_gas, list):
            self.adsorbate_gas = [self.adsorbate_gas] if self.adsorbate_gas is not None else []
        self.adsorbate_gas = [v if isinstance(v, str) else str(v) for v in self.adsorbate_gas]

        if not isinstance(self.degassing_temperature, list):
            self.degassing_temperature = [self.degassing_temperature] if self.degassing_temperature is not None else []
        self.degassing_temperature = [v if isinstance(v, float) else float(v) for v in self.degassing_temperature]

        if not isinstance(self.measurement_temperature, list):
            self.measurement_temperature = [self.measurement_temperature] if self.measurement_temperature is not None else []
        self.measurement_temperature = [v if isinstance(v, float) else float(v) for v in self.measurement_temperature]

        if not isinstance(self.pore_size_distribution_method, list):
            self.pore_size_distribution_method = [self.pore_size_distribution_method] if self.pore_size_distribution_method is not None else []
        self.pore_size_distribution_method = [v if isinstance(v, str) else str(v) for v in self.pore_size_distribution_method]

        if not isinstance(self.sample_mass, list):
            self.sample_mass = [self.sample_mass] if self.sample_mass is not None else []
        self.sample_mass = [v if isinstance(v, float) else float(v) for v in self.sample_mass]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElementalAnalysis(CharacterizationTechnique):
    """
    Elemental analysis
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0001075"]
    class_class_curie: ClassVar[str] = "CHMO:0001075"
    class_name: ClassVar[str] = "ElementalAnalysis"
    class_model_uri: ClassVar[URIRef] = CATCORE.ElementalAnalysis

    elements_analyzed: Optional[Union[str, list[str]]] = empty_list()
    combustion_temperature: Optional[Union[float, list[float]]] = empty_list()
    carrier_gas: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.elements_analyzed, list):
            self.elements_analyzed = [self.elements_analyzed] if self.elements_analyzed is not None else []
        self.elements_analyzed = [v if isinstance(v, str) else str(v) for v in self.elements_analyzed]

        if not isinstance(self.combustion_temperature, list):
            self.combustion_temperature = [self.combustion_temperature] if self.combustion_temperature is not None else []
        self.combustion_temperature = [v if isinstance(v, float) else float(v) for v in self.combustion_temperature]

        if not isinstance(self.carrier_gas, list):
            self.carrier_gas = [self.carrier_gas] if self.carrier_gas is not None else []
        self.carrier_gas = [v if isinstance(v, str) else str(v) for v in self.carrier_gas]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UVVisSpectroscopy(CharacterizationTechnique):
    """
    Ultraviolet-visible spectroscopy
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0000079"]
    class_class_curie: ClassVar[str] = "voc4cat:0000079"
    class_name: ClassVar[str] = "UVVisSpectroscopy"
    class_model_uri: ClassVar[URIRef] = CATCORE.UVVisSpectroscopy

    minimum_wavelength: Optional[Union[float, list[float]]] = empty_list()
    maximum_wavelength: Optional[Union[float, list[float]]] = empty_list()
    path_length: Optional[Union[float, list[float]]] = empty_list()
    solvent: Optional[Union[str, list[str]]] = empty_list()
    concentration: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.minimum_wavelength, list):
            self.minimum_wavelength = [self.minimum_wavelength] if self.minimum_wavelength is not None else []
        self.minimum_wavelength = [v if isinstance(v, float) else float(v) for v in self.minimum_wavelength]

        if not isinstance(self.maximum_wavelength, list):
            self.maximum_wavelength = [self.maximum_wavelength] if self.maximum_wavelength is not None else []
        self.maximum_wavelength = [v if isinstance(v, float) else float(v) for v in self.maximum_wavelength]

        if not isinstance(self.path_length, list):
            self.path_length = [self.path_length] if self.path_length is not None else []
        self.path_length = [v if isinstance(v, float) else float(v) for v in self.path_length]

        if not isinstance(self.solvent, list):
            self.solvent = [self.solvent] if self.solvent is not None else []
        self.solvent = [v if isinstance(v, str) else str(v) for v in self.solvent]

        if not isinstance(self.concentration, list):
            self.concentration = [self.concentration] if self.concentration is not None else []
        self.concentration = [v if isinstance(v, float) else float(v) for v in self.concentration]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DRIFTS(CharacterizationTechnique):
    """
    Diffuse reflectance infrared Fourier transform spectroscopy
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000645"]
    class_class_curie: ClassVar[str] = "CHMO:0000645"
    class_name: ClassVar[str] = "DRIFTS"
    class_model_uri: ClassVar[URIRef] = CATCORE.DRIFTS

    adsorption_gas: Optional[Union[str, list[str]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()
    flow_rate: Optional[Union[float, list[float]]] = empty_list()
    diluting_reference: Optional[Union[str, list[str]]] = empty_list()
    ratio_reference_sample: Optional[Union[float, list[float]]] = empty_list()
    step_size: Optional[Union[float, list[float]]] = empty_list()
    resolution: Optional[Union[float, list[float]]] = empty_list()
    background_correction_method: Optional[Union[str, list[str]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()
    number_of_scans: Optional[Union[int, list[int]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.adsorption_gas, list):
            self.adsorption_gas = [self.adsorption_gas] if self.adsorption_gas is not None else []
        self.adsorption_gas = [v if isinstance(v, str) else str(v) for v in self.adsorption_gas]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        if not isinstance(self.flow_rate, list):
            self.flow_rate = [self.flow_rate] if self.flow_rate is not None else []
        self.flow_rate = [v if isinstance(v, float) else float(v) for v in self.flow_rate]

        if not isinstance(self.diluting_reference, list):
            self.diluting_reference = [self.diluting_reference] if self.diluting_reference is not None else []
        self.diluting_reference = [v if isinstance(v, str) else str(v) for v in self.diluting_reference]

        if not isinstance(self.ratio_reference_sample, list):
            self.ratio_reference_sample = [self.ratio_reference_sample] if self.ratio_reference_sample is not None else []
        self.ratio_reference_sample = [v if isinstance(v, float) else float(v) for v in self.ratio_reference_sample]

        if not isinstance(self.step_size, list):
            self.step_size = [self.step_size] if self.step_size is not None else []
        self.step_size = [v if isinstance(v, float) else float(v) for v in self.step_size]

        if not isinstance(self.resolution, list):
            self.resolution = [self.resolution] if self.resolution is not None else []
        self.resolution = [v if isinstance(v, float) else float(v) for v in self.resolution]

        if not isinstance(self.background_correction_method, list):
            self.background_correction_method = [self.background_correction_method] if self.background_correction_method is not None else []
        self.background_correction_method = [v if isinstance(v, str) else str(v) for v in self.background_correction_method]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.number_of_scans, list):
            self.number_of_scans = [self.number_of_scans] if self.number_of_scans is not None else []
        self.number_of_scans = [v if isinstance(v, int) else int(v) for v in self.number_of_scans]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CyclicVoltammetry(CharacterizationTechnique):
    """
    Cyclic voltammetry
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000025"]
    class_class_curie: ClassVar[str] = "CHMO:0000025"
    class_name: ClassVar[str] = "CyclicVoltammetry"
    class_model_uri: ClassVar[URIRef] = CATCORE.CyclicVoltammetry

    scan_rate: Optional[Union[float, list[float]]] = empty_list()
    minimum_potential: Optional[Union[float, list[float]]] = empty_list()
    maximum_potential: Optional[Union[float, list[float]]] = empty_list()
    step_size_potential: Optional[Union[float, list[float]]] = empty_list()
    electrolyte_composition: Optional[Union[str, list[str]]] = empty_list()
    electrolyte_concentration: Optional[Union[float, list[float]]] = empty_list()
    reference_electrode: Optional[Union[str, list[str]]] = empty_list()
    number_of_cycles: Optional[Union[int, list[int]]] = empty_list()
    working_electrode: Optional[Union[str, list[str]]] = empty_list()
    counter_electrode: Optional[Union[str, list[str]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.scan_rate, list):
            self.scan_rate = [self.scan_rate] if self.scan_rate is not None else []
        self.scan_rate = [v if isinstance(v, float) else float(v) for v in self.scan_rate]

        if not isinstance(self.minimum_potential, list):
            self.minimum_potential = [self.minimum_potential] if self.minimum_potential is not None else []
        self.minimum_potential = [v if isinstance(v, float) else float(v) for v in self.minimum_potential]

        if not isinstance(self.maximum_potential, list):
            self.maximum_potential = [self.maximum_potential] if self.maximum_potential is not None else []
        self.maximum_potential = [v if isinstance(v, float) else float(v) for v in self.maximum_potential]

        if not isinstance(self.step_size_potential, list):
            self.step_size_potential = [self.step_size_potential] if self.step_size_potential is not None else []
        self.step_size_potential = [v if isinstance(v, float) else float(v) for v in self.step_size_potential]

        if not isinstance(self.electrolyte_composition, list):
            self.electrolyte_composition = [self.electrolyte_composition] if self.electrolyte_composition is not None else []
        self.electrolyte_composition = [v if isinstance(v, str) else str(v) for v in self.electrolyte_composition]

        if not isinstance(self.electrolyte_concentration, list):
            self.electrolyte_concentration = [self.electrolyte_concentration] if self.electrolyte_concentration is not None else []
        self.electrolyte_concentration = [v if isinstance(v, float) else float(v) for v in self.electrolyte_concentration]

        if not isinstance(self.reference_electrode, list):
            self.reference_electrode = [self.reference_electrode] if self.reference_electrode is not None else []
        self.reference_electrode = [v if isinstance(v, str) else str(v) for v in self.reference_electrode]

        if not isinstance(self.number_of_cycles, list):
            self.number_of_cycles = [self.number_of_cycles] if self.number_of_cycles is not None else []
        self.number_of_cycles = [v if isinstance(v, int) else int(v) for v in self.number_of_cycles]

        if not isinstance(self.working_electrode, list):
            self.working_electrode = [self.working_electrode] if self.working_electrode is not None else []
        self.working_electrode = [v if isinstance(v, str) else str(v) for v in self.working_electrode]

        if not isinstance(self.counter_electrode, list):
            self.counter_electrode = [self.counter_electrode] if self.counter_electrode is not None else []
        self.counter_electrode = [v if isinstance(v, str) else str(v) for v in self.counter_electrode]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DynamicLightScattering(CharacterizationTechnique):
    """
    Dynamic light scattering
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000167"]
    class_class_curie: ClassVar[str] = "CHMO:0000167"
    class_name: ClassVar[str] = "DynamicLightScattering"
    class_model_uri: ClassVar[URIRef] = CATCORE.DynamicLightScattering

    solvent: Optional[Union[str, list[str]]] = empty_list()
    concentration: Optional[Union[float, list[float]]] = empty_list()
    light_wavelength: Optional[Union[float, list[float]]] = empty_list()
    scattering_angle: Optional[Union[float, list[float]]] = empty_list()
    refractive_index: Optional[Union[float, list[float]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()
    dispersant: Optional[Union[str, list[str]]] = empty_list()
    measurement_duration: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.solvent, list):
            self.solvent = [self.solvent] if self.solvent is not None else []
        self.solvent = [v if isinstance(v, str) else str(v) for v in self.solvent]

        if not isinstance(self.concentration, list):
            self.concentration = [self.concentration] if self.concentration is not None else []
        self.concentration = [v if isinstance(v, float) else float(v) for v in self.concentration]

        if not isinstance(self.light_wavelength, list):
            self.light_wavelength = [self.light_wavelength] if self.light_wavelength is not None else []
        self.light_wavelength = [v if isinstance(v, float) else float(v) for v in self.light_wavelength]

        if not isinstance(self.scattering_angle, list):
            self.scattering_angle = [self.scattering_angle] if self.scattering_angle is not None else []
        self.scattering_angle = [v if isinstance(v, float) else float(v) for v in self.scattering_angle]

        if not isinstance(self.refractive_index, list):
            self.refractive_index = [self.refractive_index] if self.refractive_index is not None else []
        self.refractive_index = [v if isinstance(v, float) else float(v) for v in self.refractive_index]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.dispersant, list):
            self.dispersant = [self.dispersant] if self.dispersant is not None else []
        self.dispersant = [v if isinstance(v, str) else str(v) for v in self.dispersant]

        if not isinstance(self.measurement_duration, list):
            self.measurement_duration = [self.measurement_duration] if self.measurement_duration is not None else []
        self.measurement_duration = [v if isinstance(v, float) else float(v) for v in self.measurement_duration]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ESIMS(CharacterizationTechnique):
    """
    Electrospray ionisation mass spectrometry
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000482"]
    class_class_curie: ClassVar[str] = "CHMO:0000482"
    class_name: ClassVar[str] = "ESI_MS"
    class_model_uri: ClassVar[URIRef] = CATCORE.ESIMS

    operation_mode: Optional[Union[str, list[str]]] = empty_list()
    mz_minimum: Optional[Union[float, list[float]]] = empty_list()
    mz_maximum: Optional[Union[float, list[float]]] = empty_list()
    spray_voltage: Optional[Union[float, list[float]]] = empty_list()
    capillary_temperature: Optional[Union[float, list[float]]] = empty_list()
    solvent_composition: Optional[Union[str, list[str]]] = empty_list()
    flow_rate: Optional[Union[float, list[float]]] = empty_list()
    carrier_gas: Optional[Union[str, list[str]]] = empty_list()
    concentration: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.operation_mode, list):
            self.operation_mode = [self.operation_mode] if self.operation_mode is not None else []
        self.operation_mode = [v if isinstance(v, str) else str(v) for v in self.operation_mode]

        if not isinstance(self.mz_minimum, list):
            self.mz_minimum = [self.mz_minimum] if self.mz_minimum is not None else []
        self.mz_minimum = [v if isinstance(v, float) else float(v) for v in self.mz_minimum]

        if not isinstance(self.mz_maximum, list):
            self.mz_maximum = [self.mz_maximum] if self.mz_maximum is not None else []
        self.mz_maximum = [v if isinstance(v, float) else float(v) for v in self.mz_maximum]

        if not isinstance(self.spray_voltage, list):
            self.spray_voltage = [self.spray_voltage] if self.spray_voltage is not None else []
        self.spray_voltage = [v if isinstance(v, float) else float(v) for v in self.spray_voltage]

        if not isinstance(self.capillary_temperature, list):
            self.capillary_temperature = [self.capillary_temperature] if self.capillary_temperature is not None else []
        self.capillary_temperature = [v if isinstance(v, float) else float(v) for v in self.capillary_temperature]

        if not isinstance(self.solvent_composition, list):
            self.solvent_composition = [self.solvent_composition] if self.solvent_composition is not None else []
        self.solvent_composition = [v if isinstance(v, str) else str(v) for v in self.solvent_composition]

        if not isinstance(self.flow_rate, list):
            self.flow_rate = [self.flow_rate] if self.flow_rate is not None else []
        self.flow_rate = [v if isinstance(v, float) else float(v) for v in self.flow_rate]

        if not isinstance(self.carrier_gas, list):
            self.carrier_gas = [self.carrier_gas] if self.carrier_gas is not None else []
        self.carrier_gas = [v if isinstance(v, str) else str(v) for v in self.carrier_gas]

        if not isinstance(self.concentration, list):
            self.concentration = [self.concentration] if self.concentration is not None else []
        self.concentration = [v if isinstance(v, float) else float(v) for v in self.concentration]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhotoluminescenceSpectroscopy(CharacterizationTechnique):
    """
    Photoluminescence spectroscopy
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["PhotoluminescenceSpectroscopy"]
    class_class_curie: ClassVar[str] = "catcore:PhotoluminescenceSpectroscopy"
    class_name: ClassVar[str] = "PhotoluminescenceSpectroscopy"
    class_model_uri: ClassVar[URIRef] = CATCORE.PhotoluminescenceSpectroscopy

    excitation_wavelength: Optional[Union[float, list[float]]] = empty_list()
    emission_wavelength: Optional[Union[float, list[float]]] = empty_list()
    optical_filter: Optional[Union[str, list[str]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()
    emission_range: Optional[Union[str, list[str]]] = empty_list()
    slit_width: Optional[Union[float, list[float]]] = empty_list()
    step_size: Optional[Union[float, list[float]]] = empty_list()
    integration_time: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.excitation_wavelength, list):
            self.excitation_wavelength = [self.excitation_wavelength] if self.excitation_wavelength is not None else []
        self.excitation_wavelength = [v if isinstance(v, float) else float(v) for v in self.excitation_wavelength]

        if not isinstance(self.emission_wavelength, list):
            self.emission_wavelength = [self.emission_wavelength] if self.emission_wavelength is not None else []
        self.emission_wavelength = [v if isinstance(v, float) else float(v) for v in self.emission_wavelength]

        if not isinstance(self.optical_filter, list):
            self.optical_filter = [self.optical_filter] if self.optical_filter is not None else []
        self.optical_filter = [v if isinstance(v, str) else str(v) for v in self.optical_filter]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.emission_range, list):
            self.emission_range = [self.emission_range] if self.emission_range is not None else []
        self.emission_range = [v if isinstance(v, str) else str(v) for v in self.emission_range]

        if not isinstance(self.slit_width, list):
            self.slit_width = [self.slit_width] if self.slit_width is not None else []
        self.slit_width = [v if isinstance(v, float) else float(v) for v in self.slit_width]

        if not isinstance(self.step_size, list):
            self.step_size = [self.step_size] if self.step_size is not None else []
        self.step_size = [v if isinstance(v, float) else float(v) for v in self.step_size]

        if not isinstance(self.integration_time, list):
            self.integration_time = [self.integration_time] if self.integration_time is not None else []
        self.integration_time = [v if isinstance(v, float) else float(v) for v in self.integration_time]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhotoluminescenceLifetime(CharacterizationTechnique):
    """
    Photoluminescence lifetime measurement
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["PhotoluminescenceLifetime"]
    class_class_curie: ClassVar[str] = "catcore:PhotoluminescenceLifetime"
    class_name: ClassVar[str] = "PhotoluminescenceLifetime"
    class_model_uri: ClassVar[URIRef] = CATCORE.PhotoluminescenceLifetime

    excitation_wavelength: Optional[Union[float, list[float]]] = empty_list()
    emission_wavelength: Optional[Union[float, list[float]]] = empty_list()
    optical_filter: Optional[Union[str, list[str]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()
    lifetime_fitting_model: Optional[Union[str, list[str]]] = empty_list()
    number_of_shots: Optional[Union[int, list[int]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.excitation_wavelength, list):
            self.excitation_wavelength = [self.excitation_wavelength] if self.excitation_wavelength is not None else []
        self.excitation_wavelength = [v if isinstance(v, float) else float(v) for v in self.excitation_wavelength]

        if not isinstance(self.emission_wavelength, list):
            self.emission_wavelength = [self.emission_wavelength] if self.emission_wavelength is not None else []
        self.emission_wavelength = [v if isinstance(v, float) else float(v) for v in self.emission_wavelength]

        if not isinstance(self.optical_filter, list):
            self.optical_filter = [self.optical_filter] if self.optical_filter is not None else []
        self.optical_filter = [v if isinstance(v, str) else str(v) for v in self.optical_filter]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.lifetime_fitting_model, list):
            self.lifetime_fitting_model = [self.lifetime_fitting_model] if self.lifetime_fitting_model is not None else []
        self.lifetime_fitting_model = [v if isinstance(v, str) else str(v) for v in self.lifetime_fitting_model]

        if not isinstance(self.number_of_shots, list):
            self.number_of_shots = [self.number_of_shots] if self.number_of_shots is not None else []
        self.number_of_shots = [v if isinstance(v, int) else int(v) for v in self.number_of_shots]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SizeExclusionChromatography(CharacterizationTechnique):
    """
    Size-exclusion chromatography
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AFP["0000843"]
    class_class_curie: ClassVar[str] = "AFP:0000843"
    class_name: ClassVar[str] = "SizeExclusionChromatography"
    class_model_uri: ClassVar[URIRef] = CATCORE.SizeExclusionChromatography

    column_type: Optional[Union[str, list[str]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()
    eluent: Optional[Union[str, list[str]]] = empty_list()
    flow_rate: Optional[Union[float, list[float]]] = empty_list()
    calibration_standard: Optional[Union[str, list[str]]] = empty_list()
    injection_volume: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.column_type, list):
            self.column_type = [self.column_type] if self.column_type is not None else []
        self.column_type = [v if isinstance(v, str) else str(v) for v in self.column_type]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.eluent, list):
            self.eluent = [self.eluent] if self.eluent is not None else []
        self.eluent = [v if isinstance(v, str) else str(v) for v in self.eluent]

        if not isinstance(self.flow_rate, list):
            self.flow_rate = [self.flow_rate] if self.flow_rate is not None else []
        self.flow_rate = [v if isinstance(v, float) else float(v) for v in self.flow_rate]

        if not isinstance(self.calibration_standard, list):
            self.calibration_standard = [self.calibration_standard] if self.calibration_standard is not None else []
        self.calibration_standard = [v if isinstance(v, str) else str(v) for v in self.calibration_standard]

        if not isinstance(self.injection_volume, list):
            self.injection_volume = [self.injection_volume] if self.injection_volume is not None else []
        self.injection_volume = [v if isinstance(v, float) else float(v) for v in self.injection_volume]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HPLCMS(CharacterizationTechnique):
    """
    High-performance liquid chromatography mass spectrometry
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000796"]
    class_class_curie: ClassVar[str] = "CHMO:0000796"
    class_name: ClassVar[str] = "HPLC_MS"
    class_model_uri: ClassVar[URIRef] = CATCORE.HPLCMS

    column_type: Optional[Union[str, list[str]]] = empty_list()
    eluent: Optional[Union[str, list[str]]] = empty_list()
    gradient_program: Optional[Union[str, list[str]]] = empty_list()
    ionization_mode: Optional[Union[str, list[str]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()
    flow_rate: Optional[Union[float, list[float]]] = empty_list()
    injection_volume: Optional[Union[float, list[float]]] = empty_list()
    external_standard: Optional[Union[str, list[str]]] = empty_list()
    internal_standard: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.column_type, list):
            self.column_type = [self.column_type] if self.column_type is not None else []
        self.column_type = [v if isinstance(v, str) else str(v) for v in self.column_type]

        if not isinstance(self.eluent, list):
            self.eluent = [self.eluent] if self.eluent is not None else []
        self.eluent = [v if isinstance(v, str) else str(v) for v in self.eluent]

        if not isinstance(self.gradient_program, list):
            self.gradient_program = [self.gradient_program] if self.gradient_program is not None else []
        self.gradient_program = [v if isinstance(v, str) else str(v) for v in self.gradient_program]

        if not isinstance(self.ionization_mode, list):
            self.ionization_mode = [self.ionization_mode] if self.ionization_mode is not None else []
        self.ionization_mode = [v if isinstance(v, str) else str(v) for v in self.ionization_mode]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.flow_rate, list):
            self.flow_rate = [self.flow_rate] if self.flow_rate is not None else []
        self.flow_rate = [v if isinstance(v, float) else float(v) for v in self.flow_rate]

        if not isinstance(self.injection_volume, list):
            self.injection_volume = [self.injection_volume] if self.injection_volume is not None else []
        self.injection_volume = [v if isinstance(v, float) else float(v) for v in self.injection_volume]

        if not isinstance(self.external_standard, list):
            self.external_standard = [self.external_standard] if self.external_standard is not None else []
        self.external_standard = [v if isinstance(v, str) else str(v) for v in self.external_standard]

        if not isinstance(self.internal_standard, list):
            self.internal_standard = [self.internal_standard] if self.internal_standard is not None else []
        self.internal_standard = [v if isinstance(v, str) else str(v) for v in self.internal_standard]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SingleCrystalXRD(CharacterizationTechnique):
    """
    Single crystal X-ray diffraction
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000852"]
    class_class_curie: ClassVar[str] = "CHMO:0000852"
    class_name: ClassVar[str] = "SingleCrystalXRD"
    class_model_uri: ClassVar[URIRef] = CATCORE.SingleCrystalXRD

    xray_source: Optional[Union[str, list[str]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.xray_source, list):
            self.xray_source = [self.xray_source] if self.xray_source is not None else []
        self.xray_source = [v if isinstance(v, str) else str(v) for v in self.xray_source]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EDX(CharacterizationTechnique):
    """
    Energy-dispersive X-ray emission spectroscopy
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0000309"]
    class_class_curie: ClassVar[str] = "CHMO:0000309"
    class_name: ClassVar[str] = "EDX"
    class_model_uri: ClassVar[URIRef] = CATCORE.EDX

    primary_energy: Optional[Union[float, list[float]]] = empty_list()
    counting_time: Optional[Union[float, list[float]]] = empty_list()
    resolution: Optional[Union[float, list[float]]] = empty_list()
    calibration_method: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.primary_energy, list):
            self.primary_energy = [self.primary_energy] if self.primary_energy is not None else []
        self.primary_energy = [v if isinstance(v, float) else float(v) for v in self.primary_energy]

        if not isinstance(self.counting_time, list):
            self.counting_time = [self.counting_time] if self.counting_time is not None else []
        self.counting_time = [v if isinstance(v, float) else float(v) for v in self.counting_time]

        if not isinstance(self.resolution, list):
            self.resolution = [self.resolution] if self.resolution is not None else []
        self.resolution = [v if isinstance(v, float) else float(v) for v in self.resolution]

        if not isinstance(self.calibration_method, list):
            self.calibration_method = [self.calibration_method] if self.calibration_method is not None else []
        self.calibration_method = [v if isinstance(v, str) else str(v) for v in self.calibration_method]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TPO(CharacterizationTechnique):
    """
    Temperature-programmed oxidation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0002907"]
    class_class_curie: ClassVar[str] = "CHMO:0002907"
    class_name: ClassVar[str] = "TPO"
    class_model_uri: ClassVar[URIRef] = CATCORE.TPO

    oxidizing_gas_composition: Optional[Union[str, list[str]]] = empty_list()
    heating_rate: Optional[Union[float, list[float]]] = empty_list()
    minimum_temperature: Optional[Union[float, list[float]]] = empty_list()
    maximum_temperature: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.oxidizing_gas_composition, list):
            self.oxidizing_gas_composition = [self.oxidizing_gas_composition] if self.oxidizing_gas_composition is not None else []
        self.oxidizing_gas_composition = [v if isinstance(v, str) else str(v) for v in self.oxidizing_gas_composition]

        if not isinstance(self.heating_rate, list):
            self.heating_rate = [self.heating_rate] if self.heating_rate is not None else []
        self.heating_rate = [v if isinstance(v, float) else float(v) for v in self.heating_rate]

        if not isinstance(self.minimum_temperature, list):
            self.minimum_temperature = [self.minimum_temperature] if self.minimum_temperature is not None else []
        self.minimum_temperature = [v if isinstance(v, float) else float(v) for v in self.minimum_temperature]

        if not isinstance(self.maximum_temperature, list):
            self.maximum_temperature = [self.maximum_temperature] if self.maximum_temperature is not None else []
        self.maximum_temperature = [v if isinstance(v, float) else float(v) for v in self.maximum_temperature]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TPR(CharacterizationTechnique):
    """
    Temperature-programmed reduction
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0002908"]
    class_class_curie: ClassVar[str] = "CHMO:0002908"
    class_name: ClassVar[str] = "TPR"
    class_model_uri: ClassVar[URIRef] = CATCORE.TPR

    reducing_gas_composition: Optional[Union[str, list[str]]] = empty_list()
    heating_rate: Optional[Union[float, list[float]]] = empty_list()
    minimum_temperature: Optional[Union[float, list[float]]] = empty_list()
    maximum_temperature: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.reducing_gas_composition, list):
            self.reducing_gas_composition = [self.reducing_gas_composition] if self.reducing_gas_composition is not None else []
        self.reducing_gas_composition = [v if isinstance(v, str) else str(v) for v in self.reducing_gas_composition]

        if not isinstance(self.heating_rate, list):
            self.heating_rate = [self.heating_rate] if self.heating_rate is not None else []
        self.heating_rate = [v if isinstance(v, float) else float(v) for v in self.heating_rate]

        if not isinstance(self.minimum_temperature, list):
            self.minimum_temperature = [self.minimum_temperature] if self.minimum_temperature is not None else []
        self.minimum_temperature = [v if isinstance(v, float) else float(v) for v in self.minimum_temperature]

        if not isinstance(self.maximum_temperature, list):
            self.maximum_temperature = [self.maximum_temperature] if self.maximum_temperature is not None else []
        self.maximum_temperature = [v if isinstance(v, float) else float(v) for v in self.maximum_temperature]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConductivityMeasurement(CharacterizationTechnique):
    """
    Conductivity measurement
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["ConductivityMeasurement"]
    class_class_curie: ClassVar[str] = "catcore:ConductivityMeasurement"
    class_name: ClassVar[str] = "ConductivityMeasurement"
    class_model_uri: ClassVar[URIRef] = CATCORE.ConductivityMeasurement

    temperature: Optional[Union[float, list[float]]] = empty_list()
    electrode_configuration: Optional[Union[str, list[str]]] = empty_list()
    frequency: Optional[Union[float, list[float]]] = empty_list()
    ac_dc_mode: Optional[Union[str, list[str]]] = empty_list()
    sample_geometry: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.electrode_configuration, list):
            self.electrode_configuration = [self.electrode_configuration] if self.electrode_configuration is not None else []
        self.electrode_configuration = [v if isinstance(v, str) else str(v) for v in self.electrode_configuration]

        if not isinstance(self.frequency, list):
            self.frequency = [self.frequency] if self.frequency is not None else []
        self.frequency = [v if isinstance(v, float) else float(v) for v in self.frequency]

        if not isinstance(self.ac_dc_mode, list):
            self.ac_dc_mode = [self.ac_dc_mode] if self.ac_dc_mode is not None else []
        self.ac_dc_mode = [v if isinstance(v, str) else str(v) for v in self.ac_dc_mode]

        if not isinstance(self.sample_geometry, list):
            self.sample_geometry = [self.sample_geometry] if self.sample_geometry is not None else []
        self.sample_geometry = [v if isinstance(v, str) else str(v) for v in self.sample_geometry]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Reaction(CatCoreEntity):
    """
    The data class 'Reaction' describes the minimum information which should be reported
    with research data concerning the reaction for which the catalyst is applied.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["Reaction"]
    class_class_curie: ClassVar[str] = "catcore:Reaction"
    class_name: ClassVar[str] = "Reaction"
    class_model_uri: ClassVar[URIRef] = CATCORE.Reaction

    catalyst_quantity: Union[float, list[float]] = None
    reactor_design_type: Union[Union[dict, "ReactorDesignType"], list[Union[dict, "ReactorDesignType"]]] = None
    reactant: Union[str, list[str]] = None
    operation_parameters: Union[Union[dict, "OperationParameters"], list[Union[dict, "OperationParameters"]]] = None
    product_identification_method: Union[Union[dict, "ProductIdentificationMethod"], list[Union[dict, "ProductIdentificationMethod"]]] = None
    catalyst_type: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.catalyst_quantity):
            self.MissingRequiredField("catalyst_quantity")
        if not isinstance(self.catalyst_quantity, list):
            self.catalyst_quantity = [self.catalyst_quantity] if self.catalyst_quantity is not None else []
        self.catalyst_quantity = [v if isinstance(v, float) else float(v) for v in self.catalyst_quantity]

        if self._is_empty(self.reactor_design_type):
            self.MissingRequiredField("reactor_design_type")
        if not isinstance(self.reactor_design_type, list):
            self.reactor_design_type = [self.reactor_design_type] if self.reactor_design_type is not None else []
        self.reactor_design_type = [v if isinstance(v, ReactorDesignType) else ReactorDesignType(**as_dict(v)) for v in self.reactor_design_type]

        if self._is_empty(self.reactant):
            self.MissingRequiredField("reactant")
        if not isinstance(self.reactant, list):
            self.reactant = [self.reactant] if self.reactant is not None else []
        self.reactant = [v if isinstance(v, str) else str(v) for v in self.reactant]

        if self._is_empty(self.operation_parameters):
            self.MissingRequiredField("operation_parameters")
        if not isinstance(self.operation_parameters, list):
            self.operation_parameters = [self.operation_parameters] if self.operation_parameters is not None else []
        self.operation_parameters = [v if isinstance(v, OperationParameters) else OperationParameters(**as_dict(v)) for v in self.operation_parameters]

        if self._is_empty(self.product_identification_method):
            self.MissingRequiredField("product_identification_method")
        if not isinstance(self.product_identification_method, list):
            self.product_identification_method = [self.product_identification_method] if self.product_identification_method is not None else []
        self.product_identification_method = [v if isinstance(v, ProductIdentificationMethod) else ProductIdentificationMethod(**as_dict(v)) for v in self.product_identification_method]

        if not isinstance(self.catalyst_type, list):
            self.catalyst_type = [self.catalyst_type] if self.catalyst_type is not None else []
        self.catalyst_type = [v if isinstance(v, str) else str(v) for v in self.catalyst_type]

        super().__post_init__(**kwargs)


class ReactorDesignType(CatCoreEntity):
    """
    Type of reactor design used
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["ReactorDesignType"]
    class_class_curie: ClassVar[str] = "catcore:ReactorDesignType"
    class_name: ClassVar[str] = "ReactorDesignType"
    class_model_uri: ClassVar[URIRef] = CATCORE.ReactorDesignType


class ElectrochemicalReactor(ReactorDesignType):
    """
    Electrochemical reactor
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0000193"]
    class_class_curie: ClassVar[str] = "voc4cat:0000193"
    class_name: ClassVar[str] = "ElectrochemicalReactor"
    class_model_uri: ClassVar[URIRef] = CATCORE.ElectrochemicalReactor


class CSTR(ReactorDesignType):
    """
    Continuous stirred tank reactor
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0007019"]
    class_class_curie: ClassVar[str] = "voc4cat:0007019"
    class_name: ClassVar[str] = "CSTR"
    class_model_uri: ClassVar[URIRef] = CATCORE.CSTR


class PlugFlowReactor(ReactorDesignType):
    """
    Plug flow reactor model
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0007102"]
    class_class_curie: ClassVar[str] = "voc4cat:0007102"
    class_name: ClassVar[str] = "PlugFlowReactor"
    class_model_uri: ClassVar[URIRef] = CATCORE.PlugFlowReactor


class Autoclave(ReactorDesignType):
    """
    Autoclave reactor
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NCIT["C93052"]
    class_class_curie: ClassVar[str] = "NCIT:C93052"
    class_name: ClassVar[str] = "Autoclave"
    class_model_uri: ClassVar[URIRef] = CATCORE.Autoclave


class SlurryReactor(ReactorDesignType):
    """
    Slurry reactor
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["SlurryReactor"]
    class_class_curie: ClassVar[str] = "catcore:SlurryReactor"
    class_name: ClassVar[str] = "SlurryReactor"
    class_model_uri: ClassVar[URIRef] = CATCORE.SlurryReactor


class Microreactor(ReactorDesignType):
    """
    Microreactor
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0000234"]
    class_class_curie: ClassVar[str] = "voc4cat:0000234"
    class_name: ClassVar[str] = "Microreactor"
    class_model_uri: ClassVar[URIRef] = CATCORE.Microreactor


class FixedBedReactor(ReactorDesignType):
    """
    Fixed bed reactor
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["FixedBedReactor"]
    class_class_curie: ClassVar[str] = "catcore:FixedBedReactor"
    class_name: ClassVar[str] = "FixedBedReactor"
    class_model_uri: ClassVar[URIRef] = CATCORE.FixedBedReactor


@dataclass(repr=False)
class FluidizedBedReactor(ReactorDesignType):
    """
    Fluidized bed reactor
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["FluidizedBedReactor"]
    class_class_curie: ClassVar[str] = "catcore:FluidizedBedReactor"
    class_name: ClassVar[str] = "FluidizedBedReactor"
    class_model_uri: ClassVar[URIRef] = CATCORE.FluidizedBedReactor

    gas_distributor_type: Optional[Union[str, list[str]]] = empty_list()
    bed_expansion_height: Optional[Union[float, list[float]]] = empty_list()
    bubble_size_distribution: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.gas_distributor_type, list):
            self.gas_distributor_type = [self.gas_distributor_type] if self.gas_distributor_type is not None else []
        self.gas_distributor_type = [v if isinstance(v, str) else str(v) for v in self.gas_distributor_type]

        if not isinstance(self.bed_expansion_height, list):
            self.bed_expansion_height = [self.bed_expansion_height] if self.bed_expansion_height is not None else []
        self.bed_expansion_height = [v if isinstance(v, float) else float(v) for v in self.bed_expansion_height]

        if self.bubble_size_distribution is not None and not isinstance(self.bubble_size_distribution, str):
            self.bubble_size_distribution = str(self.bubble_size_distribution)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OperationParameters(CatCoreEntity):
    """
    Operation parameters for the reaction
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["OperationParameters"]
    class_class_curie: ClassVar[str] = "catcore:OperationParameters"
    class_name: ClassVar[str] = "OperationParameters"
    class_model_uri: ClassVar[URIRef] = CATCORE.OperationParameters

    reactor_temperature_range: Optional[Union[str, list[str]]] = empty_list()
    atmosphere: Optional[Union[str, list[str]]] = empty_list()
    experiment_pressure: Optional[Union[float, list[float]]] = empty_list()
    feed_composition_range: Optional[Union[str, list[str]]] = empty_list()
    experiment_duration: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.reactor_temperature_range, list):
            self.reactor_temperature_range = [self.reactor_temperature_range] if self.reactor_temperature_range is not None else []
        self.reactor_temperature_range = [v if isinstance(v, str) else str(v) for v in self.reactor_temperature_range]

        if not isinstance(self.atmosphere, list):
            self.atmosphere = [self.atmosphere] if self.atmosphere is not None else []
        self.atmosphere = [v if isinstance(v, str) else str(v) for v in self.atmosphere]

        if not isinstance(self.experiment_pressure, list):
            self.experiment_pressure = [self.experiment_pressure] if self.experiment_pressure is not None else []
        self.experiment_pressure = [v if isinstance(v, float) else float(v) for v in self.experiment_pressure]

        if not isinstance(self.feed_composition_range, list):
            self.feed_composition_range = [self.feed_composition_range] if self.feed_composition_range is not None else []
        self.feed_composition_range = [v if isinstance(v, str) else str(v) for v in self.feed_composition_range]

        if not isinstance(self.experiment_duration, list):
            self.experiment_duration = [self.experiment_duration] if self.experiment_duration is not None else []
        self.experiment_duration = [v if isinstance(v, float) else float(v) for v in self.experiment_duration]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProductIdentificationMethod(CatCoreEntity):
    """
    Method used for product identification
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["ProductIdentificationMethod"]
    class_class_curie: ClassVar[str] = "catcore:ProductIdentificationMethod"
    class_name: ClassVar[str] = "ProductIdentificationMethod"
    class_model_uri: ClassVar[URIRef] = CATCORE.ProductIdentificationMethod

    equipment: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.equipment, list):
            self.equipment = [self.equipment] if self.equipment is not None else []
        self.equipment = [v if isinstance(v, str) else str(v) for v in self.equipment]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Simulation(CatCoreEntity):
    """
    The data class 'Simulation' describes the minimum information which should be reported
    with research data for conducting simulations in the field of catalysis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["Simulation"]
    class_class_curie: ClassVar[str] = "catcore:Simulation"
    class_name: ClassVar[str] = "Simulation"
    class_model_uri: ClassVar[URIRef] = CATCORE.Simulation

    software_package: Union[str, list[str]] = None
    simulation_method: Union[Union[dict, "SimulationMethod"], list[Union[dict, "SimulationMethod"]]] = None
    calculated_property: Union[Union[dict, "CalculatedProperty"], list[Union[dict, "CalculatedProperty"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.software_package):
            self.MissingRequiredField("software_package")
        if not isinstance(self.software_package, list):
            self.software_package = [self.software_package] if self.software_package is not None else []
        self.software_package = [v if isinstance(v, str) else str(v) for v in self.software_package]

        if self._is_empty(self.simulation_method):
            self.MissingRequiredField("simulation_method")
        if not isinstance(self.simulation_method, list):
            self.simulation_method = [self.simulation_method] if self.simulation_method is not None else []
        self.simulation_method = [v if isinstance(v, SimulationMethod) else SimulationMethod(**as_dict(v)) for v in self.simulation_method]

        if self._is_empty(self.calculated_property):
            self.MissingRequiredField("calculated_property")
        if not isinstance(self.calculated_property, list):
            self.calculated_property = [self.calculated_property] if self.calculated_property is not None else []
        self.calculated_property = [v if isinstance(v, CalculatedProperty) else CalculatedProperty(**as_dict(v)) for v in self.calculated_property]

        super().__post_init__(**kwargs)


class SimulationMethod(CatCoreEntity):
    """
    Simulation method used
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["SimulationMethod"]
    class_class_curie: ClassVar[str] = "catcore:SimulationMethod"
    class_name: ClassVar[str] = "SimulationMethod"
    class_model_uri: ClassVar[URIRef] = CATCORE.SimulationMethod


@dataclass(repr=False)
class DFT(SimulationMethod):
    """
    Density functional theory
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["DFT"]
    class_class_curie: ClassVar[str] = "catcore:DFT"
    class_name: ClassVar[str] = "DFT"
    class_model_uri: ClassVar[URIRef] = CATCORE.DFT

    exchange_correlation_functional: Optional[Union[str, list[str]]] = empty_list()
    energy_cutoff: Optional[Union[float, list[float]]] = empty_list()
    convergence_criteria: Optional[Union[str, list[str]]] = empty_list()
    dft_u_parameters: Optional[Union[str, list[str]]] = empty_list()
    spin_polarization: Optional[Union[Union[bool, Bool], list[Union[bool, Bool]]]] = empty_list()
    total_energy_per_atom: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.exchange_correlation_functional, list):
            self.exchange_correlation_functional = [self.exchange_correlation_functional] if self.exchange_correlation_functional is not None else []
        self.exchange_correlation_functional = [v if isinstance(v, str) else str(v) for v in self.exchange_correlation_functional]

        if not isinstance(self.energy_cutoff, list):
            self.energy_cutoff = [self.energy_cutoff] if self.energy_cutoff is not None else []
        self.energy_cutoff = [v if isinstance(v, float) else float(v) for v in self.energy_cutoff]

        if not isinstance(self.convergence_criteria, list):
            self.convergence_criteria = [self.convergence_criteria] if self.convergence_criteria is not None else []
        self.convergence_criteria = [v if isinstance(v, str) else str(v) for v in self.convergence_criteria]

        if not isinstance(self.dft_u_parameters, list):
            self.dft_u_parameters = [self.dft_u_parameters] if self.dft_u_parameters is not None else []
        self.dft_u_parameters = [v if isinstance(v, str) else str(v) for v in self.dft_u_parameters]

        if not isinstance(self.spin_polarization, list):
            self.spin_polarization = [self.spin_polarization] if self.spin_polarization is not None else []
        self.spin_polarization = [v if isinstance(v, Bool) else Bool(v) for v in self.spin_polarization]

        if not isinstance(self.total_energy_per_atom, list):
            self.total_energy_per_atom = [self.total_energy_per_atom] if self.total_energy_per_atom is not None else []
        self.total_energy_per_atom = [v if isinstance(v, float) else float(v) for v in self.total_energy_per_atom]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolecularDynamics(SimulationMethod):
    """
    Molecular dynamics
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NCIT["C18097"]
    class_class_curie: ClassVar[str] = "NCIT:C18097"
    class_name: ClassVar[str] = "MolecularDynamics"
    class_model_uri: ClassVar[URIRef] = CATCORE.MolecularDynamics

    force_field: Optional[Union[str, list[str]]] = empty_list()
    simulation_timestep: Optional[Union[float, list[float]]] = empty_list()
    simulation_time: Optional[Union[float, list[float]]] = empty_list()
    ensemble_type: Optional[Union[str, list[str]]] = empty_list()
    number_of_atoms: Optional[Union[int, list[int]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.force_field, list):
            self.force_field = [self.force_field] if self.force_field is not None else []
        self.force_field = [v if isinstance(v, str) else str(v) for v in self.force_field]

        if not isinstance(self.simulation_timestep, list):
            self.simulation_timestep = [self.simulation_timestep] if self.simulation_timestep is not None else []
        self.simulation_timestep = [v if isinstance(v, float) else float(v) for v in self.simulation_timestep]

        if not isinstance(self.simulation_time, list):
            self.simulation_time = [self.simulation_time] if self.simulation_time is not None else []
        self.simulation_time = [v if isinstance(v, float) else float(v) for v in self.simulation_time]

        if not isinstance(self.ensemble_type, list):
            self.ensemble_type = [self.ensemble_type] if self.ensemble_type is not None else []
        self.ensemble_type = [v if isinstance(v, str) else str(v) for v in self.ensemble_type]

        if not isinstance(self.number_of_atoms, list):
            self.number_of_atoms = [self.number_of_atoms] if self.number_of_atoms is not None else []
        self.number_of_atoms = [v if isinstance(v, int) else int(v) for v in self.number_of_atoms]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Microkinetics(SimulationMethod):
    """
    Microkinetics simulation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["Microkinetics"]
    class_class_curie: ClassVar[str] = "catcore:Microkinetics"
    class_name: ClassVar[str] = "Microkinetics"
    class_model_uri: ClassVar[URIRef] = CATCORE.Microkinetics

    rate_constants: Optional[Union[str, list[str]]] = empty_list()
    solver_type: Optional[Union[str, list[str]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()
    pressure: Optional[Union[float, list[float]]] = empty_list()
    surface_coverage: Optional[Union[float, list[float]]] = empty_list()
    activation_energy: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.rate_constants, list):
            self.rate_constants = [self.rate_constants] if self.rate_constants is not None else []
        self.rate_constants = [v if isinstance(v, str) else str(v) for v in self.rate_constants]

        if not isinstance(self.solver_type, list):
            self.solver_type = [self.solver_type] if self.solver_type is not None else []
        self.solver_type = [v if isinstance(v, str) else str(v) for v in self.solver_type]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.pressure, list):
            self.pressure = [self.pressure] if self.pressure is not None else []
        self.pressure = [v if isinstance(v, float) else float(v) for v in self.pressure]

        if not isinstance(self.surface_coverage, list):
            self.surface_coverage = [self.surface_coverage] if self.surface_coverage is not None else []
        self.surface_coverage = [v if isinstance(v, float) else float(v) for v in self.surface_coverage]

        if not isinstance(self.activation_energy, list):
            self.activation_energy = [self.activation_energy] if self.activation_energy is not None else []
        self.activation_energy = [v if isinstance(v, float) else float(v) for v in self.activation_energy]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MonteCarlo(SimulationMethod):
    """
    Monte Carlo simulation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["MonteCarlo"]
    class_class_curie: ClassVar[str] = "catcore:MonteCarlo"
    class_name: ClassVar[str] = "MonteCarlo"
    class_model_uri: ClassVar[URIRef] = CATCORE.MonteCarlo

    interaction_potential: Optional[Union[str, list[str]]] = empty_list()
    number_of_steps: Optional[Union[int, list[int]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()
    lattice_size_type: Optional[Union[str, list[str]]] = empty_list()
    acceptance_criteria: Optional[Union[str, list[str]]] = empty_list()
    equilibration_steps: Optional[Union[int, list[int]]] = empty_list()
    sampling_interval: Optional[Union[int, list[int]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.interaction_potential, list):
            self.interaction_potential = [self.interaction_potential] if self.interaction_potential is not None else []
        self.interaction_potential = [v if isinstance(v, str) else str(v) for v in self.interaction_potential]

        if not isinstance(self.number_of_steps, list):
            self.number_of_steps = [self.number_of_steps] if self.number_of_steps is not None else []
        self.number_of_steps = [v if isinstance(v, int) else int(v) for v in self.number_of_steps]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        if not isinstance(self.lattice_size_type, list):
            self.lattice_size_type = [self.lattice_size_type] if self.lattice_size_type is not None else []
        self.lattice_size_type = [v if isinstance(v, str) else str(v) for v in self.lattice_size_type]

        if not isinstance(self.acceptance_criteria, list):
            self.acceptance_criteria = [self.acceptance_criteria] if self.acceptance_criteria is not None else []
        self.acceptance_criteria = [v if isinstance(v, str) else str(v) for v in self.acceptance_criteria]

        if not isinstance(self.equilibration_steps, list):
            self.equilibration_steps = [self.equilibration_steps] if self.equilibration_steps is not None else []
        self.equilibration_steps = [v if isinstance(v, int) else int(v) for v in self.equilibration_steps]

        if not isinstance(self.sampling_interval, list):
            self.sampling_interval = [self.sampling_interval] if self.sampling_interval is not None else []
        self.sampling_interval = [v if isinstance(v, int) else int(v) for v in self.sampling_interval]

        super().__post_init__(**kwargs)


class CalculatedProperty(CatCoreEntity):
    """
    Property calculated from simulation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["CalculatedProperty"]
    class_class_curie: ClassVar[str] = "catcore:CalculatedProperty"
    class_name: ClassVar[str] = "CalculatedProperty"
    class_model_uri: ClassVar[URIRef] = CATCORE.CalculatedProperty


@dataclass(repr=False)
class ThermodynamicStability(CalculatedProperty):
    """
    Thermodynamic stability property
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["ThermodynamicStability"]
    class_class_curie: ClassVar[str] = "catcore:ThermodynamicStability"
    class_name: ClassVar[str] = "ThermodynamicStability"
    class_model_uri: ClassVar[URIRef] = CATCORE.ThermodynamicStability

    formation_energy: Optional[Union[float, list[float]]] = empty_list()
    reference_energies: Optional[Union[str, list[str]]] = empty_list()
    energy_above_hull: Optional[Union[float, list[float]]] = empty_list()
    phase_diagram_type: Optional[Union[str, list[str]]] = empty_list()
    competing_phases: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.formation_energy, list):
            self.formation_energy = [self.formation_energy] if self.formation_energy is not None else []
        self.formation_energy = [v if isinstance(v, float) else float(v) for v in self.formation_energy]

        if not isinstance(self.reference_energies, list):
            self.reference_energies = [self.reference_energies] if self.reference_energies is not None else []
        self.reference_energies = [v if isinstance(v, str) else str(v) for v in self.reference_energies]

        if not isinstance(self.energy_above_hull, list):
            self.energy_above_hull = [self.energy_above_hull] if self.energy_above_hull is not None else []
        self.energy_above_hull = [v if isinstance(v, float) else float(v) for v in self.energy_above_hull]

        if not isinstance(self.phase_diagram_type, list):
            self.phase_diagram_type = [self.phase_diagram_type] if self.phase_diagram_type is not None else []
        self.phase_diagram_type = [v if isinstance(v, str) else str(v) for v in self.phase_diagram_type]

        if not isinstance(self.competing_phases, list):
            self.competing_phases = [self.competing_phases] if self.competing_phases is not None else []
        self.competing_phases = [v if isinstance(v, str) else str(v) for v in self.competing_phases]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Piezoelectricity(CalculatedProperty):
    """
    Piezoelectricity property
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["Piezoelectricity"]
    class_class_curie: ClassVar[str] = "catcore:Piezoelectricity"
    class_name: ClassVar[str] = "Piezoelectricity"
    class_model_uri: ClassVar[URIRef] = CATCORE.Piezoelectricity

    piezoelectric_tensor: Optional[Union[str, list[str]]] = empty_list()
    crystal_symmetry: Optional[Union[str, list[str]]] = empty_list()
    strain_applied: Optional[Union[float, list[float]]] = empty_list()
    ionic_electronic_contributions: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.piezoelectric_tensor, list):
            self.piezoelectric_tensor = [self.piezoelectric_tensor] if self.piezoelectric_tensor is not None else []
        self.piezoelectric_tensor = [v if isinstance(v, str) else str(v) for v in self.piezoelectric_tensor]

        if not isinstance(self.crystal_symmetry, list):
            self.crystal_symmetry = [self.crystal_symmetry] if self.crystal_symmetry is not None else []
        self.crystal_symmetry = [v if isinstance(v, str) else str(v) for v in self.crystal_symmetry]

        if not isinstance(self.strain_applied, list):
            self.strain_applied = [self.strain_applied] if self.strain_applied is not None else []
        self.strain_applied = [v if isinstance(v, float) else float(v) for v in self.strain_applied]

        if not isinstance(self.ionic_electronic_contributions, list):
            self.ionic_electronic_contributions = [self.ionic_electronic_contributions] if self.ionic_electronic_contributions is not None else []
        self.ionic_electronic_contributions = [v if isinstance(v, str) else str(v) for v in self.ionic_electronic_contributions]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElasticConstants(CalculatedProperty):
    """
    Elastic constants property
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["ElasticConstants"]
    class_class_curie: ClassVar[str] = "catcore:ElasticConstants"
    class_name: ClassVar[str] = "ElasticConstants"
    class_model_uri: ClassVar[URIRef] = CATCORE.ElasticConstants

    elastic_tensor: Optional[Union[str, list[str]]] = empty_list()
    bulk_modulus: Optional[Union[float, list[float]]] = empty_list()
    shear_modulus: Optional[Union[float, list[float]]] = empty_list()
    poisson_ratio: Optional[Union[float, list[float]]] = empty_list()
    young_modulus: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.elastic_tensor, list):
            self.elastic_tensor = [self.elastic_tensor] if self.elastic_tensor is not None else []
        self.elastic_tensor = [v if isinstance(v, str) else str(v) for v in self.elastic_tensor]

        if not isinstance(self.bulk_modulus, list):
            self.bulk_modulus = [self.bulk_modulus] if self.bulk_modulus is not None else []
        self.bulk_modulus = [v if isinstance(v, float) else float(v) for v in self.bulk_modulus]

        if not isinstance(self.shear_modulus, list):
            self.shear_modulus = [self.shear_modulus] if self.shear_modulus is not None else []
        self.shear_modulus = [v if isinstance(v, float) else float(v) for v in self.shear_modulus]

        if not isinstance(self.poisson_ratio, list):
            self.poisson_ratio = [self.poisson_ratio] if self.poisson_ratio is not None else []
        self.poisson_ratio = [v if isinstance(v, float) else float(v) for v in self.poisson_ratio]

        if not isinstance(self.young_modulus, list):
            self.young_modulus = [self.young_modulus] if self.young_modulus is not None else []
        self.young_modulus = [v if isinstance(v, float) else float(v) for v in self.young_modulus]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Surfaces(CalculatedProperty):
    """
    Surface property
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["Surfaces"]
    class_class_curie: ClassVar[str] = "catcore:Surfaces"
    class_name: ClassVar[str] = "Surfaces"
    class_model_uri: ClassVar[URIRef] = CATCORE.Surfaces

    surface_energy: Optional[Union[float, list[float]]] = empty_list()
    miller_indices: Optional[Union[str, list[str]]] = empty_list()
    slab_thickness: Optional[Union[float, list[float]]] = empty_list()
    vacuum_spacing: Optional[Union[float, list[float]]] = empty_list()
    surface_termination_method: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.surface_energy, list):
            self.surface_energy = [self.surface_energy] if self.surface_energy is not None else []
        self.surface_energy = [v if isinstance(v, float) else float(v) for v in self.surface_energy]

        if not isinstance(self.miller_indices, list):
            self.miller_indices = [self.miller_indices] if self.miller_indices is not None else []
        self.miller_indices = [v if isinstance(v, str) else str(v) for v in self.miller_indices]

        if not isinstance(self.slab_thickness, list):
            self.slab_thickness = [self.slab_thickness] if self.slab_thickness is not None else []
        self.slab_thickness = [v if isinstance(v, float) else float(v) for v in self.slab_thickness]

        if not isinstance(self.vacuum_spacing, list):
            self.vacuum_spacing = [self.vacuum_spacing] if self.vacuum_spacing is not None else []
        self.vacuum_spacing = [v if isinstance(v, float) else float(v) for v in self.vacuum_spacing]

        if not isinstance(self.surface_termination_method, list):
            self.surface_termination_method = [self.surface_termination_method] if self.surface_termination_method is not None else []
        self.surface_termination_method = [v if isinstance(v, str) else str(v) for v in self.surface_termination_method]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DielectricTensors(CalculatedProperty):
    """
    Dielectric tensors property
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["DielectricTensors"]
    class_class_curie: ClassVar[str] = "catcore:DielectricTensors"
    class_name: ClassVar[str] = "DielectricTensors"
    class_model_uri: ClassVar[URIRef] = CATCORE.DielectricTensors

    material_composition: Optional[Union[str, list[str]]] = empty_list()
    crystal_structure: Optional[Union[str, list[str]]] = empty_list()
    energy_cutoff: Optional[Union[float, list[float]]] = empty_list()
    convergence_criteria: Optional[Union[str, list[str]]] = empty_list()
    k_point_mesh: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.material_composition, list):
            self.material_composition = [self.material_composition] if self.material_composition is not None else []
        self.material_composition = [v if isinstance(v, str) else str(v) for v in self.material_composition]

        if not isinstance(self.crystal_structure, list):
            self.crystal_structure = [self.crystal_structure] if self.crystal_structure is not None else []
        self.crystal_structure = [v if isinstance(v, str) else str(v) for v in self.crystal_structure]

        if not isinstance(self.energy_cutoff, list):
            self.energy_cutoff = [self.energy_cutoff] if self.energy_cutoff is not None else []
        self.energy_cutoff = [v if isinstance(v, float) else float(v) for v in self.energy_cutoff]

        if not isinstance(self.convergence_criteria, list):
            self.convergence_criteria = [self.convergence_criteria] if self.convergence_criteria is not None else []
        self.convergence_criteria = [v if isinstance(v, str) else str(v) for v in self.convergence_criteria]

        if not isinstance(self.k_point_mesh, list):
            self.k_point_mesh = [self.k_point_mesh] if self.k_point_mesh is not None else []
        self.k_point_mesh = [v if isinstance(v, str) else str(v) for v in self.k_point_mesh]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PhononDispersion(CalculatedProperty):
    """
    Phonon dispersion property
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["PhononDispersion"]
    class_class_curie: ClassVar[str] = "catcore:PhononDispersion"
    class_name: ClassVar[str] = "PhononDispersion"
    class_model_uri: ClassVar[URIRef] = CATCORE.PhononDispersion

    material_composition: Optional[Union[str, list[str]]] = empty_list()
    crystal_structure: Optional[Union[str, list[str]]] = empty_list()
    force_constant_method: Optional[Union[str, list[str]]] = empty_list()
    kq_point_mesh: Optional[Union[str, list[str]]] = empty_list()
    smearing_parameter: Optional[Union[float, list[float]]] = empty_list()
    imaginary_modes: Optional[Union[Union[bool, Bool], list[Union[bool, Bool]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.material_composition, list):
            self.material_composition = [self.material_composition] if self.material_composition is not None else []
        self.material_composition = [v if isinstance(v, str) else str(v) for v in self.material_composition]

        if not isinstance(self.crystal_structure, list):
            self.crystal_structure = [self.crystal_structure] if self.crystal_structure is not None else []
        self.crystal_structure = [v if isinstance(v, str) else str(v) for v in self.crystal_structure]

        if not isinstance(self.force_constant_method, list):
            self.force_constant_method = [self.force_constant_method] if self.force_constant_method is not None else []
        self.force_constant_method = [v if isinstance(v, str) else str(v) for v in self.force_constant_method]

        if not isinstance(self.kq_point_mesh, list):
            self.kq_point_mesh = [self.kq_point_mesh] if self.kq_point_mesh is not None else []
        self.kq_point_mesh = [v if isinstance(v, str) else str(v) for v in self.kq_point_mesh]

        if not isinstance(self.smearing_parameter, list):
            self.smearing_parameter = [self.smearing_parameter] if self.smearing_parameter is not None else []
        self.smearing_parameter = [v if isinstance(v, float) else float(v) for v in self.smearing_parameter]

        if not isinstance(self.imaginary_modes, list):
            self.imaginary_modes = [self.imaginary_modes] if self.imaginary_modes is not None else []
        self.imaginary_modes = [v if isinstance(v, Bool) else Bool(v) for v in self.imaginary_modes]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EquationsOfState(CalculatedProperty):
    """
    Equations of state property
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["EquationsOfState"]
    class_class_curie: ClassVar[str] = "catcore:EquationsOfState"
    class_name: ClassVar[str] = "EquationsOfState"
    class_model_uri: ClassVar[URIRef] = CATCORE.EquationsOfState

    material_composition: Optional[Union[str, list[str]]] = empty_list()
    crystal_structure: Optional[Union[str, list[str]]] = empty_list()
    fit_method: Optional[Union[str, list[str]]] = empty_list()
    energy_cutoff: Optional[Union[float, list[float]]] = empty_list()
    k_point_mesh: Optional[Union[str, list[str]]] = empty_list()
    bulk_modulus: Optional[Union[float, list[float]]] = empty_list()
    pressure_derivative: Optional[Union[float, list[float]]] = empty_list()
    fit_residuals: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.material_composition, list):
            self.material_composition = [self.material_composition] if self.material_composition is not None else []
        self.material_composition = [v if isinstance(v, str) else str(v) for v in self.material_composition]

        if not isinstance(self.crystal_structure, list):
            self.crystal_structure = [self.crystal_structure] if self.crystal_structure is not None else []
        self.crystal_structure = [v if isinstance(v, str) else str(v) for v in self.crystal_structure]

        if not isinstance(self.fit_method, list):
            self.fit_method = [self.fit_method] if self.fit_method is not None else []
        self.fit_method = [v if isinstance(v, str) else str(v) for v in self.fit_method]

        if not isinstance(self.energy_cutoff, list):
            self.energy_cutoff = [self.energy_cutoff] if self.energy_cutoff is not None else []
        self.energy_cutoff = [v if isinstance(v, float) else float(v) for v in self.energy_cutoff]

        if not isinstance(self.k_point_mesh, list):
            self.k_point_mesh = [self.k_point_mesh] if self.k_point_mesh is not None else []
        self.k_point_mesh = [v if isinstance(v, str) else str(v) for v in self.k_point_mesh]

        if not isinstance(self.bulk_modulus, list):
            self.bulk_modulus = [self.bulk_modulus] if self.bulk_modulus is not None else []
        self.bulk_modulus = [v if isinstance(v, float) else float(v) for v in self.bulk_modulus]

        if not isinstance(self.pressure_derivative, list):
            self.pressure_derivative = [self.pressure_derivative] if self.pressure_derivative is not None else []
        self.pressure_derivative = [v if isinstance(v, float) else float(v) for v in self.pressure_derivative]

        if not isinstance(self.fit_residuals, list):
            self.fit_residuals = [self.fit_residuals] if self.fit_residuals is not None else []
        self.fit_residuals = [v if isinstance(v, float) else float(v) for v in self.fit_residuals]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AqueousStability(CalculatedProperty):
    """
    Aqueous stability property
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["AqueousStability"]
    class_class_curie: ClassVar[str] = "catcore:AqueousStability"
    class_name: ClassVar[str] = "AqueousStability"
    class_model_uri: ClassVar[URIRef] = CATCORE.AqueousStability

    material_composition: Optional[Union[str, list[str]]] = empty_list()
    crystal_structure: Optional[Union[str, list[str]]] = empty_list()
    ph_range: Optional[Union[str, list[str]]] = empty_list()
    potential_range: Optional[Union[str, list[str]]] = empty_list()
    solvation_model: Optional[Union[str, list[str]]] = empty_list()
    ionic_strength: Optional[Union[float, list[float]]] = empty_list()
    temperature: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.material_composition, list):
            self.material_composition = [self.material_composition] if self.material_composition is not None else []
        self.material_composition = [v if isinstance(v, str) else str(v) for v in self.material_composition]

        if not isinstance(self.crystal_structure, list):
            self.crystal_structure = [self.crystal_structure] if self.crystal_structure is not None else []
        self.crystal_structure = [v if isinstance(v, str) else str(v) for v in self.crystal_structure]

        if not isinstance(self.ph_range, list):
            self.ph_range = [self.ph_range] if self.ph_range is not None else []
        self.ph_range = [v if isinstance(v, str) else str(v) for v in self.ph_range]

        if not isinstance(self.potential_range, list):
            self.potential_range = [self.potential_range] if self.potential_range is not None else []
        self.potential_range = [v if isinstance(v, str) else str(v) for v in self.potential_range]

        if not isinstance(self.solvation_model, list):
            self.solvation_model = [self.solvation_model] if self.solvation_model is not None else []
        self.solvation_model = [v if isinstance(v, str) else str(v) for v in self.solvation_model]

        if not isinstance(self.ionic_strength, list):
            self.ionic_strength = [self.ionic_strength] if self.ionic_strength is not None else []
        self.ionic_strength = [v if isinstance(v, float) else float(v) for v in self.ionic_strength]

        if not isinstance(self.temperature, list):
            self.temperature = [self.temperature] if self.temperature is not None else []
        self.temperature = [v if isinstance(v, float) else float(v) for v in self.temperature]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GrainBoundaries(CalculatedProperty):
    """
    Grain boundaries property
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["GrainBoundaries"]
    class_class_curie: ClassVar[str] = "catcore:GrainBoundaries"
    class_name: ClassVar[str] = "GrainBoundaries"
    class_model_uri: ClassVar[URIRef] = CATCORE.GrainBoundaries

    material_composition: Optional[Union[str, list[str]]] = empty_list()
    grain_boundary_plane: Optional[Union[str, list[str]]] = empty_list()
    misorientation_angle: Optional[Union[float, list[float]]] = empty_list()
    grain_boundary_energy: Optional[Union[float, list[float]]] = empty_list()
    simulation_cell_size: Optional[Union[str, list[str]]] = empty_list()
    gb_excess_volume: Optional[Union[float, list[float]]] = empty_list()
    gb_structural_units: Optional[Union[str, list[str]]] = empty_list()
    charge_defect_segregation: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.material_composition, list):
            self.material_composition = [self.material_composition] if self.material_composition is not None else []
        self.material_composition = [v if isinstance(v, str) else str(v) for v in self.material_composition]

        if not isinstance(self.grain_boundary_plane, list):
            self.grain_boundary_plane = [self.grain_boundary_plane] if self.grain_boundary_plane is not None else []
        self.grain_boundary_plane = [v if isinstance(v, str) else str(v) for v in self.grain_boundary_plane]

        if not isinstance(self.misorientation_angle, list):
            self.misorientation_angle = [self.misorientation_angle] if self.misorientation_angle is not None else []
        self.misorientation_angle = [v if isinstance(v, float) else float(v) for v in self.misorientation_angle]

        if not isinstance(self.grain_boundary_energy, list):
            self.grain_boundary_energy = [self.grain_boundary_energy] if self.grain_boundary_energy is not None else []
        self.grain_boundary_energy = [v if isinstance(v, float) else float(v) for v in self.grain_boundary_energy]

        if not isinstance(self.simulation_cell_size, list):
            self.simulation_cell_size = [self.simulation_cell_size] if self.simulation_cell_size is not None else []
        self.simulation_cell_size = [v if isinstance(v, str) else str(v) for v in self.simulation_cell_size]

        if not isinstance(self.gb_excess_volume, list):
            self.gb_excess_volume = [self.gb_excess_volume] if self.gb_excess_volume is not None else []
        self.gb_excess_volume = [v if isinstance(v, float) else float(v) for v in self.gb_excess_volume]

        if not isinstance(self.gb_structural_units, list):
            self.gb_structural_units = [self.gb_structural_units] if self.gb_structural_units is not None else []
        self.gb_structural_units = [v if isinstance(v, str) else str(v) for v in self.gb_structural_units]

        if not isinstance(self.charge_defect_segregation, list):
            self.charge_defect_segregation = [self.charge_defect_segregation] if self.charge_defect_segregation is not None else []
        self.charge_defect_segregation = [v if isinstance(v, str) else str(v) for v in self.charge_defect_segregation]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ElectronicStructure(CalculatedProperty):
    """
    Electronic structure property
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["ElectronicStructure"]
    class_class_curie: ClassVar[str] = "catcore:ElectronicStructure"
    class_name: ClassVar[str] = "ElectronicStructure"
    class_model_uri: ClassVar[URIRef] = CATCORE.ElectronicStructure

    material_composition: Optional[Union[str, list[str]]] = empty_list()
    crystal_structure: Optional[Union[str, list[str]]] = empty_list()
    k_point_mesh: Optional[Union[str, list[str]]] = empty_list()
    energy_cutoff: Optional[Union[float, list[float]]] = empty_list()
    smearing_method: Optional[Union[str, list[str]]] = empty_list()
    spin_polarized: Optional[Union[Union[bool, Bool], list[Union[bool, Bool]]]] = empty_list()
    band_path: Optional[Union[str, list[str]]] = empty_list()
    fermi_energy: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.material_composition, list):
            self.material_composition = [self.material_composition] if self.material_composition is not None else []
        self.material_composition = [v if isinstance(v, str) else str(v) for v in self.material_composition]

        if not isinstance(self.crystal_structure, list):
            self.crystal_structure = [self.crystal_structure] if self.crystal_structure is not None else []
        self.crystal_structure = [v if isinstance(v, str) else str(v) for v in self.crystal_structure]

        if not isinstance(self.k_point_mesh, list):
            self.k_point_mesh = [self.k_point_mesh] if self.k_point_mesh is not None else []
        self.k_point_mesh = [v if isinstance(v, str) else str(v) for v in self.k_point_mesh]

        if not isinstance(self.energy_cutoff, list):
            self.energy_cutoff = [self.energy_cutoff] if self.energy_cutoff is not None else []
        self.energy_cutoff = [v if isinstance(v, float) else float(v) for v in self.energy_cutoff]

        if not isinstance(self.smearing_method, list):
            self.smearing_method = [self.smearing_method] if self.smearing_method is not None else []
        self.smearing_method = [v if isinstance(v, str) else str(v) for v in self.smearing_method]

        if not isinstance(self.spin_polarized, list):
            self.spin_polarized = [self.spin_polarized] if self.spin_polarized is not None else []
        self.spin_polarized = [v if isinstance(v, Bool) else Bool(v) for v in self.spin_polarized]

        if not isinstance(self.band_path, list):
            self.band_path = [self.band_path] if self.band_path is not None else []
        self.band_path = [v if isinstance(v, str) else str(v) for v in self.band_path]

        if not isinstance(self.fermi_energy, list):
            self.fermi_energy = [self.fermi_energy] if self.fermi_energy is not None else []
        self.fermi_energy = [v if isinstance(v, float) else float(v) for v in self.fermi_energy]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Ferroelectrics(CalculatedProperty):
    """
    Ferroelectric property
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["Ferroelectrics"]
    class_class_curie: ClassVar[str] = "catcore:Ferroelectrics"
    class_name: ClassVar[str] = "Ferroelectrics"
    class_model_uri: ClassVar[URIRef] = CATCORE.Ferroelectrics

    material_composition: Optional[Union[str, list[str]]] = empty_list()
    crystal_structure: Optional[Union[str, list[str]]] = empty_list()
    polarization_direction: Optional[Union[str, list[str]]] = empty_list()
    spontaneous_polarization: Optional[Union[float, list[float]]] = empty_list()
    reference_structure: Optional[Union[str, list[str]]] = empty_list()
    switching_barrier: Optional[Union[float, list[float]]] = empty_list()
    coercive_field: Optional[Union[float, list[float]]] = empty_list()
    temperature_dependence: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.material_composition, list):
            self.material_composition = [self.material_composition] if self.material_composition is not None else []
        self.material_composition = [v if isinstance(v, str) else str(v) for v in self.material_composition]

        if not isinstance(self.crystal_structure, list):
            self.crystal_structure = [self.crystal_structure] if self.crystal_structure is not None else []
        self.crystal_structure = [v if isinstance(v, str) else str(v) for v in self.crystal_structure]

        if not isinstance(self.polarization_direction, list):
            self.polarization_direction = [self.polarization_direction] if self.polarization_direction is not None else []
        self.polarization_direction = [v if isinstance(v, str) else str(v) for v in self.polarization_direction]

        if not isinstance(self.spontaneous_polarization, list):
            self.spontaneous_polarization = [self.spontaneous_polarization] if self.spontaneous_polarization is not None else []
        self.spontaneous_polarization = [v if isinstance(v, float) else float(v) for v in self.spontaneous_polarization]

        if not isinstance(self.reference_structure, list):
            self.reference_structure = [self.reference_structure] if self.reference_structure is not None else []
        self.reference_structure = [v if isinstance(v, str) else str(v) for v in self.reference_structure]

        if not isinstance(self.switching_barrier, list):
            self.switching_barrier = [self.switching_barrier] if self.switching_barrier is not None else []
        self.switching_barrier = [v if isinstance(v, float) else float(v) for v in self.switching_barrier]

        if not isinstance(self.coercive_field, list):
            self.coercive_field = [self.coercive_field] if self.coercive_field is not None else []
        self.coercive_field = [v if isinstance(v, float) else float(v) for v in self.coercive_field]

        if not isinstance(self.temperature_dependence, list):
            self.temperature_dependence = [self.temperature_dependence] if self.temperature_dependence is not None else []
        self.temperature_dependence = [v if isinstance(v, str) else str(v) for v in self.temperature_dependence]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BandGap(CalculatedProperty):
    """
    Band gap property
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CATCORE["BandGap"]
    class_class_curie: ClassVar[str] = "catcore:BandGap"
    class_name: ClassVar[str] = "BandGap"
    class_model_uri: ClassVar[URIRef] = CATCORE.BandGap

    material_sample: Optional[Union[str, list[str]]] = empty_list()
    structure_model: Optional[Union[str, list[str]]] = empty_list()
    k_point_mesh: Optional[Union[str, list[str]]] = empty_list()
    smearing_broadening: Optional[Union[float, list[float]]] = empty_list()
    direct_indirect: Optional[Union[str, list[str]]] = empty_list()
    experimental_reference: Optional[Union[float, list[float]]] = empty_list()
    gw_hybrid_correction: Optional[Union[Union[bool, Bool], list[Union[bool, Bool]]]] = empty_list()
    excitonic_correction: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.material_sample, list):
            self.material_sample = [self.material_sample] if self.material_sample is not None else []
        self.material_sample = [v if isinstance(v, str) else str(v) for v in self.material_sample]

        if not isinstance(self.structure_model, list):
            self.structure_model = [self.structure_model] if self.structure_model is not None else []
        self.structure_model = [v if isinstance(v, str) else str(v) for v in self.structure_model]

        if not isinstance(self.k_point_mesh, list):
            self.k_point_mesh = [self.k_point_mesh] if self.k_point_mesh is not None else []
        self.k_point_mesh = [v if isinstance(v, str) else str(v) for v in self.k_point_mesh]

        if not isinstance(self.smearing_broadening, list):
            self.smearing_broadening = [self.smearing_broadening] if self.smearing_broadening is not None else []
        self.smearing_broadening = [v if isinstance(v, float) else float(v) for v in self.smearing_broadening]

        if not isinstance(self.direct_indirect, list):
            self.direct_indirect = [self.direct_indirect] if self.direct_indirect is not None else []
        self.direct_indirect = [v if isinstance(v, str) else str(v) for v in self.direct_indirect]

        if not isinstance(self.experimental_reference, list):
            self.experimental_reference = [self.experimental_reference] if self.experimental_reference is not None else []
        self.experimental_reference = [v if isinstance(v, float) else float(v) for v in self.experimental_reference]

        if not isinstance(self.gw_hybrid_correction, list):
            self.gw_hybrid_correction = [self.gw_hybrid_correction] if self.gw_hybrid_correction is not None else []
        self.gw_hybrid_correction = [v if isinstance(v, Bool) else Bool(v) for v in self.gw_hybrid_correction]

        if not isinstance(self.excitonic_correction, list):
            self.excitonic_correction = [self.excitonic_correction] if self.excitonic_correction is not None else []
        self.excitonic_correction = [v if isinstance(v, float) else float(v) for v in self.excitonic_correction]

        super().__post_init__(**kwargs)


# Enumerations
class CatalysisResearchFieldEnum(EnumDefinitionImpl):
    """
    Enumeration of catalysis research fields
    """
    heterogeneous_catalysis = PermissibleValue(
        text="heterogeneous_catalysis",
        description="Heterogeneous catalysis",
        meaning=VOC4CAT["0007001"])
    homogeneous_catalysis = PermissibleValue(
        text="homogeneous_catalysis",
        description="Homogeneous catalysis",
        meaning=VOC4CAT["0000294"])
    biocatalysis = PermissibleValue(
        text="biocatalysis",
        description="Biocatalysis",
        meaning=VOC4CAT["0000204"])
    electrocatalysis = PermissibleValue(
        text="electrocatalysis",
        description="Electrocatalysis",
        meaning=VOC4CAT["0000216"])
    hybrid_catalysis = PermissibleValue(
        text="hybrid_catalysis",
        description="Hybrid catalysis")
    other = PermissibleValue(
        text="other",
        description="Other catalysis research field")

    _defn = EnumDefinition(
        name="CatalysisResearchFieldEnum",
        description="Enumeration of catalysis research fields",
    )

class ImpregnationTypeEnum(EnumDefinitionImpl):
    """
    Enumeration of impregnation types
    """
    wet_impregnation = PermissibleValue(
        text="wet_impregnation",
        description="Wet impregnation method")
    dry_impregnation = PermissibleValue(
        text="dry_impregnation",
        description="Dry impregnation method")
    incipient_wetness = PermissibleValue(
        text="incipient_wetness",
        description="Incipient wetness impregnation")
    other = PermissibleValue(
        text="other",
        description="Other impregnation type")

    _defn = EnumDefinition(
        name="ImpregnationTypeEnum",
        description="Enumeration of impregnation types",
    )

class SampleStateEnum(EnumDefinitionImpl):
    """
    Enumeration of sample states
    """
    solid = PermissibleValue(
        text="solid",
        description="Solid state")
    liquid = PermissibleValue(
        text="liquid",
        description="Liquid state")
    gas = PermissibleValue(
        text="gas",
        description="Gas state")
    solution = PermissibleValue(
        text="solution",
        description="Solution state")
    powder = PermissibleValue(
        text="powder",
        description="Powder form")
    pellet = PermissibleValue(
        text="pellet",
        description="Pellet form")
    thin_film = PermissibleValue(
        text="thin_film",
        description="Thin film")
    other = PermissibleValue(
        text="other",
        description="Other sample state")

    _defn = EnumDefinition(
        name="SampleStateEnum",
        description="Enumeration of sample states",
    )

# Slots
class slots:
    pass

slots.identifier = Slot(uri=CATCORE.identifier, name="identifier", curie=CATCORE.curie('identifier'),
                   model_uri=CATCORE.identifier, domain=None, range=Optional[str])

slots.catalysis_research_field = Slot(uri=VOC4CAT['0000196'], name="catalysis_research_field", curie=VOC4CAT.curie('0000196'),
                   model_uri=CATCORE.catalysis_research_field, domain=None, range=Optional[Union[str, "CatalysisResearchFieldEnum"]])

slots.reaction_type = Slot(uri=VOC4CAT['0007010'], name="reaction_type", curie=VOC4CAT.curie('0007010'),
                   model_uri=CATCORE.reaction_type, domain=None, range=Optional[str])

slots.active_site = Slot(uri=VOC4CAT['0007006'], name="active_site", curie=VOC4CAT.curie('0007006'),
                   model_uri=CATCORE.active_site, domain=None, range=Optional[str])

slots.nominal_composition = Slot(uri=CATCORE.nominal_composition, name="nominal_composition", curie=CATCORE.curie('nominal_composition'),
                   model_uri=CATCORE.nominal_composition, domain=None, range=Optional[str])

slots.catalyst_measured_properties = Slot(uri=CATCORE.catalyst_measured_properties, name="catalyst_measured_properties", curie=CATCORE.curie('catalyst_measured_properties'),
                   model_uri=CATCORE.catalyst_measured_properties, domain=None, range=Optional[str])

slots.precursor = Slot(uri=CATCORE.precursor, name="precursor", curie=CATCORE.curie('precursor'),
                   model_uri=CATCORE.precursor, domain=None, range=Optional[Union[Union[dict, Precursor], list[Union[dict, Precursor]]]])

slots.precursor_quantity = Slot(uri=CATCORE.precursor_quantity, name="precursor_quantity", curie=CATCORE.curie('precursor_quantity'),
                   model_uri=CATCORE.precursor_quantity, domain=None, range=Optional[Union[float, list[float]]])

slots.preparation_method = Slot(uri=VOC4CAT['0007016'], name="preparation_method", curie=VOC4CAT.curie('0007016'),
                   model_uri=CATCORE.preparation_method, domain=None, range=Optional[Union[Union[dict, PreparationMethod], list[Union[dict, PreparationMethod]]]])

slots.impregnation_type = Slot(uri=CATCORE.impregnation_type, name="impregnation_type", curie=CATCORE.curie('impregnation_type'),
                   model_uri=CATCORE.impregnation_type, domain=None, range=Optional[Union[Union[str, "ImpregnationTypeEnum"], list[Union[str, "ImpregnationTypeEnum"]]]])

slots.impregnation_duration = Slot(uri=CATCORE.impregnation_duration, name="impregnation_duration", curie=CATCORE.curie('impregnation_duration'),
                   model_uri=CATCORE.impregnation_duration, domain=None, range=Optional[Union[float, list[float]]])

slots.impregnation_temperature = Slot(uri=CATCORE.impregnation_temperature, name="impregnation_temperature", curie=CATCORE.curie('impregnation_temperature'),
                   model_uri=CATCORE.impregnation_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.drying_device = Slot(uri=CATCORE.drying_device, name="drying_device", curie=CATCORE.curie('drying_device'),
                   model_uri=CATCORE.drying_device, domain=None, range=Optional[Union[str, list[str]]])

slots.drying_temperature = Slot(uri=CATCORE.drying_temperature, name="drying_temperature", curie=CATCORE.curie('drying_temperature'),
                   model_uri=CATCORE.drying_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.drying_time = Slot(uri=CATCORE.drying_time, name="drying_time", curie=CATCORE.curie('drying_time'),
                   model_uri=CATCORE.drying_time, domain=None, range=Optional[Union[float, list[float]]])

slots.drying_atmosphere = Slot(uri=CATCORE.drying_atmosphere, name="drying_atmosphere", curie=CATCORE.curie('drying_atmosphere'),
                   model_uri=CATCORE.drying_atmosphere, domain=None, range=Optional[Union[str, list[str]]])

slots.calcination_initial_temperature = Slot(uri=VOC4CAT['0000057'], name="calcination_initial_temperature", curie=VOC4CAT.curie('0000057'),
                   model_uri=CATCORE.calcination_initial_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.calcination_final_temperature = Slot(uri=VOC4CAT['0000058'], name="calcination_final_temperature", curie=VOC4CAT.curie('0000058'),
                   model_uri=CATCORE.calcination_final_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.calcination_dwelling_time = Slot(uri=VOC4CAT['0000060'], name="calcination_dwelling_time", curie=VOC4CAT.curie('0000060'),
                   model_uri=CATCORE.calcination_dwelling_time, domain=None, range=Optional[Union[float, list[float]]])

slots.number_of_cycles = Slot(uri=CATCORE.number_of_cycles, name="number_of_cycles", curie=CATCORE.curie('number_of_cycles'),
                   model_uri=CATCORE.number_of_cycles, domain=None, range=Optional[Union[int, list[int]]])

slots.calcination_gaseous_environment = Slot(uri=VOC4CAT['0000055'], name="calcination_gaseous_environment", curie=VOC4CAT.curie('0000055'),
                   model_uri=CATCORE.calcination_gaseous_environment, domain=None, range=Optional[Union[str, list[str]]])

slots.calcination_heating_rate = Slot(uri=VOC4CAT['0000059'], name="calcination_heating_rate", curie=VOC4CAT.curie('0000059'),
                   model_uri=CATCORE.calcination_heating_rate, domain=None, range=Optional[Union[float, list[float]]])

slots.calcination_gas_flow_rate = Slot(uri=VOC4CAT['0000056'], name="calcination_gas_flow_rate", curie=VOC4CAT.curie('0000056'),
                   model_uri=CATCORE.calcination_gas_flow_rate, domain=None, range=Optional[Union[float, list[float]]])

slots.precipitating_agent = Slot(uri=CATCORE.precipitating_agent, name="precipitating_agent", curie=CATCORE.curie('precipitating_agent'),
                   model_uri=CATCORE.precipitating_agent, domain=None, range=Optional[Union[str, list[str]]])

slots.precipitating_concentration = Slot(uri=CATCORE.precipitating_concentration, name="precipitating_concentration", curie=CATCORE.curie('precipitating_concentration'),
                   model_uri=CATCORE.precipitating_concentration, domain=None, range=Optional[Union[float, list[float]]])

slots.synthesis_ph = Slot(uri=VOC4CAT['0000052'], name="synthesis_ph", curie=VOC4CAT.curie('0000052'),
                   model_uri=CATCORE.synthesis_ph, domain=None, range=Optional[Union[float, list[float]]])

slots.mixing_rate = Slot(uri=CATCORE.mixing_rate, name="mixing_rate", curie=CATCORE.curie('mixing_rate'),
                   model_uri=CATCORE.mixing_rate, domain=None, range=Optional[Union[float, list[float]]])

slots.mixing_time = Slot(uri=CATCORE.mixing_time, name="mixing_time", curie=CATCORE.curie('mixing_time'),
                   model_uri=CATCORE.mixing_time, domain=None, range=Optional[Union[float, list[float]]])

slots.mixing_temperature = Slot(uri=CATCORE.mixing_temperature, name="mixing_temperature", curie=CATCORE.curie('mixing_temperature'),
                   model_uri=CATCORE.mixing_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.order_of_addition = Slot(uri=CATCORE.order_of_addition, name="order_of_addition", curie=CATCORE.curie('order_of_addition'),
                   model_uri=CATCORE.order_of_addition, domain=None, range=Optional[Union[str, list[str]]])

slots.filtration = Slot(uri=CATCORE.filtration, name="filtration", curie=CATCORE.curie('filtration'),
                   model_uri=CATCORE.filtration, domain=None, range=Optional[Union[str, list[str]]])

slots.purification = Slot(uri=CATCORE.purification, name="purification", curie=CATCORE.curie('purification'),
                   model_uri=CATCORE.purification, domain=None, range=Optional[Union[str, list[str]]])

slots.aging_temperature = Slot(uri=CATCORE.aging_temperature, name="aging_temperature", curie=CATCORE.curie('aging_temperature'),
                   model_uri=CATCORE.aging_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.aging_time = Slot(uri=CATCORE.aging_time, name="aging_time", curie=CATCORE.curie('aging_time'),
                   model_uri=CATCORE.aging_time, domain=None, range=Optional[Union[float, list[float]]])

slots.hydrolysis_ratio = Slot(uri=CATCORE.hydrolysis_ratio, name="hydrolysis_ratio", curie=CATCORE.curie('hydrolysis_ratio'),
                   model_uri=CATCORE.hydrolysis_ratio, domain=None, range=Optional[Union[float, list[float]]])

slots.drying = Slot(uri=CATCORE.drying, name="drying", curie=CATCORE.curie('drying'),
                   model_uri=CATCORE.drying, domain=None, range=Optional[Union[str, list[str]]])

slots.surfactant_template = Slot(uri=CATCORE.surfactant_template, name="surfactant_template", curie=CATCORE.curie('surfactant_template'),
                   model_uri=CATCORE.surfactant_template, domain=None, range=Optional[Union[str, list[str]]])

slots.filling_volume = Slot(uri=CATCORE.filling_volume, name="filling_volume", curie=CATCORE.curie('filling_volume'),
                   model_uri=CATCORE.filling_volume, domain=None, range=Optional[Union[float, list[float]]])

slots.synthesis_temperature = Slot(uri=VOC4CAT['0000051'], name="synthesis_temperature", curie=VOC4CAT.curie('0000051'),
                   model_uri=CATCORE.synthesis_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.synthesis_duration = Slot(uri=VOC4CAT['0000050'], name="synthesis_duration", curie=VOC4CAT.curie('0000050'),
                   model_uri=CATCORE.synthesis_duration, domain=None, range=Optional[Union[float, list[float]]])

slots.vessel_type = Slot(uri=CATCORE.vessel_type, name="vessel_type", curie=CATCORE.curie('vessel_type'),
                   model_uri=CATCORE.vessel_type, domain=None, range=Optional[Union[str, list[str]]])

slots.equipment = Slot(uri=VOC4CAT['0000187'], name="equipment", curie=VOC4CAT.curie('0000187'),
                   model_uri=CATCORE.equipment, domain=None, range=Optional[Union[str, list[str]]])

slots.stirring_speed = Slot(uri=CATCORE.stirring_speed, name="stirring_speed", curie=CATCORE.curie('stirring_speed'),
                   model_uri=CATCORE.stirring_speed, domain=None, range=Optional[Union[float, list[float]]])

slots.stirrer_type = Slot(uri=CATCORE.stirrer_type, name="stirrer_type", curie=CATCORE.curie('stirrer_type'),
                   model_uri=CATCORE.stirrer_type, domain=None, range=Optional[Union[str, list[str]]])

slots.cooling_rate = Slot(uri=CATCORE.cooling_rate, name="cooling_rate", curie=CATCORE.curie('cooling_rate'),
                   model_uri=CATCORE.cooling_rate, domain=None, range=Optional[Union[float, list[float]]])

slots.plasma_type = Slot(uri=CATCORE.plasma_type, name="plasma_type", curie=CATCORE.curie('plasma_type'),
                   model_uri=CATCORE.plasma_type, domain=None, range=Optional[Union[str, list[str]]])

slots.atmosphere = Slot(uri=CATCORE.atmosphere, name="atmosphere", curie=CATCORE.curie('atmosphere'),
                   model_uri=CATCORE.atmosphere, domain=None, range=Optional[Union[str, list[str]]])

slots.power_input = Slot(uri=CATCORE.power_input, name="power_input", curie=CATCORE.curie('power_input'),
                   model_uri=CATCORE.power_input, domain=None, range=Optional[Union[float, list[float]]])

slots.exposure_time = Slot(uri=CATCORE.exposure_time, name="exposure_time", curie=CATCORE.curie('exposure_time'),
                   model_uri=CATCORE.exposure_time, domain=None, range=Optional[Union[float, list[float]]])

slots.synthesis_pressure = Slot(uri=VOC4CAT['0000053'], name="synthesis_pressure", curie=VOC4CAT.curie('0000053'),
                   model_uri=CATCORE.synthesis_pressure, domain=None, range=Optional[Union[float, list[float]]])

slots.fuel = Slot(uri=CATCORE.fuel, name="fuel", curie=CATCORE.curie('fuel'),
                   model_uri=CATCORE.fuel, domain=None, range=Optional[Union[str, list[str]]])

slots.oxidizer = Slot(uri=CATCORE.oxidizer, name="oxidizer", curie=CATCORE.curie('oxidizer'),
                   model_uri=CATCORE.oxidizer, domain=None, range=Optional[Union[str, list[str]]])

slots.fuel_to_oxidizer_ratio = Slot(uri=CATCORE.fuel_to_oxidizer_ratio, name="fuel_to_oxidizer_ratio", curie=CATCORE.curie('fuel_to_oxidizer_ratio'),
                   model_uri=CATCORE.fuel_to_oxidizer_ratio, domain=None, range=Optional[Union[float, list[float]]])

slots.set_temperature = Slot(uri=CATCORE.set_temperature, name="set_temperature", curie=CATCORE.curie('set_temperature'),
                   model_uri=CATCORE.set_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.post_treatment = Slot(uri=CATCORE.post_treatment, name="post_treatment", curie=CATCORE.curie('post_treatment'),
                   model_uri=CATCORE.post_treatment, domain=None, range=Optional[Union[str, list[str]]])

slots.substrate = Slot(uri=VOC4CAT['0000024'], name="substrate", curie=VOC4CAT.curie('0000024'),
                   model_uri=CATCORE.substrate, domain=None, range=Optional[Union[str, list[str]]])

slots.pulse_time = Slot(uri=CATCORE.pulse_time, name="pulse_time", curie=CATCORE.curie('pulse_time'),
                   model_uri=CATCORE.pulse_time, domain=None, range=Optional[Union[float, list[float]]])

slots.purging_duration = Slot(uri=VOC4CAT['0000112'], name="purging_duration", curie=VOC4CAT.curie('0000112'),
                   model_uri=CATCORE.purging_duration, domain=None, range=Optional[Union[float, list[float]]])

slots.deposition_temperature = Slot(uri=CATCORE.deposition_temperature, name="deposition_temperature", curie=CATCORE.curie('deposition_temperature'),
                   model_uri=CATCORE.deposition_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.carrier_gas = Slot(uri=CATCORE.carrier_gas, name="carrier_gas", curie=CATCORE.curie('carrier_gas'),
                   model_uri=CATCORE.carrier_gas, domain=None, range=Optional[Union[str, list[str]]])

slots.deposition_time = Slot(uri=CATCORE.deposition_time, name="deposition_time", curie=CATCORE.curie('deposition_time'),
                   model_uri=CATCORE.deposition_time, domain=None, range=Optional[Union[float, list[float]]])

slots.power = Slot(uri=CATCORE.power, name="power", curie=CATCORE.curie('power'),
                   model_uri=CATCORE.power, domain=None, range=Optional[Union[float, list[float]]])

slots.microwave_frequency = Slot(uri=CATCORE.microwave_frequency, name="microwave_frequency", curie=CATCORE.curie('microwave_frequency'),
                   model_uri=CATCORE.microwave_frequency, domain=None, range=Optional[Union[float, list[float]]])

slots.stirring_duration = Slot(uri=CATCORE.stirring_duration, name="stirring_duration", curie=CATCORE.curie('stirring_duration'),
                   model_uri=CATCORE.stirring_duration, domain=None, range=Optional[Union[float, list[float]]])

slots.sonication_power = Slot(uri=CATCORE.sonication_power, name="sonication_power", curie=CATCORE.curie('sonication_power'),
                   model_uri=CATCORE.sonication_power, domain=None, range=Optional[Union[float, list[float]]])

slots.sonication_duration = Slot(uri=CATCORE.sonication_duration, name="sonication_duration", curie=CATCORE.curie('sonication_duration'),
                   model_uri=CATCORE.sonication_duration, domain=None, range=Optional[Union[float, list[float]]])

slots.temperature = Slot(uri=AFR['0001584'], name="temperature", curie=AFR.curie('0001584'),
                   model_uri=CATCORE.temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.flame_type = Slot(uri=CATCORE.flame_type, name="flame_type", curie=CATCORE.curie('flame_type'),
                   model_uri=CATCORE.flame_type, domain=None, range=Optional[Union[str, list[str]]])

slots.flow_rate = Slot(uri=CATCORE.flow_rate, name="flow_rate", curie=CATCORE.curie('flow_rate'),
                   model_uri=CATCORE.flow_rate, domain=None, range=Optional[Union[float, list[float]]])

slots.inlet_system = Slot(uri=CATCORE.inlet_system, name="inlet_system", curie=CATCORE.curie('inlet_system'),
                   model_uri=CATCORE.inlet_system, domain=None, range=Optional[Union[str, list[str]]])

slots.flame_ring = Slot(uri=CATCORE.flame_ring, name="flame_ring", curie=CATCORE.curie('flame_ring'),
                   model_uri=CATCORE.flame_ring, domain=None, range=Optional[Union[str, list[str]]])

slots.dispersant = Slot(uri=CATCORE.dispersant, name="dispersant", curie=CATCORE.curie('dispersant'),
                   model_uri=CATCORE.dispersant, domain=None, range=Optional[Union[str, list[str]]])

slots.capillary_pressure = Slot(uri=CATCORE.capillary_pressure, name="capillary_pressure", curie=CATCORE.curie('capillary_pressure'),
                   model_uri=CATCORE.capillary_pressure, domain=None, range=Optional[Union[float, list[float]]])

slots.fuel_dispersant_ratio = Slot(uri=CATCORE.fuel_dispersant_ratio, name="fuel_dispersant_ratio", curie=CATCORE.curie('fuel_dispersant_ratio'),
                   model_uri=CATCORE.fuel_dispersant_ratio, domain=None, range=Optional[Union[float, list[float]]])

slots.filtration_device = Slot(uri=CATCORE.filtration_device, name="filtration_device", curie=CATCORE.curie('filtration_device'),
                   model_uri=CATCORE.filtration_device, domain=None, range=Optional[Union[str, list[str]]])

slots.filter_type = Slot(uri=CATCORE.filter_type, name="filter_type", curie=CATCORE.curie('filter_type'),
                   model_uri=CATCORE.filter_type, domain=None, range=Optional[Union[str, list[str]]])

slots.vessel_volume = Slot(uri=CATCORE.vessel_volume, name="vessel_volume", curie=CATCORE.curie('vessel_volume'),
                   model_uri=CATCORE.vessel_volume, domain=None, range=Optional[Union[float, list[float]]])

slots.size_and_material = Slot(uri=CATCORE.size_and_material, name="size_and_material", curie=CATCORE.curie('size_and_material'),
                   model_uri=CATCORE.size_and_material, domain=None, range=Optional[Union[str, list[str]]])

slots.milling_speed = Slot(uri=CATCORE.milling_speed, name="milling_speed", curie=CATCORE.curie('milling_speed'),
                   model_uri=CATCORE.milling_speed, domain=None, range=Optional[Union[float, list[float]]])

slots.milling_duration = Slot(uri=CATCORE.milling_duration, name="milling_duration", curie=CATCORE.curie('milling_duration'),
                   model_uri=CATCORE.milling_duration, domain=None, range=Optional[Union[float, list[float]]])

slots.ball_material = Slot(uri=CATCORE.ball_material, name="ball_material", curie=CATCORE.curie('ball_material'),
                   model_uri=CATCORE.ball_material, domain=None, range=Optional[Union[str, list[str]]])

slots.ball_size = Slot(uri=CATCORE.ball_size, name="ball_size", curie=CATCORE.curie('ball_size'),
                   model_uri=CATCORE.ball_size, domain=None, range=Optional[Union[float, list[float]]])

slots.ball_to_powder_ratio = Slot(uri=CATCORE.ball_to_powder_ratio, name="ball_to_powder_ratio", curie=CATCORE.curie('ball_to_powder_ratio'),
                   model_uri=CATCORE.ball_to_powder_ratio, domain=None, range=Optional[Union[float, list[float]]])

slots.reaction_vessel = Slot(uri=CATCORE.reaction_vessel, name="reaction_vessel", curie=CATCORE.curie('reaction_vessel'),
                   model_uri=CATCORE.reaction_vessel, domain=None, range=Optional[Union[str, list[str]]])

slots.mixing_device = Slot(uri=CATCORE.mixing_device, name="mixing_device", curie=CATCORE.curie('mixing_device'),
                   model_uri=CATCORE.mixing_device, domain=None, range=Optional[Union[str, list[str]]])

slots.crystallisation_solvents = Slot(uri=CATCORE.crystallisation_solvents, name="crystallisation_solvents", curie=CATCORE.curie('crystallisation_solvents'),
                   model_uri=CATCORE.crystallisation_solvents, domain=None, range=Optional[Union[str, list[str]]])

slots.precipitation_agent = Slot(uri=CATCORE.precipitation_agent, name="precipitation_agent", curie=CATCORE.curie('precipitation_agent'),
                   model_uri=CATCORE.precipitation_agent, domain=None, range=Optional[Union[str, list[str]]])

slots.crystallisation_duration = Slot(uri=CATCORE.crystallisation_duration, name="crystallisation_duration", curie=CATCORE.curie('crystallisation_duration'),
                   model_uri=CATCORE.crystallisation_duration, domain=None, range=Optional[Union[float, list[float]]])

slots.purification_solvent = Slot(uri=CATCORE.purification_solvent, name="purification_solvent", curie=CATCORE.curie('purification_solvent'),
                   model_uri=CATCORE.purification_solvent, domain=None, range=Optional[Union[str, list[str]]])

slots.temperature_ramp = Slot(uri=CATCORE.temperature_ramp, name="temperature_ramp", curie=CATCORE.curie('temperature_ramp'),
                   model_uri=CATCORE.temperature_ramp, domain=None, range=Optional[Union[float, list[float]]])

slots.storage_conditions = Slot(uri=CATCORE.storage_conditions, name="storage_conditions", curie=CATCORE.curie('storage_conditions'),
                   model_uri=CATCORE.storage_conditions, domain=None, range=Optional[Union[str, list[str]]])

slots.support = Slot(uri=CATCORE.support, name="support", curie=CATCORE.curie('support'),
                   model_uri=CATCORE.support, domain=None, range=Optional[Union[str, list[str]]])

slots.support_preparation = Slot(uri=CATCORE.support_preparation, name="support_preparation", curie=CATCORE.curie('support_preparation'),
                   model_uri=CATCORE.support_preparation, domain=None, range=Optional[Union[str, list[str]]])

slots.solvent = Slot(uri=VOC4CAT['0007246'], name="solvent", curie=VOC4CAT.curie('0007246'),
                   model_uri=CATCORE.solvent, domain=None, range=Optional[Union[str, list[str]]])

slots.solvent_quantity = Slot(uri=CATCORE.solvent_quantity, name="solvent_quantity", curie=CATCORE.curie('solvent_quantity'),
                   model_uri=CATCORE.solvent_quantity, domain=None, range=Optional[Union[float, list[float]]])

slots.sample_pretreatment = Slot(uri=VOC4CAT['0000122'], name="sample_pretreatment", curie=VOC4CAT.curie('0000122'),
                   model_uri=CATCORE.sample_pretreatment, domain=None, range=Optional[Union[str, list[str]]])

slots.heating_procedure = Slot(uri=CATCORE.heating_procedure, name="heating_procedure", curie=CATCORE.curie('heating_procedure'),
                   model_uri=CATCORE.heating_procedure, domain=None, range=Optional[Union[str, list[str]]])

slots.characterization_technique = Slot(uri=VOC4CAT['0000066'], name="characterization_technique", curie=VOC4CAT.curie('0000066'),
                   model_uri=CATCORE.characterization_technique, domain=None, range=Optional[Union[Union[dict, CharacterizationTechnique], list[Union[dict, CharacterizationTechnique]]]])

slots.sample_state = Slot(uri=CATCORE.sample_state, name="sample_state", curie=CATCORE.curie('sample_state'),
                   model_uri=CATCORE.sample_state, domain=None, range=Optional[Union[Union[str, "SampleStateEnum"], list[Union[str, "SampleStateEnum"]]]])

slots.sample_description = Slot(uri=CATCORE.sample_description, name="sample_description", curie=CATCORE.curie('sample_description'),
                   model_uri=CATCORE.sample_description, domain=None, range=Optional[Union[str, list[str]]])

slots.detector_type = Slot(uri=AFR['0000317'], name="detector_type", curie=AFR.curie('0000317'),
                   model_uri=CATCORE.detector_type, domain=None, range=Optional[Union[str, list[str]]])

slots.sample_preparation = Slot(uri=AFP['0001159'], name="sample_preparation", curie=AFP.curie('0001159'),
                   model_uri=CATCORE.sample_preparation, domain=None, range=Optional[Union[str, list[str]]])

slots.sample_holder = Slot(uri=CATCORE.sample_holder, name="sample_holder", curie=CATCORE.curie('sample_holder'),
                   model_uri=CATCORE.sample_holder, domain=None, range=Optional[Union[str, list[str]]])

slots.xray_source = Slot(uri=OBI['0001138'], name="xray_source", curie=OBI.curie('0001138'),
                   model_uri=CATCORE.xray_source, domain=None, range=Optional[Union[str, list[str]]])

slots.operation_mode = Slot(uri=VOC4CAT['0000108'], name="operation_mode", curie=VOC4CAT.curie('0000108'),
                   model_uri=CATCORE.operation_mode, domain=None, range=Optional[Union[str, list[str]]])

slots.minimum_2theta = Slot(uri=CATCORE.minimum_2theta, name="minimum_2theta", curie=CATCORE.curie('minimum_2theta'),
                   model_uri=CATCORE.minimum_2theta, domain=None, range=Optional[Union[float, list[float]]])

slots.maximum_2theta = Slot(uri=CATCORE.maximum_2theta, name="maximum_2theta", curie=CATCORE.curie('maximum_2theta'),
                   model_uri=CATCORE.maximum_2theta, domain=None, range=Optional[Union[float, list[float]]])

slots.step_size = Slot(uri=AFR['0000950'], name="step_size", curie=AFR.curie('0000950'),
                   model_uri=CATCORE.step_size, domain=None, range=Optional[Union[float, list[float]]])

slots.monochromator = Slot(uri=CHMO['0002120'], name="monochromator", curie=CHMO.curie('0002120'),
                   model_uri=CATCORE.monochromator, domain=None, range=Optional[Union[str, list[str]]])

slots.sample_spinning_speed = Slot(uri=CATCORE.sample_spinning_speed, name="sample_spinning_speed", curie=CATCORE.curie('sample_spinning_speed'),
                   model_uri=CATCORE.sample_spinning_speed, domain=None, range=Optional[Union[float, list[float]]])

slots.experiment_duration = Slot(uri=AFR['0002455'], name="experiment_duration", curie=AFR.curie('0002455'),
                   model_uri=CATCORE.experiment_duration, domain=None, range=Optional[Union[float, list[float]]])

slots.element_analyzed = Slot(uri=CATCORE.element_analyzed, name="element_analyzed", curie=CATCORE.curie('element_analyzed'),
                   model_uri=CATCORE.element_analyzed, domain=None, range=Optional[Union[str, list[str]]])

slots.absorption_edge = Slot(uri=CATCORE.absorption_edge, name="absorption_edge", curie=CATCORE.curie('absorption_edge'),
                   model_uri=CATCORE.absorption_edge, domain=None, range=Optional[Union[str, list[str]]])

slots.minimum_energy = Slot(uri=CATCORE.minimum_energy, name="minimum_energy", curie=CATCORE.curie('minimum_energy'),
                   model_uri=CATCORE.minimum_energy, domain=None, range=Optional[Union[float, list[float]]])

slots.maximum_energy = Slot(uri=CATCORE.maximum_energy, name="maximum_energy", curie=CATCORE.curie('maximum_energy'),
                   model_uri=CATCORE.maximum_energy, domain=None, range=Optional[Union[float, list[float]]])

slots.energy_resolution = Slot(uri=AFR['0000950'], name="energy_resolution", curie=AFR.curie('0000950'),
                   model_uri=CATCORE.energy_resolution, domain=None, range=Optional[Union[float, list[float]]])

slots.beamline_source = Slot(uri=CATCORE.beamline_source, name="beamline_source", curie=CATCORE.curie('beamline_source'),
                   model_uri=CATCORE.beamline_source, domain=None, range=Optional[Union[str, list[str]]])

slots.noise_of_measurement = Slot(uri=CATCORE.noise_of_measurement, name="noise_of_measurement", curie=CATCORE.curie('noise_of_measurement'),
                   model_uri=CATCORE.noise_of_measurement, domain=None, range=Optional[Union[float, list[float]]])

slots.minimum_wavenumber = Slot(uri=CATCORE.minimum_wavenumber, name="minimum_wavenumber", curie=CATCORE.curie('minimum_wavenumber'),
                   model_uri=CATCORE.minimum_wavenumber, domain=None, range=Optional[Union[float, list[float]]])

slots.maximum_wavenumber = Slot(uri=CATCORE.maximum_wavenumber, name="maximum_wavenumber", curie=CATCORE.curie('maximum_wavenumber'),
                   model_uri=CATCORE.maximum_wavenumber, domain=None, range=Optional[Union[float, list[float]]])

slots.background_correction = Slot(uri=AFP['0003721'], name="background_correction", curie=AFP.curie('0003721'),
                   model_uri=CATCORE.background_correction, domain=None, range=Optional[Union[str, list[str]]])

slots.number_of_scans = Slot(uri=AFR['0003051'], name="number_of_scans", curie=AFR.curie('0003051'),
                   model_uri=CATCORE.number_of_scans, domain=None, range=Optional[Union[int, list[int]]])

slots.excitation_laser_wavelength = Slot(uri=AFR['0001594'], name="excitation_laser_wavelength", curie=AFR.curie('0001594'),
                   model_uri=CATCORE.excitation_laser_wavelength, domain=None, range=Optional[Union[float, list[float]]])

slots.excitation_laser_power = Slot(uri=AFR['0001595'], name="excitation_laser_power", curie=AFR.curie('0001595'),
                   model_uri=CATCORE.excitation_laser_power, domain=None, range=Optional[Union[float, list[float]]])

slots.magnification_setting = Slot(uri=AFR['0002226'], name="magnification_setting", curie=AFR.curie('0002226'),
                   model_uri=CATCORE.magnification_setting, domain=None, range=Optional[Union[float, list[float]]])

slots.integration_time = Slot(uri=AFR['0001671'], name="integration_time", curie=AFR.curie('0001671'),
                   model_uri=CATCORE.integration_time, domain=None, range=Optional[Union[float, list[float]]])

slots.filter_or_grating = Slot(uri=CATCORE.filter_or_grating, name="filter_or_grating", curie=CATCORE.curie('filter_or_grating'),
                   model_uri=CATCORE.filter_or_grating, domain=None, range=Optional[Union[str, list[str]]])

slots.external_standard = Slot(uri=CATCORE.external_standard, name="external_standard", curie=CATCORE.curie('external_standard'),
                   model_uri=CATCORE.external_standard, domain=None, range=Optional[Union[str, list[str]]])

slots.internal_standard = Slot(uri=CATCORE.internal_standard, name="internal_standard", curie=CATCORE.curie('internal_standard'),
                   model_uri=CATCORE.internal_standard, domain=None, range=Optional[Union[str, list[str]]])

slots.column_type = Slot(uri=AFR['0002026'], name="column_type", curie=AFR.curie('0002026'),
                   model_uri=CATCORE.column_type, domain=None, range=Optional[Union[str, list[str]]])

slots.carrier_gas_purity = Slot(uri=CATCORE.carrier_gas_purity, name="carrier_gas_purity", curie=CATCORE.curie('carrier_gas_purity'),
                   model_uri=CATCORE.carrier_gas_purity, domain=None, range=Optional[Union[str, list[str]]])

slots.inlet_temperature = Slot(uri=CATCORE.inlet_temperature, name="inlet_temperature", curie=CATCORE.curie('inlet_temperature'),
                   model_uri=CATCORE.inlet_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.minimum_oven_temperature = Slot(uri=CATCORE.minimum_oven_temperature, name="minimum_oven_temperature", curie=CATCORE.curie('minimum_oven_temperature'),
                   model_uri=CATCORE.minimum_oven_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.maximum_oven_temperature = Slot(uri=CATCORE.maximum_oven_temperature, name="maximum_oven_temperature", curie=CATCORE.curie('maximum_oven_temperature'),
                   model_uri=CATCORE.maximum_oven_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.heating_ramp = Slot(uri=CATCORE.heating_ramp, name="heating_ramp", curie=CATCORE.curie('heating_ramp'),
                   model_uri=CATCORE.heating_ramp, domain=None, range=Optional[Union[float, list[float]]])

slots.acquisition_mode = Slot(uri=CATCORE.acquisition_mode, name="acquisition_mode", curie=CATCORE.curie('acquisition_mode'),
                   model_uri=CATCORE.acquisition_mode, domain=None, range=Optional[Union[str, list[str]]])

slots.solvent_delay = Slot(uri=CATCORE.solvent_delay, name="solvent_delay", curie=CATCORE.curie('solvent_delay'),
                   model_uri=CATCORE.solvent_delay, domain=None, range=Optional[Union[float, list[float]]])

slots.trace_ion_detection = Slot(uri=CATCORE.trace_ion_detection, name="trace_ion_detection", curie=CATCORE.curie('trace_ion_detection'),
                   model_uri=CATCORE.trace_ion_detection, domain=None, range=Optional[Union[str, list[str]]])

slots.mz_minimum = Slot(uri=AFR['0002652'], name="mz_minimum", curie=AFR.curie('0002652'),
                   model_uri=CATCORE.mz_minimum, domain=None, range=Optional[Union[float, list[float]]])

slots.mz_maximum = Slot(uri=AFR['0002653'], name="mz_maximum", curie=AFR.curie('0002653'),
                   model_uri=CATCORE.mz_maximum, domain=None, range=Optional[Union[float, list[float]]])

slots.split_ratio = Slot(uri=CATCORE.split_ratio, name="split_ratio", curie=CATCORE.curie('split_ratio'),
                   model_uri=CATCORE.split_ratio, domain=None, range=Optional[Union[float, list[float]]])

slots.injection_volume = Slot(uri=AFR['0001577'], name="injection_volume", curie=AFR.curie('0001577'),
                   model_uri=CATCORE.injection_volume, domain=None, range=Optional[Union[float, list[float]]])

slots.nucleus = Slot(uri=CATCORE.nucleus, name="nucleus", curie=CATCORE.curie('nucleus'),
                   model_uri=CATCORE.nucleus, domain=None, range=Optional[Union[str, list[str]]])

slots.irradiation_frequency = Slot(uri=NMRCV['1400026'], name="irradiation_frequency", curie=NMRCV.curie('1400026'),
                   model_uri=CATCORE.irradiation_frequency, domain=None, range=Optional[Union[float, list[float]]])

slots.nmr_pulse_sequence = Slot(uri=NMRCV['1400037'], name="nmr_pulse_sequence", curie=NMRCV.curie('1400037'),
                   model_uri=CATCORE.nmr_pulse_sequence, domain=None, range=Optional[Union[str, list[str]]])

slots.nmr_sample_tube = Slot(uri=NMRCV['1400132'], name="nmr_sample_tube", curie=NMRCV.curie('1400132'),
                   model_uri=CATCORE.nmr_sample_tube, domain=None, range=Optional[Union[str, list[str]]])

slots.gun_type = Slot(uri=CATCORE.gun_type, name="gun_type", curie=CATCORE.curie('gun_type'),
                   model_uri=CATCORE.gun_type, domain=None, range=Optional[Union[str, list[str]]])

slots.acceleration_voltage = Slot(uri=CATCORE.acceleration_voltage, name="acceleration_voltage", curie=CATCORE.curie('acceleration_voltage'),
                   model_uri=CATCORE.acceleration_voltage, domain=None, range=Optional[Union[float, list[float]]])

slots.calibration_method = Slot(uri=CATCORE.calibration_method, name="calibration_method", curie=CATCORE.curie('calibration_method'),
                   model_uri=CATCORE.calibration_method, domain=None, range=Optional[Union[str, list[str]]])

slots.detection_limit = Slot(uri=NCIT.C105701, name="detection_limit", curie=NCIT.curie('C105701'),
                   model_uri=CATCORE.detection_limit, domain=None, range=Optional[Union[float, list[float]]])

slots.matrix_effect_correction = Slot(uri=CATCORE.matrix_effect_correction, name="matrix_effect_correction", curie=CATCORE.curie('matrix_effect_correction'),
                   model_uri=CATCORE.matrix_effect_correction, domain=None, range=Optional[Union[str, list[str]]])

slots.image_resolution = Slot(uri=CATCORE.image_resolution, name="image_resolution", curie=CATCORE.curie('image_resolution'),
                   model_uri=CATCORE.image_resolution, domain=None, range=Optional[Union[float, list[float]]])

slots.field_emitter = Slot(uri=CATCORE.field_emitter, name="field_emitter", curie=CATCORE.curie('field_emitter'),
                   model_uri=CATCORE.field_emitter, domain=None, range=Optional[Union[str, list[str]]])

slots.initial_temperature = Slot(uri=NCIT.C164644, name="initial_temperature", curie=NCIT.curie('C164644'),
                   model_uri=CATCORE.initial_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.final_temperature = Slot(uri=NCIT.C164644, name="final_temperature", curie=NCIT.curie('C164644'),
                   model_uri=CATCORE.final_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.heating_rate = Slot(uri=CATCORE.heating_rate, name="heating_rate", curie=CATCORE.curie('heating_rate'),
                   model_uri=CATCORE.heating_rate, domain=None, range=Optional[Union[float, list[float]]])

slots.sample_mass = Slot(uri=VOC4CAT['0007038'], name="sample_mass", curie=VOC4CAT.curie('0007038'),
                   model_uri=CATCORE.sample_mass, domain=None, range=Optional[Union[float, list[float]]])

slots.total_acquisition_time = Slot(uri=CATCORE.total_acquisition_time, name="total_acquisition_time", curie=CATCORE.curie('total_acquisition_time'),
                   model_uri=CATCORE.total_acquisition_time, domain=None, range=Optional[Union[float, list[float]]])

slots.spot_size = Slot(uri=CATCORE.spot_size, name="spot_size", curie=CATCORE.curie('spot_size'),
                   model_uri=CATCORE.spot_size, domain=None, range=Optional[Union[float, list[float]]])

slots.lense_mode = Slot(uri=VOC4CAT['0000108'], name="lense_mode", curie=VOC4CAT.curie('0000108'),
                   model_uri=CATCORE.lense_mode, domain=None, range=Optional[Union[str, list[str]]])

slots.pass_energy = Slot(uri=CATCORE.pass_energy, name="pass_energy", curie=CATCORE.curie('pass_energy'),
                   model_uri=CATCORE.pass_energy, domain=None, range=Optional[Union[float, list[float]]])

slots.charge_compensation = Slot(uri=CATCORE.charge_compensation, name="charge_compensation", curie=CATCORE.curie('charge_compensation'),
                   model_uri=CATCORE.charge_compensation, domain=None, range=Optional[Union[str, list[str]]])

slots.adsorbate_gas = Slot(uri=CATCORE.adsorbate_gas, name="adsorbate_gas", curie=CATCORE.curie('adsorbate_gas'),
                   model_uri=CATCORE.adsorbate_gas, domain=None, range=Optional[Union[str, list[str]]])

slots.degassing_temperature = Slot(uri=CATCORE.degassing_temperature, name="degassing_temperature", curie=CATCORE.curie('degassing_temperature'),
                   model_uri=CATCORE.degassing_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.measurement_temperature = Slot(uri=CATCORE.measurement_temperature, name="measurement_temperature", curie=CATCORE.curie('measurement_temperature'),
                   model_uri=CATCORE.measurement_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.pore_size_distribution_method = Slot(uri=CATCORE.pore_size_distribution_method, name="pore_size_distribution_method", curie=CATCORE.curie('pore_size_distribution_method'),
                   model_uri=CATCORE.pore_size_distribution_method, domain=None, range=Optional[Union[str, list[str]]])

slots.elements_analyzed = Slot(uri=CATCORE.elements_analyzed, name="elements_analyzed", curie=CATCORE.curie('elements_analyzed'),
                   model_uri=CATCORE.elements_analyzed, domain=None, range=Optional[Union[str, list[str]]])

slots.combustion_temperature = Slot(uri=CATCORE.combustion_temperature, name="combustion_temperature", curie=CATCORE.curie('combustion_temperature'),
                   model_uri=CATCORE.combustion_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.minimum_wavelength = Slot(uri=CATCORE.minimum_wavelength, name="minimum_wavelength", curie=CATCORE.curie('minimum_wavelength'),
                   model_uri=CATCORE.minimum_wavelength, domain=None, range=Optional[Union[float, list[float]]])

slots.maximum_wavelength = Slot(uri=CATCORE.maximum_wavelength, name="maximum_wavelength", curie=CATCORE.curie('maximum_wavelength'),
                   model_uri=CATCORE.maximum_wavelength, domain=None, range=Optional[Union[float, list[float]]])

slots.path_length = Slot(uri=AFQ['0000268'], name="path_length", curie=AFQ.curie('0000268'),
                   model_uri=CATCORE.path_length, domain=None, range=Optional[Union[float, list[float]]])

slots.concentration = Slot(uri=VOC4CAT['0007244'], name="concentration", curie=VOC4CAT.curie('0007244'),
                   model_uri=CATCORE.concentration, domain=None, range=Optional[Union[float, list[float]]])

slots.adsorption_gas = Slot(uri=CATCORE.adsorption_gas, name="adsorption_gas", curie=CATCORE.curie('adsorption_gas'),
                   model_uri=CATCORE.adsorption_gas, domain=None, range=Optional[Union[str, list[str]]])

slots.diluting_reference = Slot(uri=CATCORE.diluting_reference, name="diluting_reference", curie=CATCORE.curie('diluting_reference'),
                   model_uri=CATCORE.diluting_reference, domain=None, range=Optional[Union[str, list[str]]])

slots.ratio_reference_sample = Slot(uri=CATCORE.ratio_reference_sample, name="ratio_reference_sample", curie=CATCORE.curie('ratio_reference_sample'),
                   model_uri=CATCORE.ratio_reference_sample, domain=None, range=Optional[Union[float, list[float]]])

slots.resolution = Slot(uri=CATCORE.resolution, name="resolution", curie=CATCORE.curie('resolution'),
                   model_uri=CATCORE.resolution, domain=None, range=Optional[Union[float, list[float]]])

slots.background_correction_method = Slot(uri=CATCORE.background_correction_method, name="background_correction_method", curie=CATCORE.curie('background_correction_method'),
                   model_uri=CATCORE.background_correction_method, domain=None, range=Optional[Union[str, list[str]]])

slots.scan_rate = Slot(uri=VOC4CAT['0007213'], name="scan_rate", curie=VOC4CAT.curie('0007213'),
                   model_uri=CATCORE.scan_rate, domain=None, range=Optional[Union[float, list[float]]])

slots.minimum_potential = Slot(uri=CATCORE.minimum_potential, name="minimum_potential", curie=CATCORE.curie('minimum_potential'),
                   model_uri=CATCORE.minimum_potential, domain=None, range=Optional[Union[float, list[float]]])

slots.maximum_potential = Slot(uri=CATCORE.maximum_potential, name="maximum_potential", curie=CATCORE.curie('maximum_potential'),
                   model_uri=CATCORE.maximum_potential, domain=None, range=Optional[Union[float, list[float]]])

slots.step_size_potential = Slot(uri=VOC4CAT['0007218'], name="step_size_potential", curie=VOC4CAT.curie('0007218'),
                   model_uri=CATCORE.step_size_potential, domain=None, range=Optional[Union[float, list[float]]])

slots.electrolyte_composition = Slot(uri=CATCORE.electrolyte_composition, name="electrolyte_composition", curie=CATCORE.curie('electrolyte_composition'),
                   model_uri=CATCORE.electrolyte_composition, domain=None, range=Optional[Union[str, list[str]]])

slots.electrolyte_concentration = Slot(uri=CATCORE.electrolyte_concentration, name="electrolyte_concentration", curie=CATCORE.curie('electrolyte_concentration'),
                   model_uri=CATCORE.electrolyte_concentration, domain=None, range=Optional[Union[float, list[float]]])

slots.reference_electrode = Slot(uri=VOC4CAT['0007204'], name="reference_electrode", curie=VOC4CAT.curie('0007204'),
                   model_uri=CATCORE.reference_electrode, domain=None, range=Optional[Union[str, list[str]]])

slots.working_electrode = Slot(uri=VOC4CAT['0007202'], name="working_electrode", curie=VOC4CAT.curie('0007202'),
                   model_uri=CATCORE.working_electrode, domain=None, range=Optional[Union[str, list[str]]])

slots.counter_electrode = Slot(uri=VOC4CAT['0007203'], name="counter_electrode", curie=VOC4CAT.curie('0007203'),
                   model_uri=CATCORE.counter_electrode, domain=None, range=Optional[Union[str, list[str]]])

slots.light_wavelength = Slot(uri=VOC4CAT['0000176'], name="light_wavelength", curie=VOC4CAT.curie('0000176'),
                   model_uri=CATCORE.light_wavelength, domain=None, range=Optional[Union[float, list[float]]])

slots.scattering_angle = Slot(uri=CATCORE.scattering_angle, name="scattering_angle", curie=CATCORE.curie('scattering_angle'),
                   model_uri=CATCORE.scattering_angle, domain=None, range=Optional[Union[float, list[float]]])

slots.refractive_index = Slot(uri=CATCORE.refractive_index, name="refractive_index", curie=CATCORE.curie('refractive_index'),
                   model_uri=CATCORE.refractive_index, domain=None, range=Optional[Union[float, list[float]]])

slots.measurement_duration = Slot(uri=CATCORE.measurement_duration, name="measurement_duration", curie=CATCORE.curie('measurement_duration'),
                   model_uri=CATCORE.measurement_duration, domain=None, range=Optional[Union[float, list[float]]])

slots.spray_voltage = Slot(uri=CHMO['0002792'], name="spray_voltage", curie=CHMO.curie('0002792'),
                   model_uri=CATCORE.spray_voltage, domain=None, range=Optional[Union[float, list[float]]])

slots.capillary_temperature = Slot(uri=CATCORE.capillary_temperature, name="capillary_temperature", curie=CATCORE.curie('capillary_temperature'),
                   model_uri=CATCORE.capillary_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.solvent_composition = Slot(uri=VOC4CAT['0007246'], name="solvent_composition", curie=VOC4CAT.curie('0007246'),
                   model_uri=CATCORE.solvent_composition, domain=None, range=Optional[Union[str, list[str]]])

slots.excitation_wavelength = Slot(uri=AFR['0002479'], name="excitation_wavelength", curie=AFR.curie('0002479'),
                   model_uri=CATCORE.excitation_wavelength, domain=None, range=Optional[Union[float, list[float]]])

slots.emission_wavelength = Slot(uri=NCIT.C204101, name="emission_wavelength", curie=NCIT.curie('C204101'),
                   model_uri=CATCORE.emission_wavelength, domain=None, range=Optional[Union[float, list[float]]])

slots.optical_filter = Slot(uri=CATCORE.optical_filter, name="optical_filter", curie=CATCORE.curie('optical_filter'),
                   model_uri=CATCORE.optical_filter, domain=None, range=Optional[Union[str, list[str]]])

slots.emission_range = Slot(uri=CATCORE.emission_range, name="emission_range", curie=CATCORE.curie('emission_range'),
                   model_uri=CATCORE.emission_range, domain=None, range=Optional[Union[str, list[str]]])

slots.slit_width = Slot(uri=CATCORE.slit_width, name="slit_width", curie=CATCORE.curie('slit_width'),
                   model_uri=CATCORE.slit_width, domain=None, range=Optional[Union[float, list[float]]])

slots.lifetime_fitting_model = Slot(uri=CATCORE.lifetime_fitting_model, name="lifetime_fitting_model", curie=CATCORE.curie('lifetime_fitting_model'),
                   model_uri=CATCORE.lifetime_fitting_model, domain=None, range=Optional[Union[str, list[str]]])

slots.number_of_shots = Slot(uri=CATCORE.number_of_shots, name="number_of_shots", curie=CATCORE.curie('number_of_shots'),
                   model_uri=CATCORE.number_of_shots, domain=None, range=Optional[Union[int, list[int]]])

slots.eluent = Slot(uri=AFRL['0000011'], name="eluent", curie=AFRL.curie('0000011'),
                   model_uri=CATCORE.eluent, domain=None, range=Optional[Union[str, list[str]]])

slots.calibration_standard = Slot(uri=CATCORE.calibration_standard, name="calibration_standard", curie=CATCORE.curie('calibration_standard'),
                   model_uri=CATCORE.calibration_standard, domain=None, range=Optional[Union[str, list[str]]])

slots.gradient_program = Slot(uri=CATCORE.gradient_program, name="gradient_program", curie=CATCORE.curie('gradient_program'),
                   model_uri=CATCORE.gradient_program, domain=None, range=Optional[Union[str, list[str]]])

slots.ionization_mode = Slot(uri=CATCORE.ionization_mode, name="ionization_mode", curie=CATCORE.curie('ionization_mode'),
                   model_uri=CATCORE.ionization_mode, domain=None, range=Optional[Union[str, list[str]]])

slots.primary_energy = Slot(uri=CATCORE.primary_energy, name="primary_energy", curie=CATCORE.curie('primary_energy'),
                   model_uri=CATCORE.primary_energy, domain=None, range=Optional[Union[float, list[float]]])

slots.counting_time = Slot(uri=CATCORE.counting_time, name="counting_time", curie=CATCORE.curie('counting_time'),
                   model_uri=CATCORE.counting_time, domain=None, range=Optional[Union[float, list[float]]])

slots.oxidizing_gas_composition = Slot(uri=CATCORE.oxidizing_gas_composition, name="oxidizing_gas_composition", curie=CATCORE.curie('oxidizing_gas_composition'),
                   model_uri=CATCORE.oxidizing_gas_composition, domain=None, range=Optional[Union[str, list[str]]])

slots.reducing_gas_composition = Slot(uri=CATCORE.reducing_gas_composition, name="reducing_gas_composition", curie=CATCORE.curie('reducing_gas_composition'),
                   model_uri=CATCORE.reducing_gas_composition, domain=None, range=Optional[Union[str, list[str]]])

slots.minimum_temperature = Slot(uri=CATCORE.minimum_temperature, name="minimum_temperature", curie=CATCORE.curie('minimum_temperature'),
                   model_uri=CATCORE.minimum_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.maximum_temperature = Slot(uri=CATCORE.maximum_temperature, name="maximum_temperature", curie=CATCORE.curie('maximum_temperature'),
                   model_uri=CATCORE.maximum_temperature, domain=None, range=Optional[Union[float, list[float]]])

slots.electrode_configuration = Slot(uri=CATCORE.electrode_configuration, name="electrode_configuration", curie=CATCORE.curie('electrode_configuration'),
                   model_uri=CATCORE.electrode_configuration, domain=None, range=Optional[Union[str, list[str]]])

slots.frequency = Slot(uri=VOC4CAT['0007239'], name="frequency", curie=VOC4CAT.curie('0007239'),
                   model_uri=CATCORE.frequency, domain=None, range=Optional[Union[float, list[float]]])

slots.ac_dc_mode = Slot(uri=CATCORE.ac_dc_mode, name="ac_dc_mode", curie=CATCORE.curie('ac_dc_mode'),
                   model_uri=CATCORE.ac_dc_mode, domain=None, range=Optional[Union[str, list[str]]])

slots.sample_geometry = Slot(uri=CATCORE.sample_geometry, name="sample_geometry", curie=CATCORE.curie('sample_geometry'),
                   model_uri=CATCORE.sample_geometry, domain=None, range=Optional[Union[str, list[str]]])

slots.catalyst_quantity = Slot(uri=CATCORE.catalyst_quantity, name="catalyst_quantity", curie=CATCORE.curie('catalyst_quantity'),
                   model_uri=CATCORE.catalyst_quantity, domain=None, range=Optional[Union[float, list[float]]])

slots.catalyst_type = Slot(uri=VOC4CAT['0007014'], name="catalyst_type", curie=VOC4CAT.curie('0007014'),
                   model_uri=CATCORE.catalyst_type, domain=None, range=Optional[Union[str, list[str]]])

slots.reactor_design_type = Slot(uri=VOC4CAT['0007018'], name="reactor_design_type", curie=VOC4CAT.curie('0007018'),
                   model_uri=CATCORE.reactor_design_type, domain=None, range=Optional[Union[Union[dict, ReactorDesignType], list[Union[dict, ReactorDesignType]]]])

slots.reactant = Slot(uri=VOC4CAT['0000101'], name="reactant", curie=VOC4CAT.curie('0000101'),
                   model_uri=CATCORE.reactant, domain=None, range=Optional[Union[str, list[str]]])

slots.operation_parameters = Slot(uri=VOC4CAT['0000142'], name="operation_parameters", curie=VOC4CAT.curie('0000142'),
                   model_uri=CATCORE.operation_parameters, domain=None, range=Optional[Union[Union[dict, OperationParameters], list[Union[dict, OperationParameters]]]])

slots.reactor_temperature_range = Slot(uri=VOC4CAT['0007032'], name="reactor_temperature_range", curie=VOC4CAT.curie('0007032'),
                   model_uri=CATCORE.reactor_temperature_range, domain=None, range=Optional[Union[str, list[str]]])

slots.experiment_pressure = Slot(uri=VOC4CAT['0000118'], name="experiment_pressure", curie=VOC4CAT.curie('0000118'),
                   model_uri=CATCORE.experiment_pressure, domain=None, range=Optional[Union[float, list[float]]])

slots.feed_composition_range = Slot(uri=CATCORE.feed_composition_range, name="feed_composition_range", curie=CATCORE.curie('feed_composition_range'),
                   model_uri=CATCORE.feed_composition_range, domain=None, range=Optional[Union[str, list[str]]])

slots.product_identification_method = Slot(uri=VOC4CAT['0000129'], name="product_identification_method", curie=VOC4CAT.curie('0000129'),
                   model_uri=CATCORE.product_identification_method, domain=None, range=Optional[Union[Union[dict, ProductIdentificationMethod], list[Union[dict, ProductIdentificationMethod]]]])

slots.gas_distributor_type = Slot(uri=CATCORE.gas_distributor_type, name="gas_distributor_type", curie=CATCORE.curie('gas_distributor_type'),
                   model_uri=CATCORE.gas_distributor_type, domain=None, range=Optional[Union[str, list[str]]])

slots.bed_expansion_height = Slot(uri=CATCORE.bed_expansion_height, name="bed_expansion_height", curie=CATCORE.curie('bed_expansion_height'),
                   model_uri=CATCORE.bed_expansion_height, domain=None, range=Optional[Union[float, list[float]]])

slots.software_package = Slot(uri=CATCORE.software_package, name="software_package", curie=CATCORE.curie('software_package'),
                   model_uri=CATCORE.software_package, domain=None, range=Optional[Union[str, list[str]]])

slots.simulation_method = Slot(uri=CATCORE.simulation_method, name="simulation_method", curie=CATCORE.curie('simulation_method'),
                   model_uri=CATCORE.simulation_method, domain=None, range=Optional[Union[Union[dict, SimulationMethod], list[Union[dict, SimulationMethod]]]])

slots.calculated_property = Slot(uri=CATCORE.calculated_property, name="calculated_property", curie=CATCORE.curie('calculated_property'),
                   model_uri=CATCORE.calculated_property, domain=None, range=Optional[Union[Union[dict, CalculatedProperty], list[Union[dict, CalculatedProperty]]]])

slots.exchange_correlation_functional = Slot(uri=CATCORE.exchange_correlation_functional, name="exchange_correlation_functional", curie=CATCORE.curie('exchange_correlation_functional'),
                   model_uri=CATCORE.exchange_correlation_functional, domain=None, range=Optional[Union[str, list[str]]])

slots.energy_cutoff = Slot(uri=CATCORE.energy_cutoff, name="energy_cutoff", curie=CATCORE.curie('energy_cutoff'),
                   model_uri=CATCORE.energy_cutoff, domain=None, range=Optional[Union[float, list[float]]])

slots.convergence_criteria = Slot(uri=CATCORE.convergence_criteria, name="convergence_criteria", curie=CATCORE.curie('convergence_criteria'),
                   model_uri=CATCORE.convergence_criteria, domain=None, range=Optional[Union[str, list[str]]])

slots.dft_u_parameters = Slot(uri=CATCORE.dft_u_parameters, name="dft_u_parameters", curie=CATCORE.curie('dft_u_parameters'),
                   model_uri=CATCORE.dft_u_parameters, domain=None, range=Optional[Union[str, list[str]]])

slots.spin_polarization = Slot(uri=CATCORE.spin_polarization, name="spin_polarization", curie=CATCORE.curie('spin_polarization'),
                   model_uri=CATCORE.spin_polarization, domain=None, range=Optional[Union[Union[bool, Bool], list[Union[bool, Bool]]]])

slots.total_energy_per_atom = Slot(uri=CATCORE.total_energy_per_atom, name="total_energy_per_atom", curie=CATCORE.curie('total_energy_per_atom'),
                   model_uri=CATCORE.total_energy_per_atom, domain=None, range=Optional[Union[float, list[float]]])

slots.force_field = Slot(uri=CATCORE.force_field, name="force_field", curie=CATCORE.curie('force_field'),
                   model_uri=CATCORE.force_field, domain=None, range=Optional[Union[str, list[str]]])

slots.simulation_timestep = Slot(uri=APOLLO_SV['00000012'], name="simulation_timestep", curie=APOLLO_SV.curie('00000012'),
                   model_uri=CATCORE.simulation_timestep, domain=None, range=Optional[Union[float, list[float]]])

slots.simulation_time = Slot(uri=CATCORE.simulation_time, name="simulation_time", curie=CATCORE.curie('simulation_time'),
                   model_uri=CATCORE.simulation_time, domain=None, range=Optional[Union[float, list[float]]])

slots.ensemble_type = Slot(uri=CATCORE.ensemble_type, name="ensemble_type", curie=CATCORE.curie('ensemble_type'),
                   model_uri=CATCORE.ensemble_type, domain=None, range=Optional[Union[str, list[str]]])

slots.number_of_atoms = Slot(uri=CATCORE.number_of_atoms, name="number_of_atoms", curie=CATCORE.curie('number_of_atoms'),
                   model_uri=CATCORE.number_of_atoms, domain=None, range=Optional[Union[int, list[int]]])

slots.rate_constants = Slot(uri=NCIT.C94967, name="rate_constants", curie=NCIT.curie('C94967'),
                   model_uri=CATCORE.rate_constants, domain=None, range=Optional[Union[str, list[str]]])

slots.solver_type = Slot(uri=CATCORE.solver_type, name="solver_type", curie=CATCORE.curie('solver_type'),
                   model_uri=CATCORE.solver_type, domain=None, range=Optional[Union[str, list[str]]])

slots.pressure = Slot(uri=CATCORE.pressure, name="pressure", curie=CATCORE.curie('pressure'),
                   model_uri=CATCORE.pressure, domain=None, range=Optional[Union[float, list[float]]])

slots.surface_coverage = Slot(uri=CATCORE.surface_coverage, name="surface_coverage", curie=CATCORE.curie('surface_coverage'),
                   model_uri=CATCORE.surface_coverage, domain=None, range=Optional[Union[float, list[float]]])

slots.activation_energy = Slot(uri=CATCORE.activation_energy, name="activation_energy", curie=CATCORE.curie('activation_energy'),
                   model_uri=CATCORE.activation_energy, domain=None, range=Optional[Union[float, list[float]]])

slots.interaction_potential = Slot(uri=CATCORE.interaction_potential, name="interaction_potential", curie=CATCORE.curie('interaction_potential'),
                   model_uri=CATCORE.interaction_potential, domain=None, range=Optional[Union[str, list[str]]])

slots.number_of_steps = Slot(uri=CATCORE.number_of_steps, name="number_of_steps", curie=CATCORE.curie('number_of_steps'),
                   model_uri=CATCORE.number_of_steps, domain=None, range=Optional[Union[int, list[int]]])

slots.lattice_size_type = Slot(uri=CATCORE.lattice_size_type, name="lattice_size_type", curie=CATCORE.curie('lattice_size_type'),
                   model_uri=CATCORE.lattice_size_type, domain=None, range=Optional[Union[str, list[str]]])

slots.acceptance_criteria = Slot(uri=CATCORE.acceptance_criteria, name="acceptance_criteria", curie=CATCORE.curie('acceptance_criteria'),
                   model_uri=CATCORE.acceptance_criteria, domain=None, range=Optional[Union[str, list[str]]])

slots.equilibration_steps = Slot(uri=CATCORE.equilibration_steps, name="equilibration_steps", curie=CATCORE.curie('equilibration_steps'),
                   model_uri=CATCORE.equilibration_steps, domain=None, range=Optional[Union[int, list[int]]])

slots.sampling_interval = Slot(uri=CATCORE.sampling_interval, name="sampling_interval", curie=CATCORE.curie('sampling_interval'),
                   model_uri=CATCORE.sampling_interval, domain=None, range=Optional[Union[int, list[int]]])

slots.formation_energy = Slot(uri=CATCORE.formation_energy, name="formation_energy", curie=CATCORE.curie('formation_energy'),
                   model_uri=CATCORE.formation_energy, domain=None, range=Optional[Union[float, list[float]]])

slots.reference_energies = Slot(uri=CATCORE.reference_energies, name="reference_energies", curie=CATCORE.curie('reference_energies'),
                   model_uri=CATCORE.reference_energies, domain=None, range=Optional[Union[str, list[str]]])

slots.energy_above_hull = Slot(uri=CATCORE.energy_above_hull, name="energy_above_hull", curie=CATCORE.curie('energy_above_hull'),
                   model_uri=CATCORE.energy_above_hull, domain=None, range=Optional[Union[float, list[float]]])

slots.phase_diagram_type = Slot(uri=CATCORE.phase_diagram_type, name="phase_diagram_type", curie=CATCORE.curie('phase_diagram_type'),
                   model_uri=CATCORE.phase_diagram_type, domain=None, range=Optional[Union[str, list[str]]])

slots.competing_phases = Slot(uri=CATCORE.competing_phases, name="competing_phases", curie=CATCORE.curie('competing_phases'),
                   model_uri=CATCORE.competing_phases, domain=None, range=Optional[Union[str, list[str]]])

slots.piezoelectric_tensor = Slot(uri=CATCORE.piezoelectric_tensor, name="piezoelectric_tensor", curie=CATCORE.curie('piezoelectric_tensor'),
                   model_uri=CATCORE.piezoelectric_tensor, domain=None, range=Optional[Union[str, list[str]]])

slots.crystal_symmetry = Slot(uri=CATCORE.crystal_symmetry, name="crystal_symmetry", curie=CATCORE.curie('crystal_symmetry'),
                   model_uri=CATCORE.crystal_symmetry, domain=None, range=Optional[Union[str, list[str]]])

slots.strain_applied = Slot(uri=CATCORE.strain_applied, name="strain_applied", curie=CATCORE.curie('strain_applied'),
                   model_uri=CATCORE.strain_applied, domain=None, range=Optional[Union[float, list[float]]])

slots.ionic_electronic_contributions = Slot(uri=CATCORE.ionic_electronic_contributions, name="ionic_electronic_contributions", curie=CATCORE.curie('ionic_electronic_contributions'),
                   model_uri=CATCORE.ionic_electronic_contributions, domain=None, range=Optional[Union[str, list[str]]])

slots.elastic_tensor = Slot(uri=CATCORE.elastic_tensor, name="elastic_tensor", curie=CATCORE.curie('elastic_tensor'),
                   model_uri=CATCORE.elastic_tensor, domain=None, range=Optional[Union[str, list[str]]])

slots.bulk_modulus = Slot(uri=CATCORE.bulk_modulus, name="bulk_modulus", curie=CATCORE.curie('bulk_modulus'),
                   model_uri=CATCORE.bulk_modulus, domain=None, range=Optional[Union[float, list[float]]])

slots.shear_modulus = Slot(uri=CATCORE.shear_modulus, name="shear_modulus", curie=CATCORE.curie('shear_modulus'),
                   model_uri=CATCORE.shear_modulus, domain=None, range=Optional[Union[float, list[float]]])

slots.poisson_ratio = Slot(uri=CATCORE.poisson_ratio, name="poisson_ratio", curie=CATCORE.curie('poisson_ratio'),
                   model_uri=CATCORE.poisson_ratio, domain=None, range=Optional[Union[float, list[float]]])

slots.young_modulus = Slot(uri=CATCORE.young_modulus, name="young_modulus", curie=CATCORE.curie('young_modulus'),
                   model_uri=CATCORE.young_modulus, domain=None, range=Optional[Union[float, list[float]]])

slots.surface_energy = Slot(uri=CATCORE.surface_energy, name="surface_energy", curie=CATCORE.curie('surface_energy'),
                   model_uri=CATCORE.surface_energy, domain=None, range=Optional[Union[float, list[float]]])

slots.miller_indices = Slot(uri=CATCORE.miller_indices, name="miller_indices", curie=CATCORE.curie('miller_indices'),
                   model_uri=CATCORE.miller_indices, domain=None, range=Optional[Union[str, list[str]]])

slots.slab_thickness = Slot(uri=CATCORE.slab_thickness, name="slab_thickness", curie=CATCORE.curie('slab_thickness'),
                   model_uri=CATCORE.slab_thickness, domain=None, range=Optional[Union[float, list[float]]])

slots.vacuum_spacing = Slot(uri=CATCORE.vacuum_spacing, name="vacuum_spacing", curie=CATCORE.curie('vacuum_spacing'),
                   model_uri=CATCORE.vacuum_spacing, domain=None, range=Optional[Union[float, list[float]]])

slots.surface_termination_method = Slot(uri=CATCORE.surface_termination_method, name="surface_termination_method", curie=CATCORE.curie('surface_termination_method'),
                   model_uri=CATCORE.surface_termination_method, domain=None, range=Optional[Union[str, list[str]]])

slots.material_composition = Slot(uri=CATCORE.material_composition, name="material_composition", curie=CATCORE.curie('material_composition'),
                   model_uri=CATCORE.material_composition, domain=None, range=Optional[Union[str, list[str]]])

slots.crystal_structure = Slot(uri=SIO['001100'], name="crystal_structure", curie=SIO.curie('001100'),
                   model_uri=CATCORE.crystal_structure, domain=None, range=Optional[Union[str, list[str]]])

slots.k_point_mesh = Slot(uri=CATCORE.k_point_mesh, name="k_point_mesh", curie=CATCORE.curie('k_point_mesh'),
                   model_uri=CATCORE.k_point_mesh, domain=None, range=Optional[Union[str, list[str]]])

slots.force_constant_method = Slot(uri=CATCORE.force_constant_method, name="force_constant_method", curie=CATCORE.curie('force_constant_method'),
                   model_uri=CATCORE.force_constant_method, domain=None, range=Optional[Union[str, list[str]]])

slots.kq_point_mesh = Slot(uri=CATCORE.kq_point_mesh, name="kq_point_mesh", curie=CATCORE.curie('kq_point_mesh'),
                   model_uri=CATCORE.kq_point_mesh, domain=None, range=Optional[Union[str, list[str]]])

slots.smearing_parameter = Slot(uri=CATCORE.smearing_parameter, name="smearing_parameter", curie=CATCORE.curie('smearing_parameter'),
                   model_uri=CATCORE.smearing_parameter, domain=None, range=Optional[Union[float, list[float]]])

slots.imaginary_modes = Slot(uri=CATCORE.imaginary_modes, name="imaginary_modes", curie=CATCORE.curie('imaginary_modes'),
                   model_uri=CATCORE.imaginary_modes, domain=None, range=Optional[Union[Union[bool, Bool], list[Union[bool, Bool]]]])

slots.fit_method = Slot(uri=CATCORE.fit_method, name="fit_method", curie=CATCORE.curie('fit_method'),
                   model_uri=CATCORE.fit_method, domain=None, range=Optional[Union[str, list[str]]])

slots.pressure_derivative = Slot(uri=CATCORE.pressure_derivative, name="pressure_derivative", curie=CATCORE.curie('pressure_derivative'),
                   model_uri=CATCORE.pressure_derivative, domain=None, range=Optional[Union[float, list[float]]])

slots.fit_residuals = Slot(uri=CATCORE.fit_residuals, name="fit_residuals", curie=CATCORE.curie('fit_residuals'),
                   model_uri=CATCORE.fit_residuals, domain=None, range=Optional[Union[float, list[float]]])

slots.ph_range = Slot(uri=CATCORE.ph_range, name="ph_range", curie=CATCORE.curie('ph_range'),
                   model_uri=CATCORE.ph_range, domain=None, range=Optional[Union[str, list[str]]])

slots.potential_range = Slot(uri=CATCORE.potential_range, name="potential_range", curie=CATCORE.curie('potential_range'),
                   model_uri=CATCORE.potential_range, domain=None, range=Optional[Union[str, list[str]]])

slots.solvation_model = Slot(uri=CATCORE.solvation_model, name="solvation_model", curie=CATCORE.curie('solvation_model'),
                   model_uri=CATCORE.solvation_model, domain=None, range=Optional[Union[str, list[str]]])

slots.ionic_strength = Slot(uri=CATCORE.ionic_strength, name="ionic_strength", curie=CATCORE.curie('ionic_strength'),
                   model_uri=CATCORE.ionic_strength, domain=None, range=Optional[Union[float, list[float]]])

slots.grain_boundary_plane = Slot(uri=CATCORE.grain_boundary_plane, name="grain_boundary_plane", curie=CATCORE.curie('grain_boundary_plane'),
                   model_uri=CATCORE.grain_boundary_plane, domain=None, range=Optional[Union[str, list[str]]])

slots.misorientation_angle = Slot(uri=CATCORE.misorientation_angle, name="misorientation_angle", curie=CATCORE.curie('misorientation_angle'),
                   model_uri=CATCORE.misorientation_angle, domain=None, range=Optional[Union[float, list[float]]])

slots.grain_boundary_energy = Slot(uri=CATCORE.grain_boundary_energy, name="grain_boundary_energy", curie=CATCORE.curie('grain_boundary_energy'),
                   model_uri=CATCORE.grain_boundary_energy, domain=None, range=Optional[Union[float, list[float]]])

slots.simulation_cell_size = Slot(uri=CATCORE.simulation_cell_size, name="simulation_cell_size", curie=CATCORE.curie('simulation_cell_size'),
                   model_uri=CATCORE.simulation_cell_size, domain=None, range=Optional[Union[str, list[str]]])

slots.gb_excess_volume = Slot(uri=CATCORE.gb_excess_volume, name="gb_excess_volume", curie=CATCORE.curie('gb_excess_volume'),
                   model_uri=CATCORE.gb_excess_volume, domain=None, range=Optional[Union[float, list[float]]])

slots.gb_structural_units = Slot(uri=CATCORE.gb_structural_units, name="gb_structural_units", curie=CATCORE.curie('gb_structural_units'),
                   model_uri=CATCORE.gb_structural_units, domain=None, range=Optional[Union[str, list[str]]])

slots.charge_defect_segregation = Slot(uri=CATCORE.charge_defect_segregation, name="charge_defect_segregation", curie=CATCORE.curie('charge_defect_segregation'),
                   model_uri=CATCORE.charge_defect_segregation, domain=None, range=Optional[Union[str, list[str]]])

slots.smearing_method = Slot(uri=CATCORE.smearing_method, name="smearing_method", curie=CATCORE.curie('smearing_method'),
                   model_uri=CATCORE.smearing_method, domain=None, range=Optional[Union[str, list[str]]])

slots.spin_polarized = Slot(uri=CATCORE.spin_polarized, name="spin_polarized", curie=CATCORE.curie('spin_polarized'),
                   model_uri=CATCORE.spin_polarized, domain=None, range=Optional[Union[Union[bool, Bool], list[Union[bool, Bool]]]])

slots.band_path = Slot(uri=CATCORE.band_path, name="band_path", curie=CATCORE.curie('band_path'),
                   model_uri=CATCORE.band_path, domain=None, range=Optional[Union[str, list[str]]])

slots.fermi_energy = Slot(uri=CATCORE.fermi_energy, name="fermi_energy", curie=CATCORE.curie('fermi_energy'),
                   model_uri=CATCORE.fermi_energy, domain=None, range=Optional[Union[float, list[float]]])

slots.polarization_direction = Slot(uri=CATCORE.polarization_direction, name="polarization_direction", curie=CATCORE.curie('polarization_direction'),
                   model_uri=CATCORE.polarization_direction, domain=None, range=Optional[Union[str, list[str]]])

slots.spontaneous_polarization = Slot(uri=CATCORE.spontaneous_polarization, name="spontaneous_polarization", curie=CATCORE.curie('spontaneous_polarization'),
                   model_uri=CATCORE.spontaneous_polarization, domain=None, range=Optional[Union[float, list[float]]])

slots.reference_structure = Slot(uri=CATCORE.reference_structure, name="reference_structure", curie=CATCORE.curie('reference_structure'),
                   model_uri=CATCORE.reference_structure, domain=None, range=Optional[Union[str, list[str]]])

slots.switching_barrier = Slot(uri=CATCORE.switching_barrier, name="switching_barrier", curie=CATCORE.curie('switching_barrier'),
                   model_uri=CATCORE.switching_barrier, domain=None, range=Optional[Union[float, list[float]]])

slots.coercive_field = Slot(uri=CATCORE.coercive_field, name="coercive_field", curie=CATCORE.curie('coercive_field'),
                   model_uri=CATCORE.coercive_field, domain=None, range=Optional[Union[float, list[float]]])

slots.temperature_dependence = Slot(uri=CATCORE.temperature_dependence, name="temperature_dependence", curie=CATCORE.curie('temperature_dependence'),
                   model_uri=CATCORE.temperature_dependence, domain=None, range=Optional[Union[str, list[str]]])

slots.material_sample = Slot(uri=VOC4CAT['0005056'], name="material_sample", curie=VOC4CAT.curie('0005056'),
                   model_uri=CATCORE.material_sample, domain=None, range=Optional[Union[str, list[str]]])

slots.structure_model = Slot(uri=CATCORE.structure_model, name="structure_model", curie=CATCORE.curie('structure_model'),
                   model_uri=CATCORE.structure_model, domain=None, range=Optional[Union[str, list[str]]])

slots.smearing_broadening = Slot(uri=CATCORE.smearing_broadening, name="smearing_broadening", curie=CATCORE.curie('smearing_broadening'),
                   model_uri=CATCORE.smearing_broadening, domain=None, range=Optional[Union[float, list[float]]])

slots.direct_indirect = Slot(uri=CATCORE.direct_indirect, name="direct_indirect", curie=CATCORE.curie('direct_indirect'),
                   model_uri=CATCORE.direct_indirect, domain=None, range=Optional[Union[str, list[str]]])

slots.experimental_reference = Slot(uri=CATCORE.experimental_reference, name="experimental_reference", curie=CATCORE.curie('experimental_reference'),
                   model_uri=CATCORE.experimental_reference, domain=None, range=Optional[Union[float, list[float]]])

slots.gw_hybrid_correction = Slot(uri=CATCORE.gw_hybrid_correction, name="gw_hybrid_correction", curie=CATCORE.curie('gw_hybrid_correction'),
                   model_uri=CATCORE.gw_hybrid_correction, domain=None, range=Optional[Union[Union[bool, Bool], list[Union[bool, Bool]]]])

slots.excitonic_correction = Slot(uri=CATCORE.excitonic_correction, name="excitonic_correction", curie=CATCORE.curie('excitonic_correction'),
                   model_uri=CATCORE.excitonic_correction, domain=None, range=Optional[Union[float, list[float]]])

slots.bubble_size_distribution = Slot(uri=CATCORE.bubble_size_distribution, name="bubble_size_distribution", curie=CATCORE.curie('bubble_size_distribution'),
                   model_uri=CATCORE.bubble_size_distribution, domain=None, range=Optional[str])

slots.CatCore_catalysis_research_field = Slot(uri=VOC4CAT['0000196'], name="CatCore_catalysis_research_field", curie=VOC4CAT.curie('0000196'),
                   model_uri=CATCORE.CatCore_catalysis_research_field, domain=CatCore, range=Union[str, "CatalysisResearchFieldEnum"])

slots.CatCore_reaction_type = Slot(uri=VOC4CAT['0007010'], name="CatCore_reaction_type", curie=VOC4CAT.curie('0007010'),
                   model_uri=CATCORE.CatCore_reaction_type, domain=CatCore, range=str)

slots.CatCore_active_site = Slot(uri=VOC4CAT['0007006'], name="CatCore_active_site", curie=VOC4CAT.curie('0007006'),
                   model_uri=CATCORE.CatCore_active_site, domain=CatCore, range=Optional[str])

slots.Synthesis_nominal_composition = Slot(uri=CATCORE.nominal_composition, name="Synthesis_nominal_composition", curie=CATCORE.curie('nominal_composition'),
                   model_uri=CATCORE.Synthesis_nominal_composition, domain=Synthesis, range=str)

slots.Synthesis_catalyst_measured_properties = Slot(uri=CATCORE.catalyst_measured_properties, name="Synthesis_catalyst_measured_properties", curie=CATCORE.curie('catalyst_measured_properties'),
                   model_uri=CATCORE.Synthesis_catalyst_measured_properties, domain=Synthesis, range=str)

slots.Synthesis_precursor = Slot(uri=CATCORE.precursor, name="Synthesis_precursor", curie=CATCORE.curie('precursor'),
                   model_uri=CATCORE.Synthesis_precursor, domain=Synthesis, range=Union[Union[dict, "Precursor"], list[Union[dict, "Precursor"]]])

slots.Synthesis_preparation_method = Slot(uri=VOC4CAT['0007016'], name="Synthesis_preparation_method", curie=VOC4CAT.curie('0007016'),
                   model_uri=CATCORE.Synthesis_preparation_method, domain=Synthesis, range=Union[Union[dict, "PreparationMethod"], list[Union[dict, "PreparationMethod"]]])

slots.Synthesis_storage_conditions = Slot(uri=CATCORE.storage_conditions, name="Synthesis_storage_conditions", curie=CATCORE.curie('storage_conditions'),
                   model_uri=CATCORE.Synthesis_storage_conditions, domain=Synthesis, range=Optional[Union[str, list[str]]])

slots.Precursor_precursor_quantity = Slot(uri=CATCORE.precursor_quantity, name="Precursor_precursor_quantity", curie=CATCORE.curie('precursor_quantity'),
                   model_uri=CATCORE.Precursor_precursor_quantity, domain=Precursor, range=Union[float, list[float]])

slots.Characterization_equipment = Slot(uri=VOC4CAT['0000187'], name="Characterization_equipment", curie=VOC4CAT.curie('0000187'),
                   model_uri=CATCORE.Characterization_equipment, domain=Characterization, range=Union[str, list[str]])

slots.Characterization_characterization_technique = Slot(uri=VOC4CAT['0000066'], name="Characterization_characterization_technique", curie=VOC4CAT.curie('0000066'),
                   model_uri=CATCORE.Characterization_characterization_technique, domain=Characterization, range=Union[Union[dict, "CharacterizationTechnique"], list[Union[dict, "CharacterizationTechnique"]]])

slots.Reaction_catalyst_quantity = Slot(uri=CATCORE.catalyst_quantity, name="Reaction_catalyst_quantity", curie=CATCORE.curie('catalyst_quantity'),
                   model_uri=CATCORE.Reaction_catalyst_quantity, domain=Reaction, range=Union[float, list[float]])

slots.Reaction_reactor_design_type = Slot(uri=VOC4CAT['0007018'], name="Reaction_reactor_design_type", curie=VOC4CAT.curie('0007018'),
                   model_uri=CATCORE.Reaction_reactor_design_type, domain=Reaction, range=Union[Union[dict, "ReactorDesignType"], list[Union[dict, "ReactorDesignType"]]])

slots.Reaction_reactant = Slot(uri=VOC4CAT['0000101'], name="Reaction_reactant", curie=VOC4CAT.curie('0000101'),
                   model_uri=CATCORE.Reaction_reactant, domain=Reaction, range=Union[str, list[str]])

slots.Reaction_operation_parameters = Slot(uri=VOC4CAT['0000142'], name="Reaction_operation_parameters", curie=VOC4CAT.curie('0000142'),
                   model_uri=CATCORE.Reaction_operation_parameters, domain=Reaction, range=Union[Union[dict, "OperationParameters"], list[Union[dict, "OperationParameters"]]])

slots.Reaction_product_identification_method = Slot(uri=VOC4CAT['0000129'], name="Reaction_product_identification_method", curie=VOC4CAT.curie('0000129'),
                   model_uri=CATCORE.Reaction_product_identification_method, domain=Reaction, range=Union[Union[dict, "ProductIdentificationMethod"], list[Union[dict, "ProductIdentificationMethod"]]])

slots.Reaction_catalyst_type = Slot(uri=VOC4CAT['0007014'], name="Reaction_catalyst_type", curie=VOC4CAT.curie('0007014'),
                   model_uri=CATCORE.Reaction_catalyst_type, domain=Reaction, range=Optional[Union[str, list[str]]])

slots.Simulation_software_package = Slot(uri=CATCORE.software_package, name="Simulation_software_package", curie=CATCORE.curie('software_package'),
                   model_uri=CATCORE.Simulation_software_package, domain=Simulation, range=Union[str, list[str]])

slots.Simulation_simulation_method = Slot(uri=CATCORE.simulation_method, name="Simulation_simulation_method", curie=CATCORE.curie('simulation_method'),
                   model_uri=CATCORE.Simulation_simulation_method, domain=Simulation, range=Union[Union[dict, "SimulationMethod"], list[Union[dict, "SimulationMethod"]]])

slots.Simulation_calculated_property = Slot(uri=CATCORE.calculated_property, name="Simulation_calculated_property", curie=CATCORE.curie('calculated_property'),
                   model_uri=CATCORE.Simulation_calculated_property, domain=Simulation, range=Union[Union[dict, "CalculatedProperty"], list[Union[dict, "CalculatedProperty"]]])
