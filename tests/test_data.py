import os
import glob
import pytest
import yaml
from pathlib import Path
from typing import Dict, Any, Union, List

from catcore.datamodel import catcore
from linkml_runtime.loaders import yaml_loader

DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"

VALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_VALID, '*.yaml'))
INVALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_INVALID, '*.yaml'))


# Mapping from identifier patterns or context to concrete class names
CHARACTERIZATION_TECHNIQUE_MAP = {
    'xray_source': {
        'Cu Kalpha': 'PowderXRD',
        'Al Kalpha': 'XPS',
    },
    'adsorbate_gas': 'BET',
    'reducing_gas_composition': 'TPR',
    'oxidizing_gas_composition': 'TPO',
}

PREPARATION_METHOD_MAP = {
    'impregnation_type': 'Impregnation',
    'precipitating_agent': 'CoPrecipitation',  # or DepositionPrecipitation
    'hydrolysis_ratio': 'SolGel',
    'filling_volume': 'Solvothermal',
    'plasma_type': 'PlasmaAssisted',
    'fuel': 'CombustionSynthesis',
    'substrate': 'AtomicLayerDeposition',
    'microwave_frequency': 'MicrowaveAssisted',
    'sonication_power': 'SonochemicalSynthesis',
    'flame_type': 'FlameSprayPyrolysis',
    'ball_material': 'MechanochemicalSynthesis',
    'synthesis_pressure': 'Sublimation',
    'reaction_vessel': 'MolecularSynthesis',
}

SIMULATION_METHOD_MAP = {
    'exchange_correlation_functional': 'DFT',
    'force_field': 'MolecularDynamics',
    'rate_constants': 'Microkinetics',
    'interaction_potential': 'MonteCarlo',
}

CALCULATED_PROPERTY_MAP = {
    'formation_energy': 'ThermodynamicStability',
    'piezoelectric_tensor': 'Piezoelectricity',
    'elastic_tensor': 'ElasticConstants',
    'surface_energy': 'Surfaces',
    'band_path': 'ElectronicStructure',
    'polarization_direction': 'Ferroelectrics',
    'direct_indirect': 'BandGap',
}


def infer_class_type(data: Dict[str, Any], type_map: Dict[str, Any]) -> str:
    """Infer the concrete class type based on present fields."""
    for key, class_name in type_map.items():
        if key in data:
            if isinstance(class_name, dict):
                # Need to check value
                for value_pattern, cn in class_name.items():
                    if value_pattern in str(data[key]):
                        return cn
            else:
                return class_name
    return None


def instantiate_polymorphic_objects(data: Union[Dict, List], parent_key: str = None) -> Union[Dict, List]:
    """Recursively instantiate concrete classes for polymorphic fields."""
    if isinstance(data, list):
        return [instantiate_polymorphic_objects(item, parent_key) for item in data]

    if not isinstance(data, dict):
        return data

    # Recursively process nested structures first
    result = {}
    for key, value in data.items():
        result[key] = instantiate_polymorphic_objects(value, key)

    # Now handle polymorphic instantiation for specific keys
    if parent_key == 'characterization_technique':
        class_name = infer_class_type(result, CHARACTERIZATION_TECHNIQUE_MAP)
        if class_name:
            cls = getattr(catcore, class_name)
            return cls(**result)

    elif parent_key == 'preparation_method':
        class_name = infer_class_type(result, PREPARATION_METHOD_MAP)
        if class_name:
            cls = getattr(catcore, class_name)
            return cls(**result)

    elif parent_key == 'simulation_method':
        class_name = infer_class_type(result, SIMULATION_METHOD_MAP)
        if class_name:
            cls = getattr(catcore, class_name)
            return cls(**result)

    elif parent_key == 'calculated_property':
        class_name = infer_class_type(result, CALCULATED_PROPERTY_MAP)
        if class_name:
            cls = getattr(catcore, class_name)
            return cls(**result)

    return result


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """Test loading of all valid data files."""
    target_class_name = Path(filepath).stem.split("-")[0]
    tgt_class = getattr(catcore, target_class_name)

    # Load the YAML content
    with open(filepath, 'r') as f:
        data_dict = yaml.safe_load(f)

    # Handle polymorphic fields by instantiating concrete classes
    for poly_field in ['characterization_technique', 'preparation_method', 'simulation_method', 'calculated_property']:
        if poly_field in data_dict and data_dict[poly_field]:
            data_dict[poly_field] = instantiate_polymorphic_objects(
                data_dict[poly_field],
                poly_field
            )

    # Instantiate the target class
    obj = tgt_class(**data_dict)

    assert obj
