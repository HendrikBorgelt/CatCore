from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "None"
version = "1.0.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )

    @model_serializer(mode='wrap', when_used='unless-none')
    def treat_empty_lists_as_none(
            self, handler: SerializerFunctionWrapHandler,
            info: SerializationInfo) -> dict[str, Any]:
        if info.exclude_none:
            _instance = self.model_copy()
            for field, field_info in type(_instance).model_fields.items():
                if getattr(_instance, field) == [] and not(
                        field_info.is_required()):
                    setattr(_instance, field, None)
        else:
            _instance = self
        return handler(_instance, info)



class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'catcore',
     'default_range': 'string',
     'description': 'The CatCore describes the minimum information which must be '
                    'reported with research data \n'
                    'concerning the field of catalysis. This guideline helps to '
                    'handle and standardize data \n'
                    'based on the FAIR principle (Findable, Accessible, '
                    'Interoperable, Reusable).',
     'id': 'https://w3id.org/nfdi4cat/catcore',
     'imports': ['linkml:types'],
     'license': 'CC-BY-4.0',
     'name': 'catcore-metadata',
     'prefixes': {'AFP': {'prefix_prefix': 'AFP',
                          'prefix_reference': 'http://purl.allotrope.org/ontologies/process#AFP_'},
                  'AFQ': {'prefix_prefix': 'AFQ',
                          'prefix_reference': 'http://purl.allotrope.org/ontologies/quality#AFQ_'},
                  'AFR': {'prefix_prefix': 'AFR',
                          'prefix_reference': 'http://purl.allotrope.org/ontologies/result#AFR_'},
                  'AFRL': {'prefix_prefix': 'AFRL',
                           'prefix_reference': 'http://purl.allotrope.org/ontologies/role#AFRL_'},
                  'APOLLO_SV': {'prefix_prefix': 'APOLLO_SV',
                                'prefix_reference': 'http://purl.obolibrary.org/obo/APOLLO_SV_'},
                  'CHMO': {'prefix_prefix': 'CHMO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/CHMO_'},
                  'NCIT': {'prefix_prefix': 'NCIT',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/NCIT_'},
                  'OBI': {'prefix_prefix': 'OBI',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/OBI_'},
                  'SIO': {'prefix_prefix': 'SIO',
                          'prefix_reference': 'http://semanticscience.org/resource/SIO_'},
                  'catcore': {'prefix_prefix': 'catcore',
                              'prefix_reference': 'https://w3id.org/nfdi4cat/catcore/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nmrCV': {'prefix_prefix': 'nmrCV',
                            'prefix_reference': 'http://nmrML.org/nmrCV#NMR:'},
                  'voc4cat': {'prefix_prefix': 'voc4cat',
                              'prefix_reference': 'https://w3id.org/nfdi4cat/voc4cat_'}},
     'source_file': 'src/catcore/schema/catcore.yaml',
     'title': 'CatCore Metadata Reference Model'} )

class CatalysisResearchFieldEnum(str, Enum):
    """
    Enumeration of catalysis research fields
    """
    heterogeneous_catalysis = "heterogeneous_catalysis"
    """
    Heterogeneous catalysis
    """
    homogeneous_catalysis = "homogeneous_catalysis"
    """
    Homogeneous catalysis
    """
    biocatalysis = "biocatalysis"
    """
    Biocatalysis
    """
    electrocatalysis = "electrocatalysis"
    """
    Electrocatalysis
    """
    hybrid_catalysis = "hybrid_catalysis"
    """
    Hybrid catalysis
    """
    other = "other"
    """
    Other catalysis research field
    """


class ImpregnationTypeEnum(str, Enum):
    """
    Enumeration of impregnation types
    """
    wet_impregnation = "wet_impregnation"
    """
    Wet impregnation method
    """
    dry_impregnation = "dry_impregnation"
    """
    Dry impregnation method
    """
    incipient_wetness = "incipient_wetness"
    """
    Incipient wetness impregnation
    """
    other = "other"
    """
    Other impregnation type
    """


class SampleStateEnum(str, Enum):
    """
    Enumeration of sample states
    """
    solid = "solid"
    """
    Solid state
    """
    liquid = "liquid"
    """
    Liquid state
    """
    gas = "gas"
    """
    Gas state
    """
    solution = "solution"
    """
    Solution state
    """
    powder = "powder"
    """
    Powder form
    """
    pellet = "pellet"
    """
    Pellet form
    """
    thin_film = "thin_film"
    """
    Thin film
    """
    other = "other"
    """
    Other sample state
    """



class CatCoreEntity(ConfiguredBaseModel):
    """
    Root class for all CatCore entities
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class CatCore(CatCoreEntity):
    """
    The CatCore describes the minimum information which must be reported with research data 
    concerning the field of catalysis.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/nfdi4cat/catcore',
         'slot_usage': {'active_site': {'multivalued': False,
                                        'name': 'active_site',
                                        'required': False},
                        'catalysis_research_field': {'multivalued': False,
                                                     'name': 'catalysis_research_field',
                                                     'required': True},
                        'reaction_type': {'multivalued': False,
                                          'name': 'reaction_type',
                                          'required': True}}})

    catalysis_research_field: CatalysisResearchFieldEnum = Field(default=..., description="""Field of catalysis research""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCore'], 'slot_uri': 'voc4cat:0000196'} })
    reaction_type: str = Field(default=..., description="""Type of reaction""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCore'], 'slot_uri': 'voc4cat:0007010'} })
    active_site: Optional[str] = Field(default=None, description="""Active site of the catalyst""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCore'], 'recommended': True, 'slot_uri': 'voc4cat:0007006'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class Synthesis(CatCoreEntity):
    """
    The data class 'Synthesis' describes the minimum information which should be reported 
    with research data concerning the field of catalyst synthesis.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/nfdi4cat/catcore',
         'slot_usage': {'catalyst_measured_properties': {'name': 'catalyst_measured_properties',
                                                         'required': True},
                        'nominal_composition': {'name': 'nominal_composition',
                                                'required': True},
                        'precursor': {'name': 'precursor', 'required': True},
                        'preparation_method': {'name': 'preparation_method',
                                               'required': True},
                        'storage_conditions': {'name': 'storage_conditions',
                                               'recommended': True,
                                               'required': False}}})

    nominal_composition: str = Field(default=..., description="""Nominal composition of the catalyst""", json_schema_extra = { "linkml_meta": {'domain_of': ['Synthesis'], 'slot_uri': 'catcore:nominal_composition'} })
    catalyst_measured_properties: str = Field(default=..., description="""Measured properties of the catalyst (e.g., BET, sieve fraction, molar ratio)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Synthesis'], 'slot_uri': 'catcore:catalyst_measured_properties'} })
    precursor: list[Precursor] = Field(default=..., description="""Precursor material used in synthesis""", json_schema_extra = { "linkml_meta": {'domain_of': ['Synthesis'], 'slot_uri': 'catcore:precursor'} })
    preparation_method: list[PreparationMethod] = Field(default=..., description="""Method used for catalyst preparation""", json_schema_extra = { "linkml_meta": {'domain_of': ['Synthesis'], 'slot_uri': 'voc4cat:0007016'} })
    storage_conditions: Optional[list[str]] = Field(default=[], description="""Conditions for storage""", json_schema_extra = { "linkml_meta": {'domain_of': ['Synthesis'],
         'recommended': True,
         'slot_uri': 'catcore:storage_conditions'} })
    support: Optional[list[str]] = Field(default=[], description="""Support material""", json_schema_extra = { "linkml_meta": {'domain_of': ['Synthesis'], 'slot_uri': 'catcore:support'} })
    solvent: Optional[list[str]] = Field(default=[], description="""Solvent used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Synthesis',
                       'NMRSpectroscopy',
                       'UVVisSpectroscopy',
                       'DynamicLightScattering'],
         'slot_uri': 'voc4cat:0007246'} })
    sample_pretreatment: Optional[list[str]] = Field(default=[], description="""Pre-treatment of sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['Synthesis', 'Characterization'], 'slot_uri': 'voc4cat:0000122'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class Precursor(CatCoreEntity):
    """
    Precursor material used in catalyst synthesis
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/nfdi4cat/catcore',
         'slot_usage': {'precursor_quantity': {'name': 'precursor_quantity',
                                               'required': True}}})

    precursor_quantity: list[float] = Field(default=..., description="""Quantity of precursor used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Precursor'],
         'slot_uri': 'catcore:precursor_quantity',
         'unit': {'ucum_code': 'g'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class PreparationMethod(CatCoreEntity):
    """
    Method used for catalyst preparation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class Impregnation(PreparationMethod):
    """
    Impregnation method for catalyst preparation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:Impregnation',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    impregnation_type: Optional[list[ImpregnationTypeEnum]] = Field(default=[], description="""Type of impregnation method""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation'], 'slot_uri': 'catcore:impregnation_type'} })
    impregnation_duration: Optional[list[float]] = Field(default=[], description="""Duration of impregnation process""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation'],
         'slot_uri': 'catcore:impregnation_duration',
         'unit': {'ucum_code': 'h'}} })
    impregnation_temperature: Optional[list[float]] = Field(default=[], description="""Temperature during impregnation""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation'],
         'slot_uri': 'catcore:impregnation_temperature',
         'unit': {'ucum_code': 'Cel'}} })
    drying_device: Optional[list[str]] = Field(default=[], description="""Device used for drying""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'MolecularSynthesis'],
         'slot_uri': 'catcore:drying_device'} })
    drying_temperature: Optional[list[float]] = Field(default=[], description="""Temperature during drying""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'MolecularSynthesis'],
         'slot_uri': 'catcore:drying_temperature',
         'unit': {'ucum_code': 'Cel'}} })
    drying_time: Optional[list[float]] = Field(default=[], description="""Duration of drying process""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'MolecularSynthesis'],
         'slot_uri': 'catcore:drying_time',
         'unit': {'ucum_code': 'h'}} })
    drying_atmosphere: Optional[list[str]] = Field(default=[], description="""Atmosphere during drying""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis'],
         'slot_uri': 'catcore:drying_atmosphere'} })
    calcination_initial_temperature: Optional[list[float]] = Field(default=[], description="""Initial temperature for calcination""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000057',
         'unit': {'ucum_code': 'Cel'}} })
    calcination_final_temperature: Optional[list[float]] = Field(default=[], description="""Final temperature for calcination""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000058',
         'unit': {'ucum_code': 'Cel'}} })
    calcination_dwelling_time: Optional[list[float]] = Field(default=[], description="""Dwelling time at calcination temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000060',
         'unit': {'ucum_code': 'h'}} })
    number_of_cycles: Optional[list[int]] = Field(default=[], description="""Number of cycles in the process""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'AtomicLayerDeposition',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'MolecularSynthesis',
                       'XRayAbsorptionSpectroscopy',
                       'CyclicVoltammetry'],
         'slot_uri': 'catcore:number_of_cycles'} })
    calcination_gaseous_environment: Optional[list[str]] = Field(default=[], description="""Gaseous environment during calcination""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000055'} })
    calcination_heating_rate: Optional[list[float]] = Field(default=[], description="""Heating rate during calcination""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000059',
         'unit': {'ucum_code': 'Cel/min'}} })
    calcination_gas_flow_rate: Optional[list[float]] = Field(default=[], description="""Gas flow rate during calcination""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000056',
         'unit': {'ucum_code': 'mL/min'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class CoPrecipitation(PreparationMethod):
    """
    Co-precipitation method for catalyst preparation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:CoPrecipitation',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    precipitating_agent: Optional[list[str]] = Field(default=[], description="""Agent used for precipitation""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoPrecipitation', 'DepositionPrecipitation'],
         'slot_uri': 'catcore:precipitating_agent'} })
    precipitating_concentration: Optional[list[float]] = Field(default=[], description="""Concentration of precipitating agent""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoPrecipitation'],
         'slot_uri': 'catcore:precipitating_concentration',
         'unit': {'ucum_code': 'mol/L'}} })
    synthesis_ph: Optional[list[float]] = Field(default=[], description="""pH during synthesis""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoPrecipitation', 'DepositionPrecipitation'],
         'slot_uri': 'voc4cat:0000052'} })
    mixing_rate: Optional[list[float]] = Field(default=[], description="""Rate of mixing""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoPrecipitation', 'DepositionPrecipitation'],
         'slot_uri': 'catcore:mixing_rate',
         'unit': {'ucum_code': 'rpm'}} })
    mixing_time: Optional[list[float]] = Field(default=[], description="""Duration of mixing""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoPrecipitation', 'DepositionPrecipitation'],
         'slot_uri': 'catcore:mixing_time',
         'unit': {'ucum_code': 'h'}} })
    mixing_temperature: Optional[list[float]] = Field(default=[], description="""Temperature during mixing""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoPrecipitation',
                       'DepositionPrecipitation',
                       'MolecularSynthesis'],
         'slot_uri': 'catcore:mixing_temperature',
         'unit': {'ucum_code': 'Cel'}} })
    drying_device: Optional[list[str]] = Field(default=[], description="""Device used for drying""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'MolecularSynthesis'],
         'slot_uri': 'catcore:drying_device'} })
    drying_temperature: Optional[list[float]] = Field(default=[], description="""Temperature during drying""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'MolecularSynthesis'],
         'slot_uri': 'catcore:drying_temperature',
         'unit': {'ucum_code': 'Cel'}} })
    drying_time: Optional[list[float]] = Field(default=[], description="""Duration of drying process""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'MolecularSynthesis'],
         'slot_uri': 'catcore:drying_time',
         'unit': {'ucum_code': 'h'}} })
    drying_atmosphere: Optional[list[str]] = Field(default=[], description="""Atmosphere during drying""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis'],
         'slot_uri': 'catcore:drying_atmosphere'} })
    calcination_initial_temperature: Optional[list[float]] = Field(default=[], description="""Initial temperature for calcination""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000057',
         'unit': {'ucum_code': 'Cel'}} })
    calcination_final_temperature: Optional[list[float]] = Field(default=[], description="""Final temperature for calcination""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000058',
         'unit': {'ucum_code': 'Cel'}} })
    calcination_dwelling_time: Optional[list[float]] = Field(default=[], description="""Dwelling time at calcination temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000060',
         'unit': {'ucum_code': 'h'}} })
    number_of_cycles: Optional[list[int]] = Field(default=[], description="""Number of cycles in the process""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'AtomicLayerDeposition',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'MolecularSynthesis',
                       'XRayAbsorptionSpectroscopy',
                       'CyclicVoltammetry'],
         'slot_uri': 'catcore:number_of_cycles'} })
    calcination_gaseous_environment: Optional[list[str]] = Field(default=[], description="""Gaseous environment during calcination""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000055'} })
    calcination_heating_rate: Optional[list[float]] = Field(default=[], description="""Heating rate during calcination""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000059',
         'unit': {'ucum_code': 'Cel/min'}} })
    calcination_gas_flow_rate: Optional[list[float]] = Field(default=[], description="""Gas flow rate during calcination""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000056',
         'unit': {'ucum_code': 'mL/min'}} })
    order_of_addition: Optional[list[str]] = Field(default=[], description="""Order in which components are added""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoPrecipitation', 'DepositionPrecipitation'],
         'slot_uri': 'catcore:order_of_addition'} })
    filtration: Optional[list[str]] = Field(default=[], description="""Filtration method used""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoPrecipitation', 'DepositionPrecipitation'],
         'slot_uri': 'catcore:filtration'} })
    purification: Optional[list[str]] = Field(default=[], description="""Purification method used""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoPrecipitation', 'DepositionPrecipitation'],
         'slot_uri': 'catcore:purification'} })
    aging_temperature: Optional[list[float]] = Field(default=[], description="""Temperature during aging""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoPrecipitation', 'DepositionPrecipitation'],
         'slot_uri': 'catcore:aging_temperature',
         'unit': {'ucum_code': 'Cel'}} })
    aging_time: Optional[list[float]] = Field(default=[], description="""Duration of aging process""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoPrecipitation', 'SolGel', 'DepositionPrecipitation'],
         'slot_uri': 'catcore:aging_time',
         'unit': {'ucum_code': 'h'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class SolGel(PreparationMethod):
    """
    Sol-gel method for catalyst preparation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:SolGel',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    hydrolysis_ratio: Optional[list[float]] = Field(default=[], description="""Ratio for hydrolysis""", json_schema_extra = { "linkml_meta": {'domain_of': ['SolGel'], 'slot_uri': 'catcore:hydrolysis_ratio'} })
    aging_time: Optional[list[float]] = Field(default=[], description="""Duration of aging process""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoPrecipitation', 'SolGel', 'DepositionPrecipitation'],
         'slot_uri': 'catcore:aging_time',
         'unit': {'ucum_code': 'h'}} })
    drying: Optional[list[str]] = Field(default=[], description="""Drying process description""", json_schema_extra = { "linkml_meta": {'domain_of': ['SolGel'], 'slot_uri': 'catcore:drying'} })
    surfactant_template: Optional[list[str]] = Field(default=[], description="""Surfactant template used""", json_schema_extra = { "linkml_meta": {'domain_of': ['SolGel'], 'slot_uri': 'catcore:surfactant_template'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class Solvothermal(PreparationMethod):
    """
    Solvothermal method for catalyst preparation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:Solvothermal',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    filling_volume: Optional[list[float]] = Field(default=[], description="""Filling volume of vessel""", json_schema_extra = { "linkml_meta": {'domain_of': ['Solvothermal'],
         'slot_uri': 'catcore:filling_volume',
         'unit': {'ucum_code': 'mL'}} })
    synthesis_temperature: Optional[list[float]] = Field(default=[], description="""Temperature during synthesis""", json_schema_extra = { "linkml_meta": {'domain_of': ['Solvothermal',
                       'PlasmaAssisted',
                       'MicrowaveAssisted',
                       'MechanochemicalSynthesis'],
         'slot_uri': 'voc4cat:0000051',
         'unit': {'ucum_code': 'Cel'}} })
    synthesis_duration: Optional[list[float]] = Field(default=[], description="""Duration of synthesis""", json_schema_extra = { "linkml_meta": {'domain_of': ['Solvothermal',
                       'MicrowaveAssisted',
                       'Sublimation',
                       'MolecularSynthesis'],
         'slot_uri': 'voc4cat:0000050',
         'unit': {'ucum_code': 'h'}} })
    vessel_type: Optional[list[str]] = Field(default=[], description="""Type of vessel used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Solvothermal', 'CombustionSynthesis', 'MicrowaveAssisted'],
         'slot_uri': 'catcore:vessel_type'} })
    equipment: Optional[list[str]] = Field(default=[], description="""Equipment used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Solvothermal',
                       'PlasmaAssisted',
                       'CombustionSynthesis',
                       'MicrowaveAssisted',
                       'MechanochemicalSynthesis',
                       'Characterization',
                       'ProductIdentificationMethod'],
         'slot_uri': 'voc4cat:0000187'} })
    stirring_speed: Optional[list[float]] = Field(default=[], description="""Speed of stirring""", json_schema_extra = { "linkml_meta": {'domain_of': ['Solvothermal', 'MolecularSynthesis'],
         'slot_uri': 'catcore:stirring_speed',
         'unit': {'ucum_code': 'rpm'}} })
    stirrer_type: Optional[list[str]] = Field(default=[], description="""Type of stirrer used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Solvothermal'], 'slot_uri': 'catcore:stirrer_type'} })
    cooling_rate: Optional[list[float]] = Field(default=[], description="""Rate of cooling""", json_schema_extra = { "linkml_meta": {'domain_of': ['Solvothermal'],
         'slot_uri': 'catcore:cooling_rate',
         'unit': {'ucum_code': 'Cel/min'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class PlasmaAssisted(PreparationMethod):
    """
    Plasma-assisted method for catalyst preparation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:PlasmaAssisted',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    plasma_type: Optional[list[str]] = Field(default=[], description="""Type of plasma used""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlasmaAssisted'], 'slot_uri': 'catcore:plasma_type'} })
    equipment: Optional[list[str]] = Field(default=[], description="""Equipment used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Solvothermal',
                       'PlasmaAssisted',
                       'CombustionSynthesis',
                       'MicrowaveAssisted',
                       'MechanochemicalSynthesis',
                       'Characterization',
                       'ProductIdentificationMethod'],
         'slot_uri': 'voc4cat:0000187'} })
    atmosphere: Optional[list[str]] = Field(default=[], description="""Atmospheric conditions""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlasmaAssisted',
                       'CombustionSynthesis',
                       'MechanochemicalSynthesis',
                       'MolecularSynthesis',
                       'PowderXRD',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'Thermogravimetry',
                       'XPS',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'OperationParameters'],
         'slot_uri': 'catcore:atmosphere'} })
    power_input: Optional[list[float]] = Field(default=[], description="""Power input for the process""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlasmaAssisted'],
         'slot_uri': 'catcore:power_input',
         'unit': {'ucum_code': 'W'}} })
    exposure_time: Optional[list[float]] = Field(default=[], description="""Time of exposure""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlasmaAssisted'],
         'slot_uri': 'catcore:exposure_time',
         'unit': {'ucum_code': 'min'}} })
    synthesis_pressure: Optional[list[float]] = Field(default=[], description="""Pressure during synthesis""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlasmaAssisted', 'Sublimation'],
         'slot_uri': 'voc4cat:0000053',
         'unit': {'ucum_code': 'bar'}} })
    synthesis_temperature: Optional[list[float]] = Field(default=[], description="""Temperature during synthesis""", json_schema_extra = { "linkml_meta": {'domain_of': ['Solvothermal',
                       'PlasmaAssisted',
                       'MicrowaveAssisted',
                       'MechanochemicalSynthesis'],
         'slot_uri': 'voc4cat:0000051',
         'unit': {'ucum_code': 'Cel'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class CombustionSynthesis(PreparationMethod):
    """
    Combustion synthesis method for catalyst preparation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:CombustionSynthesis',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    fuel: Optional[list[str]] = Field(default=[], description="""Fuel used in combustion""", json_schema_extra = { "linkml_meta": {'domain_of': ['CombustionSynthesis'], 'slot_uri': 'catcore:fuel'} })
    oxidizer: Optional[list[str]] = Field(default=[], description="""Oxidizer used""", json_schema_extra = { "linkml_meta": {'domain_of': ['CombustionSynthesis'], 'slot_uri': 'catcore:oxidizer'} })
    fuel_to_oxidizer_ratio: Optional[list[float]] = Field(default=[], description="""Ratio of fuel to oxidizer""", json_schema_extra = { "linkml_meta": {'domain_of': ['CombustionSynthesis'],
         'slot_uri': 'catcore:fuel_to_oxidizer_ratio'} })
    set_temperature: Optional[list[float]] = Field(default=[], description="""Set temperature for the process""", json_schema_extra = { "linkml_meta": {'domain_of': ['CombustionSynthesis'],
         'slot_uri': 'catcore:set_temperature',
         'unit': {'ucum_code': 'Cel'}} })
    post_treatment: Optional[list[str]] = Field(default=[], description="""Post-treatment process""", json_schema_extra = { "linkml_meta": {'domain_of': ['CombustionSynthesis'], 'slot_uri': 'catcore:post_treatment'} })
    atmosphere: Optional[list[str]] = Field(default=[], description="""Atmospheric conditions""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlasmaAssisted',
                       'CombustionSynthesis',
                       'MechanochemicalSynthesis',
                       'MolecularSynthesis',
                       'PowderXRD',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'Thermogravimetry',
                       'XPS',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'OperationParameters'],
         'slot_uri': 'catcore:atmosphere'} })
    vessel_type: Optional[list[str]] = Field(default=[], description="""Type of vessel used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Solvothermal', 'CombustionSynthesis', 'MicrowaveAssisted'],
         'slot_uri': 'catcore:vessel_type'} })
    equipment: Optional[list[str]] = Field(default=[], description="""Equipment used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Solvothermal',
                       'PlasmaAssisted',
                       'CombustionSynthesis',
                       'MicrowaveAssisted',
                       'MechanochemicalSynthesis',
                       'Characterization',
                       'ProductIdentificationMethod'],
         'slot_uri': 'voc4cat:0000187'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class AtomicLayerDeposition(PreparationMethod):
    """
    Atomic layer deposition method for catalyst preparation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:AtomicLayerDeposition',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    substrate: Optional[list[str]] = Field(default=[], description="""Substrate material""", json_schema_extra = { "linkml_meta": {'domain_of': ['AtomicLayerDeposition'], 'slot_uri': 'voc4cat:0000024'} })
    pulse_time: Optional[list[float]] = Field(default=[], description="""Pulse time for deposition""", json_schema_extra = { "linkml_meta": {'domain_of': ['AtomicLayerDeposition'],
         'slot_uri': 'catcore:pulse_time',
         'unit': {'ucum_code': 's'}} })
    purging_duration: Optional[list[float]] = Field(default=[], description="""Duration of purging""", json_schema_extra = { "linkml_meta": {'domain_of': ['AtomicLayerDeposition'],
         'slot_uri': 'voc4cat:0000112',
         'unit': {'ucum_code': 's'}} })
    number_of_cycles: Optional[list[int]] = Field(default=[], description="""Number of cycles in the process""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'AtomicLayerDeposition',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'MolecularSynthesis',
                       'XRayAbsorptionSpectroscopy',
                       'CyclicVoltammetry'],
         'slot_uri': 'catcore:number_of_cycles'} })
    deposition_temperature: Optional[list[float]] = Field(default=[], description="""Temperature during deposition""", json_schema_extra = { "linkml_meta": {'domain_of': ['AtomicLayerDeposition', 'DepositionPrecipitation'],
         'slot_uri': 'catcore:deposition_temperature',
         'unit': {'ucum_code': 'Cel'}} })
    carrier_gas: Optional[list[str]] = Field(default=[], description="""Carrier gas used""", json_schema_extra = { "linkml_meta": {'domain_of': ['AtomicLayerDeposition', 'GCMS', 'ElementalAnalysis', 'ESI_MS'],
         'slot_uri': 'catcore:carrier_gas'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class DepositionPrecipitation(PreparationMethod):
    """
    Deposition-precipitation method for catalyst preparation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:DepositionPrecipitation',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    precipitating_agent: Optional[list[str]] = Field(default=[], description="""Agent used for precipitation""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoPrecipitation', 'DepositionPrecipitation'],
         'slot_uri': 'catcore:precipitating_agent'} })
    synthesis_ph: Optional[list[float]] = Field(default=[], description="""pH during synthesis""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoPrecipitation', 'DepositionPrecipitation'],
         'slot_uri': 'voc4cat:0000052'} })
    deposition_temperature: Optional[list[float]] = Field(default=[], description="""Temperature during deposition""", json_schema_extra = { "linkml_meta": {'domain_of': ['AtomicLayerDeposition', 'DepositionPrecipitation'],
         'slot_uri': 'catcore:deposition_temperature',
         'unit': {'ucum_code': 'Cel'}} })
    deposition_time: Optional[list[float]] = Field(default=[], description="""Time for deposition""", json_schema_extra = { "linkml_meta": {'domain_of': ['DepositionPrecipitation'],
         'slot_uri': 'catcore:deposition_time',
         'unit': {'ucum_code': 'h'}} })
    mixing_rate: Optional[list[float]] = Field(default=[], description="""Rate of mixing""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoPrecipitation', 'DepositionPrecipitation'],
         'slot_uri': 'catcore:mixing_rate',
         'unit': {'ucum_code': 'rpm'}} })
    mixing_time: Optional[list[float]] = Field(default=[], description="""Duration of mixing""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoPrecipitation', 'DepositionPrecipitation'],
         'slot_uri': 'catcore:mixing_time',
         'unit': {'ucum_code': 'h'}} })
    mixing_temperature: Optional[list[float]] = Field(default=[], description="""Temperature during mixing""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoPrecipitation',
                       'DepositionPrecipitation',
                       'MolecularSynthesis'],
         'slot_uri': 'catcore:mixing_temperature',
         'unit': {'ucum_code': 'Cel'}} })
    drying_device: Optional[list[str]] = Field(default=[], description="""Device used for drying""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'MolecularSynthesis'],
         'slot_uri': 'catcore:drying_device'} })
    drying_temperature: Optional[list[float]] = Field(default=[], description="""Temperature during drying""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'MolecularSynthesis'],
         'slot_uri': 'catcore:drying_temperature',
         'unit': {'ucum_code': 'Cel'}} })
    drying_time: Optional[list[float]] = Field(default=[], description="""Duration of drying process""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'MolecularSynthesis'],
         'slot_uri': 'catcore:drying_time',
         'unit': {'ucum_code': 'h'}} })
    drying_atmosphere: Optional[list[str]] = Field(default=[], description="""Atmosphere during drying""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis'],
         'slot_uri': 'catcore:drying_atmosphere'} })
    calcination_initial_temperature: Optional[list[float]] = Field(default=[], description="""Initial temperature for calcination""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000057',
         'unit': {'ucum_code': 'Cel'}} })
    calcination_final_temperature: Optional[list[float]] = Field(default=[], description="""Final temperature for calcination""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000058',
         'unit': {'ucum_code': 'Cel'}} })
    calcination_dwelling_time: Optional[list[float]] = Field(default=[], description="""Dwelling time at calcination temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000060',
         'unit': {'ucum_code': 'h'}} })
    number_of_cycles: Optional[list[int]] = Field(default=[], description="""Number of cycles in the process""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'AtomicLayerDeposition',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'MolecularSynthesis',
                       'XRayAbsorptionSpectroscopy',
                       'CyclicVoltammetry'],
         'slot_uri': 'catcore:number_of_cycles'} })
    calcination_gaseous_environment: Optional[list[str]] = Field(default=[], description="""Gaseous environment during calcination""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000055'} })
    calcination_heating_rate: Optional[list[float]] = Field(default=[], description="""Heating rate during calcination""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000059',
         'unit': {'ucum_code': 'Cel/min'}} })
    calcination_gas_flow_rate: Optional[list[float]] = Field(default=[], description="""Gas flow rate during calcination""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000056',
         'unit': {'ucum_code': 'mL/min'}} })
    order_of_addition: Optional[list[str]] = Field(default=[], description="""Order in which components are added""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoPrecipitation', 'DepositionPrecipitation'],
         'slot_uri': 'catcore:order_of_addition'} })
    filtration: Optional[list[str]] = Field(default=[], description="""Filtration method used""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoPrecipitation', 'DepositionPrecipitation'],
         'slot_uri': 'catcore:filtration'} })
    purification: Optional[list[str]] = Field(default=[], description="""Purification method used""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoPrecipitation', 'DepositionPrecipitation'],
         'slot_uri': 'catcore:purification'} })
    aging_temperature: Optional[list[float]] = Field(default=[], description="""Temperature during aging""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoPrecipitation', 'DepositionPrecipitation'],
         'slot_uri': 'catcore:aging_temperature',
         'unit': {'ucum_code': 'Cel'}} })
    aging_time: Optional[list[float]] = Field(default=[], description="""Duration of aging process""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoPrecipitation', 'SolGel', 'DepositionPrecipitation'],
         'slot_uri': 'catcore:aging_time',
         'unit': {'ucum_code': 'h'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class MicrowaveAssisted(PreparationMethod):
    """
    Microwave-assisted method for catalyst preparation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:MicrowaveAssisted',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    equipment: Optional[list[str]] = Field(default=[], description="""Equipment used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Solvothermal',
                       'PlasmaAssisted',
                       'CombustionSynthesis',
                       'MicrowaveAssisted',
                       'MechanochemicalSynthesis',
                       'Characterization',
                       'ProductIdentificationMethod'],
         'slot_uri': 'voc4cat:0000187'} })
    power: Optional[list[float]] = Field(default=[], description="""Power setting""", json_schema_extra = { "linkml_meta": {'domain_of': ['MicrowaveAssisted'],
         'slot_uri': 'catcore:power',
         'unit': {'ucum_code': 'W'}} })
    synthesis_duration: Optional[list[float]] = Field(default=[], description="""Duration of synthesis""", json_schema_extra = { "linkml_meta": {'domain_of': ['Solvothermal',
                       'MicrowaveAssisted',
                       'Sublimation',
                       'MolecularSynthesis'],
         'slot_uri': 'voc4cat:0000050',
         'unit': {'ucum_code': 'h'}} })
    synthesis_temperature: Optional[list[float]] = Field(default=[], description="""Temperature during synthesis""", json_schema_extra = { "linkml_meta": {'domain_of': ['Solvothermal',
                       'PlasmaAssisted',
                       'MicrowaveAssisted',
                       'MechanochemicalSynthesis'],
         'slot_uri': 'voc4cat:0000051',
         'unit': {'ucum_code': 'Cel'}} })
    microwave_frequency: Optional[list[float]] = Field(default=[], description="""Frequency of microwave""", json_schema_extra = { "linkml_meta": {'domain_of': ['MicrowaveAssisted'],
         'slot_uri': 'catcore:microwave_frequency',
         'unit': {'ucum_code': 'GHz'}} })
    vessel_type: Optional[list[str]] = Field(default=[], description="""Type of vessel used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Solvothermal', 'CombustionSynthesis', 'MicrowaveAssisted'],
         'slot_uri': 'catcore:vessel_type'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class SonochemicalSynthesis(PreparationMethod):
    """
    Sonochemical synthesis method for catalyst preparation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:SonochemicalSynthesis',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    stirring_duration: Optional[list[float]] = Field(default=[], description="""Duration of stirring""", json_schema_extra = { "linkml_meta": {'domain_of': ['SonochemicalSynthesis', 'MolecularSynthesis'],
         'slot_uri': 'catcore:stirring_duration',
         'unit': {'ucum_code': 'h'}} })
    sonication_power: Optional[list[float]] = Field(default=[], description="""Power of sonication""", json_schema_extra = { "linkml_meta": {'domain_of': ['SonochemicalSynthesis'],
         'slot_uri': 'catcore:sonication_power',
         'unit': {'ucum_code': 'W'}} })
    sonication_duration: Optional[list[float]] = Field(default=[], description="""Duration of sonication""", json_schema_extra = { "linkml_meta": {'domain_of': ['SonochemicalSynthesis'],
         'slot_uri': 'catcore:sonication_duration',
         'unit': {'ucum_code': 'min'}} })
    temperature: Optional[list[float]] = Field(default=[], description="""Temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['SonochemicalSynthesis',
                       'Sublimation',
                       'PowderXRD',
                       'XRayAbsorptionSpectroscopy',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'DynamicLightScattering',
                       'PhotoluminescenceSpectroscopy',
                       'PhotoluminescenceLifetime',
                       'SizeExclusionChromatography',
                       'HPLC_MS',
                       'SingleCrystalXRD',
                       'ConductivityMeasurement',
                       'Microkinetics',
                       'MonteCarlo',
                       'AqueousStability'],
         'slot_uri': 'AFR:0001584',
         'unit': {'ucum_code': 'Cel'}} })
    drying_device: Optional[list[str]] = Field(default=[], description="""Device used for drying""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'MolecularSynthesis'],
         'slot_uri': 'catcore:drying_device'} })
    drying_temperature: Optional[list[float]] = Field(default=[], description="""Temperature during drying""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'MolecularSynthesis'],
         'slot_uri': 'catcore:drying_temperature',
         'unit': {'ucum_code': 'Cel'}} })
    drying_time: Optional[list[float]] = Field(default=[], description="""Duration of drying process""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'MolecularSynthesis'],
         'slot_uri': 'catcore:drying_time',
         'unit': {'ucum_code': 'h'}} })
    drying_atmosphere: Optional[list[str]] = Field(default=[], description="""Atmosphere during drying""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis'],
         'slot_uri': 'catcore:drying_atmosphere'} })
    calcination_initial_temperature: Optional[list[float]] = Field(default=[], description="""Initial temperature for calcination""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000057',
         'unit': {'ucum_code': 'Cel'}} })
    calcination_final_temperature: Optional[list[float]] = Field(default=[], description="""Final temperature for calcination""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000058',
         'unit': {'ucum_code': 'Cel'}} })
    calcination_dwelling_time: Optional[list[float]] = Field(default=[], description="""Dwelling time at calcination temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000060',
         'unit': {'ucum_code': 'h'}} })
    number_of_cycles: Optional[list[int]] = Field(default=[], description="""Number of cycles in the process""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'AtomicLayerDeposition',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'MolecularSynthesis',
                       'XRayAbsorptionSpectroscopy',
                       'CyclicVoltammetry'],
         'slot_uri': 'catcore:number_of_cycles'} })
    calcination_gaseous_environment: Optional[list[str]] = Field(default=[], description="""Gaseous environment during calcination""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000055'} })
    calcination_heating_rate: Optional[list[float]] = Field(default=[], description="""Heating rate during calcination""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000059',
         'unit': {'ucum_code': 'Cel/min'}} })
    calcination_gas_flow_rate: Optional[list[float]] = Field(default=[], description="""Gas flow rate during calcination""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000056',
         'unit': {'ucum_code': 'mL/min'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class FlameSprayPyrolysis(PreparationMethod):
    """
    Flame spray pyrolysis method for catalyst preparation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'voc4cat:0007031',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    flame_type: Optional[list[str]] = Field(default=[], description="""Type of flame used""", json_schema_extra = { "linkml_meta": {'domain_of': ['FlameSprayPyrolysis'], 'slot_uri': 'catcore:flame_type'} })
    flow_rate: Optional[list[float]] = Field(default=[], description="""Flow rate""", json_schema_extra = { "linkml_meta": {'domain_of': ['FlameSprayPyrolysis',
                       'DRIFTS',
                       'ESI_MS',
                       'SizeExclusionChromatography',
                       'HPLC_MS'],
         'slot_uri': 'catcore:flow_rate',
         'unit': {'ucum_code': 'mL/min'}} })
    inlet_system: Optional[list[str]] = Field(default=[], description="""Inlet system configuration""", json_schema_extra = { "linkml_meta": {'domain_of': ['FlameSprayPyrolysis'], 'slot_uri': 'catcore:inlet_system'} })
    flame_ring: Optional[list[str]] = Field(default=[], description="""Flame ring configuration""", json_schema_extra = { "linkml_meta": {'domain_of': ['FlameSprayPyrolysis'], 'slot_uri': 'catcore:flame_ring'} })
    dispersant: Optional[list[str]] = Field(default=[], description="""Dispersant used""", json_schema_extra = { "linkml_meta": {'domain_of': ['FlameSprayPyrolysis', 'DynamicLightScattering'],
         'slot_uri': 'catcore:dispersant'} })
    capillary_pressure: Optional[list[float]] = Field(default=[], description="""Capillary pressure""", json_schema_extra = { "linkml_meta": {'domain_of': ['FlameSprayPyrolysis'],
         'slot_uri': 'catcore:capillary_pressure',
         'unit': {'ucum_code': 'bar'}} })
    fuel_dispersant_ratio: Optional[list[float]] = Field(default=[], description="""Ratio of fuel to dispersant""", json_schema_extra = { "linkml_meta": {'domain_of': ['FlameSprayPyrolysis'],
         'slot_uri': 'catcore:fuel_dispersant_ratio'} })
    filtration_device: Optional[list[str]] = Field(default=[], description="""Device used for filtration""", json_schema_extra = { "linkml_meta": {'domain_of': ['FlameSprayPyrolysis', 'MolecularSynthesis'],
         'slot_uri': 'catcore:filtration_device'} })
    filter_type: Optional[list[str]] = Field(default=[], description="""Type of filter used""", json_schema_extra = { "linkml_meta": {'domain_of': ['FlameSprayPyrolysis', 'MolecularSynthesis'],
         'slot_uri': 'catcore:filter_type'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class MechanochemicalSynthesis(PreparationMethod):
    """
    Mechanochemical synthesis method for catalyst preparation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:MechanochemicalSynthesis',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    equipment: Optional[list[str]] = Field(default=[], description="""Equipment used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Solvothermal',
                       'PlasmaAssisted',
                       'CombustionSynthesis',
                       'MicrowaveAssisted',
                       'MechanochemicalSynthesis',
                       'Characterization',
                       'ProductIdentificationMethod'],
         'slot_uri': 'voc4cat:0000187'} })
    vessel_volume: Optional[list[float]] = Field(default=[], description="""Volume of vessel""", json_schema_extra = { "linkml_meta": {'domain_of': ['MechanochemicalSynthesis'],
         'slot_uri': 'catcore:vessel_volume',
         'unit': {'ucum_code': 'mL'}} })
    size_and_material: Optional[list[str]] = Field(default=[], description="""Size and material of components""", json_schema_extra = { "linkml_meta": {'domain_of': ['MechanochemicalSynthesis'],
         'slot_uri': 'catcore:size_and_material'} })
    milling_speed: Optional[list[float]] = Field(default=[], description="""Speed of milling""", json_schema_extra = { "linkml_meta": {'domain_of': ['MechanochemicalSynthesis'],
         'slot_uri': 'catcore:milling_speed',
         'unit': {'ucum_code': 'rpm'}} })
    milling_duration: Optional[list[float]] = Field(default=[], description="""Duration of milling""", json_schema_extra = { "linkml_meta": {'domain_of': ['MechanochemicalSynthesis'],
         'slot_uri': 'catcore:milling_duration',
         'unit': {'ucum_code': 'h'}} })
    synthesis_temperature: Optional[list[float]] = Field(default=[], description="""Temperature during synthesis""", json_schema_extra = { "linkml_meta": {'domain_of': ['Solvothermal',
                       'PlasmaAssisted',
                       'MicrowaveAssisted',
                       'MechanochemicalSynthesis'],
         'slot_uri': 'voc4cat:0000051',
         'unit': {'ucum_code': 'Cel'}} })
    atmosphere: Optional[list[str]] = Field(default=[], description="""Atmospheric conditions""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlasmaAssisted',
                       'CombustionSynthesis',
                       'MechanochemicalSynthesis',
                       'MolecularSynthesis',
                       'PowderXRD',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'Thermogravimetry',
                       'XPS',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'OperationParameters'],
         'slot_uri': 'catcore:atmosphere'} })
    ball_material: Optional[list[str]] = Field(default=[], description="""Material of milling balls""", json_schema_extra = { "linkml_meta": {'domain_of': ['MechanochemicalSynthesis'], 'slot_uri': 'catcore:ball_material'} })
    ball_size: Optional[list[float]] = Field(default=[], description="""Size of milling balls""", json_schema_extra = { "linkml_meta": {'domain_of': ['MechanochemicalSynthesis'],
         'slot_uri': 'catcore:ball_size',
         'unit': {'ucum_code': 'mm'}} })
    ball_to_powder_ratio: Optional[list[float]] = Field(default=[], description="""Ratio of ball to powder""", json_schema_extra = { "linkml_meta": {'domain_of': ['MechanochemicalSynthesis'],
         'slot_uri': 'catcore:ball_to_powder_ratio'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class Sublimation(PreparationMethod):
    """
    Sublimation method for catalyst preparation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:Sublimation',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    temperature: Optional[list[float]] = Field(default=[], description="""Temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['SonochemicalSynthesis',
                       'Sublimation',
                       'PowderXRD',
                       'XRayAbsorptionSpectroscopy',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'DynamicLightScattering',
                       'PhotoluminescenceSpectroscopy',
                       'PhotoluminescenceLifetime',
                       'SizeExclusionChromatography',
                       'HPLC_MS',
                       'SingleCrystalXRD',
                       'ConductivityMeasurement',
                       'Microkinetics',
                       'MonteCarlo',
                       'AqueousStability'],
         'slot_uri': 'AFR:0001584',
         'unit': {'ucum_code': 'Cel'}} })
    synthesis_pressure: Optional[list[float]] = Field(default=[], description="""Pressure during synthesis""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlasmaAssisted', 'Sublimation'],
         'slot_uri': 'voc4cat:0000053',
         'unit': {'ucum_code': 'bar'}} })
    synthesis_duration: Optional[list[float]] = Field(default=[], description="""Duration of synthesis""", json_schema_extra = { "linkml_meta": {'domain_of': ['Solvothermal',
                       'MicrowaveAssisted',
                       'Sublimation',
                       'MolecularSynthesis'],
         'slot_uri': 'voc4cat:0000050',
         'unit': {'ucum_code': 'h'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class MolecularSynthesis(PreparationMethod):
    """
    Molecular synthesis method for catalyst preparation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:MolecularSynthesis',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    atmosphere: Optional[list[str]] = Field(default=[], description="""Atmospheric conditions""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlasmaAssisted',
                       'CombustionSynthesis',
                       'MechanochemicalSynthesis',
                       'MolecularSynthesis',
                       'PowderXRD',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'Thermogravimetry',
                       'XPS',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'OperationParameters'],
         'slot_uri': 'catcore:atmosphere'} })
    synthesis_duration: Optional[list[float]] = Field(default=[], description="""Duration of synthesis""", json_schema_extra = { "linkml_meta": {'domain_of': ['Solvothermal',
                       'MicrowaveAssisted',
                       'Sublimation',
                       'MolecularSynthesis'],
         'slot_uri': 'voc4cat:0000050',
         'unit': {'ucum_code': 'h'}} })
    reaction_vessel: Optional[list[str]] = Field(default=[], description="""Vessel used for reaction""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSynthesis'], 'slot_uri': 'catcore:reaction_vessel'} })
    mixing_device: Optional[list[str]] = Field(default=[], description="""Device used for mixing""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSynthesis'], 'slot_uri': 'catcore:mixing_device'} })
    stirring_duration: Optional[list[float]] = Field(default=[], description="""Duration of stirring""", json_schema_extra = { "linkml_meta": {'domain_of': ['SonochemicalSynthesis', 'MolecularSynthesis'],
         'slot_uri': 'catcore:stirring_duration',
         'unit': {'ucum_code': 'h'}} })
    stirring_speed: Optional[list[float]] = Field(default=[], description="""Speed of stirring""", json_schema_extra = { "linkml_meta": {'domain_of': ['Solvothermal', 'MolecularSynthesis'],
         'slot_uri': 'catcore:stirring_speed',
         'unit': {'ucum_code': 'rpm'}} })
    mixing_temperature: Optional[list[float]] = Field(default=[], description="""Temperature during mixing""", json_schema_extra = { "linkml_meta": {'domain_of': ['CoPrecipitation',
                       'DepositionPrecipitation',
                       'MolecularSynthesis'],
         'slot_uri': 'catcore:mixing_temperature',
         'unit': {'ucum_code': 'Cel'}} })
    filtration_device: Optional[list[str]] = Field(default=[], description="""Device used for filtration""", json_schema_extra = { "linkml_meta": {'domain_of': ['FlameSprayPyrolysis', 'MolecularSynthesis'],
         'slot_uri': 'catcore:filtration_device'} })
    filter_type: Optional[list[str]] = Field(default=[], description="""Type of filter used""", json_schema_extra = { "linkml_meta": {'domain_of': ['FlameSprayPyrolysis', 'MolecularSynthesis'],
         'slot_uri': 'catcore:filter_type'} })
    crystallisation_solvents: Optional[list[str]] = Field(default=[], description="""Solvents used for crystallisation""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSynthesis'],
         'slot_uri': 'catcore:crystallisation_solvents'} })
    precipitation_agent: Optional[list[str]] = Field(default=[], description="""Agent used for precipitation""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSynthesis'], 'slot_uri': 'catcore:precipitation_agent'} })
    crystallisation_duration: Optional[list[float]] = Field(default=[], description="""Duration of crystallisation""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSynthesis'],
         'slot_uri': 'catcore:crystallisation_duration',
         'unit': {'ucum_code': 'h'}} })
    purification_solvent: Optional[list[str]] = Field(default=[], description="""Solvent used for purification""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSynthesis'],
         'slot_uri': 'catcore:purification_solvent'} })
    number_of_cycles: Optional[list[int]] = Field(default=[], description="""Number of cycles in the process""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'AtomicLayerDeposition',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'MolecularSynthesis',
                       'XRayAbsorptionSpectroscopy',
                       'CyclicVoltammetry'],
         'slot_uri': 'catcore:number_of_cycles'} })
    drying_device: Optional[list[str]] = Field(default=[], description="""Device used for drying""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'MolecularSynthesis'],
         'slot_uri': 'catcore:drying_device'} })
    drying_temperature: Optional[list[float]] = Field(default=[], description="""Temperature during drying""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'MolecularSynthesis'],
         'slot_uri': 'catcore:drying_temperature',
         'unit': {'ucum_code': 'Cel'}} })
    temperature_ramp: Optional[list[float]] = Field(default=[], description="""Temperature ramp rate""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularSynthesis'],
         'slot_uri': 'catcore:temperature_ramp',
         'unit': {'ucum_code': 'Cel/min'}} })
    drying_time: Optional[list[float]] = Field(default=[], description="""Duration of drying process""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'MolecularSynthesis'],
         'slot_uri': 'catcore:drying_time',
         'unit': {'ucum_code': 'h'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class ExsolutionSynthesis(PreparationMethod):
    """
    Exsolution synthesis method for catalyst preparation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:ExsolutionSynthesis',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    calcination_initial_temperature: Optional[list[float]] = Field(default=[], description="""Initial temperature for calcination""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000057',
         'unit': {'ucum_code': 'Cel'}} })
    calcination_final_temperature: Optional[list[float]] = Field(default=[], description="""Final temperature for calcination""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000058',
         'unit': {'ucum_code': 'Cel'}} })
    calcination_dwelling_time: Optional[list[float]] = Field(default=[], description="""Dwelling time at calcination temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000060',
         'unit': {'ucum_code': 'h'}} })
    calcination_gaseous_environment: Optional[list[str]] = Field(default=[], description="""Gaseous environment during calcination""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000055'} })
    calcination_heating_rate: Optional[list[float]] = Field(default=[], description="""Heating rate during calcination""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000059',
         'unit': {'ucum_code': 'Cel/min'}} })
    calcination_gas_flow_rate: Optional[list[float]] = Field(default=[], description="""Gas flow rate during calcination""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'ExsolutionSynthesis'],
         'slot_uri': 'voc4cat:0000056',
         'unit': {'ucum_code': 'mL/min'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class Characterization(CatCoreEntity):
    """
    The data class 'Characterization' describes the minimum information which should be 
    reported with research data to describe the nature of the catalyst.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/nfdi4cat/catcore',
         'slot_usage': {'characterization_technique': {'name': 'characterization_technique',
                                                       'required': True},
                        'equipment': {'name': 'equipment', 'required': True}}})

    equipment: list[str] = Field(default=..., description="""Equipment used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Solvothermal',
                       'PlasmaAssisted',
                       'CombustionSynthesis',
                       'MicrowaveAssisted',
                       'MechanochemicalSynthesis',
                       'Characterization',
                       'ProductIdentificationMethod'],
         'slot_uri': 'voc4cat:0000187'} })
    characterization_technique: list[CharacterizationTechnique] = Field(default=..., description="""Technique used for characterization""", json_schema_extra = { "linkml_meta": {'domain_of': ['Characterization'], 'slot_uri': 'voc4cat:0000066'} })
    sample_state: Optional[list[SampleStateEnum]] = Field(default=[], description="""State of the sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['Characterization'], 'slot_uri': 'catcore:sample_state'} })
    sample_description: Optional[list[str]] = Field(default=[], description="""Description of the sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['Characterization'], 'slot_uri': 'catcore:sample_description'} })
    detector_type: Optional[list[str]] = Field(default=[], description="""Type of detector used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Characterization'], 'slot_uri': 'AFR:0000317'} })
    sample_preparation: Optional[list[str]] = Field(default=[], description="""Preparation of sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['Characterization'], 'slot_uri': 'AFP:0001159'} })
    sample_pretreatment: Optional[list[str]] = Field(default=[], description="""Pre-treatment of sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['Synthesis', 'Characterization'], 'slot_uri': 'voc4cat:0000122'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class CharacterizationTechnique(CatCoreEntity):
    """
    Characterization technique used for catalyst analysis
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class PowderXRD(CharacterizationTechnique):
    """
    Powder X-ray diffraction
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CHMO:0000158',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    xray_source: Optional[list[str]] = Field(default=[], description="""X-ray source used""", json_schema_extra = { "linkml_meta": {'domain_of': ['PowderXRD', 'XPS', 'SingleCrystalXRD'],
         'slot_uri': 'OBI:0001138'} })
    atmosphere: Optional[list[str]] = Field(default=[], description="""Atmospheric conditions""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlasmaAssisted',
                       'CombustionSynthesis',
                       'MechanochemicalSynthesis',
                       'MolecularSynthesis',
                       'PowderXRD',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'Thermogravimetry',
                       'XPS',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'OperationParameters'],
         'slot_uri': 'catcore:atmosphere'} })
    operation_mode: Optional[list[str]] = Field(default=[], description="""Operation mode of the instrument""", json_schema_extra = { "linkml_meta": {'domain_of': ['PowderXRD',
                       'XRayAbsorptionSpectroscopy',
                       'InfraredSpectroscopy',
                       'TransmissionElectronMicroscopy',
                       'Thermogravimetry',
                       'ESI_MS'],
         'slot_uri': 'voc4cat:0000108'} })
    minimum_2theta: Optional[list[float]] = Field(default=[], description="""Minimum 2-theta angle""", json_schema_extra = { "linkml_meta": {'domain_of': ['PowderXRD'],
         'slot_uri': 'catcore:minimum_2theta',
         'unit': {'ucum_code': 'deg'}} })
    maximum_2theta: Optional[list[float]] = Field(default=[], description="""Maximum 2-theta angle""", json_schema_extra = { "linkml_meta": {'domain_of': ['PowderXRD'],
         'slot_uri': 'catcore:maximum_2theta',
         'unit': {'ucum_code': 'deg'}} })
    step_size: Optional[list[float]] = Field(default=[], description="""Step size for measurements""", json_schema_extra = { "linkml_meta": {'domain_of': ['PowderXRD',
                       'InfraredSpectroscopy',
                       'XPS',
                       'DRIFTS',
                       'PhotoluminescenceSpectroscopy'],
         'slot_uri': 'AFR:0000950'} })
    monochromator: Optional[list[str]] = Field(default=[], description="""Monochromator type used""", json_schema_extra = { "linkml_meta": {'domain_of': ['PowderXRD', 'XRayAbsorptionSpectroscopy'],
         'slot_uri': 'CHMO:0002120'} })
    temperature: Optional[list[float]] = Field(default=[], description="""Temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['SonochemicalSynthesis',
                       'Sublimation',
                       'PowderXRD',
                       'XRayAbsorptionSpectroscopy',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'DynamicLightScattering',
                       'PhotoluminescenceSpectroscopy',
                       'PhotoluminescenceLifetime',
                       'SizeExclusionChromatography',
                       'HPLC_MS',
                       'SingleCrystalXRD',
                       'ConductivityMeasurement',
                       'Microkinetics',
                       'MonteCarlo',
                       'AqueousStability'],
         'slot_uri': 'AFR:0001584',
         'unit': {'ucum_code': 'Cel'}} })
    sample_spinning_speed: Optional[list[float]] = Field(default=[], description="""Sample spinning speed""", json_schema_extra = { "linkml_meta": {'domain_of': ['PowderXRD'],
         'slot_uri': 'catcore:sample_spinning_speed',
         'unit': {'ucum_code': 'rpm'}} })
    experiment_duration: Optional[list[float]] = Field(default=[], description="""Duration of the experiment""", json_schema_extra = { "linkml_meta": {'domain_of': ['PowderXRD', 'OperationParameters'],
         'slot_uri': 'AFR:0002455',
         'unit': {'ucum_code': 'h'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class XRayAbsorptionSpectroscopy(CharacterizationTechnique):
    """
    X-ray absorption spectroscopy
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'voc4cat:0000286',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    operation_mode: Optional[list[str]] = Field(default=[], description="""Operation mode of the instrument""", json_schema_extra = { "linkml_meta": {'domain_of': ['PowderXRD',
                       'XRayAbsorptionSpectroscopy',
                       'InfraredSpectroscopy',
                       'TransmissionElectronMicroscopy',
                       'Thermogravimetry',
                       'ESI_MS'],
         'slot_uri': 'voc4cat:0000108'} })
    element_analyzed: Optional[list[str]] = Field(default=[], description="""Chemical element being analyzed""", json_schema_extra = { "linkml_meta": {'domain_of': ['XRayAbsorptionSpectroscopy', 'ICPAES'],
         'slot_uri': 'catcore:element_analyzed'} })
    absorption_edge: Optional[list[str]] = Field(default=[], description="""Absorption edge measured""", json_schema_extra = { "linkml_meta": {'domain_of': ['XRayAbsorptionSpectroscopy'],
         'slot_uri': 'catcore:absorption_edge'} })
    monochromator: Optional[list[str]] = Field(default=[], description="""Monochromator type used""", json_schema_extra = { "linkml_meta": {'domain_of': ['PowderXRD', 'XRayAbsorptionSpectroscopy'],
         'slot_uri': 'CHMO:0002120'} })
    minimum_energy: Optional[list[float]] = Field(default=[], description="""Minimum energy value""", json_schema_extra = { "linkml_meta": {'domain_of': ['XRayAbsorptionSpectroscopy', 'XPS'],
         'slot_uri': 'catcore:minimum_energy',
         'unit': {'ucum_code': 'eV'}} })
    maximum_energy: Optional[list[float]] = Field(default=[], description="""Maximum energy value""", json_schema_extra = { "linkml_meta": {'domain_of': ['XRayAbsorptionSpectroscopy', 'XPS'],
         'slot_uri': 'catcore:maximum_energy',
         'unit': {'ucum_code': 'eV'}} })
    energy_resolution: Optional[list[float]] = Field(default=[], description="""Energy resolution of the measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['XRayAbsorptionSpectroscopy'],
         'slot_uri': 'AFR:0000950',
         'unit': {'ucum_code': 'eV'}} })
    temperature: Optional[list[float]] = Field(default=[], description="""Temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['SonochemicalSynthesis',
                       'Sublimation',
                       'PowderXRD',
                       'XRayAbsorptionSpectroscopy',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'DynamicLightScattering',
                       'PhotoluminescenceSpectroscopy',
                       'PhotoluminescenceLifetime',
                       'SizeExclusionChromatography',
                       'HPLC_MS',
                       'SingleCrystalXRD',
                       'ConductivityMeasurement',
                       'Microkinetics',
                       'MonteCarlo',
                       'AqueousStability'],
         'slot_uri': 'AFR:0001584',
         'unit': {'ucum_code': 'Cel'}} })
    beamline_source: Optional[list[str]] = Field(default=[], description="""Beamline source identification""", json_schema_extra = { "linkml_meta": {'domain_of': ['XRayAbsorptionSpectroscopy'],
         'slot_uri': 'catcore:beamline_source'} })
    noise_of_measurement: Optional[list[float]] = Field(default=[], description="""Noise level of the measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['XRayAbsorptionSpectroscopy'],
         'slot_uri': 'catcore:noise_of_measurement'} })
    number_of_cycles: Optional[list[int]] = Field(default=[], description="""Number of cycles in the process""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'AtomicLayerDeposition',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'MolecularSynthesis',
                       'XRayAbsorptionSpectroscopy',
                       'CyclicVoltammetry'],
         'slot_uri': 'catcore:number_of_cycles'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class InfraredSpectroscopy(CharacterizationTechnique):
    """
    Infrared spectroscopy
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:InfraredSpectroscopy',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    operation_mode: Optional[list[str]] = Field(default=[], description="""Operation mode of the instrument""", json_schema_extra = { "linkml_meta": {'domain_of': ['PowderXRD',
                       'XRayAbsorptionSpectroscopy',
                       'InfraredSpectroscopy',
                       'TransmissionElectronMicroscopy',
                       'Thermogravimetry',
                       'ESI_MS'],
         'slot_uri': 'voc4cat:0000108'} })
    minimum_wavenumber: Optional[list[float]] = Field(default=[], description="""Minimum wavenumber""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfraredSpectroscopy'],
         'slot_uri': 'catcore:minimum_wavenumber',
         'unit': {'ucum_code': 'cm-1'}} })
    maximum_wavenumber: Optional[list[float]] = Field(default=[], description="""Maximum wavenumber""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfraredSpectroscopy'],
         'slot_uri': 'catcore:maximum_wavenumber',
         'unit': {'ucum_code': 'cm-1'}} })
    step_size: Optional[list[float]] = Field(default=[], description="""Step size for measurements""", json_schema_extra = { "linkml_meta": {'domain_of': ['PowderXRD',
                       'InfraredSpectroscopy',
                       'XPS',
                       'DRIFTS',
                       'PhotoluminescenceSpectroscopy'],
         'slot_uri': 'AFR:0000950'} })
    temperature: Optional[list[float]] = Field(default=[], description="""Temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['SonochemicalSynthesis',
                       'Sublimation',
                       'PowderXRD',
                       'XRayAbsorptionSpectroscopy',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'DynamicLightScattering',
                       'PhotoluminescenceSpectroscopy',
                       'PhotoluminescenceLifetime',
                       'SizeExclusionChromatography',
                       'HPLC_MS',
                       'SingleCrystalXRD',
                       'ConductivityMeasurement',
                       'Microkinetics',
                       'MonteCarlo',
                       'AqueousStability'],
         'slot_uri': 'AFR:0001584',
         'unit': {'ucum_code': 'Cel'}} })
    background_correction: Optional[list[str]] = Field(default=[], description="""Background correction method""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfraredSpectroscopy'], 'slot_uri': 'AFP:0003721'} })
    number_of_scans: Optional[list[int]] = Field(default=[], description="""Number of scans performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'XPS',
                       'DRIFTS'],
         'slot_uri': 'AFR:0003051'} })
    atmosphere: Optional[list[str]] = Field(default=[], description="""Atmospheric conditions""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlasmaAssisted',
                       'CombustionSynthesis',
                       'MechanochemicalSynthesis',
                       'MolecularSynthesis',
                       'PowderXRD',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'Thermogravimetry',
                       'XPS',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'OperationParameters'],
         'slot_uri': 'catcore:atmosphere'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class RamanSpectroscopy(CharacterizationTechnique):
    """
    Raman spectroscopy
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'voc4cat:0000069',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    excitation_laser_wavelength: Optional[list[float]] = Field(default=[], description="""Excitation laser wavelength""", json_schema_extra = { "linkml_meta": {'domain_of': ['RamanSpectroscopy'],
         'slot_uri': 'AFR:0001594',
         'unit': {'ucum_code': 'nm'}} })
    excitation_laser_power: Optional[list[float]] = Field(default=[], description="""Excitation laser power""", json_schema_extra = { "linkml_meta": {'domain_of': ['RamanSpectroscopy'],
         'slot_uri': 'AFR:0001595',
         'unit': {'ucum_code': 'mW'}} })
    magnification_setting: Optional[list[float]] = Field(default=[], description="""Magnification setting""", json_schema_extra = { "linkml_meta": {'domain_of': ['RamanSpectroscopy', 'TransmissionElectronMicroscopy'],
         'slot_uri': 'AFR:0002226'} })
    integration_time: Optional[list[float]] = Field(default=[], description="""Integration time""", json_schema_extra = { "linkml_meta": {'domain_of': ['RamanSpectroscopy', 'PhotoluminescenceSpectroscopy'],
         'slot_uri': 'AFR:0001671',
         'unit': {'ucum_code': 's'}} })
    number_of_scans: Optional[list[int]] = Field(default=[], description="""Number of scans performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'XPS',
                       'DRIFTS'],
         'slot_uri': 'AFR:0003051'} })
    atmosphere: Optional[list[str]] = Field(default=[], description="""Atmospheric conditions""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlasmaAssisted',
                       'CombustionSynthesis',
                       'MechanochemicalSynthesis',
                       'MolecularSynthesis',
                       'PowderXRD',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'Thermogravimetry',
                       'XPS',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'OperationParameters'],
         'slot_uri': 'catcore:atmosphere'} })
    temperature: Optional[list[float]] = Field(default=[], description="""Temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['SonochemicalSynthesis',
                       'Sublimation',
                       'PowderXRD',
                       'XRayAbsorptionSpectroscopy',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'DynamicLightScattering',
                       'PhotoluminescenceSpectroscopy',
                       'PhotoluminescenceLifetime',
                       'SizeExclusionChromatography',
                       'HPLC_MS',
                       'SingleCrystalXRD',
                       'ConductivityMeasurement',
                       'Microkinetics',
                       'MonteCarlo',
                       'AqueousStability'],
         'slot_uri': 'AFR:0001584',
         'unit': {'ucum_code': 'Cel'}} })
    filter_or_grating: Optional[list[str]] = Field(default=[], description="""Filter or grating used""", json_schema_extra = { "linkml_meta": {'domain_of': ['RamanSpectroscopy'], 'slot_uri': 'catcore:filter_or_grating'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class GCMS(CharacterizationTechnique):
    """
    Gas chromatography-mass spectrometry
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CHMO:0000497',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    external_standard: Optional[list[str]] = Field(default=[], description="""External standard used for calibration""", json_schema_extra = { "linkml_meta": {'domain_of': ['GCMS', 'HPLC_MS'], 'slot_uri': 'catcore:external_standard'} })
    internal_standard: Optional[list[str]] = Field(default=[], description="""Internal standard used for calibration""", json_schema_extra = { "linkml_meta": {'domain_of': ['GCMS', 'HPLC_MS'], 'slot_uri': 'catcore:internal_standard'} })
    column_type: Optional[list[str]] = Field(default=[], description="""Type of chromatography column""", json_schema_extra = { "linkml_meta": {'domain_of': ['GCMS', 'SizeExclusionChromatography', 'HPLC_MS'],
         'slot_uri': 'AFR:0002026'} })
    carrier_gas: Optional[list[str]] = Field(default=[], description="""Carrier gas used""", json_schema_extra = { "linkml_meta": {'domain_of': ['AtomicLayerDeposition', 'GCMS', 'ElementalAnalysis', 'ESI_MS'],
         'slot_uri': 'catcore:carrier_gas'} })
    carrier_gas_purity: Optional[list[str]] = Field(default=[], description="""Purity of carrier gas""", json_schema_extra = { "linkml_meta": {'domain_of': ['GCMS'], 'slot_uri': 'catcore:carrier_gas_purity'} })
    inlet_temperature: Optional[list[float]] = Field(default=[], description="""Inlet temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['GCMS'],
         'slot_uri': 'catcore:inlet_temperature',
         'unit': {'ucum_code': 'Cel'}} })
    minimum_oven_temperature: Optional[list[float]] = Field(default=[], description="""Minimum oven temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['GCMS'],
         'slot_uri': 'catcore:minimum_oven_temperature',
         'unit': {'ucum_code': 'Cel'}} })
    maximum_oven_temperature: Optional[list[float]] = Field(default=[], description="""Maximum oven temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['GCMS'],
         'slot_uri': 'catcore:maximum_oven_temperature',
         'unit': {'ucum_code': 'Cel'}} })
    heating_ramp: Optional[list[float]] = Field(default=[], description="""Heating ramp rate""", json_schema_extra = { "linkml_meta": {'domain_of': ['GCMS'],
         'slot_uri': 'catcore:heating_ramp',
         'unit': {'ucum_code': 'Cel/min'}} })
    heating_procedure: Optional[list[str]] = Field(default=[], description="""Heating procedure used""", json_schema_extra = { "linkml_meta": {'domain_of': ['GCMS', 'Thermogravimetry'],
         'slot_uri': 'catcore:heating_procedure'} })
    acquisition_mode: Optional[list[str]] = Field(default=[], description="""Data acquisition mode""", json_schema_extra = { "linkml_meta": {'domain_of': ['GCMS'], 'slot_uri': 'catcore:acquisition_mode'} })
    solvent_delay: Optional[list[float]] = Field(default=[], description="""Solvent delay time""", json_schema_extra = { "linkml_meta": {'domain_of': ['GCMS'],
         'slot_uri': 'catcore:solvent_delay',
         'unit': {'ucum_code': 'min'}} })
    trace_ion_detection: Optional[list[str]] = Field(default=[], description="""Trace ion detection setting""", json_schema_extra = { "linkml_meta": {'domain_of': ['GCMS'], 'slot_uri': 'catcore:trace_ion_detection'} })
    mz_minimum: Optional[list[float]] = Field(default=[], description="""Minimum m/z value""", json_schema_extra = { "linkml_meta": {'domain_of': ['GCMS', 'ESI_MS'], 'slot_uri': 'AFR:0002652'} })
    mz_maximum: Optional[list[float]] = Field(default=[], description="""Maximum m/z value""", json_schema_extra = { "linkml_meta": {'domain_of': ['GCMS', 'ESI_MS'], 'slot_uri': 'AFR:0002653'} })
    split_ratio: Optional[list[float]] = Field(default=[], description="""Split ratio for injection""", json_schema_extra = { "linkml_meta": {'domain_of': ['GCMS'], 'slot_uri': 'catcore:split_ratio'} })
    injection_volume: Optional[list[float]] = Field(default=[], description="""Injection volume""", json_schema_extra = { "linkml_meta": {'domain_of': ['GCMS', 'SizeExclusionChromatography', 'HPLC_MS'],
         'slot_uri': 'AFR:0001577',
         'unit': {'ucum_code': 'uL'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class NMRSpectroscopy(CharacterizationTechnique):
    """
    Nuclear magnetic resonance spectroscopy
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'voc4cat:0000073',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    nucleus: Optional[list[str]] = Field(default=[], description="""Nucleus being observed""", json_schema_extra = { "linkml_meta": {'domain_of': ['NMRSpectroscopy'], 'slot_uri': 'catcore:nucleus'} })
    solvent: Optional[list[str]] = Field(default=[], description="""Solvent used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Synthesis',
                       'NMRSpectroscopy',
                       'UVVisSpectroscopy',
                       'DynamicLightScattering'],
         'slot_uri': 'voc4cat:0007246'} })
    irradiation_frequency: Optional[list[float]] = Field(default=[], description="""Irradiation frequency""", json_schema_extra = { "linkml_meta": {'domain_of': ['NMRSpectroscopy'],
         'slot_uri': 'nmrCV:1400026',
         'unit': {'ucum_code': 'MHz'}} })
    temperature: Optional[list[float]] = Field(default=[], description="""Temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['SonochemicalSynthesis',
                       'Sublimation',
                       'PowderXRD',
                       'XRayAbsorptionSpectroscopy',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'DynamicLightScattering',
                       'PhotoluminescenceSpectroscopy',
                       'PhotoluminescenceLifetime',
                       'SizeExclusionChromatography',
                       'HPLC_MS',
                       'SingleCrystalXRD',
                       'ConductivityMeasurement',
                       'Microkinetics',
                       'MonteCarlo',
                       'AqueousStability'],
         'slot_uri': 'AFR:0001584',
         'unit': {'ucum_code': 'Cel'}} })
    nmr_pulse_sequence: Optional[list[str]] = Field(default=[], description="""NMR pulse sequence used""", json_schema_extra = { "linkml_meta": {'domain_of': ['NMRSpectroscopy'], 'slot_uri': 'nmrCV:1400037'} })
    nmr_sample_tube: Optional[list[str]] = Field(default=[], description="""NMR sample tube type""", json_schema_extra = { "linkml_meta": {'domain_of': ['NMRSpectroscopy'], 'slot_uri': 'nmrCV:1400132'} })
    number_of_scans: Optional[list[int]] = Field(default=[], description="""Number of scans performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'XPS',
                       'DRIFTS'],
         'slot_uri': 'AFR:0003051'} })
    atmosphere: Optional[list[str]] = Field(default=[], description="""Atmospheric conditions""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlasmaAssisted',
                       'CombustionSynthesis',
                       'MechanochemicalSynthesis',
                       'MolecularSynthesis',
                       'PowderXRD',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'Thermogravimetry',
                       'XPS',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'OperationParameters'],
         'slot_uri': 'catcore:atmosphere'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class TransmissionElectronMicroscopy(CharacterizationTechnique):
    """
    Transmission electron microscopy
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'voc4cat:0000078',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    operation_mode: Optional[list[str]] = Field(default=[], description="""Operation mode of the instrument""", json_schema_extra = { "linkml_meta": {'domain_of': ['PowderXRD',
                       'XRayAbsorptionSpectroscopy',
                       'InfraredSpectroscopy',
                       'TransmissionElectronMicroscopy',
                       'Thermogravimetry',
                       'ESI_MS'],
         'slot_uri': 'voc4cat:0000108'} })
    gun_type: Optional[list[str]] = Field(default=[], description="""Type of electron gun""", json_schema_extra = { "linkml_meta": {'domain_of': ['TransmissionElectronMicroscopy', 'ScanningElectronMicroscopy'],
         'slot_uri': 'catcore:gun_type'} })
    acceleration_voltage: Optional[list[float]] = Field(default=[], description="""Acceleration voltage""", json_schema_extra = { "linkml_meta": {'domain_of': ['TransmissionElectronMicroscopy', 'ScanningElectronMicroscopy'],
         'slot_uri': 'catcore:acceleration_voltage',
         'unit': {'ucum_code': 'kV'}} })
    magnification_setting: Optional[list[float]] = Field(default=[], description="""Magnification setting""", json_schema_extra = { "linkml_meta": {'domain_of': ['RamanSpectroscopy', 'TransmissionElectronMicroscopy'],
         'slot_uri': 'AFR:0002226'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class ICPAES(CharacterizationTechnique):
    """
    Inductively-coupled plasma atomic emission spectroscopy
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CHMO:0000267',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    element_analyzed: Optional[list[str]] = Field(default=[], description="""Chemical element being analyzed""", json_schema_extra = { "linkml_meta": {'domain_of': ['XRayAbsorptionSpectroscopy', 'ICPAES'],
         'slot_uri': 'catcore:element_analyzed'} })
    calibration_method: Optional[list[str]] = Field(default=[], description="""Calibration method used""", json_schema_extra = { "linkml_meta": {'domain_of': ['ICPAES', 'EDX'], 'slot_uri': 'catcore:calibration_method'} })
    detection_limit: Optional[list[float]] = Field(default=[], description="""Detection limit""", json_schema_extra = { "linkml_meta": {'domain_of': ['ICPAES'], 'slot_uri': 'NCIT:C105701'} })
    matrix_effect_correction: Optional[list[str]] = Field(default=[], description="""Matrix effect correction method""", json_schema_extra = { "linkml_meta": {'domain_of': ['ICPAES'], 'slot_uri': 'catcore:matrix_effect_correction'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class ScanningElectronMicroscopy(CharacterizationTechnique):
    """
    Scanning electron microscopy
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'voc4cat:0000075',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    gun_type: Optional[list[str]] = Field(default=[], description="""Type of electron gun""", json_schema_extra = { "linkml_meta": {'domain_of': ['TransmissionElectronMicroscopy', 'ScanningElectronMicroscopy'],
         'slot_uri': 'catcore:gun_type'} })
    acceleration_voltage: Optional[list[float]] = Field(default=[], description="""Acceleration voltage""", json_schema_extra = { "linkml_meta": {'domain_of': ['TransmissionElectronMicroscopy', 'ScanningElectronMicroscopy'],
         'slot_uri': 'catcore:acceleration_voltage',
         'unit': {'ucum_code': 'kV'}} })
    image_resolution: Optional[list[float]] = Field(default=[], description="""Image resolution""", json_schema_extra = { "linkml_meta": {'domain_of': ['ScanningElectronMicroscopy'],
         'slot_uri': 'catcore:image_resolution',
         'unit': {'ucum_code': 'nm'}} })
    field_emitter: Optional[list[str]] = Field(default=[], description="""Field emitter type""", json_schema_extra = { "linkml_meta": {'domain_of': ['ScanningElectronMicroscopy'],
         'slot_uri': 'catcore:field_emitter'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class Thermogravimetry(CharacterizationTechnique):
    """
    Thermogravimetry
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CHMO:0000690',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    operation_mode: Optional[list[str]] = Field(default=[], description="""Operation mode of the instrument""", json_schema_extra = { "linkml_meta": {'domain_of': ['PowderXRD',
                       'XRayAbsorptionSpectroscopy',
                       'InfraredSpectroscopy',
                       'TransmissionElectronMicroscopy',
                       'Thermogravimetry',
                       'ESI_MS'],
         'slot_uri': 'voc4cat:0000108'} })
    atmosphere: Optional[list[str]] = Field(default=[], description="""Atmospheric conditions""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlasmaAssisted',
                       'CombustionSynthesis',
                       'MechanochemicalSynthesis',
                       'MolecularSynthesis',
                       'PowderXRD',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'Thermogravimetry',
                       'XPS',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'OperationParameters'],
         'slot_uri': 'catcore:atmosphere'} })
    initial_temperature: Optional[list[float]] = Field(default=[], description="""Initial temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thermogravimetry'],
         'slot_uri': 'NCIT:C164644',
         'unit': {'ucum_code': 'Cel'}} })
    final_temperature: Optional[list[float]] = Field(default=[], description="""Final temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thermogravimetry'],
         'slot_uri': 'NCIT:C164644',
         'unit': {'ucum_code': 'Cel'}} })
    heating_rate: Optional[list[float]] = Field(default=[], description="""Heating rate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thermogravimetry', 'TPO', 'TPR'],
         'slot_uri': 'catcore:heating_rate',
         'unit': {'ucum_code': 'Cel/min'}} })
    heating_procedure: Optional[list[str]] = Field(default=[], description="""Heating procedure used""", json_schema_extra = { "linkml_meta": {'domain_of': ['GCMS', 'Thermogravimetry'],
         'slot_uri': 'catcore:heating_procedure'} })
    sample_mass: Optional[list[float]] = Field(default=[], description="""Mass of sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thermogravimetry', 'BET'],
         'slot_uri': 'voc4cat:0007038',
         'unit': {'ucum_code': 'mg'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class XPS(CharacterizationTechnique):
    """
    X-ray photoelectron spectroscopy
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CHMO:0000404',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    xray_source: Optional[list[str]] = Field(default=[], description="""X-ray source used""", json_schema_extra = { "linkml_meta": {'domain_of': ['PowderXRD', 'XPS', 'SingleCrystalXRD'],
         'slot_uri': 'OBI:0001138'} })
    total_acquisition_time: Optional[list[float]] = Field(default=[], description="""Total acquisition time""", json_schema_extra = { "linkml_meta": {'domain_of': ['XPS'],
         'slot_uri': 'catcore:total_acquisition_time',
         'unit': {'ucum_code': 's'}} })
    number_of_scans: Optional[list[int]] = Field(default=[], description="""Number of scans performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'XPS',
                       'DRIFTS'],
         'slot_uri': 'AFR:0003051'} })
    spot_size: Optional[list[float]] = Field(default=[], description="""Spot size for analysis""", json_schema_extra = { "linkml_meta": {'domain_of': ['XPS'],
         'slot_uri': 'catcore:spot_size',
         'unit': {'ucum_code': 'mm'}} })
    lense_mode: Optional[list[str]] = Field(default=[], description="""Lens mode setting""", json_schema_extra = { "linkml_meta": {'domain_of': ['XPS'], 'slot_uri': 'voc4cat:0000108'} })
    minimum_energy: Optional[list[float]] = Field(default=[], description="""Minimum energy value""", json_schema_extra = { "linkml_meta": {'domain_of': ['XRayAbsorptionSpectroscopy', 'XPS'],
         'slot_uri': 'catcore:minimum_energy',
         'unit': {'ucum_code': 'eV'}} })
    maximum_energy: Optional[list[float]] = Field(default=[], description="""Maximum energy value""", json_schema_extra = { "linkml_meta": {'domain_of': ['XRayAbsorptionSpectroscopy', 'XPS'],
         'slot_uri': 'catcore:maximum_energy',
         'unit': {'ucum_code': 'eV'}} })
    step_size: Optional[list[float]] = Field(default=[], description="""Step size for measurements""", json_schema_extra = { "linkml_meta": {'domain_of': ['PowderXRD',
                       'InfraredSpectroscopy',
                       'XPS',
                       'DRIFTS',
                       'PhotoluminescenceSpectroscopy'],
         'slot_uri': 'AFR:0000950'} })
    pass_energy: Optional[list[float]] = Field(default=[], description="""Pass energy setting""", json_schema_extra = { "linkml_meta": {'domain_of': ['XPS'],
         'slot_uri': 'catcore:pass_energy',
         'unit': {'ucum_code': 'eV'}} })
    charge_compensation: Optional[list[str]] = Field(default=[], description="""Charge compensation method""", json_schema_extra = { "linkml_meta": {'domain_of': ['XPS'], 'slot_uri': 'catcore:charge_compensation'} })
    atmosphere: Optional[list[str]] = Field(default=[], description="""Atmospheric conditions""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlasmaAssisted',
                       'CombustionSynthesis',
                       'MechanochemicalSynthesis',
                       'MolecularSynthesis',
                       'PowderXRD',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'Thermogravimetry',
                       'XPS',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'OperationParameters'],
         'slot_uri': 'catcore:atmosphere'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class BET(CharacterizationTechnique):
    """
    Brunauer-Emmett-Teller surface area analysis
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:BET', 'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    adsorbate_gas: Optional[list[str]] = Field(default=[], description="""Adsorbate gas used""", json_schema_extra = { "linkml_meta": {'domain_of': ['BET'], 'slot_uri': 'catcore:adsorbate_gas'} })
    degassing_temperature: Optional[list[float]] = Field(default=[], description="""Degassing temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['BET'],
         'slot_uri': 'catcore:degassing_temperature',
         'unit': {'ucum_code': 'Cel'}} })
    measurement_temperature: Optional[list[float]] = Field(default=[], description="""Measurement temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['BET'],
         'slot_uri': 'catcore:measurement_temperature',
         'unit': {'ucum_code': 'K'}} })
    pore_size_distribution_method: Optional[list[str]] = Field(default=[], description="""Method for pore size distribution analysis""", json_schema_extra = { "linkml_meta": {'domain_of': ['BET'], 'slot_uri': 'catcore:pore_size_distribution_method'} })
    sample_mass: Optional[list[float]] = Field(default=[], description="""Mass of sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thermogravimetry', 'BET'],
         'slot_uri': 'voc4cat:0007038',
         'unit': {'ucum_code': 'mg'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class ElementalAnalysis(CharacterizationTechnique):
    """
    Elemental analysis
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CHMO:0001075',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    elements_analyzed: Optional[list[str]] = Field(default=[], description="""Elements analyzed""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementalAnalysis'], 'slot_uri': 'catcore:elements_analyzed'} })
    combustion_temperature: Optional[list[float]] = Field(default=[], description="""Combustion temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElementalAnalysis'],
         'slot_uri': 'catcore:combustion_temperature',
         'unit': {'ucum_code': 'Cel'}} })
    carrier_gas: Optional[list[str]] = Field(default=[], description="""Carrier gas used""", json_schema_extra = { "linkml_meta": {'domain_of': ['AtomicLayerDeposition', 'GCMS', 'ElementalAnalysis', 'ESI_MS'],
         'slot_uri': 'catcore:carrier_gas'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class UVVisSpectroscopy(CharacterizationTechnique):
    """
    Ultraviolet-visible spectroscopy
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'voc4cat:0000079',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    minimum_wavelength: Optional[list[float]] = Field(default=[], description="""Minimum wavelength""", json_schema_extra = { "linkml_meta": {'domain_of': ['UVVisSpectroscopy'],
         'slot_uri': 'catcore:minimum_wavelength',
         'unit': {'ucum_code': 'nm'}} })
    maximum_wavelength: Optional[list[float]] = Field(default=[], description="""Maximum wavelength""", json_schema_extra = { "linkml_meta": {'domain_of': ['UVVisSpectroscopy'],
         'slot_uri': 'catcore:maximum_wavelength',
         'unit': {'ucum_code': 'nm'}} })
    path_length: Optional[list[float]] = Field(default=[], description="""Path length of cell""", json_schema_extra = { "linkml_meta": {'domain_of': ['UVVisSpectroscopy'],
         'slot_uri': 'AFQ:0000268',
         'unit': {'ucum_code': 'cm'}} })
    solvent: Optional[list[str]] = Field(default=[], description="""Solvent used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Synthesis',
                       'NMRSpectroscopy',
                       'UVVisSpectroscopy',
                       'DynamicLightScattering'],
         'slot_uri': 'voc4cat:0007246'} })
    concentration: Optional[list[float]] = Field(default=[], description="""Concentration of sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['UVVisSpectroscopy', 'DynamicLightScattering', 'ESI_MS'],
         'slot_uri': 'voc4cat:0007244',
         'unit': {'ucum_code': 'mol/L'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class DRIFTS(CharacterizationTechnique):
    """
    Diffuse reflectance infrared Fourier transform spectroscopy
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CHMO:0000645',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    adsorption_gas: Optional[list[str]] = Field(default=[], description="""Adsorption gas used""", json_schema_extra = { "linkml_meta": {'domain_of': ['DRIFTS'], 'slot_uri': 'catcore:adsorption_gas'} })
    atmosphere: Optional[list[str]] = Field(default=[], description="""Atmospheric conditions""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlasmaAssisted',
                       'CombustionSynthesis',
                       'MechanochemicalSynthesis',
                       'MolecularSynthesis',
                       'PowderXRD',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'Thermogravimetry',
                       'XPS',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'OperationParameters'],
         'slot_uri': 'catcore:atmosphere'} })
    flow_rate: Optional[list[float]] = Field(default=[], description="""Flow rate""", json_schema_extra = { "linkml_meta": {'domain_of': ['FlameSprayPyrolysis',
                       'DRIFTS',
                       'ESI_MS',
                       'SizeExclusionChromatography',
                       'HPLC_MS'],
         'slot_uri': 'catcore:flow_rate',
         'unit': {'ucum_code': 'mL/min'}} })
    diluting_reference: Optional[list[str]] = Field(default=[], description="""Diluting reference material""", json_schema_extra = { "linkml_meta": {'domain_of': ['DRIFTS'], 'slot_uri': 'catcore:diluting_reference'} })
    ratio_reference_sample: Optional[list[float]] = Field(default=[], description="""Ratio of reference to sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['DRIFTS'], 'slot_uri': 'catcore:ratio_reference_sample'} })
    step_size: Optional[list[float]] = Field(default=[], description="""Step size for measurements""", json_schema_extra = { "linkml_meta": {'domain_of': ['PowderXRD',
                       'InfraredSpectroscopy',
                       'XPS',
                       'DRIFTS',
                       'PhotoluminescenceSpectroscopy'],
         'slot_uri': 'AFR:0000950'} })
    resolution: Optional[list[float]] = Field(default=[], description="""Spectral resolution""", json_schema_extra = { "linkml_meta": {'domain_of': ['DRIFTS', 'EDX'],
         'slot_uri': 'catcore:resolution',
         'unit': {'ucum_code': 'cm-1'}} })
    background_correction_method: Optional[list[str]] = Field(default=[], description="""Background correction method used""", json_schema_extra = { "linkml_meta": {'domain_of': ['DRIFTS'], 'slot_uri': 'catcore:background_correction_method'} })
    temperature: Optional[list[float]] = Field(default=[], description="""Temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['SonochemicalSynthesis',
                       'Sublimation',
                       'PowderXRD',
                       'XRayAbsorptionSpectroscopy',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'DynamicLightScattering',
                       'PhotoluminescenceSpectroscopy',
                       'PhotoluminescenceLifetime',
                       'SizeExclusionChromatography',
                       'HPLC_MS',
                       'SingleCrystalXRD',
                       'ConductivityMeasurement',
                       'Microkinetics',
                       'MonteCarlo',
                       'AqueousStability'],
         'slot_uri': 'AFR:0001584',
         'unit': {'ucum_code': 'Cel'}} })
    number_of_scans: Optional[list[int]] = Field(default=[], description="""Number of scans performed""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'XPS',
                       'DRIFTS'],
         'slot_uri': 'AFR:0003051'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class CyclicVoltammetry(CharacterizationTechnique):
    """
    Cyclic voltammetry
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CHMO:0000025',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    scan_rate: Optional[list[float]] = Field(default=[], description="""Scan rate for voltammetry""", json_schema_extra = { "linkml_meta": {'domain_of': ['CyclicVoltammetry'],
         'slot_uri': 'voc4cat:0007213',
         'unit': {'ucum_code': 'mV/s'}} })
    minimum_potential: Optional[list[float]] = Field(default=[], description="""Minimum potential""", json_schema_extra = { "linkml_meta": {'domain_of': ['CyclicVoltammetry'],
         'slot_uri': 'catcore:minimum_potential',
         'unit': {'ucum_code': 'V'}} })
    maximum_potential: Optional[list[float]] = Field(default=[], description="""Maximum potential""", json_schema_extra = { "linkml_meta": {'domain_of': ['CyclicVoltammetry'],
         'slot_uri': 'catcore:maximum_potential',
         'unit': {'ucum_code': 'V'}} })
    step_size_potential: Optional[list[float]] = Field(default=[], description="""Step size for potential""", json_schema_extra = { "linkml_meta": {'domain_of': ['CyclicVoltammetry'],
         'slot_uri': 'voc4cat:0007218',
         'unit': {'ucum_code': 'mV'}} })
    electrolyte_composition: Optional[list[str]] = Field(default=[], description="""Composition of electrolyte""", json_schema_extra = { "linkml_meta": {'domain_of': ['CyclicVoltammetry'],
         'slot_uri': 'catcore:electrolyte_composition'} })
    electrolyte_concentration: Optional[list[float]] = Field(default=[], description="""Concentration of electrolyte""", json_schema_extra = { "linkml_meta": {'domain_of': ['CyclicVoltammetry'],
         'slot_uri': 'catcore:electrolyte_concentration',
         'unit': {'ucum_code': 'mol/L'}} })
    reference_electrode: Optional[list[str]] = Field(default=[], description="""Reference electrode used""", json_schema_extra = { "linkml_meta": {'domain_of': ['CyclicVoltammetry'], 'slot_uri': 'voc4cat:0007204'} })
    number_of_cycles: Optional[list[int]] = Field(default=[], description="""Number of cycles in the process""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impregnation',
                       'CoPrecipitation',
                       'AtomicLayerDeposition',
                       'DepositionPrecipitation',
                       'SonochemicalSynthesis',
                       'MolecularSynthesis',
                       'XRayAbsorptionSpectroscopy',
                       'CyclicVoltammetry'],
         'slot_uri': 'catcore:number_of_cycles'} })
    working_electrode: Optional[list[str]] = Field(default=[], description="""Working electrode used""", json_schema_extra = { "linkml_meta": {'domain_of': ['CyclicVoltammetry'], 'slot_uri': 'voc4cat:0007202'} })
    counter_electrode: Optional[list[str]] = Field(default=[], description="""Counter electrode used""", json_schema_extra = { "linkml_meta": {'domain_of': ['CyclicVoltammetry'], 'slot_uri': 'voc4cat:0007203'} })
    atmosphere: Optional[list[str]] = Field(default=[], description="""Atmospheric conditions""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlasmaAssisted',
                       'CombustionSynthesis',
                       'MechanochemicalSynthesis',
                       'MolecularSynthesis',
                       'PowderXRD',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'Thermogravimetry',
                       'XPS',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'OperationParameters'],
         'slot_uri': 'catcore:atmosphere'} })
    temperature: Optional[list[float]] = Field(default=[], description="""Temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['SonochemicalSynthesis',
                       'Sublimation',
                       'PowderXRD',
                       'XRayAbsorptionSpectroscopy',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'DynamicLightScattering',
                       'PhotoluminescenceSpectroscopy',
                       'PhotoluminescenceLifetime',
                       'SizeExclusionChromatography',
                       'HPLC_MS',
                       'SingleCrystalXRD',
                       'ConductivityMeasurement',
                       'Microkinetics',
                       'MonteCarlo',
                       'AqueousStability'],
         'slot_uri': 'AFR:0001584',
         'unit': {'ucum_code': 'Cel'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class DynamicLightScattering(CharacterizationTechnique):
    """
    Dynamic light scattering
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CHMO:0000167',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    solvent: Optional[list[str]] = Field(default=[], description="""Solvent used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Synthesis',
                       'NMRSpectroscopy',
                       'UVVisSpectroscopy',
                       'DynamicLightScattering'],
         'slot_uri': 'voc4cat:0007246'} })
    concentration: Optional[list[float]] = Field(default=[], description="""Concentration of sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['UVVisSpectroscopy', 'DynamicLightScattering', 'ESI_MS'],
         'slot_uri': 'voc4cat:0007244',
         'unit': {'ucum_code': 'mol/L'}} })
    light_wavelength: Optional[list[float]] = Field(default=[], description="""Light wavelength used""", json_schema_extra = { "linkml_meta": {'domain_of': ['DynamicLightScattering'],
         'slot_uri': 'voc4cat:0000176',
         'unit': {'ucum_code': 'nm'}} })
    scattering_angle: Optional[list[float]] = Field(default=[], description="""Scattering angle""", json_schema_extra = { "linkml_meta": {'domain_of': ['DynamicLightScattering'],
         'slot_uri': 'catcore:scattering_angle',
         'unit': {'ucum_code': 'deg'}} })
    refractive_index: Optional[list[float]] = Field(default=[], description="""Refractive index""", json_schema_extra = { "linkml_meta": {'domain_of': ['DynamicLightScattering'],
         'slot_uri': 'catcore:refractive_index'} })
    temperature: Optional[list[float]] = Field(default=[], description="""Temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['SonochemicalSynthesis',
                       'Sublimation',
                       'PowderXRD',
                       'XRayAbsorptionSpectroscopy',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'DynamicLightScattering',
                       'PhotoluminescenceSpectroscopy',
                       'PhotoluminescenceLifetime',
                       'SizeExclusionChromatography',
                       'HPLC_MS',
                       'SingleCrystalXRD',
                       'ConductivityMeasurement',
                       'Microkinetics',
                       'MonteCarlo',
                       'AqueousStability'],
         'slot_uri': 'AFR:0001584',
         'unit': {'ucum_code': 'Cel'}} })
    dispersant: Optional[list[str]] = Field(default=[], description="""Dispersant used""", json_schema_extra = { "linkml_meta": {'domain_of': ['FlameSprayPyrolysis', 'DynamicLightScattering'],
         'slot_uri': 'catcore:dispersant'} })
    measurement_duration: Optional[list[float]] = Field(default=[], description="""Duration of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['DynamicLightScattering'],
         'slot_uri': 'catcore:measurement_duration',
         'unit': {'ucum_code': 's'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class ESIMS(CharacterizationTechnique):
    """
    Electrospray ionisation mass spectrometry
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CHMO:0000482',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    operation_mode: Optional[list[str]] = Field(default=[], description="""Operation mode of the instrument""", json_schema_extra = { "linkml_meta": {'domain_of': ['PowderXRD',
                       'XRayAbsorptionSpectroscopy',
                       'InfraredSpectroscopy',
                       'TransmissionElectronMicroscopy',
                       'Thermogravimetry',
                       'ESI_MS'],
         'slot_uri': 'voc4cat:0000108'} })
    mz_minimum: Optional[list[float]] = Field(default=[], description="""Minimum m/z value""", json_schema_extra = { "linkml_meta": {'domain_of': ['GCMS', 'ESI_MS'], 'slot_uri': 'AFR:0002652'} })
    mz_maximum: Optional[list[float]] = Field(default=[], description="""Maximum m/z value""", json_schema_extra = { "linkml_meta": {'domain_of': ['GCMS', 'ESI_MS'], 'slot_uri': 'AFR:0002653'} })
    spray_voltage: Optional[list[float]] = Field(default=[], description="""Spray voltage for ionization""", json_schema_extra = { "linkml_meta": {'domain_of': ['ESI_MS'],
         'slot_uri': 'CHMO:0002792',
         'unit': {'ucum_code': 'kV'}} })
    capillary_temperature: Optional[list[float]] = Field(default=[], description="""Capillary temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['ESI_MS'],
         'slot_uri': 'catcore:capillary_temperature',
         'unit': {'ucum_code': 'Cel'}} })
    solvent_composition: Optional[list[str]] = Field(default=[], description="""Solvent composition""", json_schema_extra = { "linkml_meta": {'domain_of': ['ESI_MS'], 'slot_uri': 'voc4cat:0007246'} })
    flow_rate: Optional[list[float]] = Field(default=[], description="""Flow rate""", json_schema_extra = { "linkml_meta": {'domain_of': ['FlameSprayPyrolysis',
                       'DRIFTS',
                       'ESI_MS',
                       'SizeExclusionChromatography',
                       'HPLC_MS'],
         'slot_uri': 'catcore:flow_rate',
         'unit': {'ucum_code': 'mL/min'}} })
    carrier_gas: Optional[list[str]] = Field(default=[], description="""Carrier gas used""", json_schema_extra = { "linkml_meta": {'domain_of': ['AtomicLayerDeposition', 'GCMS', 'ElementalAnalysis', 'ESI_MS'],
         'slot_uri': 'catcore:carrier_gas'} })
    concentration: Optional[list[float]] = Field(default=[], description="""Concentration of sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['UVVisSpectroscopy', 'DynamicLightScattering', 'ESI_MS'],
         'slot_uri': 'voc4cat:0007244',
         'unit': {'ucum_code': 'mol/L'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class PhotoluminescenceSpectroscopy(CharacterizationTechnique):
    """
    Photoluminescence spectroscopy
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:PhotoluminescenceSpectroscopy',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    excitation_wavelength: Optional[list[float]] = Field(default=[], description="""Excitation wavelength""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhotoluminescenceSpectroscopy', 'PhotoluminescenceLifetime'],
         'slot_uri': 'AFR:0002479',
         'unit': {'ucum_code': 'nm'}} })
    emission_wavelength: Optional[list[float]] = Field(default=[], description="""Emission wavelength""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhotoluminescenceSpectroscopy', 'PhotoluminescenceLifetime'],
         'slot_uri': 'NCIT:C204101',
         'unit': {'ucum_code': 'nm'}} })
    optical_filter: Optional[list[str]] = Field(default=[], description="""Optical filter used""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhotoluminescenceSpectroscopy', 'PhotoluminescenceLifetime'],
         'slot_uri': 'catcore:optical_filter'} })
    temperature: Optional[list[float]] = Field(default=[], description="""Temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['SonochemicalSynthesis',
                       'Sublimation',
                       'PowderXRD',
                       'XRayAbsorptionSpectroscopy',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'DynamicLightScattering',
                       'PhotoluminescenceSpectroscopy',
                       'PhotoluminescenceLifetime',
                       'SizeExclusionChromatography',
                       'HPLC_MS',
                       'SingleCrystalXRD',
                       'ConductivityMeasurement',
                       'Microkinetics',
                       'MonteCarlo',
                       'AqueousStability'],
         'slot_uri': 'AFR:0001584',
         'unit': {'ucum_code': 'Cel'}} })
    emission_range: Optional[list[str]] = Field(default=[], description="""Emission range measured""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhotoluminescenceSpectroscopy'],
         'slot_uri': 'catcore:emission_range'} })
    slit_width: Optional[list[float]] = Field(default=[], description="""Slit width setting""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhotoluminescenceSpectroscopy'],
         'slot_uri': 'catcore:slit_width',
         'unit': {'ucum_code': 'nm'}} })
    step_size: Optional[list[float]] = Field(default=[], description="""Step size for measurements""", json_schema_extra = { "linkml_meta": {'domain_of': ['PowderXRD',
                       'InfraredSpectroscopy',
                       'XPS',
                       'DRIFTS',
                       'PhotoluminescenceSpectroscopy'],
         'slot_uri': 'AFR:0000950'} })
    integration_time: Optional[list[float]] = Field(default=[], description="""Integration time""", json_schema_extra = { "linkml_meta": {'domain_of': ['RamanSpectroscopy', 'PhotoluminescenceSpectroscopy'],
         'slot_uri': 'AFR:0001671',
         'unit': {'ucum_code': 's'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class PhotoluminescenceLifetime(CharacterizationTechnique):
    """
    Photoluminescence lifetime measurement
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:PhotoluminescenceLifetime',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    excitation_wavelength: Optional[list[float]] = Field(default=[], description="""Excitation wavelength""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhotoluminescenceSpectroscopy', 'PhotoluminescenceLifetime'],
         'slot_uri': 'AFR:0002479',
         'unit': {'ucum_code': 'nm'}} })
    emission_wavelength: Optional[list[float]] = Field(default=[], description="""Emission wavelength""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhotoluminescenceSpectroscopy', 'PhotoluminescenceLifetime'],
         'slot_uri': 'NCIT:C204101',
         'unit': {'ucum_code': 'nm'}} })
    optical_filter: Optional[list[str]] = Field(default=[], description="""Optical filter used""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhotoluminescenceSpectroscopy', 'PhotoluminescenceLifetime'],
         'slot_uri': 'catcore:optical_filter'} })
    temperature: Optional[list[float]] = Field(default=[], description="""Temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['SonochemicalSynthesis',
                       'Sublimation',
                       'PowderXRD',
                       'XRayAbsorptionSpectroscopy',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'DynamicLightScattering',
                       'PhotoluminescenceSpectroscopy',
                       'PhotoluminescenceLifetime',
                       'SizeExclusionChromatography',
                       'HPLC_MS',
                       'SingleCrystalXRD',
                       'ConductivityMeasurement',
                       'Microkinetics',
                       'MonteCarlo',
                       'AqueousStability'],
         'slot_uri': 'AFR:0001584',
         'unit': {'ucum_code': 'Cel'}} })
    lifetime_fitting_model: Optional[list[str]] = Field(default=[], description="""Lifetime fitting model used""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhotoluminescenceLifetime'],
         'slot_uri': 'catcore:lifetime_fitting_model'} })
    number_of_shots: Optional[list[int]] = Field(default=[], description="""Number of shots for measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhotoluminescenceLifetime'],
         'slot_uri': 'catcore:number_of_shots'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class SizeExclusionChromatography(CharacterizationTechnique):
    """
    Size-exclusion chromatography
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'AFP:0000843', 'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    column_type: Optional[list[str]] = Field(default=[], description="""Type of chromatography column""", json_schema_extra = { "linkml_meta": {'domain_of': ['GCMS', 'SizeExclusionChromatography', 'HPLC_MS'],
         'slot_uri': 'AFR:0002026'} })
    temperature: Optional[list[float]] = Field(default=[], description="""Temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['SonochemicalSynthesis',
                       'Sublimation',
                       'PowderXRD',
                       'XRayAbsorptionSpectroscopy',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'DynamicLightScattering',
                       'PhotoluminescenceSpectroscopy',
                       'PhotoluminescenceLifetime',
                       'SizeExclusionChromatography',
                       'HPLC_MS',
                       'SingleCrystalXRD',
                       'ConductivityMeasurement',
                       'Microkinetics',
                       'MonteCarlo',
                       'AqueousStability'],
         'slot_uri': 'AFR:0001584',
         'unit': {'ucum_code': 'Cel'}} })
    eluent: Optional[list[str]] = Field(default=[], description="""Eluent used""", json_schema_extra = { "linkml_meta": {'domain_of': ['SizeExclusionChromatography', 'HPLC_MS'],
         'slot_uri': 'AFRL:0000011'} })
    flow_rate: Optional[list[float]] = Field(default=[], description="""Flow rate""", json_schema_extra = { "linkml_meta": {'domain_of': ['FlameSprayPyrolysis',
                       'DRIFTS',
                       'ESI_MS',
                       'SizeExclusionChromatography',
                       'HPLC_MS'],
         'slot_uri': 'catcore:flow_rate',
         'unit': {'ucum_code': 'mL/min'}} })
    calibration_standard: Optional[list[str]] = Field(default=[], description="""Calibration standard used""", json_schema_extra = { "linkml_meta": {'domain_of': ['SizeExclusionChromatography'],
         'slot_uri': 'catcore:calibration_standard'} })
    injection_volume: Optional[list[float]] = Field(default=[], description="""Injection volume""", json_schema_extra = { "linkml_meta": {'domain_of': ['GCMS', 'SizeExclusionChromatography', 'HPLC_MS'],
         'slot_uri': 'AFR:0001577',
         'unit': {'ucum_code': 'uL'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class HPLCMS(CharacterizationTechnique):
    """
    High-performance liquid chromatography mass spectrometry
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CHMO:0000796',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    column_type: Optional[list[str]] = Field(default=[], description="""Type of chromatography column""", json_schema_extra = { "linkml_meta": {'domain_of': ['GCMS', 'SizeExclusionChromatography', 'HPLC_MS'],
         'slot_uri': 'AFR:0002026'} })
    eluent: Optional[list[str]] = Field(default=[], description="""Eluent used""", json_schema_extra = { "linkml_meta": {'domain_of': ['SizeExclusionChromatography', 'HPLC_MS'],
         'slot_uri': 'AFRL:0000011'} })
    gradient_program: Optional[list[str]] = Field(default=[], description="""Gradient program for elution""", json_schema_extra = { "linkml_meta": {'domain_of': ['HPLC_MS'], 'slot_uri': 'catcore:gradient_program'} })
    ionization_mode: Optional[list[str]] = Field(default=[], description="""Ionization mode used""", json_schema_extra = { "linkml_meta": {'domain_of': ['HPLC_MS'], 'slot_uri': 'catcore:ionization_mode'} })
    temperature: Optional[list[float]] = Field(default=[], description="""Temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['SonochemicalSynthesis',
                       'Sublimation',
                       'PowderXRD',
                       'XRayAbsorptionSpectroscopy',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'DynamicLightScattering',
                       'PhotoluminescenceSpectroscopy',
                       'PhotoluminescenceLifetime',
                       'SizeExclusionChromatography',
                       'HPLC_MS',
                       'SingleCrystalXRD',
                       'ConductivityMeasurement',
                       'Microkinetics',
                       'MonteCarlo',
                       'AqueousStability'],
         'slot_uri': 'AFR:0001584',
         'unit': {'ucum_code': 'Cel'}} })
    flow_rate: Optional[list[float]] = Field(default=[], description="""Flow rate""", json_schema_extra = { "linkml_meta": {'domain_of': ['FlameSprayPyrolysis',
                       'DRIFTS',
                       'ESI_MS',
                       'SizeExclusionChromatography',
                       'HPLC_MS'],
         'slot_uri': 'catcore:flow_rate',
         'unit': {'ucum_code': 'mL/min'}} })
    injection_volume: Optional[list[float]] = Field(default=[], description="""Injection volume""", json_schema_extra = { "linkml_meta": {'domain_of': ['GCMS', 'SizeExclusionChromatography', 'HPLC_MS'],
         'slot_uri': 'AFR:0001577',
         'unit': {'ucum_code': 'uL'}} })
    external_standard: Optional[list[str]] = Field(default=[], description="""External standard used for calibration""", json_schema_extra = { "linkml_meta": {'domain_of': ['GCMS', 'HPLC_MS'], 'slot_uri': 'catcore:external_standard'} })
    internal_standard: Optional[list[str]] = Field(default=[], description="""Internal standard used for calibration""", json_schema_extra = { "linkml_meta": {'domain_of': ['GCMS', 'HPLC_MS'], 'slot_uri': 'catcore:internal_standard'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class SingleCrystalXRD(CharacterizationTechnique):
    """
    Single crystal X-ray diffraction
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CHMO:0000852',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    xray_source: Optional[list[str]] = Field(default=[], description="""X-ray source used""", json_schema_extra = { "linkml_meta": {'domain_of': ['PowderXRD', 'XPS', 'SingleCrystalXRD'],
         'slot_uri': 'OBI:0001138'} })
    temperature: Optional[list[float]] = Field(default=[], description="""Temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['SonochemicalSynthesis',
                       'Sublimation',
                       'PowderXRD',
                       'XRayAbsorptionSpectroscopy',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'DynamicLightScattering',
                       'PhotoluminescenceSpectroscopy',
                       'PhotoluminescenceLifetime',
                       'SizeExclusionChromatography',
                       'HPLC_MS',
                       'SingleCrystalXRD',
                       'ConductivityMeasurement',
                       'Microkinetics',
                       'MonteCarlo',
                       'AqueousStability'],
         'slot_uri': 'AFR:0001584',
         'unit': {'ucum_code': 'Cel'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class EDX(CharacterizationTechnique):
    """
    Energy-dispersive X-ray emission spectroscopy
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CHMO:0000309',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    primary_energy: Optional[list[float]] = Field(default=[], description="""Primary energy of electron beam""", json_schema_extra = { "linkml_meta": {'domain_of': ['EDX'],
         'slot_uri': 'catcore:primary_energy',
         'unit': {'ucum_code': 'keV'}} })
    counting_time: Optional[list[float]] = Field(default=[], description="""Counting time for detection""", json_schema_extra = { "linkml_meta": {'domain_of': ['EDX'],
         'slot_uri': 'catcore:counting_time',
         'unit': {'ucum_code': 's'}} })
    resolution: Optional[list[float]] = Field(default=[], description="""Spectral resolution""", json_schema_extra = { "linkml_meta": {'domain_of': ['DRIFTS', 'EDX'],
         'slot_uri': 'catcore:resolution',
         'unit': {'ucum_code': 'cm-1'}} })
    calibration_method: Optional[list[str]] = Field(default=[], description="""Calibration method used""", json_schema_extra = { "linkml_meta": {'domain_of': ['ICPAES', 'EDX'], 'slot_uri': 'catcore:calibration_method'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class TPO(CharacterizationTechnique):
    """
    Temperature-programmed oxidation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CHMO:0002907',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    oxidizing_gas_composition: Optional[list[str]] = Field(default=[], description="""Composition of oxidizing gas""", json_schema_extra = { "linkml_meta": {'domain_of': ['TPO'], 'slot_uri': 'catcore:oxidizing_gas_composition'} })
    heating_rate: Optional[list[float]] = Field(default=[], description="""Heating rate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thermogravimetry', 'TPO', 'TPR'],
         'slot_uri': 'catcore:heating_rate',
         'unit': {'ucum_code': 'Cel/min'}} })
    minimum_temperature: Optional[list[float]] = Field(default=[], description="""Minimum temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['TPO', 'TPR'],
         'slot_uri': 'catcore:minimum_temperature',
         'unit': {'ucum_code': 'Cel'}} })
    maximum_temperature: Optional[list[float]] = Field(default=[], description="""Maximum temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['TPO', 'TPR'],
         'slot_uri': 'catcore:maximum_temperature',
         'unit': {'ucum_code': 'Cel'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class TPR(CharacterizationTechnique):
    """
    Temperature-programmed reduction
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'CHMO:0002908',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    reducing_gas_composition: Optional[list[str]] = Field(default=[], description="""Composition of reducing gas""", json_schema_extra = { "linkml_meta": {'domain_of': ['TPR'], 'slot_uri': 'catcore:reducing_gas_composition'} })
    heating_rate: Optional[list[float]] = Field(default=[], description="""Heating rate""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thermogravimetry', 'TPO', 'TPR'],
         'slot_uri': 'catcore:heating_rate',
         'unit': {'ucum_code': 'Cel/min'}} })
    minimum_temperature: Optional[list[float]] = Field(default=[], description="""Minimum temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['TPO', 'TPR'],
         'slot_uri': 'catcore:minimum_temperature',
         'unit': {'ucum_code': 'Cel'}} })
    maximum_temperature: Optional[list[float]] = Field(default=[], description="""Maximum temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['TPO', 'TPR'],
         'slot_uri': 'catcore:maximum_temperature',
         'unit': {'ucum_code': 'Cel'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class ConductivityMeasurement(CharacterizationTechnique):
    """
    Conductivity measurement
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:ConductivityMeasurement',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    temperature: Optional[list[float]] = Field(default=[], description="""Temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['SonochemicalSynthesis',
                       'Sublimation',
                       'PowderXRD',
                       'XRayAbsorptionSpectroscopy',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'DynamicLightScattering',
                       'PhotoluminescenceSpectroscopy',
                       'PhotoluminescenceLifetime',
                       'SizeExclusionChromatography',
                       'HPLC_MS',
                       'SingleCrystalXRD',
                       'ConductivityMeasurement',
                       'Microkinetics',
                       'MonteCarlo',
                       'AqueousStability'],
         'slot_uri': 'AFR:0001584',
         'unit': {'ucum_code': 'Cel'}} })
    electrode_configuration: Optional[list[str]] = Field(default=[], description="""Configuration of electrodes""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConductivityMeasurement'],
         'slot_uri': 'catcore:electrode_configuration'} })
    frequency: Optional[list[float]] = Field(default=[], description="""Frequency of measurement""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConductivityMeasurement'],
         'slot_uri': 'voc4cat:0007239',
         'unit': {'ucum_code': 'Hz'}} })
    ac_dc_mode: Optional[list[str]] = Field(default=[], description="""AC or DC measurement mode""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConductivityMeasurement'], 'slot_uri': 'catcore:ac_dc_mode'} })
    sample_geometry: Optional[list[str]] = Field(default=[], description="""Geometry of the sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['ConductivityMeasurement'],
         'slot_uri': 'catcore:sample_geometry'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class Reaction(CatCoreEntity):
    """
    The data class 'Reaction' describes the minimum information which should be reported 
    with research data concerning the reaction for which the catalyst is applied.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/nfdi4cat/catcore',
         'slot_usage': {'catalyst_quantity': {'name': 'catalyst_quantity',
                                              'required': True},
                        'catalyst_type': {'name': 'catalyst_type',
                                          'recommended': True,
                                          'required': False},
                        'operation_parameters': {'name': 'operation_parameters',
                                                 'required': True},
                        'product_identification_method': {'name': 'product_identification_method',
                                                          'required': True},
                        'reactant': {'name': 'reactant', 'required': True},
                        'reactor_design_type': {'name': 'reactor_design_type',
                                                'required': True}}})

    catalyst_quantity: list[float] = Field(default=..., description="""Quantity of catalyst used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Reaction'],
         'slot_uri': 'catcore:catalyst_quantity',
         'unit': {'ucum_code': 'g'}} })
    reactor_design_type: list[ReactorDesignType] = Field(default=..., description="""Type of reactor design""", json_schema_extra = { "linkml_meta": {'domain_of': ['Reaction'], 'slot_uri': 'voc4cat:0007018'} })
    reactant: list[str] = Field(default=..., description="""Reactant used in the reaction""", json_schema_extra = { "linkml_meta": {'domain_of': ['Reaction'], 'slot_uri': 'voc4cat:0000101'} })
    operation_parameters: list[OperationParameters] = Field(default=..., description="""Operation parameters for the reaction""", json_schema_extra = { "linkml_meta": {'domain_of': ['Reaction'], 'slot_uri': 'voc4cat:0000142'} })
    product_identification_method: list[ProductIdentificationMethod] = Field(default=..., description="""Method used for product identification""", json_schema_extra = { "linkml_meta": {'domain_of': ['Reaction'], 'slot_uri': 'voc4cat:0000129'} })
    catalyst_type: Optional[list[str]] = Field(default=[], description="""Type of catalyst""", json_schema_extra = { "linkml_meta": {'domain_of': ['Reaction'], 'recommended': True, 'slot_uri': 'voc4cat:0007014'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class ReactorDesignType(CatCoreEntity):
    """
    Type of reactor design used
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class ElectrochemicalReactor(ReactorDesignType):
    """
    Electrochemical reactor
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'voc4cat:0000193',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class CSTR(ReactorDesignType):
    """
    Continuous stirred tank reactor
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'voc4cat:0007019',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class PlugFlowReactor(ReactorDesignType):
    """
    Plug flow reactor model
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'voc4cat:0007102',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class Autoclave(ReactorDesignType):
    """
    Autoclave reactor
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'NCIT:C93052', 'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class SlurryReactor(ReactorDesignType):
    """
    Slurry reactor
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:SlurryReactor',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class Microreactor(ReactorDesignType):
    """
    Microreactor
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'voc4cat:0000234',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class FixedBedReactor(ReactorDesignType):
    """
    Fixed bed reactor
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:FixedBedReactor',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class FluidizedBedReactor(ReactorDesignType):
    """
    Fluidized bed reactor
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:FluidizedBedReactor',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    gas_distributor_type: Optional[list[str]] = Field(default=[], description="""Type of gas distributor""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluidizedBedReactor'],
         'slot_uri': 'catcore:gas_distributor_type'} })
    bed_expansion_height: Optional[list[float]] = Field(default=[], description="""Bed expansion height""", json_schema_extra = { "linkml_meta": {'domain_of': ['FluidizedBedReactor'],
         'slot_uri': 'catcore:bed_expansion_height',
         'unit': {'ucum_code': 'cm'}} })
    bubble_size_distribution: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['FluidizedBedReactor']} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class OperationParameters(CatCoreEntity):
    """
    Operation parameters for the reaction
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    reactor_temperature_range: Optional[list[str]] = Field(default=[], description="""Temperature range in reactor""", json_schema_extra = { "linkml_meta": {'domain_of': ['OperationParameters'], 'slot_uri': 'voc4cat:0007032'} })
    atmosphere: Optional[list[str]] = Field(default=[], description="""Atmospheric conditions""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlasmaAssisted',
                       'CombustionSynthesis',
                       'MechanochemicalSynthesis',
                       'MolecularSynthesis',
                       'PowderXRD',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'Thermogravimetry',
                       'XPS',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'OperationParameters'],
         'slot_uri': 'catcore:atmosphere'} })
    experiment_pressure: Optional[list[float]] = Field(default=[], description="""Pressure during experiment""", json_schema_extra = { "linkml_meta": {'domain_of': ['OperationParameters'],
         'slot_uri': 'voc4cat:0000118',
         'unit': {'ucum_code': 'bar'}} })
    feed_composition_range: Optional[list[str]] = Field(default=[], description="""Range of feed composition""", json_schema_extra = { "linkml_meta": {'domain_of': ['OperationParameters'],
         'slot_uri': 'catcore:feed_composition_range'} })
    experiment_duration: Optional[list[float]] = Field(default=[], description="""Duration of the experiment""", json_schema_extra = { "linkml_meta": {'domain_of': ['PowderXRD', 'OperationParameters'],
         'slot_uri': 'AFR:0002455',
         'unit': {'ucum_code': 'h'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class ProductIdentificationMethod(CatCoreEntity):
    """
    Method used for product identification
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    equipment: Optional[list[str]] = Field(default=[], description="""Equipment used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Solvothermal',
                       'PlasmaAssisted',
                       'CombustionSynthesis',
                       'MicrowaveAssisted',
                       'MechanochemicalSynthesis',
                       'Characterization',
                       'ProductIdentificationMethod'],
         'slot_uri': 'voc4cat:0000187'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class Simulation(CatCoreEntity):
    """
    The data class 'Simulation' describes the minimum information which should be reported 
    with research data for conducting simulations in the field of catalysis.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/nfdi4cat/catcore',
         'slot_usage': {'calculated_property': {'name': 'calculated_property',
                                                'required': True},
                        'simulation_method': {'name': 'simulation_method',
                                              'required': True},
                        'software_package': {'name': 'software_package',
                                             'required': True}}})

    software_package: list[str] = Field(default=..., description="""Software or package used for simulation""", json_schema_extra = { "linkml_meta": {'domain_of': ['Simulation'], 'slot_uri': 'catcore:software_package'} })
    simulation_method: list[SimulationMethod] = Field(default=..., description="""Simulation method used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Simulation'], 'slot_uri': 'catcore:simulation_method'} })
    calculated_property: list[CalculatedProperty] = Field(default=..., description="""Property calculated from simulation""", json_schema_extra = { "linkml_meta": {'domain_of': ['Simulation'], 'slot_uri': 'catcore:calculated_property'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class SimulationMethod(CatCoreEntity):
    """
    Simulation method used
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class DFT(SimulationMethod):
    """
    Density functional theory
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:DFT', 'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    exchange_correlation_functional: Optional[list[str]] = Field(default=[], description="""Exchange-correlation functional used (e.g., PBE, B3LYP)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DFT'], 'slot_uri': 'catcore:exchange_correlation_functional'} })
    energy_cutoff: Optional[list[float]] = Field(default=[], description="""Energy cutoff for plane wave basis""", json_schema_extra = { "linkml_meta": {'domain_of': ['DFT',
                       'DielectricTensors',
                       'EquationsOfState',
                       'ElectronicStructure'],
         'slot_uri': 'catcore:energy_cutoff',
         'unit': {'ucum_code': 'eV'}} })
    convergence_criteria: Optional[list[str]] = Field(default=[], description="""Convergence criteria (e.g., energy, force)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DFT', 'DielectricTensors'],
         'slot_uri': 'catcore:convergence_criteria'} })
    dft_u_parameters: Optional[list[str]] = Field(default=[], description="""DFT+U parameters used""", json_schema_extra = { "linkml_meta": {'domain_of': ['DFT'], 'slot_uri': 'catcore:dft_u_parameters'} })
    spin_polarization: Optional[list[bool]] = Field(default=[], description="""Spin polarization setting""", json_schema_extra = { "linkml_meta": {'domain_of': ['DFT'], 'slot_uri': 'catcore:spin_polarization'} })
    total_energy_per_atom: Optional[list[float]] = Field(default=[], description="""Total energy per atom""", json_schema_extra = { "linkml_meta": {'domain_of': ['DFT'],
         'slot_uri': 'catcore:total_energy_per_atom',
         'unit': {'ucum_code': 'eV'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class MolecularDynamics(SimulationMethod):
    """
    Molecular dynamics
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'NCIT:C18097', 'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    force_field: Optional[list[str]] = Field(default=[], description="""Force field used""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularDynamics'], 'slot_uri': 'catcore:force_field'} })
    simulation_timestep: Optional[list[float]] = Field(default=[], description="""Time step for simulation""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularDynamics'],
         'slot_uri': 'APOLLO_SV:00000012',
         'unit': {'ucum_code': 'fs'}} })
    simulation_time: Optional[list[float]] = Field(default=[], description="""Total simulation time""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularDynamics'],
         'slot_uri': 'catcore:simulation_time',
         'unit': {'ucum_code': 'ps'}} })
    ensemble_type: Optional[list[str]] = Field(default=[], description="""Ensemble type (e.g., NVT, NPT)""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularDynamics'], 'slot_uri': 'catcore:ensemble_type'} })
    number_of_atoms: Optional[list[int]] = Field(default=[], description="""Number of atoms in simulation""", json_schema_extra = { "linkml_meta": {'domain_of': ['MolecularDynamics'], 'slot_uri': 'catcore:number_of_atoms'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class Microkinetics(SimulationMethod):
    """
    Microkinetics simulation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:Microkinetics',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    rate_constants: Optional[list[str]] = Field(default=[], description="""Rate constants or Arrhenius parameters""", json_schema_extra = { "linkml_meta": {'domain_of': ['Microkinetics'], 'slot_uri': 'NCIT:C94967'} })
    solver_type: Optional[list[str]] = Field(default=[], description="""Type of solver used""", json_schema_extra = { "linkml_meta": {'domain_of': ['Microkinetics'], 'slot_uri': 'catcore:solver_type'} })
    temperature: Optional[list[float]] = Field(default=[], description="""Temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['SonochemicalSynthesis',
                       'Sublimation',
                       'PowderXRD',
                       'XRayAbsorptionSpectroscopy',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'DynamicLightScattering',
                       'PhotoluminescenceSpectroscopy',
                       'PhotoluminescenceLifetime',
                       'SizeExclusionChromatography',
                       'HPLC_MS',
                       'SingleCrystalXRD',
                       'ConductivityMeasurement',
                       'Microkinetics',
                       'MonteCarlo',
                       'AqueousStability'],
         'slot_uri': 'AFR:0001584',
         'unit': {'ucum_code': 'Cel'}} })
    pressure: Optional[list[float]] = Field(default=[], description="""Pressure in simulation""", json_schema_extra = { "linkml_meta": {'domain_of': ['Microkinetics'],
         'slot_uri': 'catcore:pressure',
         'unit': {'ucum_code': 'bar'}} })
    surface_coverage: Optional[list[float]] = Field(default=[], description="""Surface coverage of species""", json_schema_extra = { "linkml_meta": {'domain_of': ['Microkinetics'], 'slot_uri': 'catcore:surface_coverage'} })
    activation_energy: Optional[list[float]] = Field(default=[], description="""Activation energy for each step""", json_schema_extra = { "linkml_meta": {'domain_of': ['Microkinetics'],
         'slot_uri': 'catcore:activation_energy',
         'unit': {'ucum_code': 'eV'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class MonteCarlo(SimulationMethod):
    """
    Monte Carlo simulation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:MonteCarlo',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    interaction_potential: Optional[list[str]] = Field(default=[], description="""Interaction potential used""", json_schema_extra = { "linkml_meta": {'domain_of': ['MonteCarlo'], 'slot_uri': 'catcore:interaction_potential'} })
    number_of_steps: Optional[list[int]] = Field(default=[], description="""Number of Monte Carlo steps""", json_schema_extra = { "linkml_meta": {'domain_of': ['MonteCarlo'], 'slot_uri': 'catcore:number_of_steps'} })
    temperature: Optional[list[float]] = Field(default=[], description="""Temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['SonochemicalSynthesis',
                       'Sublimation',
                       'PowderXRD',
                       'XRayAbsorptionSpectroscopy',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'DynamicLightScattering',
                       'PhotoluminescenceSpectroscopy',
                       'PhotoluminescenceLifetime',
                       'SizeExclusionChromatography',
                       'HPLC_MS',
                       'SingleCrystalXRD',
                       'ConductivityMeasurement',
                       'Microkinetics',
                       'MonteCarlo',
                       'AqueousStability'],
         'slot_uri': 'AFR:0001584',
         'unit': {'ucum_code': 'Cel'}} })
    lattice_size_type: Optional[list[str]] = Field(default=[], description="""Lattice size and type""", json_schema_extra = { "linkml_meta": {'domain_of': ['MonteCarlo'], 'slot_uri': 'catcore:lattice_size_type'} })
    acceptance_criteria: Optional[list[str]] = Field(default=[], description="""Acceptance criteria for Monte Carlo moves""", json_schema_extra = { "linkml_meta": {'domain_of': ['MonteCarlo'], 'slot_uri': 'catcore:acceptance_criteria'} })
    equilibration_steps: Optional[list[int]] = Field(default=[], description="""Number of equilibration steps""", json_schema_extra = { "linkml_meta": {'domain_of': ['MonteCarlo'], 'slot_uri': 'catcore:equilibration_steps'} })
    sampling_interval: Optional[list[int]] = Field(default=[], description="""Sampling interval for data collection""", json_schema_extra = { "linkml_meta": {'domain_of': ['MonteCarlo'], 'slot_uri': 'catcore:sampling_interval'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class CalculatedProperty(CatCoreEntity):
    """
    Property calculated from simulation
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class ThermodynamicStability(CalculatedProperty):
    """
    Thermodynamic stability property
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:ThermodynamicStability',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    formation_energy: Optional[list[float]] = Field(default=[], description="""Formation energy per atom""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThermodynamicStability'],
         'slot_uri': 'catcore:formation_energy',
         'unit': {'ucum_code': 'eV'}} })
    reference_energies: Optional[list[str]] = Field(default=[], description="""Reference elemental energies""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThermodynamicStability'],
         'slot_uri': 'catcore:reference_energies'} })
    energy_above_hull: Optional[list[float]] = Field(default=[], description="""Energy above convex hull""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThermodynamicStability'],
         'slot_uri': 'catcore:energy_above_hull',
         'unit': {'ucum_code': 'eV'}} })
    phase_diagram_type: Optional[list[str]] = Field(default=[], description="""Phase diagram type (e.g., binary, ternary)""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThermodynamicStability'],
         'slot_uri': 'catcore:phase_diagram_type'} })
    competing_phases: Optional[list[str]] = Field(default=[], description="""Competing phase list""", json_schema_extra = { "linkml_meta": {'domain_of': ['ThermodynamicStability'],
         'slot_uri': 'catcore:competing_phases'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class Piezoelectricity(CalculatedProperty):
    """
    Piezoelectricity property
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:Piezoelectricity',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    piezoelectric_tensor: Optional[list[str]] = Field(default=[], description="""Piezoelectric tensor components""", json_schema_extra = { "linkml_meta": {'domain_of': ['Piezoelectricity'], 'slot_uri': 'catcore:piezoelectric_tensor'} })
    crystal_symmetry: Optional[list[str]] = Field(default=[], description="""Crystal symmetry""", json_schema_extra = { "linkml_meta": {'domain_of': ['Piezoelectricity'], 'slot_uri': 'catcore:crystal_symmetry'} })
    strain_applied: Optional[list[float]] = Field(default=[], description="""Strain applied""", json_schema_extra = { "linkml_meta": {'domain_of': ['Piezoelectricity'], 'slot_uri': 'catcore:strain_applied'} })
    ionic_electronic_contributions: Optional[list[str]] = Field(default=[], description="""Ionic and electronic contributions""", json_schema_extra = { "linkml_meta": {'domain_of': ['Piezoelectricity'],
         'slot_uri': 'catcore:ionic_electronic_contributions'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class ElasticConstants(CalculatedProperty):
    """
    Elastic constants property
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:ElasticConstants',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    elastic_tensor: Optional[list[str]] = Field(default=[], description="""Elastic tensor components""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElasticConstants'], 'slot_uri': 'catcore:elastic_tensor'} })
    bulk_modulus: Optional[list[float]] = Field(default=[], description="""Bulk modulus""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElasticConstants', 'EquationsOfState'],
         'slot_uri': 'catcore:bulk_modulus',
         'unit': {'ucum_code': 'GPa'}} })
    shear_modulus: Optional[list[float]] = Field(default=[], description="""Shear modulus""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElasticConstants'],
         'slot_uri': 'catcore:shear_modulus',
         'unit': {'ucum_code': 'GPa'}} })
    poisson_ratio: Optional[list[float]] = Field(default=[], description="""Poisson's ratio""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElasticConstants'], 'slot_uri': 'catcore:poisson_ratio'} })
    young_modulus: Optional[list[float]] = Field(default=[], description="""Young's modulus""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElasticConstants'],
         'slot_uri': 'catcore:young_modulus',
         'unit': {'ucum_code': 'GPa'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class Surfaces(CalculatedProperty):
    """
    Surface property
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:Surfaces',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    surface_energy: Optional[list[float]] = Field(default=[], description="""Surface energy""", json_schema_extra = { "linkml_meta": {'domain_of': ['Surfaces'],
         'slot_uri': 'catcore:surface_energy',
         'unit': {'ucum_code': 'J/m2'}} })
    miller_indices: Optional[list[str]] = Field(default=[], description="""Miller indices of surface""", json_schema_extra = { "linkml_meta": {'domain_of': ['Surfaces'], 'slot_uri': 'catcore:miller_indices'} })
    slab_thickness: Optional[list[float]] = Field(default=[], description="""Slab thickness""", json_schema_extra = { "linkml_meta": {'domain_of': ['Surfaces'],
         'slot_uri': 'catcore:slab_thickness',
         'unit': {'ucum_code': 'angstrom'}} })
    vacuum_spacing: Optional[list[float]] = Field(default=[], description="""Vacuum spacing""", json_schema_extra = { "linkml_meta": {'domain_of': ['Surfaces'],
         'slot_uri': 'catcore:vacuum_spacing',
         'unit': {'ucum_code': 'angstrom'}} })
    surface_termination_method: Optional[list[str]] = Field(default=[], description="""Surface termination method""", json_schema_extra = { "linkml_meta": {'domain_of': ['Surfaces'], 'slot_uri': 'catcore:surface_termination_method'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class DielectricTensors(CalculatedProperty):
    """
    Dielectric tensors property
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:DielectricTensors',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    material_composition: Optional[list[str]] = Field(default=[], description="""Material composition""", json_schema_extra = { "linkml_meta": {'domain_of': ['DielectricTensors',
                       'PhononDispersion',
                       'EquationsOfState',
                       'AqueousStability',
                       'GrainBoundaries',
                       'ElectronicStructure',
                       'Ferroelectrics'],
         'slot_uri': 'catcore:material_composition'} })
    crystal_structure: Optional[list[str]] = Field(default=[], description="""Crystal structure (space group, lattice parameters)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DielectricTensors',
                       'PhononDispersion',
                       'EquationsOfState',
                       'AqueousStability',
                       'ElectronicStructure',
                       'Ferroelectrics'],
         'slot_uri': 'SIO:001100'} })
    energy_cutoff: Optional[list[float]] = Field(default=[], description="""Energy cutoff for plane wave basis""", json_schema_extra = { "linkml_meta": {'domain_of': ['DFT',
                       'DielectricTensors',
                       'EquationsOfState',
                       'ElectronicStructure'],
         'slot_uri': 'catcore:energy_cutoff',
         'unit': {'ucum_code': 'eV'}} })
    convergence_criteria: Optional[list[str]] = Field(default=[], description="""Convergence criteria (e.g., energy, force)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DFT', 'DielectricTensors'],
         'slot_uri': 'catcore:convergence_criteria'} })
    k_point_mesh: Optional[list[str]] = Field(default=[], description="""k-point mesh for sampling""", json_schema_extra = { "linkml_meta": {'domain_of': ['DielectricTensors',
                       'EquationsOfState',
                       'ElectronicStructure',
                       'BandGap'],
         'slot_uri': 'catcore:k_point_mesh'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class PhononDispersion(CalculatedProperty):
    """
    Phonon dispersion property
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:PhononDispersion',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    material_composition: Optional[list[str]] = Field(default=[], description="""Material composition""", json_schema_extra = { "linkml_meta": {'domain_of': ['DielectricTensors',
                       'PhononDispersion',
                       'EquationsOfState',
                       'AqueousStability',
                       'GrainBoundaries',
                       'ElectronicStructure',
                       'Ferroelectrics'],
         'slot_uri': 'catcore:material_composition'} })
    crystal_structure: Optional[list[str]] = Field(default=[], description="""Crystal structure (space group, lattice parameters)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DielectricTensors',
                       'PhononDispersion',
                       'EquationsOfState',
                       'AqueousStability',
                       'ElectronicStructure',
                       'Ferroelectrics'],
         'slot_uri': 'SIO:001100'} })
    force_constant_method: Optional[list[str]] = Field(default=[], description="""Force constant calculation method""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhononDispersion'], 'slot_uri': 'catcore:force_constant_method'} })
    kq_point_mesh: Optional[list[str]] = Field(default=[], description="""k/q-point mesh for phonons""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhononDispersion'], 'slot_uri': 'catcore:kq_point_mesh'} })
    smearing_parameter: Optional[list[float]] = Field(default=[], description="""Smearing/broadening parameter""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhononDispersion'],
         'slot_uri': 'catcore:smearing_parameter',
         'unit': {'ucum_code': 'eV'}} })
    imaginary_modes: Optional[list[bool]] = Field(default=[], description="""Imaginary modes present""", json_schema_extra = { "linkml_meta": {'domain_of': ['PhononDispersion'], 'slot_uri': 'catcore:imaginary_modes'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class EquationsOfState(CalculatedProperty):
    """
    Equations of state property
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:EquationsOfState',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    material_composition: Optional[list[str]] = Field(default=[], description="""Material composition""", json_schema_extra = { "linkml_meta": {'domain_of': ['DielectricTensors',
                       'PhononDispersion',
                       'EquationsOfState',
                       'AqueousStability',
                       'GrainBoundaries',
                       'ElectronicStructure',
                       'Ferroelectrics'],
         'slot_uri': 'catcore:material_composition'} })
    crystal_structure: Optional[list[str]] = Field(default=[], description="""Crystal structure (space group, lattice parameters)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DielectricTensors',
                       'PhononDispersion',
                       'EquationsOfState',
                       'AqueousStability',
                       'ElectronicStructure',
                       'Ferroelectrics'],
         'slot_uri': 'SIO:001100'} })
    fit_method: Optional[list[str]] = Field(default=[], description="""Fit method (e.g., Birch-Murnaghan, Vinet)""", json_schema_extra = { "linkml_meta": {'domain_of': ['EquationsOfState'], 'slot_uri': 'catcore:fit_method'} })
    energy_cutoff: Optional[list[float]] = Field(default=[], description="""Energy cutoff for plane wave basis""", json_schema_extra = { "linkml_meta": {'domain_of': ['DFT',
                       'DielectricTensors',
                       'EquationsOfState',
                       'ElectronicStructure'],
         'slot_uri': 'catcore:energy_cutoff',
         'unit': {'ucum_code': 'eV'}} })
    k_point_mesh: Optional[list[str]] = Field(default=[], description="""k-point mesh for sampling""", json_schema_extra = { "linkml_meta": {'domain_of': ['DielectricTensors',
                       'EquationsOfState',
                       'ElectronicStructure',
                       'BandGap'],
         'slot_uri': 'catcore:k_point_mesh'} })
    bulk_modulus: Optional[list[float]] = Field(default=[], description="""Bulk modulus""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElasticConstants', 'EquationsOfState'],
         'slot_uri': 'catcore:bulk_modulus',
         'unit': {'ucum_code': 'GPa'}} })
    pressure_derivative: Optional[list[float]] = Field(default=[], description="""Pressure derivative of bulk modulus""", json_schema_extra = { "linkml_meta": {'domain_of': ['EquationsOfState'], 'slot_uri': 'catcore:pressure_derivative'} })
    fit_residuals: Optional[list[float]] = Field(default=[], description="""Residuals of fit""", json_schema_extra = { "linkml_meta": {'domain_of': ['EquationsOfState'], 'slot_uri': 'catcore:fit_residuals'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class AqueousStability(CalculatedProperty):
    """
    Aqueous stability property
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:AqueousStability',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    material_composition: Optional[list[str]] = Field(default=[], description="""Material composition""", json_schema_extra = { "linkml_meta": {'domain_of': ['DielectricTensors',
                       'PhononDispersion',
                       'EquationsOfState',
                       'AqueousStability',
                       'GrainBoundaries',
                       'ElectronicStructure',
                       'Ferroelectrics'],
         'slot_uri': 'catcore:material_composition'} })
    crystal_structure: Optional[list[str]] = Field(default=[], description="""Crystal structure (space group, lattice parameters)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DielectricTensors',
                       'PhononDispersion',
                       'EquationsOfState',
                       'AqueousStability',
                       'ElectronicStructure',
                       'Ferroelectrics'],
         'slot_uri': 'SIO:001100'} })
    ph_range: Optional[list[str]] = Field(default=[], description="""pH range considered""", json_schema_extra = { "linkml_meta": {'domain_of': ['AqueousStability'], 'slot_uri': 'catcore:ph_range'} })
    potential_range: Optional[list[str]] = Field(default=[], description="""Potential range considered""", json_schema_extra = { "linkml_meta": {'domain_of': ['AqueousStability'], 'slot_uri': 'catcore:potential_range'} })
    solvation_model: Optional[list[str]] = Field(default=[], description="""Solvation model used""", json_schema_extra = { "linkml_meta": {'domain_of': ['AqueousStability'], 'slot_uri': 'catcore:solvation_model'} })
    ionic_strength: Optional[list[float]] = Field(default=[], description="""Ionic strength of solution""", json_schema_extra = { "linkml_meta": {'domain_of': ['AqueousStability'],
         'slot_uri': 'catcore:ionic_strength',
         'unit': {'ucum_code': 'mol/L'}} })
    temperature: Optional[list[float]] = Field(default=[], description="""Temperature""", json_schema_extra = { "linkml_meta": {'domain_of': ['SonochemicalSynthesis',
                       'Sublimation',
                       'PowderXRD',
                       'XRayAbsorptionSpectroscopy',
                       'InfraredSpectroscopy',
                       'RamanSpectroscopy',
                       'NMRSpectroscopy',
                       'DRIFTS',
                       'CyclicVoltammetry',
                       'DynamicLightScattering',
                       'PhotoluminescenceSpectroscopy',
                       'PhotoluminescenceLifetime',
                       'SizeExclusionChromatography',
                       'HPLC_MS',
                       'SingleCrystalXRD',
                       'ConductivityMeasurement',
                       'Microkinetics',
                       'MonteCarlo',
                       'AqueousStability'],
         'slot_uri': 'AFR:0001584',
         'unit': {'ucum_code': 'Cel'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class GrainBoundaries(CalculatedProperty):
    """
    Grain boundaries property
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:GrainBoundaries',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    material_composition: Optional[list[str]] = Field(default=[], description="""Material composition""", json_schema_extra = { "linkml_meta": {'domain_of': ['DielectricTensors',
                       'PhononDispersion',
                       'EquationsOfState',
                       'AqueousStability',
                       'GrainBoundaries',
                       'ElectronicStructure',
                       'Ferroelectrics'],
         'slot_uri': 'catcore:material_composition'} })
    grain_boundary_plane: Optional[list[str]] = Field(default=[], description="""Grain boundary plane""", json_schema_extra = { "linkml_meta": {'domain_of': ['GrainBoundaries'], 'slot_uri': 'catcore:grain_boundary_plane'} })
    misorientation_angle: Optional[list[float]] = Field(default=[], description="""Misorientation angle""", json_schema_extra = { "linkml_meta": {'domain_of': ['GrainBoundaries'],
         'slot_uri': 'catcore:misorientation_angle',
         'unit': {'ucum_code': 'deg'}} })
    grain_boundary_energy: Optional[list[float]] = Field(default=[], description="""Grain boundary energy""", json_schema_extra = { "linkml_meta": {'domain_of': ['GrainBoundaries'],
         'slot_uri': 'catcore:grain_boundary_energy',
         'unit': {'ucum_code': 'J/m2'}} })
    simulation_cell_size: Optional[list[str]] = Field(default=[], description="""Simulation cell size""", json_schema_extra = { "linkml_meta": {'domain_of': ['GrainBoundaries'], 'slot_uri': 'catcore:simulation_cell_size'} })
    gb_excess_volume: Optional[list[float]] = Field(default=[], description="""GB excess volume""", json_schema_extra = { "linkml_meta": {'domain_of': ['GrainBoundaries'], 'slot_uri': 'catcore:gb_excess_volume'} })
    gb_structural_units: Optional[list[str]] = Field(default=[], description="""GB structural units description""", json_schema_extra = { "linkml_meta": {'domain_of': ['GrainBoundaries'], 'slot_uri': 'catcore:gb_structural_units'} })
    charge_defect_segregation: Optional[list[str]] = Field(default=[], description="""Charge or defect segregation data""", json_schema_extra = { "linkml_meta": {'domain_of': ['GrainBoundaries'],
         'slot_uri': 'catcore:charge_defect_segregation'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class ElectronicStructure(CalculatedProperty):
    """
    Electronic structure property
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:ElectronicStructure',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    material_composition: Optional[list[str]] = Field(default=[], description="""Material composition""", json_schema_extra = { "linkml_meta": {'domain_of': ['DielectricTensors',
                       'PhononDispersion',
                       'EquationsOfState',
                       'AqueousStability',
                       'GrainBoundaries',
                       'ElectronicStructure',
                       'Ferroelectrics'],
         'slot_uri': 'catcore:material_composition'} })
    crystal_structure: Optional[list[str]] = Field(default=[], description="""Crystal structure (space group, lattice parameters)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DielectricTensors',
                       'PhononDispersion',
                       'EquationsOfState',
                       'AqueousStability',
                       'ElectronicStructure',
                       'Ferroelectrics'],
         'slot_uri': 'SIO:001100'} })
    k_point_mesh: Optional[list[str]] = Field(default=[], description="""k-point mesh for sampling""", json_schema_extra = { "linkml_meta": {'domain_of': ['DielectricTensors',
                       'EquationsOfState',
                       'ElectronicStructure',
                       'BandGap'],
         'slot_uri': 'catcore:k_point_mesh'} })
    energy_cutoff: Optional[list[float]] = Field(default=[], description="""Energy cutoff for plane wave basis""", json_schema_extra = { "linkml_meta": {'domain_of': ['DFT',
                       'DielectricTensors',
                       'EquationsOfState',
                       'ElectronicStructure'],
         'slot_uri': 'catcore:energy_cutoff',
         'unit': {'ucum_code': 'eV'}} })
    smearing_method: Optional[list[str]] = Field(default=[], description="""Smearing method and width""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElectronicStructure'], 'slot_uri': 'catcore:smearing_method'} })
    spin_polarized: Optional[list[bool]] = Field(default=[], description="""Spin-polarized calculation""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElectronicStructure'], 'slot_uri': 'catcore:spin_polarized'} })
    band_path: Optional[list[str]] = Field(default=[], description="""Band path used""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElectronicStructure'], 'slot_uri': 'catcore:band_path'} })
    fermi_energy: Optional[list[float]] = Field(default=[], description="""Fermi energy""", json_schema_extra = { "linkml_meta": {'domain_of': ['ElectronicStructure'],
         'slot_uri': 'catcore:fermi_energy',
         'unit': {'ucum_code': 'eV'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class Ferroelectrics(CalculatedProperty):
    """
    Ferroelectric property
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:Ferroelectrics',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    material_composition: Optional[list[str]] = Field(default=[], description="""Material composition""", json_schema_extra = { "linkml_meta": {'domain_of': ['DielectricTensors',
                       'PhononDispersion',
                       'EquationsOfState',
                       'AqueousStability',
                       'GrainBoundaries',
                       'ElectronicStructure',
                       'Ferroelectrics'],
         'slot_uri': 'catcore:material_composition'} })
    crystal_structure: Optional[list[str]] = Field(default=[], description="""Crystal structure (space group, lattice parameters)""", json_schema_extra = { "linkml_meta": {'domain_of': ['DielectricTensors',
                       'PhononDispersion',
                       'EquationsOfState',
                       'AqueousStability',
                       'ElectronicStructure',
                       'Ferroelectrics'],
         'slot_uri': 'SIO:001100'} })
    polarization_direction: Optional[list[str]] = Field(default=[], description="""Polarization direction""", json_schema_extra = { "linkml_meta": {'domain_of': ['Ferroelectrics'], 'slot_uri': 'catcore:polarization_direction'} })
    spontaneous_polarization: Optional[list[float]] = Field(default=[], description="""Spontaneous polarization magnitude""", json_schema_extra = { "linkml_meta": {'domain_of': ['Ferroelectrics'],
         'slot_uri': 'catcore:spontaneous_polarization',
         'unit': {'ucum_code': 'uC/cm2'}} })
    reference_structure: Optional[list[str]] = Field(default=[], description="""Reference paraelectric structure""", json_schema_extra = { "linkml_meta": {'domain_of': ['Ferroelectrics'], 'slot_uri': 'catcore:reference_structure'} })
    switching_barrier: Optional[list[float]] = Field(default=[], description="""Switching barrier""", json_schema_extra = { "linkml_meta": {'domain_of': ['Ferroelectrics'],
         'slot_uri': 'catcore:switching_barrier',
         'unit': {'ucum_code': 'eV'}} })
    coercive_field: Optional[list[float]] = Field(default=[], description="""Coercive field""", json_schema_extra = { "linkml_meta": {'domain_of': ['Ferroelectrics'],
         'slot_uri': 'catcore:coercive_field',
         'unit': {'ucum_code': 'kV/cm'}} })
    temperature_dependence: Optional[list[str]] = Field(default=[], description="""Temperature dependence""", json_schema_extra = { "linkml_meta": {'domain_of': ['Ferroelectrics'], 'slot_uri': 'catcore:temperature_dependence'} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


class BandGap(CalculatedProperty):
    """
    Band gap property
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'catcore:BandGap',
         'from_schema': 'https://w3id.org/nfdi4cat/catcore'})

    material_sample: Optional[list[str]] = Field(default=[], description="""Material sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['BandGap'], 'slot_uri': 'voc4cat:0005056'} })
    structure_model: Optional[list[str]] = Field(default=[], description="""Structure or model used""", json_schema_extra = { "linkml_meta": {'domain_of': ['BandGap'], 'slot_uri': 'catcore:structure_model'} })
    k_point_mesh: Optional[list[str]] = Field(default=[], description="""k-point mesh for sampling""", json_schema_extra = { "linkml_meta": {'domain_of': ['DielectricTensors',
                       'EquationsOfState',
                       'ElectronicStructure',
                       'BandGap'],
         'slot_uri': 'catcore:k_point_mesh'} })
    smearing_broadening: Optional[list[float]] = Field(default=[], description="""Smearing or broadening parameter""", json_schema_extra = { "linkml_meta": {'domain_of': ['BandGap'],
         'slot_uri': 'catcore:smearing_broadening',
         'unit': {'ucum_code': 'eV'}} })
    direct_indirect: Optional[list[str]] = Field(default=[], description="""Direct or indirect band gap""", json_schema_extra = { "linkml_meta": {'domain_of': ['BandGap'], 'slot_uri': 'catcore:direct_indirect'} })
    experimental_reference: Optional[list[float]] = Field(default=[], description="""Experimental reference value""", json_schema_extra = { "linkml_meta": {'domain_of': ['BandGap'],
         'slot_uri': 'catcore:experimental_reference',
         'unit': {'ucum_code': 'eV'}} })
    gw_hybrid_correction: Optional[list[bool]] = Field(default=[], description="""GW or hybrid correction used""", json_schema_extra = { "linkml_meta": {'domain_of': ['BandGap'], 'slot_uri': 'catcore:gw_hybrid_correction'} })
    excitonic_correction: Optional[list[float]] = Field(default=[], description="""Excitonic correction applied""", json_schema_extra = { "linkml_meta": {'domain_of': ['BandGap'],
         'slot_uri': 'catcore:excitonic_correction',
         'unit': {'ucum_code': 'eV'}} })
    identifier: Optional[str] = Field(default=None, description="""Unique identifier for the entity""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatCoreEntity'], 'slot_uri': 'catcore:identifier'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
CatCoreEntity.model_rebuild()
CatCore.model_rebuild()
Synthesis.model_rebuild()
Precursor.model_rebuild()
PreparationMethod.model_rebuild()
Impregnation.model_rebuild()
CoPrecipitation.model_rebuild()
SolGel.model_rebuild()
Solvothermal.model_rebuild()
PlasmaAssisted.model_rebuild()
CombustionSynthesis.model_rebuild()
AtomicLayerDeposition.model_rebuild()
DepositionPrecipitation.model_rebuild()
MicrowaveAssisted.model_rebuild()
SonochemicalSynthesis.model_rebuild()
FlameSprayPyrolysis.model_rebuild()
MechanochemicalSynthesis.model_rebuild()
Sublimation.model_rebuild()
MolecularSynthesis.model_rebuild()
ExsolutionSynthesis.model_rebuild()
Characterization.model_rebuild()
CharacterizationTechnique.model_rebuild()
PowderXRD.model_rebuild()
XRayAbsorptionSpectroscopy.model_rebuild()
InfraredSpectroscopy.model_rebuild()
RamanSpectroscopy.model_rebuild()
GCMS.model_rebuild()
NMRSpectroscopy.model_rebuild()
TransmissionElectronMicroscopy.model_rebuild()
ICPAES.model_rebuild()
ScanningElectronMicroscopy.model_rebuild()
Thermogravimetry.model_rebuild()
XPS.model_rebuild()
BET.model_rebuild()
ElementalAnalysis.model_rebuild()
UVVisSpectroscopy.model_rebuild()
DRIFTS.model_rebuild()
CyclicVoltammetry.model_rebuild()
DynamicLightScattering.model_rebuild()
ESIMS.model_rebuild()
PhotoluminescenceSpectroscopy.model_rebuild()
PhotoluminescenceLifetime.model_rebuild()
SizeExclusionChromatography.model_rebuild()
HPLCMS.model_rebuild()
SingleCrystalXRD.model_rebuild()
EDX.model_rebuild()
TPO.model_rebuild()
TPR.model_rebuild()
ConductivityMeasurement.model_rebuild()
Reaction.model_rebuild()
ReactorDesignType.model_rebuild()
ElectrochemicalReactor.model_rebuild()
CSTR.model_rebuild()
PlugFlowReactor.model_rebuild()
Autoclave.model_rebuild()
SlurryReactor.model_rebuild()
Microreactor.model_rebuild()
FixedBedReactor.model_rebuild()
FluidizedBedReactor.model_rebuild()
OperationParameters.model_rebuild()
ProductIdentificationMethod.model_rebuild()
Simulation.model_rebuild()
SimulationMethod.model_rebuild()
DFT.model_rebuild()
MolecularDynamics.model_rebuild()
Microkinetics.model_rebuild()
MonteCarlo.model_rebuild()
CalculatedProperty.model_rebuild()
ThermodynamicStability.model_rebuild()
Piezoelectricity.model_rebuild()
ElasticConstants.model_rebuild()
Surfaces.model_rebuild()
DielectricTensors.model_rebuild()
PhononDispersion.model_rebuild()
EquationsOfState.model_rebuild()
AqueousStability.model_rebuild()
GrainBoundaries.model_rebuild()
ElectronicStructure.model_rebuild()
Ferroelectrics.model_rebuild()
BandGap.model_rebuild()
