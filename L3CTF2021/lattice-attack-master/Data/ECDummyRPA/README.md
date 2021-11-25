
## Data set "ECDummyRPA"

Real traces on OpenSSL ECDSA

From the publication, presented at SSTIC2021 :

Return of ECC dummy point additions  
Simple Power Analysis on efficient P-256 implementation  
[PDF link](https://www.sstic.org/media/SSTIC2021/SSTIC-actes/return_of_ecc_dummy_point_additions_simple_power_a/SSTIC2021-Article-return_of_ecc_dummy_point_additions_simple_power_analysis_on_efficient_p-256_implementation-russon.pdf)

by Andy Russon

6000 ECDSA 256r1 signatures

[Software repository](https://github.com/orangecertcc/ecdummyrpa)

[Data URL](https://github.com/orangecertcc/ecdummyrpa/raw/main/sample.tar.gz)

Using the *gen_input* script, the online data link above is read and file traces are parsed and filtered to build a JSON file compatible with the expected input format for LatticeAttack.

From this directory :

`
python3 gen_input.py && python3 ../../lattice_attack.py
`

Improvements from the research paper :

* No need of scikit-learn, a basic arithmetic mean is enough to assess the height of the flat valley, and filter the correct signatures. This just requires a manual threshold value.

