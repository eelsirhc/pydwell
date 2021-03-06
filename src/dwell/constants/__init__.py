"""NIST constants module.

This module contains the `NIST <http: //physics.nist.gov/constants>`_
constants obtained by parsing the NIST dataset in the top level directory
of this package.
The data is stored in a dictionary with keys corresponding to the NIST name
for the constant, and the value is an tuple with entries corresponding to
the value [0], uncertainty [1], and units[2].
"""
import math

data = {
    "{220} lattice spacing of silicon":
        (192.0155714e-12, 0.0000032e-12,  "m"),
    "alpha particle-electron mass ratio":
        (7294.2995361, 0.0000029,  ""),
    "alpha particle mass":
        (6.64465675e-27, 0.00000029e-27,  "kg"),
    "alpha particle mass energy equivalent":
        (5.97191967e-10, 0.00000026e-10,  "J"),
    "alpha particle mass energy equivalent in MeV":
        (3727.379240, 0.000082,  "MeV"),
    "alpha particle mass in u":
        (4.001506179125, 0.000000000062,  "u"),
    "alpha particle molar mass":
        (4.001506179125e-3, 0.000000000062e-3,  "kg mol^-1"),
    "alpha particle-proton mass ratio":
        (3.97259968933, 0.00000000036,  ""),
    "Angstrom star":
        (1.00001495e-10, 0.00000090e-10,  "m"),
    "atomic mass constant":
        (1.660538921e-27, 0.000000073e-27,  "kg"),
    "atomic mass constant energy equivalent":
        (1.492417954e-10, 0.000000066e-10,  "J"),
    "atomic mass constant energy equivalent in MeV":
        (931.494061, 0.000021,  "MeV"),
    "atomic mass unit-electron volt relationship":
        (931.494061e6, 0.000021e6,  "eV"),
    "atomic mass unit-hartree relationship":
        (3.4231776845e7, 0.0000000024e7,  "E_h"),
    "atomic mass unit-hertz relationship":
        (2.2523427168e23, 0.0000000016e23,  "Hz"),
    "atomic mass unit-inverse meter relationship":
        (7.5130066042e14, 0.0000000053e14,  "m^-1"),
    "atomic mass unit-joule relationship":
        (1.492417954e-10, 0.000000066e-10,  "J"),
    "atomic mass unit-kelvin relationship":
        (1.08095408e13, 0.00000098e13,  "K"),
    "atomic mass unit-kilogram relationship":
        (1.660538921e-27, 0.000000073e-27,  "kg"),
    "atomic unit of 1st hyperpolarizability":
        (3.206361449e-53, 0.000000071e-53,  "C^3 m^3 J^-2"),
    "atomic unit of 2nd hyperpolarizability":
        (6.23538054e-65, 0.00000028e-65,  "C^4 m^4 J^-3"),
    "atomic unit of action":
        (1.054571726e-34, 0.000000047e-34,  "J s"),
    "atomic unit of charge":
        (1.602176565e-19, 0.000000035e-19,  "C"),
    "atomic unit of charge density":
        (1.081202338e12, 0.000000024e12,  "C m^-3"),
    "atomic unit of current":
        (6.62361795e-3, 0.00000015e-3,  "A"),
    "atomic unit of electric dipole mom.":
        (8.47835326e-30, 0.00000019e-30,  "C m"),
    "atomic unit of electric field":
        (5.14220652e11, 0.00000011e11,  "V m^-1"),
    "atomic unit of electric field gradient":
        (9.71736200e21, 0.00000021e21,  "V m^-2"),
    "atomic unit of electric polarizability":
        (1.6487772754e-41, 0.0000000016e-41,  "C^2 m^2 J^-1"),
    "atomic unit of electric potential":
        (27.21138505, 0.00000060,  "V"),
    "atomic unit of electric quadrupole mom.":
        (4.486551331e-40, 0.000000099e-40,  "C m^2"),
    "atomic unit of energy":
        (4.35974434e-18, 0.00000019e-18,  "J"),
    "atomic unit of force":
        (8.23872278e-8, 0.00000036e-8,  "N"),
    "atomic unit of length":
        (0.52917721092e-10, 0.00000000017e-10,  "m"),
    "atomic unit of mag. dipole mom.":
        (1.854801936e-23, 0.000000041e-23,  "J T^-1"),
    "atomic unit of mag. flux density":
        (2.350517464e5, 0.000000052e5,  "T"),
    "atomic unit of magnetizability":
        (7.891036607e-29, 0.000000013e-29,  "J T^-2"),
    "atomic unit of mass":
        (9.10938291e-31, 0.00000040e-31,  "kg"),
    "atomic unit of mom.um":
        (1.992851740e-24, 0.000000088e-24,  "kg m s^-1"),
    "atomic unit of permittivity":
        (1.112650056e-10, 0.0,  "F m^-1"),
    "atomic unit of time":
        (2.418884326502e-17, 0.000000000012e-1,  "7 s"),
    "atomic unit of velocity":
        (2.18769126379e6, 0.00000000071e6,  "m s^-1"),
    "Avogadro constant":
        (6.02214129e23, 0.00000027e23,  "mol^-1"),
    "Bohr magneton":
        (927.400968e-26, 0.000020e-26,  "J T^-1"),
    "Bohr magneton in eV/T":
        (5.7883818066e-5, 0.0000000038e-5,  "eV T^-1"),
    "Bohr magneton in Hz/T":
        (13.99624555e9, 0.00000031e9,  "Hz T^-1"),
    "Bohr magneton in inverse meters per tesla":
        (46.6864498, 0.0000010,  "m^-1 T^-1"),
    "Bohr magneton in K/T":
        (0.67171388, 0.00000061,  "K T^-1"),
    "Bohr radius":
        (0.52917721092e-10, 0.00000000017e-10,  "m"),
    "Boltzmann constant":
        (1.3806488e-23, 0.0000013e-23,  "J K^-1"),
    "Boltzmann constant in eV/K":
        (8.6173324e-5, 0.0000078e-5,  "eV K^-1"),
    "Boltzmann constant in Hz/K":
        (2.0836618e10, 0.0000019e10,  "Hz K^-1"),
    "Boltzmann constant in inverse meters per kelvin":
        (69.503476, 0.000063,  "m^-1 K^-1"),
    "characteristic impedance of vacuum":
        (376.730313461, 0.0,  "ohm"),
    "classical electron radius":
        (2.8179403267e-15, 0.0000000027e-15,  "m"),
    "Compton wavelength":
        (2.4263102389e-12, 0.0000000016e-12,  "m"),
    "Compton wavelength over 2 pi":
        (386.15926800e-15, 0.00000025e-15,  "m"),
    "conductance quantum":
        (7.7480917346e-5, 0.0000000025e-5,  "S"),
    "conventional value of Josephson constant":
        (483597.9e9, 0.0,  "Hz V^-1"),
    "conventional value of von Klitzing constant":
        (25812.807, 0.0,  "ohm"),
    "Cu x unit":
        (1.00207697e-13, 0.00000028e-13,  "m"),
    "deuteron-electron mag. mom. ratio":
        (-4.664345537e-4, 0.000000039e-4,  ""),
    "deuteron-electron mass ratio":
        (3670.4829652, 0.0000015,  ""),
    "deuteron g factor":
        (0.8574382308, 0.0000000072,  ""),
    "deuteron mag. mom.":
        (0.433073489e-26, 0.000000010e-26,  "J T^-1"),
    "deuteron mag. mom. to Bohr magneton ratio":
        (0.4669754556e-3, 0.0000000039e-3,  ""),
    "deuteron mag. mom. to nuclear magneton ratio":
        (0.8574382308, 0.0000000072,  ""),
    "deuteron mass":
        (3.34358348e-27, 0.00000015e-27,  "kg"),
    "deuteron mass energy equivalent":
        (3.00506297e-10, 0.00000013e-10,  "J"),
    "deuteron mass energy equivalent in MeV":
        (1875.612859, 0.000041,  "MeV"),
    "deuteron mass in u":
        (2.013553212712, 0.000000000077,  "u"),
    "deuteron molar mass":
        (2.013553212712e-3, 0.000000000077e-3,  "kg mol^-1"),
    "deuteron-neutron mag. mom. ratio":
        (-0.44820652, 0.00000011,  ""),
    "deuteron-proton mag. mom. ratio":
        (0.3070122070, 0.0000000024,  ""),
    "deuteron-proton mass ratio":
        (1.99900750097, 0.00000000018,  ""),
    "deuteron rms charge radius":
        (2.1424e-15, 0.0021e-15,  "m"),
    "electric constant":
        (8.854187817e-12, 0.0,  "F m^-1"),
    "electron charge to mass quotient":
        (-1.758820088e11, 0.000000039e11,  "C kg^-1"),
    "electron-deuteron mag. mom. ratio":
        (-2143.923498, 0.000018,  ""),
    "electron-deuteron mass ratio":
        (2.7244371095e-4, 0.0000000011e-4,  ""),
    "electron g factor":
        (-2.00231930436153, 0.00000000000053,  ""),
    "electron gyromag. ratio":
        (1.760859708e11, 0.000000039e11,  "s^-1 T^-1"),
    "electron gyromag. ratio over 2 pi":
        (28024.95266, 0.00062,  "MHz T^-1"),
    "electron-helion mass ratio":
        (1.8195430761e-4, 0.0000000017e-4,  ""),
    "electron mag. mom.":
        (-928.476430e-26, 0.000021e-26,  "J T^-1"),
    "electron mag. mom. anomaly":
        (1.15965218076e-3, 0.00000000027e-3,  ""),
    "electron mag. mom. to Bohr magneton ratio":
        (-1.00115965218076, 0.00000000000027,  ""),
    "electron mag. mom. to nuclear magneton ratio":
        (-1838.28197090, 0.00000075,  ""),
    "electron mass":
        (9.10938291e-31, 0.00000040e-31,  "kg"),
    "electron mass energy equivalent":
        (8.18710506e-14, 0.00000036e-14,  "J"),
    "electron mass energy equivalent in MeV":
        (0.510998928, 0.000000011,  "MeV"),
    "electron mass in u":
        (5.4857990946e-4, 0.0000000022e-4,  "u"),
    "electron molar mass":
        (5.4857990946e-7, 0.0000000022e-7,  "kg mol^-1"),
    "electron-muon mag. mom. ratio":
        (206.7669896, 0.0000052,  ""),
    "electron-muon mass ratio":
        (4.83633166e-3, 0.00000012e-3,  ""),
    "electron-neutron mag. mom. ratio":
        (960.92050, 0.00023,  ""),
    "electron-neutron mass ratio":
        (5.4386734461e-4, 0.0000000032e-4,  ""),
    "electron-proton mag. mom. ratio":
        (-658.2106848, 0.0000054,  ""),
    "electron-proton mass ratio":
        (5.4461702178e-4, 0.0000000022e-4,  ""),
    "electron-tau mass ratio":
        (2.87592e-4, 0.00026e-4,  ""),
    "electron to alpha particle mass ratio":
        (1.37093355578e-4, 0.00000000055e-4,  ""),
    "electron to shielded helion mag. mom. ratio":
        (864.058257, 0.000010,  ""),
    "electron to shielded proton mag. mom. ratio":
        (-658.2275971, 0.0000072,  ""),
    "electron-triton mass ratio":
        (1.8192000653e-4, 0.0000000017e-4,  ""),
    "electron volt":
        (1.602176565e-19, 0.000000035e-19,  "J"),
    "electron volt-atomic mass unit relationship":
        (1.073544150e-9, 0.000000024e-9,  "u"),
    "electron volt-hartree relationship":
        (3.674932379e-2, 0.000000081e-2,  "E_h"),
    "electron volt-hertz relationship":
        (2.417989348e14, 0.000000053e14,  "Hz"),
    "electron volt-inverse meter relationship":
        (8.06554429e5, 0.00000018e5,  "m^-1"),
    "electron volt-joule relationship":
        (1.602176565e-19, 0.000000035e-19,  "J"),
    "electron volt-kelvin relationship":
        (1.1604519e4, 0.0000011e4,  "K"),
    "electron volt-kilogram relationship":
        (1.782661845e-36, 0.000000039e-36,  "kg"),
    "elementary charge":
        (1.602176565e-19, 0.000000035e-19,  "C"),
    "elementary charge over h":
        (2.417989348e14, 0.000000053e14,  "A J^-1"),
    "Faraday constant":
        (96485.3365, 0.0021,  "C mol^-1"),
    "Faraday constant for conventional electric current":
        (96485.3321, 0.0043,  "C_90 mol^-1"),
    "Fermi coupling constant":
        (1.166364e-5, 0.000005e-5,  "GeV^-2"),
    "fine-structure constant":
        (7.2973525698e-3, 0.0000000024e-3,  ""),
    "first radiation constant":
        (3.74177153e-16, 0.00000017e-16,  "W m^2"),
    "first radiation constant for spectral radiance":
        (1.191042869e-16, 0.000000053e-16,  "W m^2 sr^-1"),
    "hartree-atomic mass unit relationship":
        (2.9212623246e-8, 0.0000000021e-8,  "u"),
    "hartree-electron volt relationship":
        (27.21138505, 0.00000060,  "eV"),
    "Hartree energy":
        (4.35974434e-18, 0.00000019e-18,  "J"),
    "Hartree energy in eV":
        (27.21138505, 0.00000060,  "eV"),
    "hartree-hertz relationship":
        (6.579683920729e15, 0.000000000033e15,  "Hz"),
    "hartree-inverse meter relationship":
        (2.194746313708e7, 0.000000000011e7,  "m^-1"),
    "hartree-joule relationship":
        (4.35974434e-18, 0.00000019e-18,  "J"),
    "hartree-kelvin relationship":
        (3.1577504e5, 0.0000029e5,  "K"),
    "hartree-kilogram relationship":
        (4.85086979e-35, 0.00000021e-35,  "kg"),
    "helion-electron mass ratio":
        (5495.8852754, 0.0000050,  ""),
    "helion g factor":
        (-4.255250613, 0.000000050,  ""),
    "helion mag. mom.":
        (-1.074617486e-26, 0.000000027e-26,  "J T^-1"),
    "helion mag. mom. to Bohr magneton ratio":
        (-1.158740958e-3, 0.000000014e-3,  ""),
    "helion mag. mom. to nuclear magneton ratio":
        (-2.127625306, 0.000000025,  ""),
    "helion mass":
        (5.00641234e-27, 0.00000022e-27,  "kg"),
    "helion mass energy equivalent":
        (4.49953902e-10, 0.00000020e-10,  "J"),
    "helion mass energy equivalent in MeV":
        (2808.391482, 0.000062,  "MeV"),
    "helion mass in u":
        (3.0149322468, 0.0000000025,  "u"),
    "helion molar mass":
        (3.0149322468e-3, 0.0000000025e-3,  "kg mol^-1"),
    "helion-proton mass ratio":
        (2.9931526707, 0.0000000025,  ""),
    "hertz-atomic mass unit relationship":
        (4.4398216689e-24, 0.0000000031e-24,  "u"),
    "hertz-electron volt relationship":
        (4.135667516e-15, 0.000000091e-15,  "eV"),
    "hertz-hartree relationship":
        (1.5198298460045e-16, 0.0000000000076e-16,  "E_h"),
    "hertz-inverse meter relationship":
        (3.335640951e-9, 0.0,  "m^-1"),
    "hertz-joule relationship":
        (6.62606957e-34, 0.00000029e-34,  "J"),
    "hertz-kelvin relationship":
        (4.7992434e-11, 0.0000044e-11,  "K"),
    "hertz-kilogram relationship":
        (7.37249668e-51, 0.00000033e-51,  "kg"),
    "inverse fine-structure constant":
        (137.035999074, 0.000000044,  ""),
    "inverse meter-atomic mass unit relationship":
        (1.33102505120e-15, 0.00000000094e-15,  "u"),
    "inverse meter-electron volt relationship":
        (1.239841930e-6, 0.000000027e-6,  "eV"),
    "inverse meter-hartree relationship":
        (4.556335252755e-8, 0.000000000023e-8,  "E_h"),
    "inverse meter-hertz relationship":
        (299792458, 0.0,  "Hz"),
    "inverse meter-joule relationship":
        (1.986445684e-25, 0.000000088e-25,  "J"),
    "inverse meter-kelvin relationship":
        (1.4387770e-2, 0.0000013e-2,  "K"),
    "inverse meter-kilogram relationship":
        (2.210218902e-42, 0.000000098e-42,  "kg"),
    "inverse of conductance quantum":
        (12906.4037217, 0.0000042,  "ohm"),
    "Josephson constant":
        (483597.870e9, 0.011e9,  "Hz V^-1"),
    "joule-atomic mass unit relationship":
        (6.70053585e9, 0.00000030e9,  "u"),
    "joule-electron volt relationship":
        (6.24150934e18, 0.00000014e18,  "eV"),
    "joule-hartree relationship":
        (2.29371248e17, 0.00000010e17,  "E_h"),
    "joule-hertz relationship":
        (1.509190311e33, 0.000000067e33,  "Hz"),
    "joule-inverse meter relationship":
        (5.03411701e24, 0.00000022e24,  "m^-1"),
    "joule-kelvin relationship":
        (7.2429716e22, 0.0000066e22,  "K"),
    "joule-kilogram relationship":
        (1.112650056e-17, 0.0,  "kg"),
    "kelvin-atomic mass unit relationship":
        (9.2510868e-14, 0.0000084e-14,  "u"),
    "kelvin-electron volt relationship":
        (8.6173324e-5, 0.0000078e-5,  "eV"),
    "kelvin-hartree relationship":
        (3.1668114e-6, 0.0000029e-6,  "E_h"),
    "kelvin-hertz relationship":
        (2.0836618e10, 0.0000019e10,  "Hz"),
    "kelvin-inverse meter relationship":
        (69.503476, 0.000063,  "m^-1"),
    "kelvin-joule relationship":
        (1.3806488e-23, 0.0000013e-23,  "J"),
    "kelvin-kilogram relationship":
        (1.5361790e-40, 0.0000014e-40,  "kg"),
    "kilogram-atomic mass unit relationship":
        (6.02214129e26, 0.00000027e26,  "u"),
    "kilogram-electron volt relationship":
        (5.60958885e35, 0.00000012e35,  "eV"),
    "kilogram-hartree relationship":
        (2.061485968e34, 0.000000091e34,  "E_h"),
    "kilogram-hertz relationship":
        (1.356392608e50, 0.000000060e50,  "Hz"),
    "kilogram-inverse meter relationship":
        (4.52443873e41, 0.00000020e41,  "m^-1"),
    "kilogram-joule relationship":
        (8.987551787e16, 0.0,  "J"),
    "kilogram-kelvin relationship":
        (6.5096582e39, 0.0000059e39,  "K"),
    "lattice parameter of silicon":
        (543.1020504e-12, 0.0000089e-12,  "m"),
    "Loschmidt constant (273.15 K, 100 kPa)":
        (2.6516462e25, 0.0000024e25,  "m^-3"),
    "Loschmidt constant (273.15 K, 101.325 kPa)":
        (2.6867805e25, 0.0000024e25,  "m^-3"),
    "mag. constant":
        (12.566370614e-7, 0.0,  "N A^-2"),
    "mag. flux quantum":
        (2.067833758e-15, 0.000000046e-15,  "Wb"),
    "molar gas constant":
        (8.3144621, 0.0000075,  "J mol^-1 K^-1"),
    "molar mass constant":
        (1e-3, 0.0,  "kg mol^-1"),
    "molar mass of carbon-12":
        (12e-3, 0.0,  "kg mol^-1"),
    "molar Planck constant":
        (3.9903127176e-10, 0.0000000028e-10,  "J s mol^-1"),
    "molar Planck constant times c":
        (0.119626565779, 0.000000000084,  "J m mol^-1"),
    "molar volume of ideal gas (273.15 K, 100 kPa)":
        (22.710953e-3, 0.000021e-3,  "m^3 mol^-1"),
    "molar volume of ideal gas (273.15 K, 101.325 kPa)":
        (22.413968e-3, 0.000020e-3,  "m^3 mol^-1"),
    "molar volume of silicon":
        (12.05883301e-6, 0.00000080e-6,  "m^3 mol^-1"),
    "Mo x unit":
        (1.00209952e-13, 0.00000053e-13,  "m"),
    "muon Compton wavelength":
        (11.73444103e-15, 0.00000030e-15,  "m"),
    "muon Compton wavelength over 2 pi":
        (1.867594294e-15, 0.000000047e-15,  "m"),
    "muon-electron mass ratio":
        (206.7682843, 0.0000052,  ""),
    "muon g factor":
        (-2.0023318418, 0.0000000013,  ""),
    "muon mag. mom.":
        (-4.49044807e-26, 0.00000015e-26,  "J T^-1"),
    "muon mag. mom. anomaly":
        (1.16592091e-3, 0.00000063e-3,  ""),
    "muon mag. mom. to Bohr magneton ratio":
        (-4.84197044e-3, 0.00000012e-3,  ""),
    "muon mag. mom. to nuclear magneton ratio":
        (-8.89059697, 0.00000022,  ""),
    "muon mass":
        (1.883531475e-28, 0.000000096e-28,  "kg"),
    "muon mass energy equivalent":
        (1.692833667e-11, 0.000000086e-11,  "J"),
    "muon mass energy equivalent in MeV":
        (105.6583715, 0.0000035,  "MeV"),
    "muon mass in u":
        (0.1134289267, 0.0000000029,  "u"),
    "muon molar mass":
        (0.1134289267e-3, 0.0000000029e-3,  "kg mol^-1"),
    "muon-neutron mass ratio":
        (0.1124545177, 0.0000000028,  ""),
    "muon-proton mag. mom. ratio":
        (-3.183345107, 0.000000084,  ""),
    "muon-proton mass ratio":
        (0.1126095272, 0.0000000028,  ""),
    "muon-tau mass ratio":
        (5.94649e-2, 0.00054e-2,  ""),
    "natural unit of action":
        (1.054571726e-34, 0.000000047e-34,  "J s"),
    "natural unit of action in eV s":
        (6.58211928e-16, 0.00000015e-16,  "eV s"),
    "natural unit of energy":
        (8.18710506e-14, 0.00000036e-14,  "J"),
    "natural unit of energy in MeV":
        (0.510998928, 0.000000011,  "MeV"),
    "natural unit of length":
        (386.15926800e-15, 0.00000025e-15,  "m"),
    "natural unit of mass":
        (9.10938291e-31, 0.00000040e-31,  "kg"),
    "natural unit of mom.um":
        (2.73092429e-22, 0.00000012e-22,  "kg m s^-1"),
    "natural unit of mom.um in MeV/c":
        (0.510998928, 0.000000011,  "MeV/c"),
    "natural unit of time":
        (1.28808866833e-21, 0.00000000083e-21,  "s"),
    "natural unit of velocity":
        (299792458, 0.0,  "m s^-1"),
    "neutron Compton wavelength":
        (1.3195909068e-15, 0.0000000011e-15,  "m"),
    "neutron Compton wavelength over 2 pi":
        (0.21001941568e-15, 0.00000000017e-15,  "m"),
    "neutron-electron mag. mom. ratio":
        (1.04066882e-3, 0.00000025e-3,  ""),
    "neutron-electron mass ratio":
        (1838.6836605, 0.0000011,  ""),
    "neutron g factor":
        (-3.82608545, 0.00000090,  ""),
    "neutron gyromag. ratio":
        (1.83247179e8, 0.00000043e8,  "s^-1 T^-1"),
    "neutron gyromag. ratio over 2 pi":
        (29.1646943, 0.0000069,  "MHz T^-1"),
    "neutron mag. mom.":
        (-0.96623647e-26, 0.00000023e-26,  "J T^-1"),
    "neutron mag. mom. to Bohr magneton ratio":
        (-1.04187563e-3, 0.00000025e-3,  ""),
    "neutron mag. mom. to nuclear magneton ratio":
        (-1.91304272, 0.00000045,  ""),
    "neutron mass":
        (1.674927351e-27, 0.000000074e-27,  "kg"),
    "neutron mass energy equivalent":
        (1.505349631e-10, 0.000000066e-10,  "J"),
    "neutron mass energy equivalent in MeV":
        (939.565379, 0.000021,  "MeV"),
    "neutron mass in u":
        (1.00866491600, 0.00000000043,  "u"),
    "neutron molar mass":
        (1.00866491600e-3, 0.00000000043e-3,  "kg mol^-1"),
    "neutron-muon mass ratio":
        (8.89248400, 0.00000022,  ""),
    "neutron-proton mag. mom. ratio":
        (-0.68497934, 0.00000016,  ""),
    "neutron-proton mass difference":
        (2.30557392e-30, 0.00000076e-30,  ""),
    "neutron-proton mass difference energy equivalent":
        (2.07214650e-13, 0.00000068e-13,  ""),
    "neutron-proton mass difference energy equivalent in MeV":
        (1.29333217, 0.00000042,  ""),
    "neutron-proton mass difference in u":
        (0.00138844919, 0.00000000045,  ""),
    "neutron-proton mass ratio":
        (1.00137841917, 0.00000000045,  ""),
    "neutron-tau mass ratio":
        (0.528790, 0.000048,  ""),
    "neutron to shielded proton mag. mom. ratio":
        (-0.68499694, 0.00000016,  ""),
    "Newtonian constant of gravitation":
        (6.67384e-11, 0.00080e-11,  "m^3 kg^-1 s^-2"),
    "Newtonian constant of gravitation over h-bar c":
        (6.70837e-39, 0.00080e-39,  "(GeV/c^2)^-2"),
    "nuclear magneton":
        (5.05078353e-27, 0.00000011e-27,  "J T^-1"),
    "nuclear magneton in eV/T":
        (3.1524512605e-8, 0.0000000022e-8,  "eV T^-1"),
    "nuclear magneton in inverse meters per tesla":
        (2.542623527e-2, 0.000000056e-2,  "m^-1 T^-1"),
    "nuclear magneton in K/T":
        (3.6582682e-4, 0.0000033e-4,  "K T^-1"),
    "nuclear magneton in MHz/T":
        (7.62259357, 0.00000017,  "MHz T^-1"),
    "Planck constant":
        (6.62606957e-34, 0.00000029e-34,  "J s"),
    "Planck constant in eV s":
        (4.135667516e-15, 0.000000091e-15,  "eV s"),
    "Planck constant over 2 pi":
        (1.054571726e-34, 0.000000047e-34,  "J s"),
    "Planck constant over 2 pi in eV s":
        (6.58211928e-16, 0.00000015e-16,  "eV s"),
    "Planck constant over 2 pi times c in MeV fm":
        (197.3269718, 0.0000044,  "MeV fm"),
    "Planck length":
        (1.616199e-35, 0.000097e-35,  "m"),
    "Planck mass":
        (2.17651e-8, 0.00013e-8,  "kg"),
    "Planck mass energy equivalent in GeV":
        (1.220932e19, 0.000073e19,  "GeV"),
    "Planck temperature":
        (1.416833e32, 0.000085e32,  "K"),
    "Planck time":
        (5.39106e-44, 0.00032e-44,  "s"),
    "proton charge to mass quotient":
        (9.57883358e7, 0.00000021e7,  "C kg^-1"),
    "proton Compton wavelength":
        (1.32140985623e-15, 0.00000000094e-15,  "m"),
    "proton Compton wavelength over 2 pi":
        (0.21030891047e-15, 0.00000000015e-15,  "m"),
    "proton-electron mass ratio":
        (1836.15267245, 0.00000075,  ""),
    "proton g factor":
        (5.585694713, 0.000000046,  ""),
    "proton gyromag. ratio":
        (2.675222005e8, 0.000000063e8,  "s^-1 T^-1"),
    "proton gyromag. ratio over 2 pi":
        (42.5774806, 0.0000010,  "MHz T^-1"),
    "proton mag. mom.":
        (1.410606743e-26, 0.000000033e-26,  "J T^-1"),
    "proton mag. mom. to Bohr magneton ratio":
        (1.521032210e-3, 0.000000012e-3,  ""),
    "proton mag. mom. to nuclear magneton ratio":
        (2.792847356, 0.000000023,  ""),
    "proton mag. shielding correction":
        (25.694e-6, 0.014e-6,  ""),
    "proton mass":
        (1.672621777e-27, 0.000000074e-27,  "kg"),
    "proton mass energy equivalent":
        (1.503277484e-10, 0.000000066e-10,  "J"),
    "proton mass energy equivalent in MeV":
        (938.272046, 0.000021,  "MeV"),
    "proton mass in u":
        (1.007276466812, 0.000000000090,  "u"),
    "proton molar mass":
        (1.007276466812e-3, 0.000000000090e-3,  "kg mol^-1"),
    "proton-muon mass ratio":
        (8.88024331, 0.00000022,  ""),
    "proton-neutron mag. mom. ratio":
        (-1.45989806, 0.00000034,  ""),
    "proton-neutron mass ratio":
        (0.99862347826, 0.00000000045,  ""),
    "proton rms charge radius":
        (0.8775e-15, 0.0051e-15,  "m"),
    "proton-tau mass ratio":
        (0.528063, 0.000048,  ""),
    "quantum of circulation":
        (3.6369475520e-4, 0.0000000024e-4,  "m^2 s^-1"),
    "quantum of circulation times 2":
        (7.2738951040e-4, 0.0000000047e-4,  "m^2 s^-1"),
    "Rydberg constant":
        (10973731.568539, 0.000055,  "m^-1"),
    "Rydberg constant times c in Hz":
        (3.289841960364e15, 0.000000000017e15,  "Hz"),
    "Rydberg constant times hc in eV":
        (13.60569253, 0.00000030,  "eV"),
    "Rydberg constant times hc in J":
        (2.179872171e-18, 0.000000096e-18,  "J"),
    "Sackur-Tetrode constant (1 K, 100 kPa)":
        (-1.1517078, 0.0000023,  ""),
    "Sackur-Tetrode constant (1 K, 101.325 kPa)":
        (-1.1648708, 0.0000023,  ""),
    "second radiation constant":
        (1.4387770e-2, 0.0000013e-2,  "m K"),
    "shielded helion gyromag. ratio":
        (2.037894659e8, 0.000000051e8,  "s^-1 T^-1"),
    "shielded helion gyromag. ratio over 2 pi":
        (32.43410084, 0.00000081,  "MHz T^-1"),
    "shielded helion mag. mom.":
        (-1.074553044e-26, 0.000000027e-26,  "J T^-1"),
    "shielded helion mag. mom. to Bohr magneton ratio":
        (-1.158671471e-3, 0.000000014e-3,  ""),
    "shielded helion mag. mom. to nuclear magneton ratio":
        (-2.127497718, 0.000000025,  ""),
    "shielded helion to proton mag. mom. ratio":
        (-0.761766558, 0.000000011,  ""),
    "shielded helion to shielded proton mag. mom. ratio":
        (-0.7617861313, 0.0000000033,  ""),
    "shielded proton gyromag. ratio":
        (2.675153268e8, 0.000000066e8,  "s^-1 T^-1"),
    "shielded proton gyromag. ratio over 2 pi":
        (42.5763866, 0.0000010,  "MHz T^-1"),
    "shielded proton mag. mom.":
        (1.410570499e-26, 0.000000035e-26,  "J T^-1"),
    "shielded proton mag. mom. to Bohr magneton ratio":
        (1.520993128e-3, 0.000000017e-3,  ""),
    "shielded proton mag. mom. to nuclear magneton ratio":
        (2.792775598, 0.000000030,  ""),
    "speed of light in vacuum":
        (299792458., 0.0,  "m s^-1"),
    "standard acceleration of gravity":
        (9.80665, 0.0,  "m s^-2"),
    "standard atmosphere":
        (101325., 0.0,  "Pa"),
    "standard-state pressure":
        (100000., 0.0,  "Pa"),
    "Stefan-Boltzmann constant":
        (5.670373e-8, 0.000021e-8,  "W m^-2 K^-4"),
    "tau Compton wavelength":
        (0.697787e-15, 0.000063e-15,  "m"),
    "tau Compton wavelength over 2 pi":
        (0.111056e-15, 0.000010e-15,  "m"),
    "tau-electron mass ratio":
        (3477.15, 0.31,  ""),
    "tau mass":
        (3.16747e-27, 0.00029e-27,  "kg"),
    "tau mass energy equivalent":
        (2.84678e-10, 0.00026e-10,  "J"),
    "tau mass energy equivalent in MeV":
        (1776.82, 0.16,  "MeV"),
    "tau mass in u":
        (1.90749, 0.00017,  "u"),
    "tau molar mass":
        (1.90749e-3, 0.00017e-3,  "kg mol^-1"),
    "tau-muon mass ratio":
        (16.8167, 0.0015,  ""),
    "tau-neutron mass ratio":
        (1.89111, 0.00017,  ""),
    "tau-proton mass ratio":
        (1.89372, 0.00017,  ""),
    "Thomson cross section":
        (0.6652458734e-28, 0.0000000013e-28,  "m^2"),
    "triton-electron mass ratio":
        (5496.9215267, 0.0000050,  ""),
    "triton g factor":
        (5.957924896, 0.000000076,  ""),
    "triton mag. mom.":
        (1.504609447e-26, 0.000000038e-26,  "J T^-1"),
    "triton mag. mom. to Bohr magneton ratio":
        (1.622393657e-3, 0.000000021e-3,  ""),
    "triton mag. mom. to nuclear magneton ratio":
        (2.978962448, 0.000000038,  ""),
    "triton mass":
        (5.00735630e-27, 0.00000022e-27,  "kg"),
    "triton mass energy equivalent":
        (4.50038741e-10, 0.00000020e-10,  "J"),
    "triton mass energy equivalent in MeV":
        (2808.921005, 0.000062,  "MeV"),
    "triton mass in u":
        (3.0155007134, 0.0000000025,  "u"),
    "triton molar mass":
        (3.0155007134e-3, 0.0000000025e-3,  "kg mol^-1"),
    "triton-proton mass ratio":
        (2.9937170308, 0.0000000025,  ""),
    "unified atomic mass unit":
        (1.660538921e-27, 0.000000073e-27,  "kg"),
    "von Klitzing constant":
        (25812.8074434, 0.0000084,  "ohm"),
    "weak mixing angle":
        (0.2223, 0.0021,  ""),
    "Wien frequency displacement law constant":
        (5.8789254e10, 0.0000053e10,  "Hz K^-1"),
    "Wien wavelength displacement law constant":
        (2.8977721e-3, 0.0000026e-3,  "m K"),
}


c = data["speed of light in vacuum"][0]
epsilon_0 = data["atomic unit of permittivity"][0]
h = data["Planck constant"][0]
hbar = data["Planck constant"][0] / (2*math.pi)
G = data["Newtonian constant of gravitation"][0]
g = data["standard acceleration of gravity"][0]
e = data["electron volt"][0]
R = data["molar gas constant"][0]
alpha = data["fine-structure constant"][0]
N_A = data["Avogadro constant"][0]
k_B = data["Boltzmann constant"][0]
sigma = data["Stefan-Boltzmann constant"][0]
Wien = data["Wien wavelength displacement law constant"][0]
Rydberg = data["Rydberg constant"][0]
m_e = data["electron mass"][0]
m_p = data["proton mass"][0]
m_n = data["neutron mass"][0]


def Value(key):
    """Return the value stored for the constant name entered.

    : param key:  name of the constant
    : type key:  string

    : returns:  constant value
    : rtype:  float
    """
    return data[key][0]


def Uncertainty(key):
    """Return the uncertainty stored for the constant name entered.

    : param key:  name of the constant
    : type key:  string

    : returns:  constant uncertainty
    : rtype:  float
    """
    return data[key][1]


def Unit(key):
    """Return the units stored for the constant name entered.

    : param key:  name of the constant
    : type key:  string

    : returns:  constant units
    : rtype:  string
    """
    return data[key][2]
