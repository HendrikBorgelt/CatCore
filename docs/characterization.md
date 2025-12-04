# Characterization

The data class 'Characterization' describes the minimum information which should be 
reported with research data to describe the nature of the catalyst.

**Schema Reference:** [Characterization](https://w3id.org/nfdi4cat/catcore/elements/Characterization)

## Slots

<details markdown="1">
<summary><strong>equipment (Required, Multivalued)</strong></summary>

**Description:** Equipment used

**Range:** string

**URI:** [`voc4cat:0000187`](voc4cat:0000187)

**Schema Reference:** [equipment](elements/equipment.md)

</details>

<details markdown="1">
<summary><strong>characterization technique (Required, Multivalued)</strong></summary>

**Description:** Technique used for characterization

**Range:** CharacterizationTechnique

**URI:** [`voc4cat:0000066`](voc4cat:0000066)

**Schema Reference:** [characterization_technique](elements/characterization_technique.md)

**Range Class Details:**

<details markdown="1">
<summary><strong>CharacterizationTechnique</strong></summary>

**Abstract Class**

**Description:** Characterization technique used for catalyst analysis

**Schema Reference:** [CharacterizationTechnique](elements/CharacterizationTechnique.md)

</details>

**Subclasses of CharacterizationTechnique:**

<details markdown="1">
<summary><strong>PowderXRD</strong></summary>

**Description:** Powder X-ray diffraction

**URI:** [`CHMO:0000158`](CHMO:0000158)

**Schema Reference:** [PowderXRD](elements/PowderXRD.md)

**Slots**

<details markdown="1">
<summary><strong>xray source (Optional, Multivalued)</strong></summary>

**Description:** X-ray source used

**Range:** string

**URI:** [`OBI:0001138`](OBI:0001138)

**Schema Reference:** [xray_source](elements/xray_source.md)

</details>

<details markdown="1">
<summary><strong>atmosphere (Optional, Multivalued)</strong></summary>

**Description:** Atmospheric conditions

**Range:** string

**URI:** [`catcore:atmosphere`](catcore:atmosphere)

**Schema Reference:** [atmosphere](elements/atmosphere.md)

</details>

<details markdown="1">
<summary><strong>operation mode (Optional, Multivalued)</strong></summary>

**Description:** Operation mode of the instrument

**Range:** string

**URI:** [`voc4cat:0000108`](voc4cat:0000108)

**Schema Reference:** [operation_mode](elements/operation_mode.md)

</details>

<details markdown="1">
<summary><strong>minimum 2theta (Optional, Multivalued)</strong></summary>

**Description:** Minimum 2-theta angle

**Range:** float

**URI:** [`catcore:minimum_2theta`](catcore:minimum_2theta)

**Schema Reference:** [minimum_2theta](elements/minimum_2theta.md)

**Unit:** deg

</details>

<details markdown="1">
<summary><strong>maximum 2theta (Optional, Multivalued)</strong></summary>

**Description:** Maximum 2-theta angle

**Range:** float

**URI:** [`catcore:maximum_2theta`](catcore:maximum_2theta)

**Schema Reference:** [maximum_2theta](elements/maximum_2theta.md)

**Unit:** deg

</details>

<details markdown="1">
<summary><strong>step size (Optional, Multivalued)</strong></summary>

**Description:** Step size for measurements

**Range:** float

**URI:** [`AFR:0000950`](AFR:0000950)

**Schema Reference:** [step_size](elements/step_size.md)

</details>

<details markdown="1">
<summary><strong>monochromator (Optional, Multivalued)</strong></summary>

**Description:** Monochromator type used

**Range:** string

**URI:** [`CHMO:0002120`](CHMO:0002120)

**Schema Reference:** [monochromator](elements/monochromator.md)

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
<summary><strong>sample spinning speed (Optional, Multivalued)</strong></summary>

**Description:** Sample spinning speed

**Range:** float

**URI:** [`catcore:sample_spinning_speed`](catcore:sample_spinning_speed)

**Schema Reference:** [sample_spinning_speed](elements/sample_spinning_speed.md)

**Unit:** rpm

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

<details markdown="1">
<summary><strong>XRayAbsorptionSpectroscopy</strong></summary>

**Description:** X-ray absorption spectroscopy

**URI:** [`voc4cat:0000286`](voc4cat:0000286)

**Schema Reference:** [XRayAbsorptionSpectroscopy](elements/XRayAbsorptionSpectroscopy.md)

**Slots**

<details markdown="1">
<summary><strong>operation mode (Optional, Multivalued)</strong></summary>

**Description:** Operation mode of the instrument

**Range:** string

**URI:** [`voc4cat:0000108`](voc4cat:0000108)

**Schema Reference:** [operation_mode](elements/operation_mode.md)

</details>

<details markdown="1">
<summary><strong>element analyzed (Optional, Multivalued)</strong></summary>

**Description:** Chemical element being analyzed

**Range:** string

**URI:** [`catcore:element_analyzed`](catcore:element_analyzed)

**Schema Reference:** [element_analyzed](elements/element_analyzed.md)

</details>

<details markdown="1">
<summary><strong>absorption edge (Optional, Multivalued)</strong></summary>

**Description:** Absorption edge measured

**Range:** string

**URI:** [`catcore:absorption_edge`](catcore:absorption_edge)

**Schema Reference:** [absorption_edge](elements/absorption_edge.md)

</details>

<details markdown="1">
<summary><strong>monochromator (Optional, Multivalued)</strong></summary>

**Description:** Monochromator type used

**Range:** string

**URI:** [`CHMO:0002120`](CHMO:0002120)

**Schema Reference:** [monochromator](elements/monochromator.md)

</details>

<details markdown="1">
<summary><strong>minimum energy (Optional, Multivalued)</strong></summary>

**Description:** Minimum energy value

**Range:** float

**URI:** [`catcore:minimum_energy`](catcore:minimum_energy)

**Schema Reference:** [minimum_energy](elements/minimum_energy.md)

**Unit:** eV

</details>

<details markdown="1">
<summary><strong>maximum energy (Optional, Multivalued)</strong></summary>

**Description:** Maximum energy value

**Range:** float

**URI:** [`catcore:maximum_energy`](catcore:maximum_energy)

**Schema Reference:** [maximum_energy](elements/maximum_energy.md)

**Unit:** eV

</details>

<details markdown="1">
<summary><strong>energy resolution (Optional, Multivalued)</strong></summary>

**Description:** Energy resolution of the measurement

**Range:** float

**URI:** [`AFR:0000950`](AFR:0000950)

**Schema Reference:** [energy_resolution](elements/energy_resolution.md)

**Unit:** eV

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
<summary><strong>beamline source (Optional, Multivalued)</strong></summary>

**Description:** Beamline source identification

**Range:** string

**URI:** [`catcore:beamline_source`](catcore:beamline_source)

**Schema Reference:** [beamline_source](elements/beamline_source.md)

</details>

<details markdown="1">
<summary><strong>noise of measurement (Optional, Multivalued)</strong></summary>

**Description:** Noise level of the measurement

**Range:** float

**URI:** [`catcore:noise_of_measurement`](catcore:noise_of_measurement)

**Schema Reference:** [noise_of_measurement](elements/noise_of_measurement.md)

</details>

<details markdown="1">
<summary><strong>number of cycles (Optional, Multivalued)</strong></summary>

**Description:** Number of cycles in the process

**Range:** integer

**URI:** [`catcore:number_of_cycles`](catcore:number_of_cycles)

**Schema Reference:** [number_of_cycles](elements/number_of_cycles.md)

</details>

</details>

<details markdown="1">
<summary><strong>InfraredSpectroscopy</strong></summary>

**Description:** Infrared spectroscopy

**URI:** [`catcore:InfraredSpectroscopy`](catcore:InfraredSpectroscopy)

**Schema Reference:** [InfraredSpectroscopy](elements/InfraredSpectroscopy.md)

**Slots**

<details markdown="1">
<summary><strong>operation mode (Optional, Multivalued)</strong></summary>

**Description:** Operation mode of the instrument

**Range:** string

**URI:** [`voc4cat:0000108`](voc4cat:0000108)

**Schema Reference:** [operation_mode](elements/operation_mode.md)

</details>

<details markdown="1">
<summary><strong>minimum wavenumber (Optional, Multivalued)</strong></summary>

**Description:** Minimum wavenumber

**Range:** float

**URI:** [`catcore:minimum_wavenumber`](catcore:minimum_wavenumber)

**Schema Reference:** [minimum_wavenumber](elements/minimum_wavenumber.md)

**Unit:** cm-1

</details>

<details markdown="1">
<summary><strong>maximum wavenumber (Optional, Multivalued)</strong></summary>

**Description:** Maximum wavenumber

**Range:** float

**URI:** [`catcore:maximum_wavenumber`](catcore:maximum_wavenumber)

**Schema Reference:** [maximum_wavenumber](elements/maximum_wavenumber.md)

**Unit:** cm-1

</details>

<details markdown="1">
<summary><strong>step size (Optional, Multivalued)</strong></summary>

**Description:** Step size for measurements

**Range:** float

**URI:** [`AFR:0000950`](AFR:0000950)

**Schema Reference:** [step_size](elements/step_size.md)

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
<summary><strong>background correction (Optional, Multivalued)</strong></summary>

**Description:** Background correction method

**Range:** string

**URI:** [`AFP:0003721`](AFP:0003721)

**Schema Reference:** [background_correction](elements/background_correction.md)

</details>

<details markdown="1">
<summary><strong>number of scans (Optional, Multivalued)</strong></summary>

**Description:** Number of scans performed

**Range:** integer

**URI:** [`AFR:0003051`](AFR:0003051)

**Schema Reference:** [number_of_scans](elements/number_of_scans.md)

</details>

<details markdown="1">
<summary><strong>atmosphere (Optional, Multivalued)</strong></summary>

**Description:** Atmospheric conditions

**Range:** string

**URI:** [`catcore:atmosphere`](catcore:atmosphere)

**Schema Reference:** [atmosphere](elements/atmosphere.md)

</details>

</details>

<details markdown="1">
<summary><strong>RamanSpectroscopy</strong></summary>

**Description:** Raman spectroscopy

**URI:** [`voc4cat:0000069`](voc4cat:0000069)

**Schema Reference:** [RamanSpectroscopy](elements/RamanSpectroscopy.md)

**Slots**

<details markdown="1">
<summary><strong>excitation laser wavelength (Optional, Multivalued)</strong></summary>

**Description:** Excitation laser wavelength

**Range:** float

**URI:** [`AFR:0001594`](AFR:0001594)

**Schema Reference:** [excitation_laser_wavelength](elements/excitation_laser_wavelength.md)

**Unit:** nm

</details>

<details markdown="1">
<summary><strong>excitation laser power (Optional, Multivalued)</strong></summary>

**Description:** Excitation laser power

**Range:** float

**URI:** [`AFR:0001595`](AFR:0001595)

**Schema Reference:** [excitation_laser_power](elements/excitation_laser_power.md)

**Unit:** mW

</details>

<details markdown="1">
<summary><strong>magnification setting (Optional, Multivalued)</strong></summary>

**Description:** Magnification setting

**Range:** float

**URI:** [`AFR:0002226`](AFR:0002226)

**Schema Reference:** [magnification_setting](elements/magnification_setting.md)

</details>

<details markdown="1">
<summary><strong>integration time (Optional, Multivalued)</strong></summary>

**Description:** Integration time

**Range:** float

**URI:** [`AFR:0001671`](AFR:0001671)

**Schema Reference:** [integration_time](elements/integration_time.md)

**Unit:** s

</details>

<details markdown="1">
<summary><strong>number of scans (Optional, Multivalued)</strong></summary>

**Description:** Number of scans performed

**Range:** integer

**URI:** [`AFR:0003051`](AFR:0003051)

**Schema Reference:** [number_of_scans](elements/number_of_scans.md)

</details>

<details markdown="1">
<summary><strong>atmosphere (Optional, Multivalued)</strong></summary>

**Description:** Atmospheric conditions

**Range:** string

**URI:** [`catcore:atmosphere`](catcore:atmosphere)

**Schema Reference:** [atmosphere](elements/atmosphere.md)

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
<summary><strong>filter or grating (Optional, Multivalued)</strong></summary>

**Description:** Filter or grating used

**Range:** string

**URI:** [`catcore:filter_or_grating`](catcore:filter_or_grating)

**Schema Reference:** [filter_or_grating](elements/filter_or_grating.md)

</details>

</details>

<details markdown="1">
<summary><strong>GCMS</strong></summary>

**Description:** Gas chromatography-mass spectrometry

**URI:** [`CHMO:0000497`](CHMO:0000497)

**Schema Reference:** [GCMS](elements/GCMS.md)

**Slots**

<details markdown="1">
<summary><strong>external standard (Optional, Multivalued)</strong></summary>

**Description:** External standard used for calibration

**Range:** string

**URI:** [`catcore:external_standard`](catcore:external_standard)

**Schema Reference:** [external_standard](elements/external_standard.md)

</details>

<details markdown="1">
<summary><strong>internal standard (Optional, Multivalued)</strong></summary>

**Description:** Internal standard used for calibration

**Range:** string

**URI:** [`catcore:internal_standard`](catcore:internal_standard)

**Schema Reference:** [internal_standard](elements/internal_standard.md)

</details>

<details markdown="1">
<summary><strong>column type (Optional, Multivalued)</strong></summary>

**Description:** Type of chromatography column

**Range:** string

**URI:** [`AFR:0002026`](AFR:0002026)

**Schema Reference:** [column_type](elements/column_type.md)

</details>

<details markdown="1">
<summary><strong>carrier gas (Optional, Multivalued)</strong></summary>

**Description:** Carrier gas used

**Range:** string

**URI:** [`catcore:carrier_gas`](catcore:carrier_gas)

**Schema Reference:** [carrier_gas](elements/carrier_gas.md)

</details>

<details markdown="1">
<summary><strong>carrier gas purity (Optional, Multivalued)</strong></summary>

**Description:** Purity of carrier gas

**Range:** string

**URI:** [`catcore:carrier_gas_purity`](catcore:carrier_gas_purity)

**Schema Reference:** [carrier_gas_purity](elements/carrier_gas_purity.md)

</details>

<details markdown="1">
<summary><strong>inlet temperature (Optional, Multivalued)</strong></summary>

**Description:** Inlet temperature

**Range:** float

**URI:** [`catcore:inlet_temperature`](catcore:inlet_temperature)

**Schema Reference:** [inlet_temperature](elements/inlet_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>minimum oven temperature (Optional, Multivalued)</strong></summary>

**Description:** Minimum oven temperature

**Range:** float

**URI:** [`catcore:minimum_oven_temperature`](catcore:minimum_oven_temperature)

**Schema Reference:** [minimum_oven_temperature](elements/minimum_oven_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>maximum oven temperature (Optional, Multivalued)</strong></summary>

**Description:** Maximum oven temperature

**Range:** float

**URI:** [`catcore:maximum_oven_temperature`](catcore:maximum_oven_temperature)

**Schema Reference:** [maximum_oven_temperature](elements/maximum_oven_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>heating ramp (Optional, Multivalued)</strong></summary>

**Description:** Heating ramp rate

**Range:** float

**URI:** [`catcore:heating_ramp`](catcore:heating_ramp)

**Schema Reference:** [heating_ramp](elements/heating_ramp.md)

**Unit:** Cel/min

</details>

<details markdown="1">
<summary><strong>heating procedure (Optional, Multivalued)</strong></summary>

**Description:** Heating procedure used

**Range:** string

**URI:** [`catcore:heating_procedure`](catcore:heating_procedure)

**Schema Reference:** [heating_procedure](elements/heating_procedure.md)

</details>

<details markdown="1">
<summary><strong>acquisition mode (Optional, Multivalued)</strong></summary>

**Description:** Data acquisition mode

**Range:** string

**URI:** [`catcore:acquisition_mode`](catcore:acquisition_mode)

**Schema Reference:** [acquisition_mode](elements/acquisition_mode.md)

</details>

<details markdown="1">
<summary><strong>solvent delay (Optional, Multivalued)</strong></summary>

**Description:** Solvent delay time

**Range:** float

**URI:** [`catcore:solvent_delay`](catcore:solvent_delay)

**Schema Reference:** [solvent_delay](elements/solvent_delay.md)

**Unit:** min

</details>

<details markdown="1">
<summary><strong>trace ion detection (Optional, Multivalued)</strong></summary>

**Description:** Trace ion detection setting

**Range:** string

**URI:** [`catcore:trace_ion_detection`](catcore:trace_ion_detection)

**Schema Reference:** [trace_ion_detection](elements/trace_ion_detection.md)

</details>

<details markdown="1">
<summary><strong>mz minimum (Optional, Multivalued)</strong></summary>

**Description:** Minimum m/z value

**Range:** float

**URI:** [`AFR:0002652`](AFR:0002652)

**Schema Reference:** [mz_minimum](elements/mz_minimum.md)

</details>

<details markdown="1">
<summary><strong>mz maximum (Optional, Multivalued)</strong></summary>

**Description:** Maximum m/z value

**Range:** float

**URI:** [`AFR:0002653`](AFR:0002653)

**Schema Reference:** [mz_maximum](elements/mz_maximum.md)

</details>

<details markdown="1">
<summary><strong>split ratio (Optional, Multivalued)</strong></summary>

**Description:** Split ratio for injection

**Range:** float

**URI:** [`catcore:split_ratio`](catcore:split_ratio)

**Schema Reference:** [split_ratio](elements/split_ratio.md)

</details>

<details markdown="1">
<summary><strong>injection volume (Optional, Multivalued)</strong></summary>

**Description:** Injection volume

**Range:** float

**URI:** [`AFR:0001577`](AFR:0001577)

**Schema Reference:** [injection_volume](elements/injection_volume.md)

**Unit:** uL

</details>

</details>

<details markdown="1">
<summary><strong>NMRSpectroscopy</strong></summary>

**Description:** Nuclear magnetic resonance spectroscopy

**URI:** [`voc4cat:0000073`](voc4cat:0000073)

**Schema Reference:** [NMRSpectroscopy](elements/NMRSpectroscopy.md)

**Slots**

<details markdown="1">
<summary><strong>nucleus (Optional, Multivalued)</strong></summary>

**Description:** Nucleus being observed

**Range:** string

**URI:** [`catcore:nucleus`](catcore:nucleus)

**Schema Reference:** [nucleus](elements/nucleus.md)

</details>

<details markdown="1">
<summary><strong>solvent (Optional, Multivalued)</strong></summary>

**Description:** Solvent used

**Range:** string

**URI:** [`voc4cat:0007246`](voc4cat:0007246)

**Schema Reference:** [solvent](elements/solvent.md)

</details>

<details markdown="1">
<summary><strong>irradiation frequency (Optional, Multivalued)</strong></summary>

**Description:** Irradiation frequency

**Range:** float

**URI:** [`nmrCV:1400026`](nmrCV:1400026)

**Schema Reference:** [irradiation_frequency](elements/irradiation_frequency.md)

**Unit:** MHz

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
<summary><strong>nmr pulse sequence (Optional, Multivalued)</strong></summary>

**Description:** NMR pulse sequence used

**Range:** string

**URI:** [`nmrCV:1400037`](nmrCV:1400037)

**Schema Reference:** [nmr_pulse_sequence](elements/nmr_pulse_sequence.md)

</details>

<details markdown="1">
<summary><strong>nmr sample tube (Optional, Multivalued)</strong></summary>

**Description:** NMR sample tube type

**Range:** string

**URI:** [`nmrCV:1400132`](nmrCV:1400132)

**Schema Reference:** [nmr_sample_tube](elements/nmr_sample_tube.md)

</details>

<details markdown="1">
<summary><strong>number of scans (Optional, Multivalued)</strong></summary>

**Description:** Number of scans performed

**Range:** integer

**URI:** [`AFR:0003051`](AFR:0003051)

**Schema Reference:** [number_of_scans](elements/number_of_scans.md)

</details>

<details markdown="1">
<summary><strong>atmosphere (Optional, Multivalued)</strong></summary>

**Description:** Atmospheric conditions

**Range:** string

**URI:** [`catcore:atmosphere`](catcore:atmosphere)

**Schema Reference:** [atmosphere](elements/atmosphere.md)

</details>

</details>

<details markdown="1">
<summary><strong>TransmissionElectronMicroscopy</strong></summary>

**Description:** Transmission electron microscopy

**URI:** [`voc4cat:0000078`](voc4cat:0000078)

**Schema Reference:** [TransmissionElectronMicroscopy](elements/TransmissionElectronMicroscopy.md)

**Slots**

<details markdown="1">
<summary><strong>operation mode (Optional, Multivalued)</strong></summary>

**Description:** Operation mode of the instrument

**Range:** string

**URI:** [`voc4cat:0000108`](voc4cat:0000108)

**Schema Reference:** [operation_mode](elements/operation_mode.md)

</details>

<details markdown="1">
<summary><strong>gun type (Optional, Multivalued)</strong></summary>

**Description:** Type of electron gun

**Range:** string

**URI:** [`catcore:gun_type`](catcore:gun_type)

**Schema Reference:** [gun_type](elements/gun_type.md)

</details>

<details markdown="1">
<summary><strong>acceleration voltage (Optional, Multivalued)</strong></summary>

**Description:** Acceleration voltage

**Range:** float

**URI:** [`catcore:acceleration_voltage`](catcore:acceleration_voltage)

**Schema Reference:** [acceleration_voltage](elements/acceleration_voltage.md)

**Unit:** kV

</details>

<details markdown="1">
<summary><strong>magnification setting (Optional, Multivalued)</strong></summary>

**Description:** Magnification setting

**Range:** float

**URI:** [`AFR:0002226`](AFR:0002226)

**Schema Reference:** [magnification_setting](elements/magnification_setting.md)

</details>

</details>

<details markdown="1">
<summary><strong>ICPAES</strong></summary>

**Description:** Inductively-coupled plasma atomic emission spectroscopy

**URI:** [`CHMO:0000267`](CHMO:0000267)

**Schema Reference:** [ICPAES](elements/ICPAES.md)

**Slots**

<details markdown="1">
<summary><strong>element analyzed (Optional, Multivalued)</strong></summary>

**Description:** Chemical element being analyzed

**Range:** string

**URI:** [`catcore:element_analyzed`](catcore:element_analyzed)

**Schema Reference:** [element_analyzed](elements/element_analyzed.md)

</details>

<details markdown="1">
<summary><strong>calibration method (Optional, Multivalued)</strong></summary>

**Description:** Calibration method used

**Range:** string

**URI:** [`catcore:calibration_method`](catcore:calibration_method)

**Schema Reference:** [calibration_method](elements/calibration_method.md)

</details>

<details markdown="1">
<summary><strong>detection limit (Optional, Multivalued)</strong></summary>

**Description:** Detection limit

**Range:** float

**URI:** [`NCIT:C105701`](NCIT:C105701)

**Schema Reference:** [detection_limit](elements/detection_limit.md)

</details>

<details markdown="1">
<summary><strong>matrix effect correction (Optional, Multivalued)</strong></summary>

**Description:** Matrix effect correction method

**Range:** string

**URI:** [`catcore:matrix_effect_correction`](catcore:matrix_effect_correction)

**Schema Reference:** [matrix_effect_correction](elements/matrix_effect_correction.md)

</details>

</details>

<details markdown="1">
<summary><strong>ScanningElectronMicroscopy</strong></summary>

**Description:** Scanning electron microscopy

**URI:** [`voc4cat:0000075`](voc4cat:0000075)

**Schema Reference:** [ScanningElectronMicroscopy](elements/ScanningElectronMicroscopy.md)

**Slots**

<details markdown="1">
<summary><strong>gun type (Optional, Multivalued)</strong></summary>

**Description:** Type of electron gun

**Range:** string

**URI:** [`catcore:gun_type`](catcore:gun_type)

**Schema Reference:** [gun_type](elements/gun_type.md)

</details>

<details markdown="1">
<summary><strong>acceleration voltage (Optional, Multivalued)</strong></summary>

**Description:** Acceleration voltage

**Range:** float

**URI:** [`catcore:acceleration_voltage`](catcore:acceleration_voltage)

**Schema Reference:** [acceleration_voltage](elements/acceleration_voltage.md)

**Unit:** kV

</details>

<details markdown="1">
<summary><strong>image resolution (Optional, Multivalued)</strong></summary>

**Description:** Image resolution

**Range:** float

**URI:** [`catcore:image_resolution`](catcore:image_resolution)

**Schema Reference:** [image_resolution](elements/image_resolution.md)

**Unit:** nm

</details>

<details markdown="1">
<summary><strong>field emitter (Optional, Multivalued)</strong></summary>

**Description:** Field emitter type

**Range:** string

**URI:** [`catcore:field_emitter`](catcore:field_emitter)

**Schema Reference:** [field_emitter](elements/field_emitter.md)

</details>

</details>

<details markdown="1">
<summary><strong>Thermogravimetry</strong></summary>

**Description:** Thermogravimetry

**URI:** [`CHMO:0000690`](CHMO:0000690)

**Schema Reference:** [Thermogravimetry](elements/Thermogravimetry.md)

**Slots**

<details markdown="1">
<summary><strong>operation mode (Optional, Multivalued)</strong></summary>

**Description:** Operation mode of the instrument

**Range:** string

**URI:** [`voc4cat:0000108`](voc4cat:0000108)

**Schema Reference:** [operation_mode](elements/operation_mode.md)

</details>

<details markdown="1">
<summary><strong>atmosphere (Optional, Multivalued)</strong></summary>

**Description:** Atmospheric conditions

**Range:** string

**URI:** [`catcore:atmosphere`](catcore:atmosphere)

**Schema Reference:** [atmosphere](elements/atmosphere.md)

</details>

<details markdown="1">
<summary><strong>initial temperature (Optional, Multivalued)</strong></summary>

**Description:** Initial temperature

**Range:** float

**URI:** [`NCIT:C164644`](NCIT:C164644)

**Schema Reference:** [initial_temperature](elements/initial_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>final temperature (Optional, Multivalued)</strong></summary>

**Description:** Final temperature

**Range:** float

**URI:** [`NCIT:C164644`](NCIT:C164644)

**Schema Reference:** [final_temperature](elements/final_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>heating rate (Optional, Multivalued)</strong></summary>

**Description:** Heating rate

**Range:** float

**URI:** [`catcore:heating_rate`](catcore:heating_rate)

**Schema Reference:** [heating_rate](elements/heating_rate.md)

**Unit:** Cel/min

</details>

<details markdown="1">
<summary><strong>heating procedure (Optional, Multivalued)</strong></summary>

**Description:** Heating procedure used

**Range:** string

**URI:** [`catcore:heating_procedure`](catcore:heating_procedure)

**Schema Reference:** [heating_procedure](elements/heating_procedure.md)

</details>

<details markdown="1">
<summary><strong>sample mass (Optional, Multivalued)</strong></summary>

**Description:** Mass of sample

**Range:** float

**URI:** [`voc4cat:0007038`](voc4cat:0007038)

**Schema Reference:** [sample_mass](elements/sample_mass.md)

**Unit:** mg

</details>

</details>

<details markdown="1">
<summary><strong>XPS</strong></summary>

**Description:** X-ray photoelectron spectroscopy

**URI:** [`CHMO:0000404`](CHMO:0000404)

**Schema Reference:** [XPS](elements/XPS.md)

**Slots**

<details markdown="1">
<summary><strong>xray source (Optional, Multivalued)</strong></summary>

**Description:** X-ray source used

**Range:** string

**URI:** [`OBI:0001138`](OBI:0001138)

**Schema Reference:** [xray_source](elements/xray_source.md)

</details>

<details markdown="1">
<summary><strong>total acquisition time (Optional, Multivalued)</strong></summary>

**Description:** Total acquisition time

**Range:** float

**URI:** [`catcore:total_acquisition_time`](catcore:total_acquisition_time)

**Schema Reference:** [total_acquisition_time](elements/total_acquisition_time.md)

**Unit:** s

</details>

<details markdown="1">
<summary><strong>number of scans (Optional, Multivalued)</strong></summary>

**Description:** Number of scans performed

**Range:** integer

**URI:** [`AFR:0003051`](AFR:0003051)

**Schema Reference:** [number_of_scans](elements/number_of_scans.md)

</details>

<details markdown="1">
<summary><strong>spot size (Optional, Multivalued)</strong></summary>

**Description:** Spot size for analysis

**Range:** float

**URI:** [`catcore:spot_size`](catcore:spot_size)

**Schema Reference:** [spot_size](elements/spot_size.md)

**Unit:** mm

</details>

<details markdown="1">
<summary><strong>lense mode (Optional, Multivalued)</strong></summary>

**Description:** Lens mode setting

**Range:** string

**URI:** [`voc4cat:0000108`](voc4cat:0000108)

**Schema Reference:** [lense_mode](elements/lense_mode.md)

</details>

<details markdown="1">
<summary><strong>minimum energy (Optional, Multivalued)</strong></summary>

**Description:** Minimum energy value

**Range:** float

**URI:** [`catcore:minimum_energy`](catcore:minimum_energy)

**Schema Reference:** [minimum_energy](elements/minimum_energy.md)

**Unit:** eV

</details>

<details markdown="1">
<summary><strong>maximum energy (Optional, Multivalued)</strong></summary>

**Description:** Maximum energy value

**Range:** float

**URI:** [`catcore:maximum_energy`](catcore:maximum_energy)

**Schema Reference:** [maximum_energy](elements/maximum_energy.md)

**Unit:** eV

</details>

<details markdown="1">
<summary><strong>step size (Optional, Multivalued)</strong></summary>

**Description:** Step size for measurements

**Range:** float

**URI:** [`AFR:0000950`](AFR:0000950)

**Schema Reference:** [step_size](elements/step_size.md)

</details>

<details markdown="1">
<summary><strong>pass energy (Optional, Multivalued)</strong></summary>

**Description:** Pass energy setting

**Range:** float

**URI:** [`catcore:pass_energy`](catcore:pass_energy)

**Schema Reference:** [pass_energy](elements/pass_energy.md)

**Unit:** eV

</details>

<details markdown="1">
<summary><strong>charge compensation (Optional, Multivalued)</strong></summary>

**Description:** Charge compensation method

**Range:** string

**URI:** [`catcore:charge_compensation`](catcore:charge_compensation)

**Schema Reference:** [charge_compensation](elements/charge_compensation.md)

</details>

<details markdown="1">
<summary><strong>atmosphere (Optional, Multivalued)</strong></summary>

**Description:** Atmospheric conditions

**Range:** string

**URI:** [`catcore:atmosphere`](catcore:atmosphere)

**Schema Reference:** [atmosphere](elements/atmosphere.md)

</details>

</details>

<details markdown="1">
<summary><strong>BET</strong></summary>

**Description:** Brunauer-Emmett-Teller surface area analysis

**URI:** [`catcore:BET`](catcore:BET)

**Schema Reference:** [BET](elements/BET.md)

**Slots**

<details markdown="1">
<summary><strong>adsorbate gas (Optional, Multivalued)</strong></summary>

**Description:** Adsorbate gas used

**Range:** string

**URI:** [`catcore:adsorbate_gas`](catcore:adsorbate_gas)

**Schema Reference:** [adsorbate_gas](elements/adsorbate_gas.md)

</details>

<details markdown="1">
<summary><strong>degassing temperature (Optional, Multivalued)</strong></summary>

**Description:** Degassing temperature

**Range:** float

**URI:** [`catcore:degassing_temperature`](catcore:degassing_temperature)

**Schema Reference:** [degassing_temperature](elements/degassing_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>measurement temperature (Optional, Multivalued)</strong></summary>

**Description:** Measurement temperature

**Range:** float

**URI:** [`catcore:measurement_temperature`](catcore:measurement_temperature)

**Schema Reference:** [measurement_temperature](elements/measurement_temperature.md)

**Unit:** K

</details>

<details markdown="1">
<summary><strong>pore size distribution method (Optional, Multivalued)</strong></summary>

**Description:** Method for pore size distribution analysis

**Range:** string

**URI:** [`catcore:pore_size_distribution_method`](catcore:pore_size_distribution_method)

**Schema Reference:** [pore_size_distribution_method](elements/pore_size_distribution_method.md)

</details>

<details markdown="1">
<summary><strong>sample mass (Optional, Multivalued)</strong></summary>

**Description:** Mass of sample

**Range:** float

**URI:** [`voc4cat:0007038`](voc4cat:0007038)

**Schema Reference:** [sample_mass](elements/sample_mass.md)

**Unit:** mg

</details>

</details>

<details markdown="1">
<summary><strong>ElementalAnalysis</strong></summary>

**Description:** Elemental analysis

**URI:** [`CHMO:0001075`](CHMO:0001075)

**Schema Reference:** [ElementalAnalysis](elements/ElementalAnalysis.md)

**Slots**

<details markdown="1">
<summary><strong>elements analyzed (Optional, Multivalued)</strong></summary>

**Description:** Elements analyzed

**Range:** string

**URI:** [`catcore:elements_analyzed`](catcore:elements_analyzed)

**Schema Reference:** [elements_analyzed](elements/elements_analyzed.md)

</details>

<details markdown="1">
<summary><strong>combustion temperature (Optional, Multivalued)</strong></summary>

**Description:** Combustion temperature

**Range:** float

**URI:** [`catcore:combustion_temperature`](catcore:combustion_temperature)

**Schema Reference:** [combustion_temperature](elements/combustion_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>carrier gas (Optional, Multivalued)</strong></summary>

**Description:** Carrier gas used

**Range:** string

**URI:** [`catcore:carrier_gas`](catcore:carrier_gas)

**Schema Reference:** [carrier_gas](elements/carrier_gas.md)

</details>

</details>

<details markdown="1">
<summary><strong>UVVisSpectroscopy</strong></summary>

**Description:** Ultraviolet-visible spectroscopy

**URI:** [`voc4cat:0000079`](voc4cat:0000079)

**Schema Reference:** [UVVisSpectroscopy](elements/UVVisSpectroscopy.md)

**Slots**

<details markdown="1">
<summary><strong>minimum wavelength (Optional, Multivalued)</strong></summary>

**Description:** Minimum wavelength

**Range:** float

**URI:** [`catcore:minimum_wavelength`](catcore:minimum_wavelength)

**Schema Reference:** [minimum_wavelength](elements/minimum_wavelength.md)

**Unit:** nm

</details>

<details markdown="1">
<summary><strong>maximum wavelength (Optional, Multivalued)</strong></summary>

**Description:** Maximum wavelength

**Range:** float

**URI:** [`catcore:maximum_wavelength`](catcore:maximum_wavelength)

**Schema Reference:** [maximum_wavelength](elements/maximum_wavelength.md)

**Unit:** nm

</details>

<details markdown="1">
<summary><strong>path length (Optional, Multivalued)</strong></summary>

**Description:** Path length of cell

**Range:** float

**URI:** [`AFQ:0000268`](AFQ:0000268)

**Schema Reference:** [path_length](elements/path_length.md)

**Unit:** cm

</details>

<details markdown="1">
<summary><strong>solvent (Optional, Multivalued)</strong></summary>

**Description:** Solvent used

**Range:** string

**URI:** [`voc4cat:0007246`](voc4cat:0007246)

**Schema Reference:** [solvent](elements/solvent.md)

</details>

<details markdown="1">
<summary><strong>concentration (Optional, Multivalued)</strong></summary>

**Description:** Concentration of sample

**Range:** float

**URI:** [`voc4cat:0007244`](voc4cat:0007244)

**Schema Reference:** [concentration](elements/concentration.md)

**Unit:** mol/L

</details>

</details>

<details markdown="1">
<summary><strong>DRIFTS</strong></summary>

**Description:** Diffuse reflectance infrared Fourier transform spectroscopy

**URI:** [`CHMO:0000645`](CHMO:0000645)

**Schema Reference:** [DRIFTS](elements/DRIFTS.md)

**Slots**

<details markdown="1">
<summary><strong>adsorption gas (Optional, Multivalued)</strong></summary>

**Description:** Adsorption gas used

**Range:** string

**URI:** [`catcore:adsorption_gas`](catcore:adsorption_gas)

**Schema Reference:** [adsorption_gas](elements/adsorption_gas.md)

</details>

<details markdown="1">
<summary><strong>atmosphere (Optional, Multivalued)</strong></summary>

**Description:** Atmospheric conditions

**Range:** string

**URI:** [`catcore:atmosphere`](catcore:atmosphere)

**Schema Reference:** [atmosphere](elements/atmosphere.md)

</details>

<details markdown="1">
<summary><strong>flow rate (Optional, Multivalued)</strong></summary>

**Description:** Flow rate

**Range:** float

**URI:** [`catcore:flow_rate`](catcore:flow_rate)

**Schema Reference:** [flow_rate](elements/flow_rate.md)

**Unit:** mL/min

</details>

<details markdown="1">
<summary><strong>diluting reference (Optional, Multivalued)</strong></summary>

**Description:** Diluting reference material

**Range:** string

**URI:** [`catcore:diluting_reference`](catcore:diluting_reference)

**Schema Reference:** [diluting_reference](elements/diluting_reference.md)

</details>

<details markdown="1">
<summary><strong>ratio reference sample (Optional, Multivalued)</strong></summary>

**Description:** Ratio of reference to sample

**Range:** float

**URI:** [`catcore:ratio_reference_sample`](catcore:ratio_reference_sample)

**Schema Reference:** [ratio_reference_sample](elements/ratio_reference_sample.md)

</details>

<details markdown="1">
<summary><strong>step size (Optional, Multivalued)</strong></summary>

**Description:** Step size for measurements

**Range:** float

**URI:** [`AFR:0000950`](AFR:0000950)

**Schema Reference:** [step_size](elements/step_size.md)

</details>

<details markdown="1">
<summary><strong>resolution (Optional, Multivalued)</strong></summary>

**Description:** Spectral resolution

**Range:** float

**URI:** [`catcore:resolution`](catcore:resolution)

**Schema Reference:** [resolution](elements/resolution.md)

**Unit:** cm-1

</details>

<details markdown="1">
<summary><strong>background correction method (Optional, Multivalued)</strong></summary>

**Description:** Background correction method used

**Range:** string

**URI:** [`catcore:background_correction_method`](catcore:background_correction_method)

**Schema Reference:** [background_correction_method](elements/background_correction_method.md)

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
<summary><strong>number of scans (Optional, Multivalued)</strong></summary>

**Description:** Number of scans performed

**Range:** integer

**URI:** [`AFR:0003051`](AFR:0003051)

**Schema Reference:** [number_of_scans](elements/number_of_scans.md)

</details>

</details>

<details markdown="1">
<summary><strong>CyclicVoltammetry</strong></summary>

**Description:** Cyclic voltammetry

**URI:** [`CHMO:0000025`](CHMO:0000025)

**Schema Reference:** [CyclicVoltammetry](elements/CyclicVoltammetry.md)

**Slots**

<details markdown="1">
<summary><strong>scan rate (Optional, Multivalued)</strong></summary>

**Description:** Scan rate for voltammetry

**Range:** float

**URI:** [`voc4cat:0007213`](voc4cat:0007213)

**Schema Reference:** [scan_rate](elements/scan_rate.md)

**Unit:** mV/s

</details>

<details markdown="1">
<summary><strong>minimum potential (Optional, Multivalued)</strong></summary>

**Description:** Minimum potential

**Range:** float

**URI:** [`catcore:minimum_potential`](catcore:minimum_potential)

**Schema Reference:** [minimum_potential](elements/minimum_potential.md)

**Unit:** V

</details>

<details markdown="1">
<summary><strong>maximum potential (Optional, Multivalued)</strong></summary>

**Description:** Maximum potential

**Range:** float

**URI:** [`catcore:maximum_potential`](catcore:maximum_potential)

**Schema Reference:** [maximum_potential](elements/maximum_potential.md)

**Unit:** V

</details>

<details markdown="1">
<summary><strong>step size potential (Optional, Multivalued)</strong></summary>

**Description:** Step size for potential

**Range:** float

**URI:** [`voc4cat:0007218`](voc4cat:0007218)

**Schema Reference:** [step_size_potential](elements/step_size_potential.md)

**Unit:** mV

</details>

<details markdown="1">
<summary><strong>electrolyte composition (Optional, Multivalued)</strong></summary>

**Description:** Composition of electrolyte

**Range:** string

**URI:** [`catcore:electrolyte_composition`](catcore:electrolyte_composition)

**Schema Reference:** [electrolyte_composition](elements/electrolyte_composition.md)

</details>

<details markdown="1">
<summary><strong>electrolyte concentration (Optional, Multivalued)</strong></summary>

**Description:** Concentration of electrolyte

**Range:** float

**URI:** [`catcore:electrolyte_concentration`](catcore:electrolyte_concentration)

**Schema Reference:** [electrolyte_concentration](elements/electrolyte_concentration.md)

**Unit:** mol/L

</details>

<details markdown="1">
<summary><strong>reference electrode (Optional, Multivalued)</strong></summary>

**Description:** Reference electrode used

**Range:** string

**URI:** [`voc4cat:0007204`](voc4cat:0007204)

**Schema Reference:** [reference_electrode](elements/reference_electrode.md)

</details>

<details markdown="1">
<summary><strong>number of cycles (Optional, Multivalued)</strong></summary>

**Description:** Number of cycles in the process

**Range:** integer

**URI:** [`catcore:number_of_cycles`](catcore:number_of_cycles)

**Schema Reference:** [number_of_cycles](elements/number_of_cycles.md)

</details>

<details markdown="1">
<summary><strong>working electrode (Optional, Multivalued)</strong></summary>

**Description:** Working electrode used

**Range:** string

**URI:** [`voc4cat:0007202`](voc4cat:0007202)

**Schema Reference:** [working_electrode](elements/working_electrode.md)

</details>

<details markdown="1">
<summary><strong>counter electrode (Optional, Multivalued)</strong></summary>

**Description:** Counter electrode used

**Range:** string

**URI:** [`voc4cat:0007203`](voc4cat:0007203)

**Schema Reference:** [counter_electrode](elements/counter_electrode.md)

</details>

<details markdown="1">
<summary><strong>atmosphere (Optional, Multivalued)</strong></summary>

**Description:** Atmospheric conditions

**Range:** string

**URI:** [`catcore:atmosphere`](catcore:atmosphere)

**Schema Reference:** [atmosphere](elements/atmosphere.md)

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
<summary><strong>DynamicLightScattering</strong></summary>

**Description:** Dynamic light scattering

**URI:** [`CHMO:0000167`](CHMO:0000167)

**Schema Reference:** [DynamicLightScattering](elements/DynamicLightScattering.md)

**Slots**

<details markdown="1">
<summary><strong>solvent (Optional, Multivalued)</strong></summary>

**Description:** Solvent used

**Range:** string

**URI:** [`voc4cat:0007246`](voc4cat:0007246)

**Schema Reference:** [solvent](elements/solvent.md)

</details>

<details markdown="1">
<summary><strong>concentration (Optional, Multivalued)</strong></summary>

**Description:** Concentration of sample

**Range:** float

**URI:** [`voc4cat:0007244`](voc4cat:0007244)

**Schema Reference:** [concentration](elements/concentration.md)

**Unit:** mol/L

</details>

<details markdown="1">
<summary><strong>light wavelength (Optional, Multivalued)</strong></summary>

**Description:** Light wavelength used

**Range:** float

**URI:** [`voc4cat:0000176`](voc4cat:0000176)

**Schema Reference:** [light_wavelength](elements/light_wavelength.md)

**Unit:** nm

</details>

<details markdown="1">
<summary><strong>scattering angle (Optional, Multivalued)</strong></summary>

**Description:** Scattering angle

**Range:** float

**URI:** [`catcore:scattering_angle`](catcore:scattering_angle)

**Schema Reference:** [scattering_angle](elements/scattering_angle.md)

**Unit:** deg

</details>

<details markdown="1">
<summary><strong>refractive index (Optional, Multivalued)</strong></summary>

**Description:** Refractive index

**Range:** float

**URI:** [`catcore:refractive_index`](catcore:refractive_index)

**Schema Reference:** [refractive_index](elements/refractive_index.md)

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
<summary><strong>dispersant (Optional, Multivalued)</strong></summary>

**Description:** Dispersant used

**Range:** string

**URI:** [`catcore:dispersant`](catcore:dispersant)

**Schema Reference:** [dispersant](elements/dispersant.md)

</details>

<details markdown="1">
<summary><strong>measurement duration (Optional, Multivalued)</strong></summary>

**Description:** Duration of measurement

**Range:** float

**URI:** [`catcore:measurement_duration`](catcore:measurement_duration)

**Schema Reference:** [measurement_duration](elements/measurement_duration.md)

**Unit:** s

</details>

</details>

<details markdown="1">
<summary><strong>ESI MS</strong></summary>

**Description:** Electrospray ionisation mass spectrometry

**URI:** [`CHMO:0000482`](CHMO:0000482)

**Schema Reference:** [ESI_MS](elements/ESI_MS.md)

**Slots**

<details markdown="1">
<summary><strong>operation mode (Optional, Multivalued)</strong></summary>

**Description:** Operation mode of the instrument

**Range:** string

**URI:** [`voc4cat:0000108`](voc4cat:0000108)

**Schema Reference:** [operation_mode](elements/operation_mode.md)

</details>

<details markdown="1">
<summary><strong>mz minimum (Optional, Multivalued)</strong></summary>

**Description:** Minimum m/z value

**Range:** float

**URI:** [`AFR:0002652`](AFR:0002652)

**Schema Reference:** [mz_minimum](elements/mz_minimum.md)

</details>

<details markdown="1">
<summary><strong>mz maximum (Optional, Multivalued)</strong></summary>

**Description:** Maximum m/z value

**Range:** float

**URI:** [`AFR:0002653`](AFR:0002653)

**Schema Reference:** [mz_maximum](elements/mz_maximum.md)

</details>

<details markdown="1">
<summary><strong>spray voltage (Optional, Multivalued)</strong></summary>

**Description:** Spray voltage for ionization

**Range:** float

**URI:** [`CHMO:0002792`](CHMO:0002792)

**Schema Reference:** [spray_voltage](elements/spray_voltage.md)

**Unit:** kV

</details>

<details markdown="1">
<summary><strong>capillary temperature (Optional, Multivalued)</strong></summary>

**Description:** Capillary temperature

**Range:** float

**URI:** [`catcore:capillary_temperature`](catcore:capillary_temperature)

**Schema Reference:** [capillary_temperature](elements/capillary_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>solvent composition (Optional, Multivalued)</strong></summary>

**Description:** Solvent composition

**Range:** string

**URI:** [`voc4cat:0007246`](voc4cat:0007246)

**Schema Reference:** [solvent_composition](elements/solvent_composition.md)

</details>

<details markdown="1">
<summary><strong>flow rate (Optional, Multivalued)</strong></summary>

**Description:** Flow rate

**Range:** float

**URI:** [`catcore:flow_rate`](catcore:flow_rate)

**Schema Reference:** [flow_rate](elements/flow_rate.md)

**Unit:** mL/min

</details>

<details markdown="1">
<summary><strong>carrier gas (Optional, Multivalued)</strong></summary>

**Description:** Carrier gas used

**Range:** string

**URI:** [`catcore:carrier_gas`](catcore:carrier_gas)

**Schema Reference:** [carrier_gas](elements/carrier_gas.md)

</details>

<details markdown="1">
<summary><strong>concentration (Optional, Multivalued)</strong></summary>

**Description:** Concentration of sample

**Range:** float

**URI:** [`voc4cat:0007244`](voc4cat:0007244)

**Schema Reference:** [concentration](elements/concentration.md)

**Unit:** mol/L

</details>

</details>

<details markdown="1">
<summary><strong>PhotoluminescenceSpectroscopy</strong></summary>

**Description:** Photoluminescence spectroscopy

**URI:** [`catcore:PhotoluminescenceSpectroscopy`](catcore:PhotoluminescenceSpectroscopy)

**Schema Reference:** [PhotoluminescenceSpectroscopy](elements/PhotoluminescenceSpectroscopy.md)

**Slots**

<details markdown="1">
<summary><strong>excitation wavelength (Optional, Multivalued)</strong></summary>

**Description:** Excitation wavelength

**Range:** float

**URI:** [`AFR:0002479`](AFR:0002479)

**Schema Reference:** [excitation_wavelength](elements/excitation_wavelength.md)

**Unit:** nm

</details>

<details markdown="1">
<summary><strong>emission wavelength (Optional, Multivalued)</strong></summary>

**Description:** Emission wavelength

**Range:** float

**URI:** [`NCIT:C204101`](NCIT:C204101)

**Schema Reference:** [emission_wavelength](elements/emission_wavelength.md)

**Unit:** nm

</details>

<details markdown="1">
<summary><strong>optical filter (Optional, Multivalued)</strong></summary>

**Description:** Optical filter used

**Range:** string

**URI:** [`catcore:optical_filter`](catcore:optical_filter)

**Schema Reference:** [optical_filter](elements/optical_filter.md)

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
<summary><strong>emission range (Optional, Multivalued)</strong></summary>

**Description:** Emission range measured

**Range:** string

**URI:** [`catcore:emission_range`](catcore:emission_range)

**Schema Reference:** [emission_range](elements/emission_range.md)

</details>

<details markdown="1">
<summary><strong>slit width (Optional, Multivalued)</strong></summary>

**Description:** Slit width setting

**Range:** float

**URI:** [`catcore:slit_width`](catcore:slit_width)

**Schema Reference:** [slit_width](elements/slit_width.md)

**Unit:** nm

</details>

<details markdown="1">
<summary><strong>step size (Optional, Multivalued)</strong></summary>

**Description:** Step size for measurements

**Range:** float

**URI:** [`AFR:0000950`](AFR:0000950)

**Schema Reference:** [step_size](elements/step_size.md)

</details>

<details markdown="1">
<summary><strong>integration time (Optional, Multivalued)</strong></summary>

**Description:** Integration time

**Range:** float

**URI:** [`AFR:0001671`](AFR:0001671)

**Schema Reference:** [integration_time](elements/integration_time.md)

**Unit:** s

</details>

</details>

<details markdown="1">
<summary><strong>PhotoluminescenceLifetime</strong></summary>

**Description:** Photoluminescence lifetime measurement

**URI:** [`catcore:PhotoluminescenceLifetime`](catcore:PhotoluminescenceLifetime)

**Schema Reference:** [PhotoluminescenceLifetime](elements/PhotoluminescenceLifetime.md)

**Slots**

<details markdown="1">
<summary><strong>excitation wavelength (Optional, Multivalued)</strong></summary>

**Description:** Excitation wavelength

**Range:** float

**URI:** [`AFR:0002479`](AFR:0002479)

**Schema Reference:** [excitation_wavelength](elements/excitation_wavelength.md)

**Unit:** nm

</details>

<details markdown="1">
<summary><strong>emission wavelength (Optional, Multivalued)</strong></summary>

**Description:** Emission wavelength

**Range:** float

**URI:** [`NCIT:C204101`](NCIT:C204101)

**Schema Reference:** [emission_wavelength](elements/emission_wavelength.md)

**Unit:** nm

</details>

<details markdown="1">
<summary><strong>optical filter (Optional, Multivalued)</strong></summary>

**Description:** Optical filter used

**Range:** string

**URI:** [`catcore:optical_filter`](catcore:optical_filter)

**Schema Reference:** [optical_filter](elements/optical_filter.md)

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
<summary><strong>lifetime fitting model (Optional, Multivalued)</strong></summary>

**Description:** Lifetime fitting model used

**Range:** string

**URI:** [`catcore:lifetime_fitting_model`](catcore:lifetime_fitting_model)

**Schema Reference:** [lifetime_fitting_model](elements/lifetime_fitting_model.md)

</details>

<details markdown="1">
<summary><strong>number of shots (Optional, Multivalued)</strong></summary>

**Description:** Number of shots for measurement

**Range:** integer

**URI:** [`catcore:number_of_shots`](catcore:number_of_shots)

**Schema Reference:** [number_of_shots](elements/number_of_shots.md)

</details>

</details>

<details markdown="1">
<summary><strong>SizeExclusionChromatography</strong></summary>

**Description:** Size-exclusion chromatography

**URI:** [`AFP:0000843`](AFP:0000843)

**Schema Reference:** [SizeExclusionChromatography](elements/SizeExclusionChromatography.md)

**Slots**

<details markdown="1">
<summary><strong>column type (Optional, Multivalued)</strong></summary>

**Description:** Type of chromatography column

**Range:** string

**URI:** [`AFR:0002026`](AFR:0002026)

**Schema Reference:** [column_type](elements/column_type.md)

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
<summary><strong>eluent (Optional, Multivalued)</strong></summary>

**Description:** Eluent used

**Range:** string

**URI:** [`AFRL:0000011`](AFRL:0000011)

**Schema Reference:** [eluent](elements/eluent.md)

</details>

<details markdown="1">
<summary><strong>flow rate (Optional, Multivalued)</strong></summary>

**Description:** Flow rate

**Range:** float

**URI:** [`catcore:flow_rate`](catcore:flow_rate)

**Schema Reference:** [flow_rate](elements/flow_rate.md)

**Unit:** mL/min

</details>

<details markdown="1">
<summary><strong>calibration standard (Optional, Multivalued)</strong></summary>

**Description:** Calibration standard used

**Range:** string

**URI:** [`catcore:calibration_standard`](catcore:calibration_standard)

**Schema Reference:** [calibration_standard](elements/calibration_standard.md)

</details>

<details markdown="1">
<summary><strong>injection volume (Optional, Multivalued)</strong></summary>

**Description:** Injection volume

**Range:** float

**URI:** [`AFR:0001577`](AFR:0001577)

**Schema Reference:** [injection_volume](elements/injection_volume.md)

**Unit:** uL

</details>

</details>

<details markdown="1">
<summary><strong>HPLC MS</strong></summary>

**Description:** High-performance liquid chromatography mass spectrometry

**URI:** [`CHMO:0000796`](CHMO:0000796)

**Schema Reference:** [HPLC_MS](elements/HPLC_MS.md)

**Slots**

<details markdown="1">
<summary><strong>column type (Optional, Multivalued)</strong></summary>

**Description:** Type of chromatography column

**Range:** string

**URI:** [`AFR:0002026`](AFR:0002026)

**Schema Reference:** [column_type](elements/column_type.md)

</details>

<details markdown="1">
<summary><strong>eluent (Optional, Multivalued)</strong></summary>

**Description:** Eluent used

**Range:** string

**URI:** [`AFRL:0000011`](AFRL:0000011)

**Schema Reference:** [eluent](elements/eluent.md)

</details>

<details markdown="1">
<summary><strong>gradient program (Optional, Multivalued)</strong></summary>

**Description:** Gradient program for elution

**Range:** string

**URI:** [`catcore:gradient_program`](catcore:gradient_program)

**Schema Reference:** [gradient_program](elements/gradient_program.md)

</details>

<details markdown="1">
<summary><strong>ionization mode (Optional, Multivalued)</strong></summary>

**Description:** Ionization mode used

**Range:** string

**URI:** [`catcore:ionization_mode`](catcore:ionization_mode)

**Schema Reference:** [ionization_mode](elements/ionization_mode.md)

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
<summary><strong>flow rate (Optional, Multivalued)</strong></summary>

**Description:** Flow rate

**Range:** float

**URI:** [`catcore:flow_rate`](catcore:flow_rate)

**Schema Reference:** [flow_rate](elements/flow_rate.md)

**Unit:** mL/min

</details>

<details markdown="1">
<summary><strong>injection volume (Optional, Multivalued)</strong></summary>

**Description:** Injection volume

**Range:** float

**URI:** [`AFR:0001577`](AFR:0001577)

**Schema Reference:** [injection_volume](elements/injection_volume.md)

**Unit:** uL

</details>

<details markdown="1">
<summary><strong>external standard (Optional, Multivalued)</strong></summary>

**Description:** External standard used for calibration

**Range:** string

**URI:** [`catcore:external_standard`](catcore:external_standard)

**Schema Reference:** [external_standard](elements/external_standard.md)

</details>

<details markdown="1">
<summary><strong>internal standard (Optional, Multivalued)</strong></summary>

**Description:** Internal standard used for calibration

**Range:** string

**URI:** [`catcore:internal_standard`](catcore:internal_standard)

**Schema Reference:** [internal_standard](elements/internal_standard.md)

</details>

</details>

<details markdown="1">
<summary><strong>SingleCrystalXRD</strong></summary>

**Description:** Single crystal X-ray diffraction

**URI:** [`CHMO:0000852`](CHMO:0000852)

**Schema Reference:** [SingleCrystalXRD](elements/SingleCrystalXRD.md)

**Slots**

<details markdown="1">
<summary><strong>xray source (Optional, Multivalued)</strong></summary>

**Description:** X-ray source used

**Range:** string

**URI:** [`OBI:0001138`](OBI:0001138)

**Schema Reference:** [xray_source](elements/xray_source.md)

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
<summary><strong>EDX</strong></summary>

**Description:** Energy-dispersive X-ray emission spectroscopy

**URI:** [`CHMO:0000309`](CHMO:0000309)

**Schema Reference:** [EDX](elements/EDX.md)

**Slots**

<details markdown="1">
<summary><strong>primary energy (Optional, Multivalued)</strong></summary>

**Description:** Primary energy of electron beam

**Range:** float

**URI:** [`catcore:primary_energy`](catcore:primary_energy)

**Schema Reference:** [primary_energy](elements/primary_energy.md)

**Unit:** keV

</details>

<details markdown="1">
<summary><strong>counting time (Optional, Multivalued)</strong></summary>

**Description:** Counting time for detection

**Range:** float

**URI:** [`catcore:counting_time`](catcore:counting_time)

**Schema Reference:** [counting_time](elements/counting_time.md)

**Unit:** s

</details>

<details markdown="1">
<summary><strong>resolution (Optional, Multivalued)</strong></summary>

**Description:** Spectral resolution

**Range:** float

**URI:** [`catcore:resolution`](catcore:resolution)

**Schema Reference:** [resolution](elements/resolution.md)

**Unit:** cm-1

</details>

<details markdown="1">
<summary><strong>calibration method (Optional, Multivalued)</strong></summary>

**Description:** Calibration method used

**Range:** string

**URI:** [`catcore:calibration_method`](catcore:calibration_method)

**Schema Reference:** [calibration_method](elements/calibration_method.md)

</details>

</details>

<details markdown="1">
<summary><strong>TPO</strong></summary>

**Description:** Temperature-programmed oxidation

**URI:** [`CHMO:0002907`](CHMO:0002907)

**Schema Reference:** [TPO](elements/TPO.md)

**Slots**

<details markdown="1">
<summary><strong>oxidizing gas composition (Optional, Multivalued)</strong></summary>

**Description:** Composition of oxidizing gas

**Range:** string

**URI:** [`catcore:oxidizing_gas_composition`](catcore:oxidizing_gas_composition)

**Schema Reference:** [oxidizing_gas_composition](elements/oxidizing_gas_composition.md)

</details>

<details markdown="1">
<summary><strong>heating rate (Optional, Multivalued)</strong></summary>

**Description:** Heating rate

**Range:** float

**URI:** [`catcore:heating_rate`](catcore:heating_rate)

**Schema Reference:** [heating_rate](elements/heating_rate.md)

**Unit:** Cel/min

</details>

<details markdown="1">
<summary><strong>minimum temperature (Optional, Multivalued)</strong></summary>

**Description:** Minimum temperature

**Range:** float

**URI:** [`catcore:minimum_temperature`](catcore:minimum_temperature)

**Schema Reference:** [minimum_temperature](elements/minimum_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>maximum temperature (Optional, Multivalued)</strong></summary>

**Description:** Maximum temperature

**Range:** float

**URI:** [`catcore:maximum_temperature`](catcore:maximum_temperature)

**Schema Reference:** [maximum_temperature](elements/maximum_temperature.md)

**Unit:** Cel

</details>

</details>

<details markdown="1">
<summary><strong>TPR</strong></summary>

**Description:** Temperature-programmed reduction

**URI:** [`CHMO:0002908`](CHMO:0002908)

**Schema Reference:** [TPR](elements/TPR.md)

**Slots**

<details markdown="1">
<summary><strong>reducing gas composition (Optional, Multivalued)</strong></summary>

**Description:** Composition of reducing gas

**Range:** string

**URI:** [`catcore:reducing_gas_composition`](catcore:reducing_gas_composition)

**Schema Reference:** [reducing_gas_composition](elements/reducing_gas_composition.md)

</details>

<details markdown="1">
<summary><strong>heating rate (Optional, Multivalued)</strong></summary>

**Description:** Heating rate

**Range:** float

**URI:** [`catcore:heating_rate`](catcore:heating_rate)

**Schema Reference:** [heating_rate](elements/heating_rate.md)

**Unit:** Cel/min

</details>

<details markdown="1">
<summary><strong>minimum temperature (Optional, Multivalued)</strong></summary>

**Description:** Minimum temperature

**Range:** float

**URI:** [`catcore:minimum_temperature`](catcore:minimum_temperature)

**Schema Reference:** [minimum_temperature](elements/minimum_temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>maximum temperature (Optional, Multivalued)</strong></summary>

**Description:** Maximum temperature

**Range:** float

**URI:** [`catcore:maximum_temperature`](catcore:maximum_temperature)

**Schema Reference:** [maximum_temperature](elements/maximum_temperature.md)

**Unit:** Cel

</details>

</details>

<details markdown="1">
<summary><strong>ConductivityMeasurement</strong></summary>

**Description:** Conductivity measurement

**URI:** [`catcore:ConductivityMeasurement`](catcore:ConductivityMeasurement)

**Schema Reference:** [ConductivityMeasurement](elements/ConductivityMeasurement.md)

**Slots**

<details markdown="1">
<summary><strong>temperature (Optional, Multivalued)</strong></summary>

**Description:** Temperature

**Range:** float

**URI:** [`AFR:0001584`](AFR:0001584)

**Schema Reference:** [temperature](elements/temperature.md)

**Unit:** Cel

</details>

<details markdown="1">
<summary><strong>electrode configuration (Optional, Multivalued)</strong></summary>

**Description:** Configuration of electrodes

**Range:** string

**URI:** [`catcore:electrode_configuration`](catcore:electrode_configuration)

**Schema Reference:** [electrode_configuration](elements/electrode_configuration.md)

</details>

<details markdown="1">
<summary><strong>frequency (Optional, Multivalued)</strong></summary>

**Description:** Frequency of measurement

**Range:** float

**URI:** [`voc4cat:0007239`](voc4cat:0007239)

**Schema Reference:** [frequency](elements/frequency.md)

**Unit:** Hz

</details>

<details markdown="1">
<summary><strong>ac dc mode (Optional, Multivalued)</strong></summary>

**Description:** AC or DC measurement mode

**Range:** string

**URI:** [`catcore:ac_dc_mode`](catcore:ac_dc_mode)

**Schema Reference:** [ac_dc_mode](elements/ac_dc_mode.md)

</details>

<details markdown="1">
<summary><strong>sample geometry (Optional, Multivalued)</strong></summary>

**Description:** Geometry of the sample

**Range:** string

**URI:** [`catcore:sample_geometry`](catcore:sample_geometry)

**Schema Reference:** [sample_geometry](elements/sample_geometry.md)

</details>

</details>

</details>

<details markdown="1">
<summary><strong>sample state (Optional, Multivalued)</strong></summary>

**Description:** State of the sample

**Range:** SampleStateEnum

**URI:** [`catcore:sample_state`](catcore:sample_state)

**Schema Reference:** [sample_state](elements/sample_state.md)

</details>

<details markdown="1">
<summary><strong>sample description (Optional, Multivalued)</strong></summary>

**Description:** Description of the sample

**Range:** string

**URI:** [`catcore:sample_description`](catcore:sample_description)

**Schema Reference:** [sample_description](elements/sample_description.md)

</details>

<details markdown="1">
<summary><strong>detector type (Optional, Multivalued)</strong></summary>

**Description:** Type of detector used

**Range:** string

**URI:** [`AFR:0000317`](AFR:0000317)

**Schema Reference:** [detector_type](elements/detector_type.md)

</details>

<details markdown="1">
<summary><strong>sample preparation (Optional, Multivalued)</strong></summary>

**Description:** Preparation of sample

**Range:** string

**URI:** [`AFP:0001159`](AFP:0001159)

**Schema Reference:** [sample_preparation](elements/sample_preparation.md)

</details>

<details markdown="1">
<summary><strong>sample pretreatment (Optional, Multivalued)</strong></summary>

**Description:** Pre-treatment of sample

**Range:** string

**URI:** [`voc4cat:0000122`](voc4cat:0000122)

**Schema Reference:** [sample_pretreatment](elements/sample_pretreatment.md)

</details>

