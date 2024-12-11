{ pkgs ? import (fetchTarball {
  url = "https://github.com/NixOS/nixpkgs/archive/refs/tags/24.05.tar.gz";
}) {} }:

pkgs.mkShell {
  buildInputs = [ 
    pkgs.python312Packages.amaranth
    pkgs.yosys
    ];
  shellHook = ''
    python3 rtlil_from_amaranth_examples.py --outdir ./corpus
    python3 rtlil_from_vexriscv_sources.py --outdir ./corpus
  '';
}